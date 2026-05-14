---
title: Agent框架与平台篇
date: 2025-04-24
tags: [Agent, LangChain, LangGraph, AutoGen, CrewAI, Dify, Coze, n8n]
category: Agent智能体
---

# 主流框架全景图

## 框架选型决策树

```
你的需求是什么？
    │
    ├── 只是学习/入门？
    │   └── → Swarm（OpenAI）：最简单，适合理解概念
    │
    ├── 快速构建产品原型？
    │   └── → LangChain：生态最丰富，文档最全
    │
    ├── 需要复杂状态机/条件分支？
    │   └── → LangGraph：LangChain 的升级版，支持复杂流程图
    │
    ├── 构建多 Agent 协作系统？
    │   ├── → AutoGen（微软）：多 Agent 对话框架
    │   └── → CrewAI：面向团队协作，简单易用
    │
    ├── 企业级生产部署？
    │   └── → LangGraph + LangSmith（监控）
    │
    └── 不想写代码？
        └── → Dify / Coze / n8n（可视化平台）
```

## 主流框架对比

| 框架 | 来源 | Stars | 特点 | 学习曲线 |
|------|------|-------|------|---------|
| LangChain | 独立 | 90K+ | 生态最丰富，组件多 | 中等 |
| LangGraph | LangChain | 10K+ | 状态图，支持循环/分支 | 较高 |
| AutoGen | 微软 | 38K+ | 多 Agent 对话，功能强大 | 中等 |
| CrewAI | 独立 | 25K+ | 角色扮演式多 Agent | 低 |
| Swarm | OpenAI | 18K+ | 轻量，适合学习 | 低 |
| LlamaIndex | 独立 | 35K+ | 专注 RAG 和数据处理 | 中等 |
| Haystack | deepset | 17K+ | 企业级 NLP 流水线 | 较高 |
| Dspy | Stanford | 20K+ | 程序化提示优化 | 高 |

---

## LangChain 核心模块

```python
# LangChain 基本结构示例

from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import tool

# 1. 定义工具（用装饰器方式更简洁）
@tool
def search_web(query: str) -> str:
    """搜索网络上的最新信息"""
    return f"搜索结果：{query}"

@tool  
def get_stock_price(symbol: str) -> str:
    """获取股票价格"""
    return f"{symbol} 当前价格：100元"

# 2. 创建 Prompt 模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个专业的金融助手，帮用户分析市场信息。"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# 3. 组装 Agent
llm = ChatOpenAI(model="gpt-4o", temperature=0)
tools = [search_web, get_stock_price]
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 4. 运行
result = agent_executor.invoke({
    "input": "分析一下茅台的最新股价走势",
    "chat_history": []
})
```

---

## LangGraph：状态图 Agent

LangGraph 是构建复杂 Agent 流程的最佳选择：

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, List
import operator

# 定义状态
class AgentState(TypedDict):
    messages: Annotated[List, operator.add]  # 消息历史
    task_status: str                          # 任务状态
    results: dict                             # 中间结果

# 定义节点
def plan_node(state: AgentState):
    """规划节点：生成执行计划"""
    plan = llm.invoke("根据用户需求制定计划：" + str(state["messages"]))
    return {"task_status": "planned", "results": {"plan": plan}}

def execute_node(state: AgentState):
    """执行节点：按计划执行工具"""
    return {"task_status": "executed"}

def evaluate_node(state: AgentState):
    """评估节点：判断是否完成"""
    if is_task_complete(state):
        return {"task_status": "complete"}
    return {"task_status": "need_retry"}

# 构建图
workflow = StateGraph(AgentState)
workflow.add_node("plan", plan_node)
workflow.add_node("execute", execute_node)
workflow.add_node("evaluate", evaluate_node)

# 添加边（流程控制）
workflow.set_entry_point("plan")
workflow.add_edge("plan", "execute")
workflow.add_edge("execute", "evaluate")
workflow.add_conditional_edges(
    "evaluate",
    lambda state: "end" if state["task_status"] == "complete" else "retry",
    {
        "end": END,
        "retry": "plan"  # 失败时重新规划
    }
)

# 编译并运行
app = workflow.compile()
result = app.invoke({"messages": [("user", "帮我分析一下竞争对手")]})
```

---

# 主流平台对比 (Dify / Coze / n8n)

> 适合不想写代码或者想快速搭建产品的开发者/产品经理

## 平台选型一览

| 平台 | 类型 | 定位 | 代码需求 | 特色 |
|------|------|------|---------|------|
| Dify | 开源 | 企业级 AI 应用开发 | 低代码 | 支持私有化部署，功能完整 |
| Coze（扣子） | 商业 | 国内主流 Bot 平台 | 无代码 | 字节出品，接入渠道多 |
| n8n | 开源 | 工作流自动化 | 低代码 | 400+集成，适合自动化 |
| FastGPT | 开源 | 知识库问答 | 低代码 | RAG 场景专注 |
| 百炼（阿里） | 商业 | 企业 Agent 平台 | 低代码 | 国内云端，合规性好 |
| 智谱清言 | 商业 | C端智能助手 | 无代码 | 中文场景优化 |

---

## Dify 深度解析

```
Dify 适合场景：
  ✅ 企业内部知识库 + 对话系统
  ✅ 需要私有化部署（数据不出公司）
  ✅ 多模型灵活切换
  ✅ 有开发团队的企业

Dify 核心功能：
  1. 工作流（Workflow）
     用可视化拖拽设计 Agent 流程
     支持条件判断、循环、并行执行
  
  2. 知识库（Knowledge Base）
     上传文档 → 自动分块 → 向量化 → 检索
     支持 PDF、Word、网页等格式
  
  3. 多模型支持
     OpenAI、Claude、Qwen、DeepSeek 等均支持
  
  4. API 接口
     一键发布为 REST API，可集成到任何系统

快速开始（Docker 部署）：
  git clone https://github.com/langgenius/dify
  cd dify/docker
  docker compose up -d
  # 访问 http://localhost/
```

---

## Coze（扣子）快速上手

```
核心概念：
  Bot = Agent 的对话界面
  插件 = 工具集合（已有数百个官方插件）
  工作流 = 多步骤任务流程
  知识库 = 自定义文档库

搭建步骤（5分钟上手）：
  1. 访问 coze.cn，注册账号
  2. 新建 Bot，选择基础模型
  3. 添加插件（如：网络搜索、代码执行）
  4. 配置提示词（人格、任务范围）
  5. 测试并发布到飞书/微信/Web

实际案例 - 新闻资讯 Bot：
  步骤1：添加"新闻搜索"插件
  步骤2：设置工作流：每天8点 → 搜索科技新闻 → 整理摘要 → 发送
  步骤3：连接飞书群机器人
  结果：全自动每日简报！
```

---

> 📌 相关章节：[[Agent多智能体篇]] | [[Agent企业级架构篇]] | [[Agent实战学习篇]]
