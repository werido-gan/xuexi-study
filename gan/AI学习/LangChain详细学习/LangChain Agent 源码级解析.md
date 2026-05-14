# 🔍 LangChain Agent 源码级解析（Thought / Action 机制）

> 目标：搞清楚 LangChain Agent 是**怎么实现“会思考 + 会行动”**

---

# 🧠 一、核心问题

```text
Agent 是怎么做到：
1. 思考（Thought）
2. 决策（Action）
3. 调用工具（Tool）
4. 再思考（循环）
```

---

# 🧩 二、核心架构（源码视角）

```text id="g8s4yo"
Agent = LLM + Prompt + OutputParser + Tool + Executor
```

---

## 📌 执行链路（关键）

```text id="p6s9km"
用户输入
 ↓
AgentExecutor.run()
 ↓
LLM生成输出（带 Thought/Action）
 ↓
OutputParser解析
 ↓
执行Tool
 ↓
返回Observation
 ↓
拼接上下文
 ↓
再次调用LLM
 ↓
循环...
```

---

# 🔁 三、核心循环（最重要）

## 📌 实际源码逻辑（简化版）

```python id="y3r2xt"
while not finished:
    # 1. 调用 LLM
    output = llm(prompt)

    # 2. 解析输出
    action = parse(output)

    if action.type == "tool":
        # 3. 调用工具
        result = tool(action.input)

        # 4. 追加到上下文
        prompt += result
    else:
        # 5. 结束
        return action.final_answer
```

---

## 📌 对应概念

| 概念          | 实现              |
| ----------- | --------------- |
| Thought     | LLM生成文本         |
| Action      | LLM决定调用工具       |
| Observation | Tool返回结果        |
| Loop        | AgentExecutor循环 |

---

# 🧠 四、Thought 是怎么来的？

---

## 📌 本质

```text id="5nckcq"
Thought 不是“模块”  
而是 Prompt + LLM 的输出
```

---

## 📌 关键 Prompt（核心秘密）

```text id="5x6mde"
You are an agent. You can think step by step.

Format:

Thought: ...
Action: ...
Action Input: ...
```

👉 LLM 被“诱导”输出：

```text id="4a4w64"
Thought: 我需要查一下
Action: search
Action Input: LangChain
```

---

## 📌 结论

```text id="p7vbn3"
Thought = Prompt工程 + LLM生成
```

---

# ⚙️ 五、Action 是怎么触发的？

---

## 📌 输出解析器（OutputParser）

核心类：

```python id="4xkp98"
class AgentOutputParser:
    def parse(self, text):
        # 提取 Action / Input
```

---

## 📌 示例解析逻辑

```python id="qvlyvx"
if "Action:" in text:
    return ToolAction(name, input)
else:
    return FinalAnswer(text)
```

---

## 📌 关键点

```text id="yq7q7p"
LLM输出 → 解析 → 决定下一步
```

---

# 🧰 六、Tool 是怎么被调用的？

---

## 📌 Tool 本质

```python id="0p0a4c"
class Tool:
    def __init__(self, name, func):
        self.name = name
        self.func = func
```

---

## 📌 调用过程

```python id="j2blsr"
tool = tools[action.name]
result = tool.func(action.input)
```

---

## 📌 返回结果

```text id="f6r8hi"
Observation: 工具返回内容
```

---

# 🔁 七、循环是怎么实现的？

---

## 📌 AgentExecutor（核心类）

```python id="q6phg7"
class AgentExecutor:
    def run(self, input):
        while True:
            output = agent.plan()

            if output is Action:
                result = tool.run()
                self.memory.add(result)
            else:
                return output
```

---

## 📌 实际执行流

```text id="sklq8h"
LLM → Action → Tool → Observation → LLM → ...
```

---

# 🧠 八、完整执行过程（一步步拆）

---

## 🧩 示例

用户输入：

```text
LangChain是什么？
```

---

### 第一步：LLM生成

```text id="92nhpy"
Thought: 需要查知识库
Action: search
Action Input: LangChain
```

---

### 第二步：调用工具

```text id="ot7v5f"
Observation: LangChain 是一个框架
```

---

### 第三步：再次调用LLM

```text id="0tfqec"
Thought: 已经有答案
Final Answer: LangChain 是一个框架
```

---

# ⚠️ 九、为什么会“看起来很智能”？

---

## 📌 原因

```text id="dfyq95"
不是AI真的会思考  
而是：
Prompt + 格式约束 + 循环
```

---

## 📌 本质

```text id="qz6t0y"
Agent = 有结构的 Prompt + 循环执行器
```

---

# 🔥 十、关键源码模块总结

---

## 📦 核心类

```text id="o4e2as"
AgentExecutor      → 控制循环
Agent              → 决策逻辑
LLMChain           → 调用模型
OutputParser       → 解析输出
Tool               → 执行动作
Memory             → 保存上下文
```

---

# 🧠 十一、进阶理解（非常关键）

---

## 📌 为什么 Agent 会“乱调用工具”？

```text id="qq9d9b"
因为：
LLM在“猜”而不是“逻辑判断”
```

---

## 📌 如何优化？

### 方法1：限制工具

```text id="b1v03c"
减少可选工具数量
```

---

### 方法2：强化 Prompt

```text id="ldg4a3"
明确什么时候调用工具
```

---

### 方法3：状态机（高级）

```text id="86l4p5"
用代码控制流程，而不是完全交给LLM
```

---

# 🚀 十二、你必须掌握的本质

---

## 📌 最核心结论

```text id="btdl1q"
LangChain Agent ≠ 真正智能体  
本质是：
LLM + Prompt + 循环 + 工具调用
```

---

## 📌 思维模型

```text id="t1p6ne"
Thought → LLM输出
Action → Parser解析
Tool → Python函数
Loop → Executor控制
```

---

# 🏁 十三、终极总结

---

```text id="3c6kyo"
Agent的“思考能力”来自 Prompt  
Agent的“行动能力”来自 Tool  
Agent的“智能”来自循环
```

---

```text id="xk7k0l"
你真正要学的不是 LangChain  
而是：
如何设计“可控的推理流程”
```

---

# 🧾 END
