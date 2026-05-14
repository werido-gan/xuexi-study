---
title: Agent实战学习篇
date: 2025-04-24
tags: [Agent, 实战, 技能树, 学习路径]
category: Agent智能体
---

# 从零实战——搭建你的第一个 Agent

## 环境搭建

```bash
# 1. 安装必要的包
pip install langchain langchain-openai openai python-dotenv

# 2. 创建 .env 文件
echo "OPENAI_API_KEY=你的API密钥" > .env
# 国内可以用 DeepSeek（更便宜）
# echo "DEEPSEEK_API_KEY=你的API密钥" > .env

# 3. 验证安装
python -c "from langchain_openai import ChatOpenAI; print('安装成功！')"
```

---

## 实战一：最简单的 Agent（10分钟）

```python
# simple_agent.py
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import tool
import datetime

load_dotenv()

# ========== 定义工具 ==========
@tool
def get_current_time() -> str:
    """获取当前时间"""
    return datetime.datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")

@tool
def calculate(expression: str) -> str:
    """计算数学表达式，输入如：2+3*4"""
    try:
        result = eval(expression)
        return f"计算结果：{result}"
    except Exception as e:
        return f"计算错误：{str(e)}"

@tool
def tell_joke() -> str:
    """讲一个笑话"""
    jokes = [
        "为什么程序员总是分不清万圣节和圣诞节？因为 OCT 31 = DEC 25！",
        "一个字节走进酒吧，对酒吧说：给我8个比特！",
    ]
    import random
    return random.choice(jokes)

# ========== 创建 Agent ==========
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
tools = [get_current_time, calculate, tell_joke]

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个友好的助手，可以查询时间、做计算、讲笑话。用中文回答。"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# ========== 运行 ==========
if __name__ == "__main__":
    print("🤖 Agent 已启动！输入 'exit' 退出\n")
    chat_history = []
    
    while True:
        user_input = input("你：")
        if user_input.lower() == "exit":
            break
        
        result = agent_executor.invoke({
            "input": user_input,
            "chat_history": chat_history
        })
        
        print(f"\nAgent：{result['output']}\n")
        chat_history.extend([
            ("human", user_input),
            ("ai", result['output'])
        ])
```

---

## 实战二：带 RAG 的知识库问答 Agent

```python
# rag_agent.py
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.tools.retriever import create_retriever_tool
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 1. 加载文档并建立知识库
loader = TextLoader("company_docs.txt", encoding="utf-8")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory="./db")
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# 2. 创建检索工具
retriever_tool = create_retriever_tool(
    retriever,
    name="search_company_docs",
    description="搜索公司内部文档和知识库，当问到公司相关信息时使用此工具"
)

# 3. 添加搜索工具（外部信息补充）
from langchain_community.tools.tavily_search import TavilySearchResults
search_tool = TavilySearchResults(max_results=3)

# 4. 组装 Agent
llm = ChatOpenAI(model="gpt-4o", temperature=0)
tools = [retriever_tool, search_tool]

prompt = ChatPromptTemplate.from_messages([
    ("system", """你是公司的智能客服助手。
    回答问题时：
    1. 优先使用公司知识库中的信息
    2. 如果需要最新信息，可以搜索网络
    3. 如果不确定，请明确说明
    请用专业友好的语气回答用户问题。"""),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 5. 测试
result = agent_executor.invoke({
    "input": "我们公司的退换货政策是什么？",
    "chat_history": []
})
print(result['output'])
```

---

## 实战三：多 Agent 协作（CrewAI）

```python
# multi_agent_crew.py
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, WebsiteSearchTool

# 1. 定义 Agent 角色
researcher = Agent(
    role="市场研究员",
    goal="深入研究指定的市场趋势和竞争对手信息",
    backstory="你是一名经验丰富的市场研究专家，擅长收集和分析市场数据",
    tools=[SerperDevTool(), WebsiteSearchTool()],
    verbose=True
)

analyst = Agent(
    role="数据分析师",
    goal="对研究数据进行深入分析，找出关键洞察",
    backstory="你是一名数据驱动的分析师，善于从数据中发现有价值的规律",
    verbose=True
)

writer = Agent(
    role="报告撰写专家",
    goal="将分析结果整理成清晰、专业的市场调研报告",
    backstory="你是一名商业写作专家，能够将复杂信息转化为易读的报告",
    verbose=True
)

# 2. 定义任务
research_task = Task(
    description="研究2025年AI Agent市场的最新动态，包括主要玩家、市场规模、技术趋势",
    expected_output="详细的市场调研数据，包括具体数字和来源",
    agent=researcher
)

analysis_task = Task(
    description="基于研究员的数据，分析市场机会和挑战，找出3个最重要的战略洞察",
    expected_output="结构化的分析报告，包含SWOT分析和关键洞察",
    agent=analyst,
    context=[research_task]
)

report_task = Task(
    description="整合研究和分析结果，撰写一份3000字的专业市场调研报告",
    expected_output="完整的市场调研报告，包含摘要、正文和结论",
    agent=writer,
    context=[research_task, analysis_task]
)

# 3. 组建团队并执行
crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=[research_task, analysis_task, report_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff(inputs={"topic": "AI Agent 2025年市场分析"})
print(result)
```

---

# Agent 工程师技能树 & 学习路径

## 完整技能树

```
Agent 工程师技能树
│
├── 🔵 基础层（必须掌握）
│   ├── Python 编程
│   │   ├── 基础语法、函数、类
│   │   ├── 异步编程（async/await）⭐
│   │   ├── 常用库（requests、pydantic）
│   │   └── 环境管理（conda、venv）
│   │
│   ├── 大模型基础
│   │   ├── Transformer 架构原理
│   │   ├── Prompt Engineering（提示词工程）⭐
│   │   ├── API 调用（OpenAI、Anthropic）
│   │   └── Token、上下文窗口的概念
│   │
│   └── 开发工具
│       ├── Git 版本控制
│       ├── Docker 容器
│       ├── 命令行基础
│       └── VSCode + 调试技巧
│
├── 🟡 核心层（需要深入）
│   ├── Agent 框架
│   │   ├── LangChain 核心组件 ⭐
│   │   ├── LangGraph 状态管理 ⭐
│   │   ├── AutoGen 多 Agent
│   │   └── CrewAI 团队协作
│   │
│   ├── RAG 技术
│   │   ├── 文档解析与分块
│   │   ├── 向量数据库操作 ⭐
│   │   ├── 检索策略优化
│   │   └── RAG 评估框架
│   │
│   ├── 工具与协议
│   │   ├── Function Calling ⭐
│   │   ├── MCP 协议 ⭐
│   │   ├── REST API 设计
│   │   └── 数据库操作（SQL）
│   │
│   └── 平台工具
│       ├── Dify 工作流设计
│       ├── Coze Bot 搭建
│       └── LangSmith 监控
│
├── 🔴 进阶层（架构师必备）
│   ├── 系统设计
│   │   ├── 分布式架构
│   │   ├── 微服务设计
│   │   ├── 消息队列（Kafka、RabbitMQ）
│   │   └── 负载均衡 & 高可用
│   │
│   ├── Agent 高级技术
│   │   ├── Multi-Agent 编排 ⭐
│   │   ├── Agent 评估体系
│   │   ├── Fine-tuning 基础
│   │   └── 安全与对齐
│   │
│   ├── 云原生
│   │   ├── Kubernetes 部署
│   │   ├── CI/CD 流水线
│   │   ├── 监控（Prometheus + Grafana）
│   │   └── 成本优化
│   │
│   └── 业务落地
│       ├── 需求分析与方案设计
│       ├── 性能基准测试
│       ├── A/B 测试
│       └── 用户反馈迭代
│
└── 💡 前沿层（保持关注）
    ├── 推理模型（o1、DeepSeek R1）
    ├── 具身智能（Embodied AI）
    ├── 多模态 Agent
    └── AI 安全 & 对齐
```

---

## 分阶段学习路径

### 🚀 第一阶段：入门（1-2个月）

```
目标：理解 Agent 概念，能运行第一个 Agent

周1-2：基础知识
  □ 学习 Python 基础（如果没基础）
  □ 注册 OpenAI 账号，了解 API 调用
  □ 阅读：《什么是 LLM》《什么是 Prompt Engineering》
  □ 实践：用 Python 调用 API 做一个简单问答

周3-4：LangChain 入门
  □ 学习 LangChain 核心概念（Chain、Tool、Agent）
  □ 跑通官方示例
  □ 实践：搭建一个带搜索工具的简单 Agent

月2：动手项目
  □ 用 Dify/Coze 搭建一个知识库问答 Bot
  □ 部署到微信群或飞书
  □ 分享给朋友使用，收集反馈

✅ 里程碑：能独立搭建一个可用的 Agent 产品
```

### 🔥 第二阶段：进阶（2-3个月）

```
目标：掌握 Agent 核心架构，能处理实际业务场景

第2-3月：深入 Agent 技术
  □ 深入学习 LangGraph（状态管理、复杂流程）
  □ 实践 RAG 系统搭建（文档 → 向量化 → 检索 → 回答）
  □ 理解 MCP 协议，自己实现一个简单的 MCP Server
  □ 学习多 Agent 框架（AutoGen 或 CrewAI）

项目实战：
  □ 项目1：构建一个企业内部知识库问答系统
  □ 项目2：多 Agent 自动化研究报告生成系统
  □ 项目3：代码助手 Agent（读代码 → 理解 → 提建议）

✅ 里程碑：独立完成 2-3 个有实际用户的项目
```

### 💎 第三阶段：架构师（3-6个月）

```
目标：能设计和落地企业级 Agent 系统

第4-5月：系统设计
  □ 学习分布式系统基础
  □ 掌握 Docker + K8s 部署
  □ 学习监控、日志、告警体系
  □ 理解成本优化策略

第6月：综合实战
  □ 设计一套完整的企业 Agent 平台架构
  □ 包含：接入层、编排层、模型层、数据层、运维层
  □ 撰写技术方案文档
  □ 进行性能测试和优化

✅ 里程碑：能主导企业级 AI Agent 项目落地
```

---

> 📌 相关章节：[[Agent框架与平台篇]] | [[Agent企业级架构篇]] | [[Agent前沿趋势篇]]
