# 📝 OpenClaw 多 Agent 独立配置实战笔记

**核心目标**：在一个 OpenClaw 实例下，运行多个**相互完全独立**的 Agent。它们拥有各自的记忆、工作区（Workspace）和状态，互不干扰。这在实际的复杂工程中非常实用（例如：你可以配置一个 Agent 专属负责智能调酒机硬件的配方检索与并发调度，而另一个 Agent 则仅用于日常飞书群组的闲聊交互）。

## 1. 核心原理：工作区与沙箱隔离

在 OpenClaw 中配置多 Agent，本质上是在系统的 JSON 配置文件中定义一个 `agents.list` 数组。每个 Agent 都需要明确指定：
* **唯一的 ID** (`id`)：用于系统识别和后续绑定。
* **独立的工作区路径** (`workspace`)：物理隔离，保证记忆和文件互不冲突。
* **沙箱环境** (`sandbox`)：可选配置，用于环境的安全隔离。

## 2. 配置文件结构拆解

参考以下核心配置逻辑，你可以根据业务需求自由组合：

```json
{
  "agents": {
    "list": [
      {
        "id": "personal_agent",
        "workspace": "~/.openclaw/workspace-personal",
        "sandbox": {
          "mode": "off" // 信任环境：无沙箱限制，Agent 可以调用所有本地系统工具
        }
      },
      {
        "id": "hardware_agent",
        "workspace": "~/.openclaw/workspace-hardware",
        "sandbox": {
          "mode": "all", // 严格模式：开启全量沙箱隔离
          "scope": "agent", // 隔离级别：为该 Agent 分配一个独立的 Docker 容器
          "docker": {
            "setupCommand": "apt-get update" // 容器启动初始化命令（熟练 Ubuntu 部署的话，可以在这里预装各种依赖库）
          }
        }
      }
    ]
  }
}

3. 实操步骤：以绑定外部群聊（如飞书）为例
如果你使用的是云服务器（如腾讯云 Lighthouse），整个流程可以通过终端命令行快速搞定：
Step 1：获取渠道 ID
在飞书等聊天平台获取目标群组的唯一会话 ID。

Step 2：登录服务器与配置备份（极其重要！）
连接到你的服务器终端后，在修改任何配置前，务必先备份现有的绑定关系：
openclaw config get bindings > bindings_backup.json

Step 3：修改与追加绑定关系 (bindings)
多 Agent 的路由分发是通过 
bindings 数组实现的。你需要将特定的 agent_id 绑定到特定的通道上。
• 先读取当前配置：openclaw config get bindings
• 将新的飞书群组规则追加到原有数组中，然后用 --json 参数整体写回系统：
openclaw config set --json bindings '[{"agent_id": "personal_agent", "channel": "wechat"}, {"agent_id": "hardware_agent", "channel": "lark", "group_id": "填入你的飞书群组ID"}]'

4. 💡 避坑指南 & 常见问题
• 一对一绑定限制：目前 OpenClaw 不支持为一个群组/对话框同时配置多个 Agent。一个群组只能绑定唯一一个专属 Agent。
• 绝对独立的配置：独立出的 Agent 绝对不会继承主 Agent 的配置。只要在 agents.list 中分开了，它们就是从零开始的独立实体，需要单独调教。
• JSON 语法大坑：在终端使用 --json 命令传参时，非常容易出现引号转义错误或少写中括号/大括号。强烈建议在本地代码编辑器里写好完整的 JSON 字符串，格式化校验无误后，再复制粘贴到服务器执行。
