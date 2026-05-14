# 🚀 LangChain 实战：从 0 到 Agentic RAG（可运行项目）

> 目标：让你真正具备“写出一个能用的 Agentic RAG 系统”的能力

---

# 🧱 一、项目结构（工程级）

```text
project/
├── app.py                # 主入口（Agent 调度）
├── llm.py                # 模型封装
├── rag/
│   ├── index.py          # 构建向量库
│   ├── retriever.py      # 检索逻辑
├── tools/
│   ├── search.py         # RAG工具
│   ├── calculator.py     # 示例工具
├── agent/
│   ├── agent.py          # Agent初始化
├── config.py             # 配置
```

---

# ⚙️ 二、环境准备

```bash
pip install langchain openai faiss-cpu tiktoken
```

---

# 🧠 三、核心模块实现

---

## 📌 3.1 LLM 封装

```python
# llm.py
from langchain.chat_models import ChatOpenAI

def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )
```

---

## 📌 3.2 构建向量库（RAG）

```python
# rag/index.py
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def build_db():
    texts = [
        "LangChain 是一个用于开发 LLM 应用的框架",
        "RAG 是检索增强生成",
        "Agent 可以调用工具"
    ]

    db = FAISS.from_texts(texts, OpenAIEmbeddings())
    db.save_local("faiss_db")
```

---

## 📌 3.3 检索器

```python
# rag/retriever.py
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def get_retriever():
    db = FAISS.load_local("faiss_db", OpenAIEmbeddings())
    return db.as_retriever()
```

---

## 🧰 3.4 定义 Tool（关键）

```python
# tools/search.py
from langchain.tools import Tool
from rag.retriever import get_retriever

retriever = get_retriever()

def search_docs(query: str):
    docs = retriever.get_relevant_documents(query)
    return "\n".join([doc.page_content for doc in docs])

search_tool = Tool(
    name="RAG Search",
    func=search_docs,
    description="用于查询知识库"
)
```

---

## 🧮 示例工具

```python
# tools/calculator.py
from langchain.tools import Tool

def calc(x: str):
    return str(eval(x))

calculator_tool = Tool(
    name="Calculator",
    func=calc,
    description="用于数学计算"
)
```

---

## 🤖 3.5 Agent 初始化（核心）

```python
# agent/agent.py
from langchain.agents import initialize_agent
from llm import get_llm
from tools.search import search_tool
from tools.calculator import calculator_tool

def create_agent():
    llm = get_llm()

    tools = [search_tool, calculator_tool]

    agent = initialize_agent(
        tools,
        llm,
        agent="zero-shot-react-description",
        verbose=True
    )

    return agent
```

---

## 🚀 3.6 主入口

```python
# app.py
from agent.agent import create_agent

if __name__ == "__main__":
    agent = create_agent()

    while True:
        query = input(">> ")
        result = agent.run(query)
        print(result)
```

---

# 🔁 四、运行效果（Agentic 行为）

```text
用户：LangChain 是什么？

思考：
→ 需要查知识库

行动：
→ 调用 RAG Search

观察：
→ 得到文本

最终回答：
→ LangChain 是一个用于开发 LLM 应用的框架
```

---

# 🧠 五、升级为 Agentic RAG（关键优化）

---

## 📌 5.1 增加“反思机制”

```python
# 在 prompt 中加入
"请判断当前信息是否足够，如果不足请继续调用工具"
```

---

## 📌 5.2 限制最大步骤

```python
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    max_iterations=5
)
```

---

## 📌 5.3 增强 Prompt（非常关键）

```text
你是一个智能Agent：

1. 先思考是否需要工具
2. 如果需要，调用工具
3. 如果结果不够，再次调用
4. 最后给出答案
```

---

# ⚠️ 六、生产级优化（重点）

---

## 🔥 6.1 替换 embedding

```text
不要用默认 → 用更强模型
```

---

## 🔥 6.2 增加 Rerank

```text
检索后 → 排序 → 提升准确率
```

---

## 🔥 6.3 结果缓存

```python
from functools import lru_cache
```

---

## 🔥 6.4 日志监控

```text
记录：
- 调用了什么工具
- 调用了几次
```

---

# 🧩 七、进阶架构（你应该掌握）

---

## 📌 多 Agent

```text
Planner → Executor → Reviewer
```

---

## 📌 状态机 Agent

```text
避免：
- 死循环
- 无意义调用
```

---

## 📌 工具扩展

```text
- Web Search
- 数据库查询
- Shell执行
```

---

# 🏁 八、你现在应该掌握的能力

---

## ✅ 必会

* LangChain 基础组件
* RAG 实现
* Tool 封装
* Agent 使用

---

## ✅ 进阶

* Agentic RAG 架构
* 多工具协作
* Prompt 设计

---

## ✅ 高阶

* 自定义 Agent
* 多Agent系统
* 性能优化

---

# 🧾 九、终极总结

```text
LangChain 学习路径：

Chain → RAG → Tool → Agent → Agentic RAG
```

---

```text
核心能力：

不是“会用 LangChain”
而是“会设计 Agent 系统”
```

---

