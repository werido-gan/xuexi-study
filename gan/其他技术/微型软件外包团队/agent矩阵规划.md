# 微型 AI 软件外包团队 Agent 矩阵 — 完整搭建文档

> **版本：** v1.0（2026年4月）  
> **参考框架：** OpenClaw v3.x + LangGraph + CrewAI + Anthropic Claude API  
> **适用人群：** 独立开发者 / 小型技术团队 / AI 工程师  
> **字数：** ~15,000 字  

---

## 目录

1. [系统总体架构概览](#1-系统总体架构概览)
2. [技术选型与依赖说明](#2-技术选型与依赖说明)
3. [环境准备与项目脚手架](#3-环境准备与项目脚手架)
4. [前端控制台（Boss UI）搭建](#4-前端控制台boss-ui搭建)
5. [第一阶段：交互中枢与需求理解层](#5-第一阶段交互中枢与需求理解层)
6. [第二阶段：契约与规范生成层](#6-第二阶段契约与规范生成层)
7. [第三阶段：任务拆解与并行开发层](#7-第三阶段任务拆解与并行开发层)
8. [第四阶段：测试与沙盒审查层](#8-第四阶段测试与沙盒审查层)
9. [第五阶段：交付与总结层](#9-第五阶段交付与总结层)
10. [人工干预（Human-in-the-Loop）机制](#10-人工干预human-in-the-loop机制)
11. [OpenClaw 风格多 Agent 编排实现](#11-openclaw-风格多-agent-编排实现)
12. [Agent 状态机与熔断机制](#12-agent-状态机与熔断机制)
13. [数据库与持久化设计](#13-数据库与持久化设计)
14. [Docker 化部署方案](#14-docker-化部署方案)
15. [安全、鉴权与观测性](#15-安全鉴权与观测性)
16. [常见问题与调试指南](#16-常见问题与调试指南)
17. [Roadmap 与扩展方向](#17-roadmap-与扩展方向)

---

## 1. 系统总体架构概览

### 1.1 整体数据流

```
你（Boss）
    │
    ▼
[飞书/微信 Webhook] ──► [Boss Gateway]
                              │
                    ┌─────────▼──────────┐
                    │   任务队列(Redis)    │
                    └─────────┬──────────┘
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
    [PM Agent]          [状态存储]           [人工干预窗口]
      (PRD生成)          (Postgres)          (前端UI)
          │
          ▼
    [Architect Agent]
      (系统设计)
          │
     ┌────┴────┐
     ▼         ▼
[Contract  [Design
 Maker]    Specifier]
 (API契约)  (UI规范)
     │         │
     └────┬────┘
          ▼
    [PM Agent 2.0]
    (任务拆解/JSON任务清单)
          │
    ┌─────┴──────┐
    ▼            ▼
[Frontend    [Backend
  Agent]       Agent]
    │             │
    └──────┬───────┘
           ▼
     [QA & Code Review Agent]
     (沙盒运行 + Jest + 契约验证)
           │
      [熔断机制 max_retries=3]
           │
           ▼
     [DevOps Agent]
     (Dockerfile/Nginx生成)
           │
           ▼
     [Reporter Agent]
     (推送飞书/微信报告)
```

### 1.2 并发模型

按照 2026 年 OpenClaw 多 Agent 编排的最佳实践，本系统采用 **混合并发模型**：

- **顺序执行**（串行依赖链）：PM → Architect → Contract Maker → PM 2.0
- **并行执行**（独立任务）：Frontend Agent & Backend Agent 同步开发
- **消费者组模式**：多个 Dev Agent 实例订阅同一任务队列，确保任务不被重复消费

---

## 2. 技术选型与依赖说明

### 2.1 后端 Orchestration 层

| 组件 | 选型 | 理由 |
|------|------|------|
| Agent 编排框架 | **LangGraph** | 图状态机最适合有条件路由+重试的复杂流；2026年最高月搜索量（27,100），生产案例最多 |
| LLM Provider | **Anthropic Claude claude-sonnet-4-20250514** | 代码生成能力强，Tool Use 稳定，支持长上下文 |
| 任务队列 | **Redis + BullMQ** | 轻量、原子性强，支持优先级与死信队列 |
| 状态持久化 | **PostgreSQL** | ACID 事务，适合存储 Agent 对话历史和任务状态 |
| 沙盒执行 | **Docker SDK (dockerode)** | 真实隔离环境，防止代码注入 |
| 消息推送 | **飞书 Open API / 微信企业号 API** | 原生 Webhook 支持 |

### 2.2 前端 Boss UI 层

| 组件 | 选型 | 理由 |
|------|------|------|
| 前端框架 | **React 19 + TypeScript** | 生态最完善 |
| UI 组件库 | **shadcn/ui + Tailwind CSS** | 现代、可定制、零运行时开销 |
| 实时通信 | **Server-Sent Events (SSE)** | 单向推流，比 WebSocket 更轻量，适合 Agent 日志流式输出 |
| 状态管理 | **Zustand** | 轻量，避免 Redux 模板代码 |
| 图表可视化 | **ReactFlow** | 可视化 Agent 执行图/任务依赖 |

### 2.3 整体后端服务

| 组件      | 选型                                         |
| ------- | ------------------------------------------ |
| API 服务器 | **NestJS** (与架构师 Agent 推荐的技术栈一致，吃自己的狗粮)    |
| ORM     | **Prisma**                                 |
| 代码沙盒    | **Docker-in-Docker** 或宿主机 Docker socket 挂载 |
| 文件存储    | **MinIO** (S3兼容，存储生成的代码产物)                 |

---

## 3. 环境准备与项目脚手架

### 3.1 前置要求

```bash
# Node.js >= 20.x (LTS)
node --version  # v20.x.x

# Docker & Docker Compose
docker --version       # 24.x+
docker compose version # 2.x+

# pnpm (推荐，比npm快3x)
npm install -g pnpm

# Python >= 3.11 (沙盒测试脚本用)
python3 --version
```

### 3.2 项目目录结构

```
ai-outsource-team/
├── apps/
│   ├── boss-ui/                 # 前端控制台 (React)
│   │   ├── src/
│   │   │   ├── components/
│   │   │   │   ├── AgentGraph/       # ReactFlow Agent可视化
│   │   │   │   ├── HumanIntervention/ # 人工干预面板
│   │   │   │   ├── TaskMonitor/      # 任务监控列表
│   │   │   │   └── OutputViewer/     # 产物预览(PRD/代码/API文档)
│   │   │   ├── stores/
│   │   │   │   └── agentStore.ts
│   │   │   └── App.tsx
│   │   └── package.json
│   │
│   └── orchestrator/            # 后端编排服务 (NestJS)
│       ├── src/
│       │   ├── agents/
│       │   │   ├── boss-gateway/
│       │   │   ├── product-manager/
│       │   │   ├── architect/
│       │   │   ├── contract-maker/
│       │   │   ├── design-specifier/
│       │   │   ├── project-manager/
│       │   │   ├── frontend-dev/
│       │   │   ├── backend-dev/
│       │   │   ├── qa-reviewer/
│       │   │   ├── devops/
│       │   │   └── reporter/
│       │   ├── graph/
│       │   │   └── workflow.graph.ts  # LangGraph 主图
│       │   ├── sandbox/
│       │   │   └── docker.sandbox.ts
│       │   ├── queue/
│       │   │   └── task.queue.ts
│       │   ├── human-loop/
│       │   │   └── intervention.service.ts
│       │   ├── sse/
│       │   │   └── event-stream.gateway.ts
│       │   └── app.module.ts
│       └── package.json
│
├── prisma/
│   └── schema.prisma
├── docker/
│   ├── docker-compose.yml
│   ├── docker-compose.prod.yml
│   └── sandbox/
│       └── Dockerfile.sandbox
├── scripts/
│   └── webhook-test.sh
└── README.md
```

### 3.3 初始化命令

```bash
# 克隆脚手架（或手动创建）
mkdir ai-outsource-team && cd ai-outsource-team
pnpm init

# 初始化工作区
cat > pnpm-workspace.yaml << EOF
packages:
  - 'apps/*'
EOF

# 创建 orchestrator (NestJS)
cd apps
npx @nestjs/cli new orchestrator --package-manager pnpm --skip-git

# 创建 boss-ui (React + Vite)
pnpm create vite boss-ui --template react-ts

# 安装核心依赖
cd orchestrator
pnpm add @langchain/core @langchain/langgraph @langchain/anthropic
pnpm add @anthropic-ai/sdk bullmq ioredis
pnpm add @nestjs/websockets @nestjs/platform-socket.io socket.io
pnpm add @prisma/client prisma dockerode
pnpm add -D @types/dockerode

cd ../boss-ui
pnpm add reactflow zustand @radix-ui/react-dialog
pnpm add lucide-react class-variance-authority clsx tailwind-merge
```

---

## 4. 前端控制台（Boss UI）搭建

Boss UI 是整个系统的神经中枢，它需要提供实时的 Agent 状态可视化、人工干预窗口、以及所有产物的预览能力。

### 4.1 主布局设计

```
┌─────────────────────────────────────────────────────────────┐
│  AI Outsource Team  [项目选择▼]      [新建项目] [设置]      │
├──────────────┬──────────────────────────┬───────────────────┤
│              │                          │                   │
│  任务历史列表 │    Agent 执行图          │  当前 Agent 输出  │
│              │    (ReactFlow)           │  (Streaming Log)  │
│  ○ Task #1   │                          │                   │
│  ● Task #2   │  [Boss]──►[PM]──►[Arch]  │  > Analyzing PRD  │
│  ○ Task #3   │             │            │  > Generating...  │
│              │          [QA]◄──[Dev]   │                   │
│              │                          │                   │
├──────────────┴──────────────────────────┴───────────────────┤
│  🟡 人工干预请求：PM Agent 需要确认需求边界                   │
│  [查看详情]  [批准并继续]  [修改后继续]  [中止任务]           │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 核心组件：AgentGraph（ReactFlow）

```tsx
// apps/boss-ui/src/components/AgentGraph/index.tsx
import React, { useCallback } from 'react';
import ReactFlow, {
  Node,
  Edge,
  useNodesState,
  useEdgesState,
  addEdge,
  Background,
  Controls,
  MiniMap,
  NodeTypes,
} from 'reactflow';
import 'reactflow/dist/style.css';

// Agent 节点类型定义
type AgentStatus = 'idle' | 'running' | 'waiting_human' | 'done' | 'error' | 'fused'; // fused = 熔断

interface AgentNodeData {
  label: string;
  status: AgentStatus;
  retryCount?: number;
  maxRetries?: number;
  outputSummary?: string;
}

// 自定义 Agent 节点渲染
const AgentNode = ({ data }: { data: AgentNodeData }) => {
  const statusColors: Record<AgentStatus, string> = {
    idle: 'bg-gray-100 border-gray-300',
    running: 'bg-blue-100 border-blue-500 animate-pulse',
    waiting_human: 'bg-yellow-100 border-yellow-500',
    done: 'bg-green-100 border-green-500',
    error: 'bg-red-100 border-red-500',
    fused: 'bg-orange-100 border-orange-600',
  };

  const statusIcons: Record<AgentStatus, string> = {
    idle: '⏸',
    running: '⚙️',
    waiting_human: '🟡',
    done: '✅',
    error: '❌',
    fused: '🔥',
  };

  return (
    <div className={`px-4 py-2 shadow-md rounded-md border-2 min-w-[140px] ${statusColors[data.status]}`}>
      <div className="flex items-center gap-2">
        <span>{statusIcons[data.status]}</span>
        <span className="font-bold text-sm">{data.label}</span>
      </div>
      {data.retryCount !== undefined && data.retryCount > 0 && (
        <div className="text-xs text-red-600 mt-1">
          重试 {data.retryCount}/{data.maxRetries}
        </div>
      )}
      {data.outputSummary && (
        <div className="text-xs text-gray-500 mt-1 truncate max-w-[120px]">
          {data.outputSummary}
        </div>
      )}
    </div>
  );
};

const nodeTypes: NodeTypes = { agentNode: AgentNode };

// 初始节点定义（对应11个Agent）
const initialNodes: Node<AgentNodeData>[] = [
  { id: 'boss',     type: 'agentNode', position: { x: 0, y: 0 },     data: { label: 'Boss Gateway', status: 'idle' } },
  { id: 'pm',       type: 'agentNode', position: { x: 200, y: 0 },   data: { label: 'PM Agent', status: 'idle' } },
  { id: 'arch',     type: 'agentNode', position: { x: 400, y: 0 },   data: { label: 'Architect', status: 'idle' } },
  { id: 'contract', type: 'agentNode', position: { x: 600, y: -80 }, data: { label: 'Contract Maker', status: 'idle' } },
  { id: 'design',   type: 'agentNode', position: { x: 600, y: 80 },  data: { label: 'Design Spec', status: 'idle' } },
  { id: 'projmgr',  type: 'agentNode', position: { x: 800, y: 0 },   data: { label: 'Project Mgr', status: 'idle' } },
  { id: 'fe',       type: 'agentNode', position: { x: 1000, y: -80 },data: { label: 'Frontend Dev', status: 'idle' } },
  { id: 'be',       type: 'agentNode', position: { x: 1000, y: 80 }, data: { label: 'Backend Dev', status: 'idle' } },
  { id: 'qa',       type: 'agentNode', position: { x: 1200, y: 0 },  data: { label: 'QA Reviewer', status: 'idle' } },
  { id: 'devops',   type: 'agentNode', position: { x: 1400, y: 0 },  data: { label: 'DevOps', status: 'idle' } },
  { id: 'reporter', type: 'agentNode', position: { x: 1600, y: 0 },  data: { label: 'Reporter', status: 'idle' } },
];

const initialEdges: Edge[] = [
  { id: 'e-boss-pm',       source: 'boss',     target: 'pm',       animated: false },
  { id: 'e-pm-arch',       source: 'pm',       target: 'arch',     animated: false },
  { id: 'e-arch-contract', source: 'arch',     target: 'contract', animated: false },
  { id: 'e-arch-design',   source: 'arch',     target: 'design',   animated: false },
  { id: 'e-contract-proj', source: 'contract', target: 'projmgr',  animated: false },
  { id: 'e-design-proj',   source: 'design',   target: 'projmgr',  animated: false },
  { id: 'e-proj-fe',       source: 'projmgr',  target: 'fe',       animated: false },
  { id: 'e-proj-be',       source: 'projmgr',  target: 'be',       animated: false },
  { id: 'e-fe-qa',         source: 'fe',       target: 'qa',       animated: false },
  { id: 'e-be-qa',         source: 'be',       target: 'qa',       animated: false },
  { id: 'e-qa-devops',     source: 'qa',       target: 'devops',   animated: false },
  { id: 'e-devops-rep',    source: 'devops',   target: 'reporter', animated: false },
];

export function AgentGraph() {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  // 通过 SSE 实时更新节点状态（见下文）
  // useAgentStatusSSE(setNodes, setEdges);

  return (
    <div style={{ width: '100%', height: '400px' }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        nodeTypes={nodeTypes}
        fitView
      >
        <Background />
        <Controls />
        <MiniMap />
      </ReactFlow>
    </div>
  );
}
```

### 4.3 核心组件：HumanIntervention（人工干预窗口）

```tsx
// apps/boss-ui/src/components/HumanIntervention/index.tsx
import React, { useState, useEffect } from 'react';

interface InterventionRequest {
  id: string;
  agentId: string;
  agentName: string;
  type: 'approval' | 'correction' | 'critical_error';
  message: string;
  context: string;           // Agent 当前处理的完整内容
  proposedOutput?: string;   // Agent 建议的输出（人工可修改）
  createdAt: string;
}

export function HumanInterventionPanel() {
  const [requests, setRequests] = useState<InterventionRequest[]>([]);
  const [selected, setSelected] = useState<InterventionRequest | null>(null);
  const [editedOutput, setEditedOutput] = useState('');

  // 通过 SSE 监听人工干预请求
  useEffect(() => {
    const es = new EventSource('/api/sse/interventions');
    es.addEventListener('intervention_request', (e) => {
      const req: InterventionRequest = JSON.parse(e.data);
      setRequests(prev => [req, ...prev]);
    });
    return () => es.close();
  }, []);

  const handleApprove = async (req: InterventionRequest) => {
    await fetch(`/api/interventions/${req.id}/approve`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ approvedOutput: editedOutput || req.proposedOutput }),
    });
    setRequests(prev => prev.filter(r => r.id !== req.id));
    setSelected(null);
  };

  const handleAbort = async (req: InterventionRequest) => {
    await fetch(`/api/interventions/${req.id}/abort`, { method: 'POST' });
    setRequests(prev => prev.filter(r => r.id !== req.id));
    setSelected(null);
  };

  const urgentCount = requests.filter(r => r.type === 'critical_error').length;

  return (
    <div className="border-t border-gray-200 bg-white">
      {/* 干预请求概要栏 */}
      <div className={`px-4 py-2 flex items-center gap-3 ${urgentCount > 0 ? 'bg-red-50' : requests.length > 0 ? 'bg-yellow-50' : 'bg-gray-50'}`}>
        <span className="text-sm font-medium">
          {requests.length === 0
            ? '✅ 无待处理干预请求'
            : `🟡 ${requests.length} 个待处理请求${urgentCount > 0 ? `（${urgentCount} 个紧急）` : ''}`}
        </span>
        {requests.length > 0 && (
          <button
            onClick={() => setSelected(requests[0])}
            className="ml-auto text-xs bg-yellow-500 hover:bg-yellow-600 text-white px-3 py-1 rounded"
          >
            处理请求
          </button>
        )}
      </div>

      {/* 干预详情弹窗 */}
      {selected && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
          <div className="bg-white rounded-xl shadow-2xl w-[800px] max-h-[80vh] overflow-y-auto">
            <div className="p-6">
              <h2 className="text-lg font-bold mb-2">
                {selected.type === 'critical_error' ? '🔥 紧急' : '🟡'} {selected.agentName} — 请求人工干预
              </h2>
              <p className="text-sm text-gray-600 mb-4">{selected.message}</p>

              {/* Agent 上下文 */}
              <details className="mb-4">
                <summary className="cursor-pointer text-sm font-medium text-blue-600">查看 Agent 上下文</summary>
                <pre className="mt-2 bg-gray-50 p-3 rounded text-xs overflow-x-auto">{selected.context}</pre>
              </details>

              {/* 可编辑输出 */}
              {selected.proposedOutput !== undefined && (
                <div className="mb-4">
                  <label className="block text-sm font-medium mb-1">Agent 建议输出（可直接修改后批准）：</label>
                  <textarea
                    className="w-full border rounded p-2 text-sm font-mono h-48"
                    value={editedOutput || selected.proposedOutput}
                    onChange={e => setEditedOutput(e.target.value)}
                  />
                </div>
              )}

              {/* 操作按钮 */}
              <div className="flex gap-3 justify-end">
                <button
                  onClick={() => handleAbort(selected)}
                  className="px-4 py-2 rounded bg-red-500 hover:bg-red-600 text-white text-sm"
                >
                  中止任务
                </button>
                <button
                  onClick={() => { setSelected(null); }}
                  className="px-4 py-2 rounded border text-sm"
                >
                  稍后处理
                </button>
                <button
                  onClick={() => handleApprove(selected)}
                  className="px-4 py-2 rounded bg-green-500 hover:bg-green-600 text-white text-sm"
                >
                  批准并继续
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
```

### 4.4 SSE 实时日志流

```tsx
// apps/boss-ui/src/hooks/useAgentStream.ts
import { useEffect, useRef } from 'react';
import { useAgentStore } from '../stores/agentStore';

export function useAgentStream(taskId: string) {
  const { updateAgentStatus, appendLog } = useAgentStore();
  const esRef = useRef<EventSource | null>(null);

  useEffect(() => {
    if (!taskId) return;

    const es = new EventSource(`/api/sse/tasks/${taskId}`);

    es.addEventListener('agent_status', (e) => {
      const { agentId, status, retryCount, outputSummary } = JSON.parse(e.data);
      updateAgentStatus(agentId, { status, retryCount, outputSummary });
    });

    es.addEventListener('agent_log', (e) => {
      const { agentId, message, level } = JSON.parse(e.data);
      appendLog(agentId, { message, level, timestamp: new Date() });
    });

    es.addEventListener('task_complete', (e) => {
      const data = JSON.parse(e.data);
      console.log('任务完成', data);
      es.close();
    });

    esRef.current = es;
    return () => es.close();
  }, [taskId]);
}
```

---

## 5. 第一阶段：交互中枢与需求理解层

### 5.1 Boss Gateway — 飞书/微信 Webhook 接入

```typescript
// apps/orchestrator/src/agents/boss-gateway/boss-gateway.service.ts
import { Injectable, Logger } from '@nestjs/common';
import Anthropic from '@anthropic-ai/sdk';
import { TaskQueueService } from '../../queue/task.queue';

@Injectable()
export class BossGatewayService {
  private readonly logger = new Logger(BossGatewayService.name);
  private readonly anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

  constructor(private readonly taskQueue: TaskQueueService) {}

  /**
   * 接收飞书消息，语音转文字 + 意图提炼
   */
  async processWebhook(payload: FeishuWebhookPayload): Promise<string> {
    let rawText = payload.event.message.content;

    // 如果是语音消息，先转文字（飞书语音消息会附带 file_key）
    if (payload.event.message.message_type === 'audio') {
      rawText = await this.transcribeAudio(payload.event.message.content);
    }

    // 用 Claude 提炼标准化文本
    const normalizedText = await this.normalizeInstruction(rawText);
    this.logger.log(`规范化指令: ${normalizedText}`);

    // 创建任务并放入队列
    const taskId = await this.taskQueue.createTask({
      rawInstruction: rawText,
      normalizedInstruction: normalizedText,
      source: 'feishu',
      userId: payload.event.sender.sender_id.user_id,
    });

    return taskId;
  }

  private async normalizeInstruction(rawText: string): Promise<string> {
    const response = await this.anthropic.messages.create({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 1000,
      system: `你是一个专业的需求翻译官。你的工作是将用户的口语化、碎片化指令，转化为一段清晰、结构化的软件需求描述文本。
      
      规则：
      1. 保留原始意图，不要过度解读
      2. 识别并保留关键实体：用户类型、核心功能、约束条件
      3. 如果用户提到了某种具体技术，原样保留
      4. 输出纯文本，不要Markdown格式
      5. 长度控制在200字以内`,
      messages: [{ role: 'user', content: rawText }],
    });

    return (response.content[0] as { text: string }).text;
  }

  private async transcribeAudio(audioFileKey: string): Promise<string> {
    // 调用飞书 API 下载音频，再调用 Whisper 或 Claude 的音频转文字
    // 此处省略具体实现，可用 OpenAI Whisper API 或飞书自带 ASR
    return '音频转文字内容';
  }
}
```

### 5.2 Product Manager Agent（PRD 生成）

```typescript
// apps/orchestrator/src/agents/product-manager/pm.agent.ts
import Anthropic from '@anthropic-ai/sdk';
import { HumanInterventionService } from '../../human-loop/intervention.service';
import { SSEGateway } from '../../sse/event-stream.gateway';

export class ProductManagerAgent {
  private readonly anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

  constructor(
    private readonly humanLoop: HumanInterventionService,
    private readonly sse: SSEGateway,
  ) {}

  async run(state: WorkflowState): Promise<Partial<WorkflowState>> {
    this.sse.emit(state.taskId, 'agent_status', { agentId: 'pm', status: 'running' });

    const prd = await this.generatePRD(state.normalizedInstruction);

    // 【人工干预检查点】：PRD 生成后，等待人工确认
    const confirmed = await this.humanLoop.requestApproval({
      taskId: state.taskId,
      agentId: 'pm',
      agentName: 'Product Manager Agent',
      type: 'approval',
      message: 'PRD 已生成，请审阅后确认继续。',
      context: state.normalizedInstruction,
      proposedOutput: prd,
    });

    // 如果人工修改了内容，用修改后的版本
    const finalPRD = confirmed.approvedOutput || prd;

    this.sse.emit(state.taskId, 'agent_status', { agentId: 'pm', status: 'done', outputSummary: 'PRD 生成完成' });

    return { prd: finalPRD };
  }

  private async generatePRD(instruction: string): Promise<string> {
    const response = await this.anthropic.messages.create({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 4000,
      system: `你是一位资深产品经理，专注于互联网/SaaS产品。
      
      你的任务是将用户的需求指令，转化为标准的产品需求文档(PRD)。
      
      PRD 必须包含以下章节：
      
      ## 1. 产品概述
      （一句话定义产品是什么、为谁服务）
      
      ## 2. 用户角色（User Personas）
      （列出2-4个核心用户角色，每个角色包含：身份、痛点、目标）
      
      ## 3. 核心功能列表（按优先级 P0/P1/P2 分级）
      
      ## 4. User Stories
      （格式：作为[用户角色]，我希望[功能]，以便[价值]）
      
      ## 5. 边缘场景与约束
      （列出5-10个需要特别处理的边缘情况）
      
      ## 6. 非功能性需求
      （性能、安全、可用性、兼容性要求）
      
      ## 7. 不在范围内（Out of Scope）
      （明确说明本期不做什么，防止范围蔓延）
      
      请用Markdown格式输出完整PRD。`,
      messages: [{ role: 'user', content: instruction }],
    });

    return (response.content[0] as { text: string }).text;
  }
}
```

### 5.3 Architect Agent（系统设计）

```typescript
// apps/orchestrator/src/agents/architect/architect.agent.ts
export class ArchitectAgent {
  private readonly anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

  async run(state: WorkflowState): Promise<Partial<WorkflowState>> {
    const systemDesign = await this.generateSystemDesign(state.prd);
    return { systemDesign };
  }

  private async generateSystemDesign(prd: string): Promise<string> {
    const response = await this.anthropic.messages.create({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 5000,
      system: `你是一位拥有10年经验的系统架构师。
      
      你的任务是基于PRD，产出完整的系统设计文档。文档必须包含：
      
      ## 1. 技术栈选型
      - 前端：（React/Vue/其他，说明理由）
      - 后端：（NestJS/FastAPI/其他，说明理由）
      - 数据库：（PostgreSQL/MongoDB/其他，说明理由）
      - 缓存：（Redis/Memcached/其他）
      - 消息队列：（如需要，选型说明）
      - 硬件/IoT：（如需MQTT/串口等，说明协议）
      - 部署：（Docker/K8s/Serverless）
      
      ## 2. 系统架构图（用Mermaid图描述）
      
      ## 3. 核心模块拆分
      （列出5-10个核心模块，每个模块说明：职责、输入、输出、内部逻辑）
      
      ## 4. 数据流描述
      （描述核心业务流程的数据流向）
      
      ## 5. 关键技术决策与理由（ADR 格式）
      
      ## 6. 性能与扩展性考量
      
      ## 7. 安全设计
      （认证方式、权限模型、数据加密策略）
      
      请用Markdown格式输出。`,
      messages: [{ role: 'user', content: `基于以下PRD设计系统架构：\n\n${prd}` }],
    });

    return (response.content[0] as { text: string }).text;
  }
}
```

---

## 6. 第二阶段：契约与规范生成层

这是整个流程中**最关键**的一步。没有这一层，前后端 Agent 就是在"盲目编码"，产出的代码必然无法对接。

### 6.1 Contract Maker Agent（API 契约生成）

```typescript
// apps/orchestrator/src/agents/contract-maker/contract-maker.agent.ts
export class ContractMakerAgent {
  private readonly anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

  async run(state: WorkflowState): Promise<Partial<WorkflowState>> {
    // 并行生成 API 契约和数据库 Schema
    const [apiContract, dbSchema] = await Promise.all([
      this.generateOpenAPISpec(state.systemDesign, state.prd),
      this.generateDatabaseSchema(state.systemDesign, state.prd),
    ]);

    return { apiContract, dbSchema };
  }

  private async generateOpenAPISpec(systemDesign: string, prd: string): Promise<string> {
    const response = await this.anthropic.messages.create({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 8000,
      system: `你是一位专业的API设计师。
      
      请基于系统设计文档和PRD，生成完整的OpenAPI 3.1规范(YAML格式)。
      
      规则：
      1. 每个API端点必须包含：路径、方法、请求体Schema、响应Schema、错误码
      2. 所有Schema都必须用$ref引用，定义在components/schemas中
      3. 必须包含认证说明（Bearer Token/API Key）
      4. 包含真实的示例值（example字段）
      5. 错误响应必须统一格式：{ code: number, message: string, data: null }
      6. 成功响应统一格式：{ code: 0, message: "ok", data: T }
      
      输出纯YAML，不要任何解释文字。`,
      messages: [{
        role: 'user',
        content: `PRD：\n${prd}\n\n系统设计：\n${systemDesign}\n\n请生成OpenAPI 3.1 YAML规范。`
      }],
    });

    return (response.content[0] as { text: string }).text;
  }

  private async generateDatabaseSchema(systemDesign: string, prd: string): Promise<string> {
    const response = await this.anthropic.messages.create({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 5000,
      system: `你是一位数据库架构师。
      
      请基于系统设计生成完整的Prisma Schema文件（schema.prisma格式）。
      
      规则：
      1. 每个模型必须包含：id（@id）、createdAt、updatedAt
      2. 合理设计关联关系（@relation）
      3. 添加必要的@unique、@@index约束
      4. 枚举类型用enum定义
      5. 同时输出对应的SQL建表语句（注释形式附在最后）
      6. 添加字段注释说明
      
      输出纯Prisma Schema，不要任何解释文字。`,
      messages: [{
        role: 'user',
        content: `PRD：\n${prd}\n\n系统设计：\n${systemDesign}\n\n请生成Prisma Schema。`
      }],
    });

    return (response.content[0] as { text: string }).text;
  }
}
```

### 6.2 Design Specifier Agent（UI/UX 规范生成）

```typescript
// apps/orchestrator/src/agents/design-specifier/design-specifier.agent.ts
export class DesignSpecifierAgent {
  private readonly anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

  async run(state: WorkflowState): Promise<Partial<WorkflowState>> {
    const designSpec = await this.generateDesignSystem(state.prd, state.stylePreference);
    return { designSpec };
  }

  private async generateDesignSystem(prd: string, stylePreference: string): Promise<string> {
    const response = await this.anthropic.messages.create({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 6000,
      system: `你是一位资深UI/UX设计师，擅长将设计意图转化为可被前端工程师精确实现的代码规范。
      
      你的输出不是设计图，而是一套完整的设计系统规范文档，包含：
      
      ## 1. Design Tokens（CSS变量定义）
      输出完整的CSS自定义属性，包括：
      - 颜色系统（主色、辅助色、中性色、语义色）精确到Hex值
      - 字体系统（font-family、font-size scale、font-weight、line-height）
      - 间距系统（spacing scale：4px基准）
      - 圆角系统
      - 阴影系统
      - 动效时间
      
      ## 2. 组件规范
      对每个核心UI组件定义：
      - 组件层级结构（HTML语义化标签建议）
      - 各状态样式（normal/hover/active/disabled/focus）
      - 尺寸变体（sm/md/lg）
      
      ## 3. 页面布局规范
      - 网格系统（列数、间距）
      - 响应式断点
      - 常见页面模板（列表页/详情页/表单页/Dashboard）的布局描述
      
      ## 4. 风格特征实现指南
      根据用户的风格偏好，提供具体CSS实现建议（例如：如果是"禅意极简"，说明具体的留白比例、无装饰原则、单色系运用方式；如果是"国风"，说明山水元素的SVG表达、古典配色方案等）
      
      ## 5. 图标规范
      推荐图标库及使用场景说明
      
      请以Markdown格式输出，CSS代码块用\`\`\`css格式。`,
      messages: [{
        role: 'user',
        content: `PRD：\n${prd}\n\n风格偏好：${stylePreference || '现代简约，专业商务感'}\n\n请生成完整的设计系统规范。`
      }],
    });

    return (response.content[0] as { text: string }).text;
  }
}
```

---

## 7. 第三阶段：任务拆解与并行开发层

### 7.1 Project Manager Agent（任务拆解）

```typescript
// apps/orchestrator/src/agents/project-manager/project-manager.agent.ts

export interface DevTask {
  id: string;
  type: 'frontend' | 'backend';
  priority: 1 | 2 | 3;      // 1=最高
  title: string;
  description: string;
  dependencies: string[];    // 依赖的其他任务ID
  inputs: {
    relevantApiEndpoints?: string[];   // 引用 openapi spec 中的路径
    relevantSchemas?: string[];        // 引用 prisma schema 中的模型名
    relevantComponents?: string[];     // 引用设计规范中的组件名
  };
  acceptanceCriteria: string[];
  estimatedLines: number;
}

export class ProjectManagerAgent {
  private readonly anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

  async run(state: WorkflowState): Promise<Partial<WorkflowState>> {
    const tasks = await this.decomposeTasks(state);
    return { taskList: tasks };
  }

  private async decomposeTasks(state: WorkflowState): Promise<DevTask[]> {
    const response = await this.anthropic.messages.create({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 8000,
      system: `你是一位技术型项目经理，擅长将大型软件项目拆解为粒度极小的开发任务。
      
      规则：
      1. 每个任务必须足够小，能在100-300行代码内完成
      2. 前端任务和后端任务要分开，并标注类型
      3. 任务间依赖必须显式声明（如"登录接口必须在用户列表页之前完成"）
      4. 每个任务的inputs必须精确引用API契约中的路径或数据库Schema中的模型名
      5. 验收标准必须可量化（如"调用POST /api/login，返回200和token"）
      6. 任务ID格式：FE-001/BE-001
      
      输出格式：严格的JSON数组，不要任何Markdown包裹，不要解释文字。
      
      JSON格式如下：
      [
        {
          "id": "BE-001",
          "type": "backend",
          "priority": 1,
          "title": "用户认证模块",
          "description": "实现JWT认证，包含注册、登录、刷新Token接口",
          "dependencies": [],
          "inputs": {
            "relevantApiEndpoints": ["/api/auth/register", "/api/auth/login", "/api/auth/refresh"],
            "relevantSchemas": ["User"]
          },
          "acceptanceCriteria": [
            "POST /api/auth/register 返回201和用户信息",
            "POST /api/auth/login 返回200和access_token/refresh_token",
            "invalid token返回401"
          ],
          "estimatedLines": 200
        }
      ]`,
      messages: [{
        role: 'user',
        content: `PRD：\n${state.prd}\n\nAPI契约（OpenAPI）前500字：\n${state.apiContract.slice(0, 500)}...\n\n数据库Schema：\n${state.dbSchema.slice(0, 500)}...\n\nUI设计规范前300字：\n${state.designSpec.slice(0, 300)}...\n\n请拆解为独立的开发任务JSON列表。`
      }],
    });

    const rawText = (response.content[0] as { text: string }).text;
    return JSON.parse(rawText) as DevTask[];
  }
}
```

### 7.2 Frontend Dev Agent

```typescript
// apps/orchestrator/src/agents/frontend-dev/frontend-dev.agent.ts
export class FrontendDevAgent {
  private readonly anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

  async run(task: DevTask, state: WorkflowState): Promise<GeneratedCode> {
    // 只传给 Agent 这个任务相关的 API 契约片段，减少 token 消耗
    const relevantApiSpec = this.extractRelevantApiSpec(
      state.apiContract,
      task.inputs.relevantApiEndpoints || []
    );

    const relevantDesignSpec = this.extractRelevantDesignSpec(
      state.designSpec,
      task.inputs.relevantComponents || []
    );

    const response = await this.anthropic.messages.create({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 8000,
      system: `你是一位高级前端工程师，技术栈为 React 19 + TypeScript + Tailwind CSS。
      
      编码规范（必须严格遵守）：
      1. 使用函数式组件 + Hooks，不用类组件
      2. Props 类型用 interface 定义
      3. 异步请求用 React Query（TanStack Query v5）
      4. API 调用必须严格按照给定的 OpenAPI 规范，包括路径、方法、请求体、响应体
      5. UI 样式必须使用给定的 Design Tokens CSS 变量，不要硬编码颜色/间距
      6. 错误处理：loading/error/empty 三种状态都要处理
      7. 文件命名：PascalCase.tsx（组件），camelCase.ts（工具函数）
      8. 每个文件开头注释：文件路径、用途说明
      
      输出格式：JSON对象，包含files数组，每个file包含path和content字段。
      不要任何Markdown包裹。`,
      messages: [{
        role: 'user',
        content: `任务：${task.title}
        
描述：${task.description}

验收标准：
${task.acceptanceCriteria.map((c, i) => `${i+1}. ${c}`).join('\n')}

相关 API 规范：
${relevantApiSpec}

相关 Design Tokens：
${relevantDesignSpec}

请生成完整的前端代码，输出JSON格式。`
      }],
    });

    return JSON.parse((response.content[0] as { text: string }).text) as GeneratedCode;
  }

  private extractRelevantApiSpec(fullSpec: string, endpoints: string[]): string {
    // 简单实现：按行扫描包含endpoint路径的区块
    // 生产环境建议 parse YAML 后按路径提取
    if (endpoints.length === 0) return fullSpec.slice(0, 2000);
    return endpoints.map(ep => `endpoint: ${ep}`).join('\n') + '\n（详见完整API文档）';
  }

  private extractRelevantDesignSpec(fullSpec: string, components: string[]): string {
    if (components.length === 0) return fullSpec.slice(0, 1000);
    return components.join(', ') + ' 组件规范（详见完整设计系统文档）';
  }
}
```

### 7.3 Backend Dev Agent

```typescript
// apps/orchestrator/src/agents/backend-dev/backend-dev.agent.ts
export class BackendDevAgent {
  private readonly anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

  async run(task: DevTask, state: WorkflowState): Promise<GeneratedCode> {
    const response = await this.anthropic.messages.create({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 8000,
      system: `你是一位高级后端工程师，技术栈为 NestJS + Prisma + PostgreSQL + TypeScript。
      
      编码规范（必须严格遵守）：
      1. 严格遵循 NestJS 模块化架构：Module/Controller/Service/DTO/Entity 分离
      2. 所有接口必须与给定的 OpenAPI 规范完全一致（路径、方法、请求体、响应格式）
      3. 响应格式统一：{ code: 0, message: "ok", data: T }
      4. 使用 class-validator + class-transformer 做 DTO 验证
      5. 使用 Prisma 操作数据库，不要写原生 SQL（除非必要）
      6. 数据库 Schema 完全来自给定的 Prisma Schema 文件
      7. 必须实现错误处理（try-catch + HttpException）
      8. 必须为 Service 方法写 JSDoc 注释
      9. 敏感信息（密码）必须用 bcryptjs hash
      
      输出格式：JSON对象，包含files数组，每个file包含path和content字段。
      不要任何Markdown包裹。`,
      messages: [{
        role: 'user',
        content: `任务：${task.title}

描述：${task.description}

验收标准：
${task.acceptanceCriteria.map((c, i) => `${i+1}. ${c}`).join('\n')}

相关 API 规范：
${task.inputs.relevantApiEndpoints?.join(', ')}

相关 Prisma Schema 模型：
${task.inputs.relevantSchemas?.join(', ')}

请生成完整的NestJS代码，输出JSON格式。`
      }],
    });

    return JSON.parse((response.content[0] as { text: string }).text) as GeneratedCode;
  }
}
```

---

## 8. 第四阶段：测试与沙盒审查层

### 8.1 Docker 沙盒服务

```typescript
// apps/orchestrator/src/sandbox/docker.sandbox.ts
import Docker from 'dockerode';
import * as path from 'path';
import * as fs from 'fs/promises';
import { Logger } from '@nestjs/common';

export interface SandboxResult {
  success: boolean;
  stdout: string;
  stderr: string;
  exitCode: number;
  duration: number;
}

@Injectable()
export class DockerSandboxService {
  private readonly logger = new Logger(DockerSandboxService.name);
  private readonly docker = new Docker({ socketPath: '/var/run/docker.sock' });

  /**
   * 在 Docker 容器中运行代码并返回结果
   */
  async runInSandbox(
    code: GeneratedCode,
    language: 'node' | 'python',
    command: string,
    timeoutMs = 30000,
  ): Promise<SandboxResult> {
    const startTime = Date.now();

    // 1. 将代码写入临时目录
    const tmpDir = `/tmp/sandbox-${Date.now()}`;
    await fs.mkdir(tmpDir, { recursive: true });

    for (const file of code.files) {
      const filePath = path.join(tmpDir, file.path);
      await fs.mkdir(path.dirname(filePath), { recursive: true });
      await fs.writeFile(filePath, file.content, 'utf-8');
    }

    // 2. 创建容器
    const image = language === 'node' ? 'node:20-alpine' : 'python:3.11-slim';

    const container = await this.docker.createContainer({
      Image: image,
      Cmd: ['sh', '-c', command],
      WorkingDir: '/workspace',
      HostConfig: {
        Binds: [`${tmpDir}:/workspace:ro`],  // 只读挂载
        Memory: 256 * 1024 * 1024,           // 256MB 内存限制
        CpuPeriod: 100000,
        CpuQuota: 50000,                      // 50% CPU 限制
        NetworkMode: 'none',                  // 禁止网络（防止代码外联）
        AutoRemove: true,
      },
    });

    // 3. 运行并收集输出
    let stdout = '';
    let stderr = '';

    await container.start();

    const stream = await container.logs({
      follow: true,
      stdout: true,
      stderr: true,
    });

    // 4. 设置超时
    const timeout = setTimeout(async () => {
      try { await container.kill(); } catch {}
    }, timeoutMs);

    await new Promise<void>((resolve, reject) => {
      container.modem.demuxStream(
        stream,
        { write: (chunk: Buffer) => { stdout += chunk.toString(); } },
        { write: (chunk: Buffer) => { stderr += chunk.toString(); } },
      );
      stream.on('end', resolve);
      stream.on('error', reject);
    });

    clearTimeout(timeout);

    // 5. 获取退出码
    const inspectData = await container.inspect().catch(() => ({ State: { ExitCode: -1 } }));

    // 6. 清理
    await fs.rm(tmpDir, { recursive: true, force: true });

    return {
      success: inspectData.State.ExitCode === 0,
      stdout,
      stderr,
      exitCode: inspectData.State.ExitCode,
      duration: Date.now() - startTime,
    };
  }

  /**
   * 运行 Jest 测试
   */
  async runJestTests(code: GeneratedCode): Promise<SandboxResult> {
    return this.runInSandbox(
      code,
      'node',
      'npm install --quiet 2>&1 | tail -5 && npx jest --forceExit --passWithNoTests 2>&1',
      60000,
    );
  }

  /**
   * 运行 TypeScript 编译检查
   */
  async runTypeCheck(code: GeneratedCode): Promise<SandboxResult> {
    return this.runInSandbox(
      code,
      'node',
      'npm install --quiet 2>&1 | tail -5 && npx tsc --noEmit 2>&1',
      45000,
    );
  }
}
```

### 8.2 QA & Code Review Agent

```typescript
// apps/orchestrator/src/agents/qa-reviewer/qa-reviewer.agent.ts
export class QAReviewerAgent {
  private readonly anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
  private readonly MAX_RETRIES = 3;

  constructor(
    private readonly sandbox: DockerSandboxService,
    private readonly humanLoop: HumanInterventionService,
    private readonly sse: SSEGateway,
  ) {}

  async run(state: WorkflowState): Promise<Partial<WorkflowState>> {
    for (let attempt = 1; attempt <= this.MAX_RETRIES; attempt++) {
      this.sse.emit(state.taskId, 'agent_status', {
        agentId: 'qa',
        status: 'running',
        retryCount: attempt - 1,
        maxRetries: this.MAX_RETRIES,
      });

      const result = await this.reviewCode(state, attempt);

      if (result.passed) {
        this.sse.emit(state.taskId, 'agent_status', { agentId: 'qa', status: 'done' });
        return { qaReport: result, qaApproved: true };
      }

      if (attempt < this.MAX_RETRIES) {
        // 将错误反馈给对应的 Dev Agent，让其重写
        this.sse.emit(state.taskId, 'agent_log', {
          agentId: 'qa',
          level: 'warn',
          message: `第 ${attempt} 次审查失败，正在反馈给 Dev Agent 重写...`,
        });

        state = await this.feedbackToDevAgent(state, result.errors);
      }
    }

    // 熔断！超过最大重试次数
    this.sse.emit(state.taskId, 'agent_status', { agentId: 'qa', status: 'fused' });
    this.sse.emit(state.taskId, 'agent_log', {
      agentId: 'qa',
      level: 'error',
      message: `🔥 熔断触发！已重试 ${this.MAX_RETRIES} 次，仍未通过审查。`,
    });

    // 请求人工介入
    await this.humanLoop.requestApproval({
      taskId: state.taskId,
      agentId: 'qa',
      agentName: 'QA Reviewer',
      type: 'critical_error',
      message: `代码审查在 ${this.MAX_RETRIES} 次重试后仍然失败，需要人工介入处理。`,
      context: JSON.stringify({ errors: state.lastQAErrors, retries: this.MAX_RETRIES }),
    });

    return { qaApproved: false, fusedAt: 'qa', lastQAErrors: state.lastQAErrors };
  }

  private async reviewCode(state: WorkflowState, attempt: number): Promise<QAResult> {
    const errors: string[] = [];

    // Step 1: TypeScript 类型检查
    const typeCheckResult = await this.sandbox.runTypeCheck(state.generatedCode);
    if (!typeCheckResult.success) {
      errors.push(`TypeScript编译失败:\n${typeCheckResult.stderr}`);
    }

    // Step 2: Jest 测试运行
    const jestResult = await this.sandbox.runJestTests(state.generatedCode);
    if (!jestResult.success) {
      errors.push(`Jest测试失败:\n${jestResult.stdout}\n${jestResult.stderr}`);
    }

    // Step 3: Claude 代码审查（契约合规性 + 代码质量）
    const codeReview = await this.runClaudeCodeReview(state);
    if (!codeReview.compliant) {
      errors.push(`契约合规性问题:\n${codeReview.issues.join('\n')}`);
    }

    return {
      passed: errors.length === 0,
      errors,
      attempt,
      typeCheckPassed: typeCheckResult.success,
      testsPassed: jestResult.success,
      contractCompliant: codeReview.compliant,
    };
  }

  private async runClaudeCodeReview(state: WorkflowState): Promise<{ compliant: boolean; issues: string[] }> {
    const response = await this.anthropic.messages.create({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 3000,
      system: `你是一位代码审查专家，专注于API契约合规性审查。
      
      你需要检查生成的代码是否：
      1. 所有API端点路径与OpenAPI规范完全一致
      2. 请求体和响应体的字段名与规范完全匹配
      3. HTTP状态码符合规范要求
      4. 数据库操作使用了正确的Prisma模型名和字段名
      5. 前端API调用使用了正确的请求方法和路径
      
      输出JSON格式：{ "compliant": boolean, "issues": string[] }
      不要任何Markdown包裹。`,
      messages: [{
        role: 'user',
        content: `OpenAPI规范（前2000字）：\n${state.apiContract.slice(0, 2000)}\n\n生成的代码摘要：\n${JSON.stringify(state.generatedCode.files.map(f => ({ path: f.path, size: f.content.length })))}`
      }],
    });

    return JSON.parse((response.content[0] as { text: string }).text);
  }

  private async feedbackToDevAgent(state: WorkflowState, errors: string[]): Promise<WorkflowState> {
    // 将错误信息追加到 state，Dev Agent 下次运行时会看到这些错误
    return {
      ...state,
      lastQAErrors: errors,
      needsRework: true,
    };
  }
}
```

---

## 9. 第五阶段：交付与总结层

### 9.1 DevOps Agent（部署配置生成）

```typescript
// apps/orchestrator/src/agents/devops/devops.agent.ts
export class DevOpsAgent {
  private readonly anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

  async run(state: WorkflowState): Promise<Partial<WorkflowState>> {
    if (!state.qaApproved) {
      return { devOpsSkipped: true };
    }

    const devopsConfig = await this.generateDevOpsConfig(state);
    return { devopsConfig };
  }

  private async generateDevOpsConfig(state: WorkflowState): Promise<DevOpsConfig> {
    const response = await this.anthropic.messages.create({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 5000,
      system: `你是一位DevOps工程师，擅长Docker和Nginx配置。
      
      请基于项目的技术栈，生成以下配置文件：
      1. 后端服务的Dockerfile（多阶段构建，最终镜像用alpine）
      2. 前端服务的Dockerfile（Nginx静态文件服务）
      3. docker-compose.prod.yml（生产环境，包含数据库、Redis、后端、前端、Nginx反向代理）
      4. Nginx反向代理配置（nginx.conf）：
         - /api/* 转发到后端
         - /* 转发到前端静态文件
         - 启用gzip压缩
         - 设置合理的缓存策略
      5. .env.example（环境变量模板）
      6. 部署脚本 deploy.sh（拉最新代码、重建镜像、滚动重启）
      
      输出JSON格式：{ "files": [ { "path": string, "content": string } ] }`,
      messages: [{
        role: 'user',
        content: `技术栈：\n${state.systemDesign?.slice(0, 1000)}\n\n请生成完整的DevOps配置文件。`
      }],
    });

    return JSON.parse((response.content[0] as { text: string }).text) as DevOpsConfig;
  }
}
```

### 9.2 Reporter Agent（飞书消息推送）

```typescript
// apps/orchestrator/src/agents/reporter/reporter.agent.ts
import axios from 'axios';

export class ReporterAgent {
  async run(state: WorkflowState): Promise<void> {
    const report = this.buildReport(state);
    await this.sendToFeishu(report, state.sourceUserId);
  }

  private buildReport(state: WorkflowState): FeishuMessage {
    const isSuccess = state.qaApproved;
    const isFused = !!state.fusedAt;

    const headerColor = isSuccess ? 'green' : isFused ? 'red' : 'yellow';
    const headerText = isSuccess
      ? '✅ 项目交付完成！'
      : isFused
      ? '🔥 项目触发熔断，需要人工介入'
      : '⚠️ 项目部分完成';

    const elements = [
      // 项目概要
      {
        tag: 'div',
        text: {
          tag: 'lark_md',
          content: `**项目名称：** ${state.projectName || '未命名项目'}\n**完成时间：** ${new Date().toLocaleString('zh-CN')}\n**总耗时：** ${Math.round((Date.now() - state.startTime) / 1000 / 60)} 分钟`,
        },
      },
    ];

    if (isSuccess) {
      elements.push({
        tag: 'div',
        text: {
          tag: 'lark_md',
          content: `**📦 交付产物：**\n- PRD 文档：已生成\n- OpenAPI 规范：已生成\n- 数据库 Schema：已生成\n- 前端代码：${state.generatedCode?.files.filter(f => f.path.includes('frontend')).length || 0} 个文件\n- 后端代码：${state.generatedCode?.files.filter(f => f.path.includes('backend')).length || 0} 个文件\n- DevOps 配置：已生成`,
        },
      });
    }

    if (isFused) {
      elements.push({
        tag: 'div',
        text: {
          tag: 'lark_md',
          content: `**🔥 熔断信息：**\n- 触发节点：${state.fusedAt}\n- 错误摘要：\n${state.lastQAErrors?.slice(0, 3).map(e => `> ${e.slice(0, 100)}...`).join('\n')}`,
        },
      });
    }

    return {
      msg_type: 'interactive',
      card: {
        header: {
          title: { tag: 'plain_text', content: headerText },
          template: headerColor,
        },
        elements,
      },
    };
  }

  private async sendToFeishu(message: FeishuMessage, userId: string): Promise<void> {
    await axios.post(process.env.FEISHU_WEBHOOK_URL!, message, {
      headers: { 'Content-Type': 'application/json' },
    });
  }
}
```

---

## 10. 人工干预（Human-in-the-Loop）机制

Human-in-the-Loop 是整个系统的安全阀。在 2026 年的生产实践中，这是 Agent 编排系统稳定性的核心保障机制。

### 10.1 干预服务核心实现

```typescript
// apps/orchestrator/src/human-loop/intervention.service.ts
import { Injectable } from '@nestjs/common';
import { EventEmitter2 } from '@nestjs/event-emitter';
import { InjectRepository } from '@nestjs/typeorm';

export interface InterventionRequest {
  taskId: string;
  agentId: string;
  agentName: string;
  type: 'approval' | 'correction' | 'critical_error';
  message: string;
  context: string;
  proposedOutput?: string;
}

export interface InterventionResult {
  approved: boolean;
  approvedOutput?: string;
  aborted?: boolean;
}

@Injectable()
export class HumanInterventionService {
  // 存储等待人工响应的 Promise resolve 函数
  private pendingInterventions = new Map<string, {
    resolve: (result: InterventionResult) => void;
    reject: (err: Error) => void;
  }>();

  constructor(
    private readonly eventEmitter: EventEmitter2,
    private readonly prisma: PrismaService,
    private readonly sse: SSEGateway,
  ) {}

  /**
   * Agent 调用此方法请求人工干预，会挂起 Agent 直到人工响应
   */
  async requestApproval(request: InterventionRequest): Promise<InterventionResult> {
    const interventionId = `intervention-${Date.now()}-${Math.random().toString(36).slice(2)}`;

    // 1. 持久化到数据库（防止服务重启丢失）
    await this.prisma.humanIntervention.create({
      data: {
        id: interventionId,
        taskId: request.taskId,
        agentId: request.agentId,
        type: request.type,
        message: request.message,
        context: request.context,
        proposedOutput: request.proposedOutput,
        status: 'pending',
      },
    });

    // 2. 通过 SSE 推送到前端
    this.sse.emit(request.taskId, 'intervention_request', {
      id: interventionId,
      ...request,
      createdAt: new Date().toISOString(),
    });

    // 3. 挂起当前 Agent，等待人工响应（最多等待 24 小时）
    return new Promise<InterventionResult>((resolve, reject) => {
      this.pendingInterventions.set(interventionId, { resolve, reject });

      // 超时机制：24小时未响应则自动中止
      setTimeout(() => {
        if (this.pendingInterventions.has(interventionId)) {
          this.pendingInterventions.delete(interventionId);
          reject(new Error(`人工干预请求 ${interventionId} 超时（24小时）`));
        }
      }, 24 * 60 * 60 * 1000);
    });
  }

  /**
   * 前端调用此方法提交人工响应
   */
  async submitResponse(
    interventionId: string,
    response: { approved: boolean; approvedOutput?: string; aborted?: boolean }
  ): Promise<void> {
    const pending = this.pendingInterventions.get(interventionId);
    if (!pending) {
      throw new Error(`干预请求 ${interventionId} 不存在或已超时`);
    }

    // 更新数据库状态
    await this.prisma.humanIntervention.update({
      where: { id: interventionId },
      data: {
        status: response.aborted ? 'aborted' : 'approved',
        respondedAt: new Date(),
        approvedOutput: response.approvedOutput,
      },
    });

    this.pendingInterventions.delete(interventionId);
    pending.resolve(response);
  }
}
```

### 10.2 干预检查点配置

在 LangGraph 工作流图中，可以在任意节点后插入检查点：

```typescript
// 检查点定义
const HUMAN_CHECKPOINT_CONFIG = {
  after_prd_generation: true,           // PRD 生成后（高价值节点）
  after_architecture_design: true,      // 架构设计后（关键决策）
  after_api_contract: false,            // API 契约（可选，低风险）
  after_task_decomposition: true,       // 任务拆解后（影响后续所有工作）
  on_qa_failure_attempt_1: false,       // QA 第1次失败（自动重试）
  on_qa_failure_attempt_2: false,       // QA 第2次失败（自动重试）
  on_qa_failure_attempt_3: true,        // QA 第3次失败 = 熔断 → 必须人工
  before_final_delivery: true,          // 最终交付前（最后把关）
};
```

---

## 11. OpenClaw 风格多 Agent 编排实现

### 11.1 LangGraph 主工作流图

LangGraph 是目前（2026年）在有条件路由+重试场景下最优秀的编排框架。以下是完整的主图实现：

```typescript
// apps/orchestrator/src/graph/workflow.graph.ts
import {
  StateGraph,
  END,
  START,
  Annotation,
  interrupt,
} from '@langchain/langgraph';
import { BaseMessage } from '@langchain/core/messages';

// 全局工作流状态定义（类比 OpenClaw 的 Session State）
const WorkflowAnnotation = Annotation.Root({
  taskId: Annotation<string>(),
  rawInstruction: Annotation<string>(),
  normalizedInstruction: Annotation<string>(),
  prd: Annotation<string>(),
  systemDesign: Annotation<string>(),
  apiContract: Annotation<string>(),
  dbSchema: Annotation<string>(),
  designSpec: Annotation<string>(),
  taskList: Annotation<DevTask[]>(),
  generatedCode: Annotation<GeneratedCode>(),
  qaReport: Annotation<QAResult>(),
  qaApproved: Annotation<boolean>(),
  qaRetryCount: Annotation<number>({ default: () => 0 }),
  devopsConfig: Annotation<DevOpsConfig>(),
  fusedAt: Annotation<string | null>({ default: () => null }),
  lastQAErrors: Annotation<string[]>({ default: () => [] }),
  needsRework: Annotation<boolean>({ default: () => false }),
  humanInterventionPending: Annotation<boolean>({ default: () => false }),
  stylePreference: Annotation<string>({ default: () => '现代简约' }),
  startTime: Annotation<number>({ default: () => Date.now() }),
  messages: Annotation<BaseMessage[]>({ default: () => [] }),
});

type WorkflowState = typeof WorkflowAnnotation.State;

// 构建主图
export function buildWorkflowGraph(services: AgentServices) {
  const graph = new StateGraph(WorkflowAnnotation);

  // ── 节点注册 ──────────────────────────────────────────────

  graph.addNode('pm_agent', async (state) => {
    return services.pm.run(state);
  });

  graph.addNode('architect_agent', async (state) => {
    return services.architect.run(state);
  });

  // Contract Maker 和 Design Specifier 并行执行
  graph.addNode('contract_and_design', async (state) => {
    const [contractResult, designResult] = await Promise.all([
      services.contractMaker.run(state),
      services.designSpecifier.run(state),
    ]);
    return { ...contractResult, ...designResult };
  });

  graph.addNode('project_manager_agent', async (state) => {
    return services.projectManager.run(state);
  });

  // Frontend 和 Backend Dev 并行执行
  graph.addNode('parallel_dev', async (state) => {
    const feTasks = state.taskList.filter(t => t.type === 'frontend');
    const beTasks = state.taskList.filter(t => t.type === 'backend');

    const [feCode, beCode] = await Promise.all([
      Promise.all(feTasks.map(task => services.frontendDev.run(task, state))),
      Promise.all(beTasks.map(task => services.backendDev.run(task, state))),
    ]);

    // 合并所有生成的代码
    const allFiles = [
      ...feCode.flatMap(c => c.files),
      ...beCode.flatMap(c => c.files),
    ];

    return { generatedCode: { files: allFiles } };
  });

  graph.addNode('qa_agent', async (state) => {
    return services.qaReviewer.run(state);
  });

  graph.addNode('devops_agent', async (state) => {
    return services.devOps.run(state);
  });

  graph.addNode('reporter_agent', async (state) => {
    await services.reporter.run(state);
    return {};
  });

  // 熔断终止节点
  graph.addNode('fuse_abort', async (state) => {
    services.sse.emit(state.taskId, 'task_complete', {
      success: false,
      reason: `熔断于节点：${state.fusedAt}`,
    });
    return {};
  });

  // ── 边（路由）定义 ────────────────────────────────────────

  graph.addEdge(START, 'pm_agent');
  graph.addEdge('pm_agent', 'architect_agent');
  graph.addEdge('architect_agent', 'contract_and_design');
  graph.addEdge('contract_and_design', 'project_manager_agent');
  graph.addEdge('project_manager_agent', 'parallel_dev');
  graph.addEdge('parallel_dev', 'qa_agent');

  // QA 条件路由（核心熔断逻辑）
  graph.addConditionalEdges('qa_agent', (state) => {
    if (state.qaApproved) {
      return 'devops_agent';  // 通过 → 继续
    }
    if (state.fusedAt) {
      return 'fuse_abort';    // 已熔断 → 终止
    }
    if (state.qaRetryCount < 3 && state.needsRework) {
      return 'parallel_dev';  // 未达上限 → 重新开发
    }
    return 'fuse_abort';      // 兜底熔断
  });

  graph.addEdge('devops_agent', 'reporter_agent');
  graph.addEdge('reporter_agent', END);
  graph.addEdge('fuse_abort', END);

  // ── 编译并添加检查点持久化 ───────────────────────────────

  const { PostgresSaver } = require('@langchain/langgraph-checkpoint-postgres');
  const checkpointer = new PostgresSaver({
    connectionString: process.env.DATABASE_URL,
  });

  return graph.compile({ checkpointer });
}
```

### 11.2 类 OpenClaw 的 Gateway 入口

参考 OpenClaw 的 Gateway 架构设计（一个长驻的 daemon，管理所有消息路由和任务调度）：

```typescript
// apps/orchestrator/src/gateway/workflow.gateway.ts
import { WebSocketGateway, SubscribeMessage, MessageBody } from '@nestjs/websockets';
import { Server } from 'socket.io';

@WebSocketGateway({ cors: true })
export class WorkflowGateway {
  @WebSocketServer()
  server: Server;

  constructor(
    private readonly workflowService: WorkflowService,
    private readonly taskQueue: TaskQueueService,
  ) {}

  // 接收新任务（类比 OpenClaw 的 Gateway 接收消息）
  @SubscribeMessage('submit_task')
  async handleNewTask(@MessageBody() data: { instruction: string; stylePreference?: string }) {
    const taskId = await this.taskQueue.createTask({
      rawInstruction: data.instruction,
      stylePreference: data.stylePreference,
    });

    // 触发工作流执行
    this.workflowService.executeWorkflow(taskId).catch(err => {
      console.error('Workflow error:', err);
    });

    return { taskId };
  }
}
```

---

## 12. Agent 状态机与熔断机制

### 12.1 状态流转图

```
任务状态机：

CREATED
  │
  ▼
NORMALIZING (Boss Gateway 处理中)
  │
  ▼
PM_RUNNING → [HUMAN_WAIT] → PM_DONE
  │
  ▼
ARCH_RUNNING → [HUMAN_WAIT] → ARCH_DONE
  │
  ▼
CONTRACT_RUNNING (并行)
DESIGN_RUNNING  (并行)
  │
  ▼
PROJMGR_RUNNING → [HUMAN_WAIT] → TASKS_READY
  │
  ▼
FE_DEV_RUNNING  (并行)
BE_DEV_RUNNING  (并行)
  │
  ▼
QA_RUNNING
  │
  ├──(通过)──► DEVOPS_RUNNING → REPORTING → DONE
  │
  ├──(失败,重试<3)──► [重新进入 DEV]
  │
  └──(失败,重试=3)──► FUSED → [HUMAN_WAIT] → ABORTED
```

### 12.2 熔断降级策略

```typescript
// apps/orchestrator/src/graph/circuit-breaker.ts

export class CircuitBreaker {
  private failureCount = 0;
  private readonly MAX_FAILURES: number;

  constructor(maxRetries = 3) {
    this.MAX_FAILURES = maxRetries;
  }

  recordFailure(error: string): 'retry' | 'fuse' {
    this.failureCount++;

    if (this.failureCount >= this.MAX_FAILURES) {
      return 'fuse';  // 触发熔断
    }

    return 'retry';   // 继续重试
  }

  getFailureCount() { return this.failureCount; }
  isOpen() { return this.failureCount >= this.MAX_FAILURES; }
  reset() { this.failureCount = 0; }
}

// 熔断后的错误报告打包
export function packErrorReport(state: WorkflowState): ErrorReport {
  return {
    taskId: state.taskId,
    fusedAt: state.fusedAt!,
    retryAttempts: state.qaRetryCount,
    errors: state.lastQAErrors,
    generatedFiles: state.generatedCode?.files.map(f => f.path) || [],
    partialDeliverables: {
      hasPRD: !!state.prd,
      hasSystemDesign: !!state.systemDesign,
      hasAPIContract: !!state.apiContract,
      hasDBSchema: !!state.dbSchema,
      hasDesignSpec: !!state.designSpec,
      hasTaskList: !!state.taskList?.length,
      hasCode: !!state.generatedCode?.files.length,
    },
    timestamp: new Date().toISOString(),
    recommendation: '请查看错误日志，重点关注第3次QA失败的具体错误信息，可能需要手动修复特定模块后重新提交。',
  };
}
```

---

## 13. 数据库与持久化设计

### 13.1 Prisma Schema

```prisma
// prisma/schema.prisma

generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

// 任务主表
model Task {
  id                    String    @id @default(cuid())
  rawInstruction        String    @db.Text
  normalizedInstruction String?   @db.Text
  stylePreference       String    @default("现代简约")
  status                TaskStatus @default(CREATED)
  source                String    @default("manual") // feishu / wechat / manual
  sourceUserId          String?
  startTime             DateTime  @default(now())
  endTime               DateTime?
  
  // 各阶段产物
  prd                   String?   @db.Text
  systemDesign          String?   @db.Text
  apiContract           String?   @db.Text
  dbSchema              String?   @db.Text
  designSpec            String?   @db.Text
  taskListJson          String?   @db.Text  // JSON格式的开发任务清单
  generatedCodeJson     String?   @db.Text  // JSON格式的生成代码索引
  qaReportJson          String?   @db.Text
  devopsConfigJson      String?   @db.Text
  
  // 质量控制
  qaRetryCount          Int       @default(0)
  fusedAt               String?   // 熔断的 AgentId
  lastQAErrors          String?   @db.Text
  
  // 关联
  agentLogs             AgentLog[]
  humanInterventions    HumanIntervention[]
  
  createdAt             DateTime  @default(now())
  updatedAt             DateTime  @updatedAt
  
  @@index([status])
  @@index([sourceUserId])
}

enum TaskStatus {
  CREATED
  NORMALIZING
  PM_RUNNING
  ARCH_RUNNING
  CONTRACT_RUNNING
  PROJMGR_RUNNING
  DEV_RUNNING
  QA_RUNNING
  DEVOPS_RUNNING
  REPORTING
  DONE
  FUSED
  ABORTED
}

// Agent 执行日志
model AgentLog {
  id        String   @id @default(cuid())
  taskId    String
  task      Task     @relation(fields: [taskId], references: [id], onDelete: Cascade)
  agentId   String
  level     LogLevel @default(INFO)
  message   String   @db.Text
  metadata  String?  @db.Text  // JSON
  createdAt DateTime @default(now())
  
  @@index([taskId, agentId])
  @@index([createdAt])
}

enum LogLevel {
  DEBUG
  INFO
  WARN
  ERROR
}

// 人工干预记录
model HumanIntervention {
  id             String              @id @default(cuid())
  taskId         String
  task           Task                @relation(fields: [taskId], references: [id], onDelete: Cascade)
  agentId        String
  type           InterventionType
  message        String              @db.Text
  context        String              @db.Text
  proposedOutput String?             @db.Text
  approvedOutput String?             @db.Text
  status         InterventionStatus  @default(PENDING)
  respondedAt    DateTime?
  createdAt      DateTime            @default(now())
  
  @@index([taskId])
  @@index([status])
}

enum InterventionType {
  APPROVAL
  CORRECTION
  CRITICAL_ERROR
}

enum InterventionStatus {
  PENDING
  APPROVED
  ABORTED
  TIMEOUT
}
```

---

## 14. Docker 化部署方案

### 14.1 开发环境 docker-compose.yml

```yaml
# docker/docker-compose.yml
version: '3.9'

services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: aidev
      POSTGRES_PASSWORD: aidev_secret
      POSTGRES_DB: ai_outsource
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U aidev"]
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes

  minio:
    image: minio/minio:latest
    ports:
      - "9000:9000"
      - "9001:9001"
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin
    volumes:
      - minio_data:/data
    command: server /data --console-address ":9001"

  orchestrator:
    build:
      context: ../apps/orchestrator
      dockerfile: Dockerfile
    ports:
      - "3001:3001"
    environment:
      - DATABASE_URL=postgresql://aidev:aidev_secret@postgres:5432/ai_outsource
      - REDIS_URL=redis://redis:6379
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - FEISHU_WEBHOOK_URL=${FEISHU_WEBHOOK_URL}
      - MINIO_ENDPOINT=minio
      - MINIO_PORT=9000
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock  # 沙盒需要访问宿主 Docker
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_started

  boss-ui:
    build:
      context: ../apps/boss-ui
      dockerfile: Dockerfile
    ports:
      - "3000:80"
    depends_on:
      - orchestrator

volumes:
  postgres_data:
  redis_data:
  minio_data:
```

### 14.2 Orchestrator Dockerfile

```dockerfile
# apps/orchestrator/Dockerfile
FROM node:20-alpine AS builder

WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN npm install -g pnpm && pnpm install --frozen-lockfile

COPY . .
RUN pnpm build

# 生产镜像
FROM node:20-alpine AS runner

WORKDIR /app
ENV NODE_ENV=production

COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/prisma ./prisma

# 运行数据库迁移并启动服务
CMD ["sh", "-c", "npx prisma migrate deploy && node dist/main.js"]
```

### 14.3 前端 Dockerfile

```dockerfile
# apps/boss-ui/Dockerfile
FROM node:20-alpine AS builder

WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN npm install -g pnpm && pnpm install --frozen-lockfile

COPY . .
RUN pnpm build

FROM nginx:alpine AS runner

COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### 14.4 Nginx 配置

```nginx
# apps/boss-ui/nginx.conf
server {
    listen 80;
    server_name _;
    
    root /usr/share/nginx/html;
    index index.html;
    
    # 前端路由（SPA）
    location / {
        try_files $uri $uri/ /index.html;
    }
    
    # API 代理到后端
    location /api/ {
        proxy_pass http://orchestrator:3001/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
    
    # SSE 流式代理（重要：禁用缓冲）
    location /api/sse/ {
        proxy_pass http://orchestrator:3001/sse/;
        proxy_http_version 1.1;
        proxy_set_header Connection '';
        proxy_buffering off;
        proxy_cache off;
        proxy_read_timeout 86400s;  # 24小时，支持长连接
        chunked_transfer_encoding on;
    }
    
    # 静态资源缓存
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
    
    # Gzip 压缩
    gzip on;
    gzip_vary on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml;
}
```

---

## 15. 安全、鉴权与观测性

### 15.1 API 鉴权

```typescript
// apps/orchestrator/src/auth/api-key.guard.ts
import { Injectable, CanActivate, ExecutionContext, UnauthorizedException } from '@nestjs/common';

@Injectable()
export class ApiKeyGuard implements CanActivate {
  canActivate(context: ExecutionContext): boolean {
    const request = context.switchToHttp().getRequest();
    const apiKey = request.headers['x-api-key'];

    if (!apiKey || apiKey !== process.env.BOSS_API_KEY) {
      throw new UnauthorizedException('Invalid API key');
    }

    return true;
  }
}
```

### 15.2 Webhook 签名验证（飞书）

```typescript
// apps/orchestrator/src/agents/boss-gateway/feishu-webhook.guard.ts
import * as crypto from 'crypto';

export function verifyFeishuSignature(
  timestamp: string,
  nonce: string,
  body: string,
  signature: string,
  secret: string
): boolean {
  const content = timestamp + nonce + secret + body;
  const computed = crypto.createHash('sha256').update(content).digest('hex');
  return computed === signature;
}
```

### 15.3 可观测性（LangSmith + 自定义日志）

```typescript
// apps/orchestrator/src/tracing/langsmith.setup.ts
process.env.LANGCHAIN_TRACING_V2 = 'true';
process.env.LANGCHAIN_PROJECT = 'ai-outsource-team';
// LANGCHAIN_API_KEY 从环境变量读取

// 自定义结构化日志（适配 Datadog/Loki）
import { Logger } from '@nestjs/common';

export class AgentLogger extends Logger {
  logAgentAction(agentId: string, action: string, metadata?: Record<string, unknown>) {
    const log = {
      level: 'info',
      agent: agentId,
      action,
      timestamp: new Date().toISOString(),
      ...metadata,
    };
    console.log(JSON.stringify(log));
  }
}
```

---

## 16. 常见问题与调试指南

### Q1: Docker 沙盒无法启动

**症状：** `DockerSandboxService.runInSandbox` 抛出 `connect ENOENT /var/run/docker.sock`

**解决：**
```bash
# 确认 Docker socket 挂载正确
docker compose exec orchestrator ls -la /var/run/docker.sock

# 如果使用 Podman，改用：
# socketPath: '/run/user/1000/podman/podman.sock'
```

### Q2: LangGraph 检查点报错（Postgres 连接失败）

**症状：** `Connection terminated unexpectedly` in LangGraph checkpoint

**解决：** 检查 `DATABASE_URL` 格式，Postgres Saver 需要完整的连接字符串：
```
postgresql://user:password@host:5432/dbname?schema=public
```

### Q3: 人工干预请求前端收不到

**症状：** SSE 连接建立但不收到 `intervention_request` 事件

**调试步骤：**
```bash
# 直接测试 SSE 端点
curl -N http://localhost:3001/sse/tasks/{taskId} \
  -H "x-api-key: your-key"

# 检查 Nginx 是否禁用了 buffering
# nginx.conf 中 proxy_buffering 必须为 off
```

### Q4: Claude API Rate Limit

**症状：** `RateLimitError: 429` 在并行 Dev Agent 阶段

**解决：** 添加请求节流
```typescript
// 使用 p-limit 控制并发
import pLimit from 'p-limit';

const limit = pLimit(5); // 最多5个并发 Claude API 请求

const results = await Promise.all(
  tasks.map(task => limit(() => agent.run(task, state)))
);
```

### Q5: 生成的代码 JSON 解析失败

**症状：** `SyntaxError: Unexpected token` when parsing Dev Agent output

**解决：** Claude 有时会在 JSON 前后加 Markdown 包裹，需要清洗：
```typescript
function extractJSON(raw: string): string {
  // 移除 ```json ... ``` 包裹
  const match = raw.match(/```(?:json)?\s*([\s\S]*?)```/);
  if (match) return match[1].trim();
  
  // 尝试直接找第一个 { 到最后一个 }
  const start = raw.indexOf('{');
  const end = raw.lastIndexOf('}');
  if (start !== -1 && end !== -1) return raw.slice(start, end + 1);
  
  return raw.trim();
}
```

---

## 17. Roadmap 与扩展方向

### 近期（1-3个月）

- **语音转文字**：接入飞书语音消息 + OpenAI Whisper，实现真正的语音驱动
- **项目模板库**：将成功的任务打包为模板（SaaS模板、电商模板、IoT模板），新任务可继承
- **代码产物版本管理**：集成 Git，每次生成的代码自动提交到对应 Branch
- **前端实时代码预览**：使用 StackBlitz WebContainer 在浏览器内实时渲染前端代码

### 中期（3-6个月）

- **多模型路由**：根据任务类型动态选择模型。代码生成用 Claude claude-sonnet-4-20250514，快速分类用 Claude Haiku 4.5，节省 token 成本约 60%
- **Agent 记忆系统**：为每个 Agent 构建独立的长期记忆（项目历史、用户偏好、代码风格学习），实现跨任务经验积累
- **成本追踪面板**：实时显示每个任务的 token 消耗和 API 费用，帮助优化提示词
- **OpenClaw 集成**：将整个系统的 Boss Gateway 替换为 OpenClaw，支持 WhatsApp/Telegram/Signal 等多平台接入

### 长期（6个月+）

- **自我迭代**：用 Reporter Agent 收集的失败案例，自动优化其他 Agent 的 System Prompt（元学习）
- **多团队协作**：支持多个"虚拟外包团队"并行运行，每个团队服务不同的客户
- **MCP 工具集成**：将常用开发工具（GitHub、Jira、Figma、Linear）通过 MCP 协议接入，Agent 可直接操作真实项目
- **硬件 Agent 支持**：在 Architect Agent 中内置 MQTT/串口/蓝牙等硬件协议设计能力，支持 IoT 项目外包

---

## 附录 A：环境变量清单

```bash
# .env.example

# AI 模型
ANTHROPIC_API_KEY=sk-ant-xxxxx

# 数据库
DATABASE_URL=postgresql://aidev:aidev_secret@localhost:5432/ai_outsource

# Redis
REDIS_URL=redis://localhost:6379

# 消息平台
FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/xxxxx
FEISHU_APP_SECRET=xxxxx
WECHAT_CORP_ID=xxxxx
WECHAT_CORP_SECRET=xxxxx
WECHAT_AGENT_ID=xxxxx

# 鉴权
BOSS_API_KEY=your-secret-api-key-change-this

# 对象存储
MINIO_ENDPOINT=localhost
MINIO_PORT=9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin
MINIO_BUCKET=ai-outsource-artifacts

# 观测性（可选）
LANGCHAIN_API_KEY=lsv2_xxxxx
LANGCHAIN_PROJECT=ai-outsource-team

# 沙盒
SANDBOX_TIMEOUT_MS=30000
SANDBOX_MEMORY_MB=256
```

## 附录 B：快速启动清单

```bash
# 1. 克隆/创建项目
git clone <your-repo> ai-outsource-team
cd ai-outsource-team

# 2. 复制环境变量
cp .env.example .env
# 编辑 .env，填入你的 ANTHROPIC_API_KEY 等

# 3. 启动基础设施
docker compose -f docker/docker-compose.yml up -d postgres redis minio

# 4. 初始化数据库
cd apps/orchestrator
npx prisma migrate dev --name init
cd ../..

# 5. 安装依赖
pnpm install

# 6. 启动开发服务
pnpm -r dev
# 后端：http://localhost:3001
# 前端：http://localhost:3000

# 7. 测试一个任务
curl -X POST http://localhost:3001/api/tasks \
  -H "Content-Type: application/json" \
  -H "x-api-key: your-secret-api-key" \
  -d '{"instruction": "帮我做一个用户管理系统，需要注册、登录、角色权限管理功能", "stylePreference": "现代简约"}'

# 打开前端 http://localhost:3000 查看实时执行过程
```

---

*文档版本：v1.0 | 最后更新：2026年4月 | 基于 OpenClaw v3.x + LangGraph + Anthropic Claude API 最新实践*