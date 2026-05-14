---
title: Agent工具与协议篇
date: 2025-04-24
tags: [Agent, Function Calling, MCP, A2A, 工具调用]
category: Agent智能体
---

# 工具调用体系 (Function Calling / MCP)

## 从提示词到函数调用的演化

```
阶段1：Prompt 模拟（2022年前）
  系统提示词中写："如果用户问天气，请输出 WEATHER:城市名"
  缺点：不稳定，模型可能不遵守格式

阶段2：Function Calling（2023年）
  OpenAI 正式发布结构化函数调用
  优点：稳定、JSON 格式化输出
  缺点：各厂商实现不统一

阶段3：MCP 协议（2024年末~）
  Anthropic 发布 Model Context Protocol
  统一标准，生态共享
```

---

## Function Calling 详解

### 工作原理

```
用户：北京明天天气怎么样？

第1步：用户 → Agent → LLM
  LLM 收到工具定义：
  {
    "name": "get_weather",
    "description": "获取指定城市天气",
    "parameters": {
      "location": {"type": "string", "描述": "城市名"},
      "date": {"type": "string", "描述": "日期"}
    }
  }

第2步：LLM 判断需要调用工具 → 输出 JSON 调用指令
  {
    "tool": "get_weather",
    "parameters": {"location": "北京", "date": "明天"}
  }

第3步：Agent 执行真实 API 调用 → 返回结果给 LLM

第4步：LLM 根据结果生成自然语言回复
  "北京明天天气晴朗，气温18-25℃，非常适合外出活动！"
```

### 代码示例（OpenAI 格式）

```python
import openai
import json

client = openai.OpenAI()

# 定义工具
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取指定地点的天气信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "城市名，如：北京、上海"
                    }
                },
                "required": ["location"]
            }
        }
    }
]

# 实际工具函数
def get_weather(location: str) -> str:
    return json.dumps({"location": location, "temperature": "22℃", "condition": "晴天"})

# 与模型交互
messages = [{"role": "user", "content": "北京今天天气怎么样？"}]
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    tools=tools
)

# 处理工具调用
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    args = json.loads(tool_call.function.arguments)
    result = get_weather(**args)
    
    messages.append(response.choices[0].message)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result
    })
    
    final_response = client.chat.completions.create(
        model="gpt-4o", 
        messages=messages
    )
    print(final_response.choices[0].message.content)
```

---

## MCP 协议详解（2024年最重要的标准）

### 什么是 MCP？

MCP（Model Context Protocol，模型上下文协议）是 Anthropic 于 2024年11月发布的开放标准协议。

> 类比：如果 Function Calling 是"点餐系统"，MCP 就是餐饮行业的统一 **标准菜单格式**，让所有餐厅和点餐平台都能无缝对接。

### MCP 架构图

```
┌─────────────────────────────────────────────────────┐
│                   MCP 架构                           │
│                                                     │
│  ┌─────────────────────────────────────────────┐   │
│  │              MCP Host                       │   │
│  │  （用户直接使用的应用：Claude、Cursor 等）    │   │
│  │                                             │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  │   │
│  │  │MCP Client│  │MCP Client│  │MCP Client│  │   │
│  │  └────┬─────┘  └────┬─────┘  └────┬─────┘  │   │
│  └───────┼─────────────┼─────────────┼─────────┘   │
│          │             │             │              │
│  ┌───────▼──┐  ┌───────▼──┐  ┌──────▼──────┐      │
│  │MCP Server│  │MCP Server│  │ MCP Server  │      │
│  │（文件系统）│  │（数据库）  │  │（搜索引擎） │      │
│  └──────────┘  └──────────┘  └─────────────┘      │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### MCP 工作六步骤

```
第1步 初始化
  MCP Host 启动 → 创建 N 个 MCP Client → 与 MCP Server 握手

第2步 发现
  MCP Client 请求 Server 的能力列表：
  - Tools（可调用的工具）
  - Resources（可读取的数据）  
  - Prompts（提示模板）

第3步 上下文提供
  Host 将 Tools 解析为 LLM 兼容的 JSON 格式

第4步 调用
  用户说"查一下 GitHub 上未关闭的 issues" →
  LLM 决定调用 GitHub MCP Server 的工具

第5步 响应
  MCP Server 执行操作，将结果返回给 Client

第6步 整合输出
  LLM 基于工具返回的信息，生成最终自然语言回复
```

### Function Calling vs MCP 对比

| 对比维度 | Function Calling | MCP |
|---------|-----------------|-----|
| 标准化程度 | 各厂商实现不同 | 统一开放标准 |
| 适用场景 | 轻量高频调用 | 复杂任务编排 |
| 工具复用 | 需要为每个模型单独适配 | 开发一次，所有模型可用 |
| 生态 | 封闭 | 开放，社区贡献丰富 |
| 学习成本 | 较低 | 中等 |

> **一句话记忆：**
> 大模型通过 **Function Calling** 表达"我要调用什么工具"，**MCP** 是统一的工具调用规范，**Agent** 是执行者。

---

## A2A 协议（Agent 间通信）

2025年 Google 发布的 **A2A（Agent-to-Agent）协议**，让不同公司的 Agent 之间可以互相"委托任务"。

```
用户 → Agent A（旅行规划 Agent）
         ↓ 委托机票任务
       Agent B（机票预订专家 Agent，另一家公司）
         ↓ 完成后返回结果
       Agent A 继续规划酒店...
```

这意味着未来会形成 **Agent 协作网络**，就像互联网让网站互联一样！

---

> 📌 相关章节：[[Agent基础概念篇]] | [[Agent核心技术篇]] | [[Agent多智能体篇]]
