---
title: Agent核心技术篇
date: 2025-04-24
tags: [Agent, LLM, 规划, 记忆, 工具, 推理范式]
category: Agent智能体
---

# Agent 的核心四大模块

> 记住公式：**Agent = 大脑（LLM） + 规划 + 记忆 + 工具**

## 模块总览

```
                    ┌─────────────────────────────┐
                    │         AI Agent             │
                    │                              │
   用户输入  ──→   │  ┌──────────────────────┐   │
                    │  │   LLM（大脑/推理核心）│   │
                    │  └──────────┬───────────┘   │
                    │             │                │
              ┌─────┴──────┐  ┌──┴──────┐         │
              │  规划模块   │  │ 记忆模块 │         │
              │  Planning  │  │ Memory  │         │
              └─────┬──────┘  └──┬──────┘         │
                    │             │                │
                    └─────┬───────┘                │
                          │                        │
                    ┌─────┴──────┐                 │
                    │  工具模块   │                 │
                    │   Tools    │                 │
                    └─────┬──────┘                 │
                    └─────────────────────────────┘
                          │
                    外部世界（API、数据库、搜索引擎…）
```

---

## 模块一：LLM 大脑

LLM 是 Agent 的核心驱动力，负责：

- **理解**：理解用户的自然语言指令
- **推理**：分析当前状态，决定下一步做什么
- **生成**：生成工具调用指令、最终回答

### 常用模型选择

| 模型 | 提供商 | 特点 | 适用场景 |
|------|--------|------|---------|
| GPT-4o | OpenAI | 强大全能 | 通用场景 |
| Claude 3.5/4 | Anthropic | 长文本、遵循指令好 | 复杂任务、代码 |
| DeepSeek R1/V3 | DeepSeek | 推理强、性价比高 | 推理密集型任务 |
| Qwen2.5 | 阿里 | 中文强、开源 | 国内部署 |
| Llama 3.1 | Meta | 开源、可本地化 | 私有化部署 |
| Gemini 1.5/2.0 | Google | 多模态、长上下文 | 多媒体任务 |

---

## 模块二：规划（Planning）

规划模块让 Agent 能够把一个复杂目标拆解成可执行的步骤。

### 规划的两种方式

**1. 任务分解（Task Decomposition）**
```
大任务："写一份市场调研报告"
    ↓
拆解为：
  Step 1: 搜索行业数据
  Step 2: 分析竞争对手
  Step 3: 整理用户痛点
  Step 4: 撰写报告框架
  Step 5: 填充内容并格式化
```

**2. 自我反思（Self-Reflection）**
```
执行后发现错误 → 反思原因 → 修正策略 → 重新执行
```

### 规划范式对比

| 范式 | 原理 | 适用场景 | 优点 | 缺点 |
|------|------|---------|------|------|
| ReAct | 边思考边行动 | 需动态适应的任务 | 灵活自适应 | 成本高 |
| Plan-and-Execute | 先规划后执行 | 结构清晰的任务 | 高效、完成率高 | 规划可能出错 |
| Chain-of-Thought | 思维链推理 | 逻辑推理任务 | 透明可解释 | 不涉及工具 |
| Tree-of-Thought | 树状探索 | 需要多方案探索 | 效果好 | 成本极高 |

---

## 模块三：记忆（Memory）

记忆让 Agent 能够"记住"过去，做出更好的决策。

```
记忆系统全景
    │
    ├── 短期记忆（Short-term Memory）
    │   └── 当前对话上下文（Context Window）
    │       容量：通常几千到几十万 Token
    │       特点：快速访问，但有长度限制，断开即消失
    │
    ├── 长期记忆（Long-term Memory）
    │   ├── 向量数据库存储（如 Pinecone、Milvus、Chroma）
    │   │   存储内容：历史对话摘要、用户偏好、重要事实
    │   │   检索方式：语义相似度搜索
    │   └── 知识图谱（如 Neo4j）
    │       存储结构化关系知识
    │
    ├── 情节记忆（Episodic Memory）
    │   └── 过去完成的任务日志
    │       作用：类比参考，"上次我是这样做的"
    │
    └── 语义记忆（Semantic Memory）
        └── 通用知识（来自模型预训练）
```

### 记忆的实际应用

```python
# 简单示例：使用向量数据库做长期记忆
from langchain.memory import VectorStoreRetrieverMemory
from langchain.vectorstores import Chroma

# 将历史对话向量化存储
vectorstore = Chroma(embedding_function=embeddings)
memory = VectorStoreRetrieverMemory(retriever=vectorstore.as_retriever())

# Agent 执行时自动存取相关记忆
memory.save_context({"input": "用户喜欢简洁的报告"}, {"output": "已记录"})
```

---

## 模块四：工具（Tools）

工具让 Agent 突破大模型自身知识的局限，与真实世界交互。

```
Agent 可以调用的工具类型

┌─────────────────────────────────────────┐
│  信息获取工具                            │
│  ├── 搜索引擎（Google、Bing、Tavily）    │
│  ├── 知识库查询（RAG 检索）              │
│  └── 数据库查询（SQL / NoSQL）           │
├─────────────────────────────────────────┤
│  执行操作工具                            │
│  ├── 代码执行（Python沙箱）              │
│  ├── 文件操作（读写文件）                 │
│  └── 浏览器自动化（Playwright）          │
├─────────────────────────────────────────┤
│  外部 API 工具                           │
│  ├── 天气 API                           │
│  ├── 地图 API                           │
│  ├── 支付 API                           │
│  └── 邮件 / 日历 API                    │
├─────────────────────────────────────────┤
│  AI 工具（调用其他模型）                 │
│  ├── 图像生成（DALL-E、Midjourney）      │
│  ├── 语音转文字（Whisper）               │
│  └── 其他专业模型                        │
└─────────────────────────────────────────┘
```

---

# Agent 的工作机制与推理范式

## 最核心的模式：ReAct（推理 + 行动）

ReAct 是目前最主流的 Agent 工作模式，来自 2022 年 Google/Princeton 的论文。

### ReAct 工作流程

```
用户提问："2024年诺贝尔物理学奖得主是谁？他们的主要贡献是什么？"

┌─────────────────────────────────────────────┐
│  第1轮                                        │
│  Thought（思考）: 我需要搜索最新的诺贝尔奖信息 │
│  Action（行动）: 调用 Search("诺贝尔物理学奖 2024") │
│  Observation（观察）: 搜索返回结果...           │
├─────────────────────────────────────────────┤
│  第2轮                                        │
│  Thought: 我已经找到得主，需要了解他们的贡献   │
│  Action: 调用 Search("John Hopfield Geoffrey Hinton 贡献") │
│  Observation: 找到了关于神经网络研究的介绍     │
├─────────────────────────────────────────────┤
│  第3轮                                        │
│  Thought: 信息已经足够了，可以给出最终答案    │
│  Final Answer: 2024年诺贝尔物理学奖授予...   │
└─────────────────────────────────────────────┘
```

### ReAct 代码示例（LangChain）

```python
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI
from langchain import hub

# 1. 定义工具
def search_tool(query: str) -> str:
    """搜索互联网信息"""
    return f"搜索结果：{query}的相关信息..."

def calculator_tool(expression: str) -> str:
    """数学计算器"""
    try:
        return str(eval(expression))
    except:
        return "计算错误"

tools = [
    Tool(name="Search", func=search_tool, description="搜索互联网上的最新信息"),
    Tool(name="Calculator", func=calculator_tool, description="进行数学计算"),
]

# 2. 初始化大模型
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# 3. 获取 ReAct Prompt 模板
prompt = hub.pull("hwchase17/react")

# 4. 创建 Agent
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, max_iterations=5)

# 5. 执行
result = agent_executor.invoke({"input": "北京今天的天气怎么样？适合跑步吗？"})
print(result["output"])
```

---

## Plan-and-Execute（先规划后执行）

适合结构化、步骤清晰的复杂任务。

```
用户需求："帮我策划一场50人的年会"

【规划阶段】LLM 生成计划：
  计划:
  1. 确定预算范围
  2. 选择活动日期
  3. 预订场地
  4. 安排餐饮
  5. 策划节目单
  6. 制作邀请函
  7. 发送通知

【执行阶段】按步骤执行：
  → 执行步骤1：向用户询问预算
  → 执行步骤2：查询日历空闲
  → 执行步骤3：调用场地预订 API
  → ...（如步骤3失败则重新规划）
```

```python
# Plan-and-Execute 示例
def plan_and_execute(problem: str):
    # 阶段1：生成计划
    plan = llm.invoke(f"""
    制定解决这个问题的详细步骤计划：
    问题：{problem}
    输出格式：按编号列出每个步骤
    """)
    
    # 阶段2：逐步执行
    steps = parse_plan(plan)
    results = []
    for step in steps:
        result = execute_step(step, previous_results=results)
        results.append(result)
        if result.get("failed"):
            return replan(problem, steps, results)
    
    # 阶段3：整合结果
    return synthesize_results(results)
```

---

## 思维链 (Chain-of-Thought, CoT)

让 Agent "说出" 推理过程，提升准确率。

```
普通问答：
  Q: 小明有10个苹果，给了小红3个，又买了5个，还剩几个？
  A: 12个  ✅

加了 CoT：
  Q: （同上）请一步步思考。
  A: 
  思考过程：
  - 初始：10个苹果
  - 给了小红3个：10 - 3 = 7个
  - 又买了5个：7 + 5 = 12个
  所以还剩 12 个苹果 ✅
```

**关键 Prompt 魔法词：**
- "Let's think step by step"（让我们一步步思考）
- "请详细推理后给出答案"

---

## 自我反思与纠错（Reflection）

```
执行结果 → 评估器（Evaluator）→ 不满足要求？→ 反思 → 重新规划 → 再次执行
                                    ↓
                                满足要求 → 输出最终答案
```

这是让 Agent 越来越强的关键机制！类似人类的"试错学习"。

---

> 📌 相关章节：[[Agent基础概念篇]] | [[Agent记忆系统篇]] | [[Agent工具与协议篇]]
