---
tags:
  - AI
  - Claude
  - 编程工具
  - 教程笔记
created: 2026-05-14
source: https://www.bilibili.com/video/BV1NvRyBzEhq
bilibili: BV1NvRyBzEhq
aliases:
  - Claude Code 教程
  - 60分钟掌握Claude Code
---

# 全网最全！60分钟全面掌握 Claude Code

> 视频来源：[B站 - 全网最全！60分钟全面掌握Claude Code～【附完整文档】](https://www.bilibili.com/video/BV1NvRyBzEhq)
> 配套资料见视频置顶评论

---

## 一、什么是 Claude Code

Claude Code 是 Anthropic 推出的**终端 AI 编程 Agent**，基于 **LLM Loop** 原理工作：

```
用户输入 → Claude 思考 → 调用工具（读/写/执行）→ 观察结果 → 继续思考 → ... → 输出结果
```

核心优势：
- **本地运行**：直接操作文件系统、终端
- **Harness 工程**：高度工程化的工具调用框架
- **上下文感知**：理解整个项目结构
- **多模态**：支持图片输入（截图、设计稿）

---

## 二、安装与启动

### 安装方式

| 方式 | 命令 |
|------|------|
| **npm** | `npm install -g @anthropic-ai/claude-code` |
| **Homebrew** | `brew install claude-code` |
| **WinGet** | `winget install Anthropic.ClaudeCode` |
| **原生安装 (macOS/Linux)** | `curl -fsSL https://claude.ai/install.sh \| bash` |
| **原生安装 (Windows)** | `irm https://claude.ai/install.ps1 \| iex` |

### 启动参数

```bash
# 基础启动
claude

# 一次性执行（无交互模式）
claude -p "分析这个项目"

# 继续上次对话
claude --continue   # 或 claude -c

# 恢复指定会话
claude --resume

# 跳过权限确认（CI/CD 中使用）
claude --dangerously-skip-permissions

# 指定工作目录
claude --cwd /path/to/project

# 添加额外目录到上下文
claude --add-dir ../shared

# 调试模式
claude --debug

# 更新
claude update
```

---

## 三、三种核心模式

按 `Shift + Tab` 切换模式：

| 模式 | 特点 | 适用场景 |
|------|------|----------|
| **普通模式** | 每个工具调用需手动确认 | 重要操作、学习阶段 |
| **自动接受模式** | 自动执行工具无需确认 | 信任度高的日常开发 |
| **Plan 模式** | 只做规划不动手修改 | 复杂任务先设计再执行 |

---

## 四、CLAUDE.md 三层记忆系统

Claude Code 的记忆系统采用**三层架构**，优先级从高到低：

| 层级 | 文件位置 | 作用 |
|------|----------|------|
| **子目录记忆** | `./子目录/CLAUDE.md` | 特定模块规范（**最高优先级**） |
| **项目记忆** | `./CLAUDE.md`（项目根目录） | 项目架构、技术栈、编码规范 |
| **全局记忆** | `~/.claude/CLAUDE.md` | 所有项目通用的个人偏好 |

> [!tip] 规则
> - Claude 自动**向上查找并合并**所有层级的 CLAUDE.md
> - 子目录配置覆盖父目录，项目配置优先于全局配置
> - 使用 `/init` 自动生成项目级 CLAUDE.md

### CLAUDE.md 编写要点

- 控制在 **100-200 行**
- 包含：项目架构、技术栈、编码规范、命名约定、测试策略
- 放在项目根目录，随代码一起版本管理
- 全局 CLAUDE.md 放个人偏好（语言、风格等）

---

## 五、核心斜杠命令

| 命令 | 功能 | 使用场景 |
|------|------|----------|
| `/init` | 初始化项目，自动生成 CLAUDE.md | 新项目首次使用 |
| `/compact` | 压缩对话上下文 | Token 接近上限时，可节省 50-60% |
| `/clear` | 清除会话历史 | 切换任务时避免上下文干扰 |
| `/cost` | 查看 Token 消耗和费用 | 监控 API 消耗 |
| `/model` | 切换 AI 模型 | 简单任务切 Haiku 省成本 |
| `/memory` | 在编辑器中打开记忆文件 | 快速更新项目规则 |
| `/review` | 触发代码审查 | PR 前自查代码质量 |
| `/doctor` | 环境诊断（检查 6 项配置） | 出现异常时排查 |
| `/help` | 显示所有可用命令 | 随时查阅 |
| `/mcp` | 管理 MCP 服务器 | 查看/添加/删除 MCP |
| `/resume` | 恢复历史会话 | 继续之前的工作 |
| `/add-dir` | 添加额外目录到上下文 | 引用外部仓库代码 |

### `/compact` 使用技巧

```bash
# 基本用法 - 自动压缩
/compact

# 带指令压缩 - 保留关键信息
/compact 重点关注认证错误和最后两个 commit 的修改
```

> [!warning] 注意
> 在任务边界处使用 compact，**不要在复杂任务中途使用**，可能丢失关键上下文。

---

## 六、会话管理

### 会话生命周期

```
创建会话 → 对话累积 → Token 增长 → /compact 压缩 → 继续工作 → /clear 清空
```

### 关键操作

- **`/resume`**：列出所有历史会话，选择恢复
- **`/compact`**：保留核心信息，丢弃冗余上下文
- **`/clear`**：完全清空，开始全新对话
- **`Ctrl+B`**：将任务放到后台执行

### Token 管理建议

- 每隔几个任务 `/cost` 检查消耗
- 简单任务（查文档、小修改）切换到 **Haiku** 模型（省约 80% Token）
- 复杂架构设计使用 **Opus** 模型

---

## 七、权限管理

### 权限模式配置

在 `.claude/settings.json` 中配置：

```json
{
  "permissions": {
    "allow": [
      "Bash(git:*)",
      "Bash(npm:*)",
      "Bash(npx:*)",
      "Read(*)",
      "Grep(*)"
    ],
    "deny": [
      "Bash(rm:*)",
      "Bash(git push:*)",
      "Bash(curl:*)"
    ]
  }
}
```

> [!tip] 权限粒度
> 可以精确到具体命令、参数、路径。例如 `Bash(git diff:*)` 放行所有 git diff，`Bash(curl:*)` 阻止所有网络请求。

---

## 八、Hooks 钩子系统

Hooks 在关键节点执行自定义脚本，五大生命周期：

| Hook 类型 | 触发时机 | 典型用途 |
|-----------|----------|----------|
| **UserPromptSubmit** | 用户发送消息前 | 输入验证、敏感词过滤 |
| **PreToolExecution** | 工具执行前 | 安全检查、危险命令拦截 |
| **PostToolExecution** | 工具执行后 | 结果审计、自动 lint |
| **Notification** | 发送通知时 | 自定义通知方式 |
| **Stop** | Claude 响应完成后 | 自动 Git 提交、清理 |

### 配置示例

```json
{
  "hooks": {
    "PreToolExecution": [{
      "command": "bash /path/to/security_check.sh",
      "timeout": 10000,
      "tools": ["Bash", "Write"]
    }],
    "Stop": [{
      "command": "bash /path/to/auto_commit.sh",
      "timeout": 5000
    }]
  }
}
```

---

## 九、MCP 服务器（Model Context Protocol）

MCP 让 Claude Code 获得更多外部工具能力。

### 常用命令

```bash
# 添加 MCP 服务器（用户级全局）
claude mcp add <名称> -s user -- npx -y <MCP包名>

# 添加 MCP 服务器（项目级）
claude mcp add <名称> -s project -- npx -y <MCP包名>

# 查看已安装列表
claude mcp list

# 删除
claude mcp remove <名称>

# 会话内交互管理
/mcp
```

### 推荐 MCP 服务器

| MCP 服务器 | 安装命令 | 用途 |
|------------|----------|------|
| **文件系统** | `@modelcontextprotocol/server-filesystem` | 读写指定目录外的文件 |
| **GitHub** | `@modelcontextprotocol/server-github` | Issue/PR 管理 |
| **PostgreSQL** | `@modelcontextprotocol/server-postgres` | 数据库查询 |
| **Puppeteer** | `@modelcontextprotocol/server-puppeteer` | 网页自动化/截图 |
| **Brave Search** | `@modelcontextprotocol/server-brave-search` | 网络搜索 |
| **Fetch** | `@anthropic/mcp-server-fetch` | API 调用/网页抓取 |
| **Playwright** | `@anthropic/mcp-server-playwright` | 浏览器自动化测试 |

### 配置文件

- 用户级：`~/.claude.json`
- 项目级：`.mcp.json`

---

## 十、自定义工具与 Skills

### 自定义斜杠命令

在 `.claude/commands/` 目录下创建 `.md` 文件即可定义斜杠命令：

```markdown
# .claude/commands/deploy.md
执行以下部署流程：
1. 运行测试套件 `npm test`
2. 构建项目 `npm run build`
3. 如果全部通过，执行 `npm run deploy`
```

使用：`/deploy`

### Skills 技能系统

Skills 是预定义的专业化工作流，通过 Skill 工具调用。常用内置 Skills：

- **/review**：代码审查
- **/init**：项目初始化
- **/simplify**：代码简化和重构审查
- **/security-review**：安全审查

---

## 十一、无头模式与自动化

### 非交互模式（CI/CD 集成）

```bash
# 单次提问
claude -p "审查这次 PR 的代码质量" --dangerously-skip-permissions

# 管道模式
echo "修复 src/auth.ts 的类型错误" | claude -p -

# 配合 git
git diff HEAD~1 | claude -p "审查这些改动"
```

### CI/CD 集成示例

```yaml
# GitHub Actions
- name: Claude Code Review
  run: |
    git diff origin/main...HEAD | claude -p "审查改动，列出潜在问题" --dangerously-skip-permissions
```

---

## 十二、多 Agent 协作

Claude Code 支持并行启动多个子 Agent：

- **Agent 团队**：主 Claude 分配任务给多个子 Agent
- **并行开发**：多个 Agent 同时处理不同文件/模块
- **独立审查**：一个 Agent 写代码，另一个 Agent 审查

```bash
# 在对话中直接要求
"启动两个子 Agent，一个修 bug，一个写测试"
```

---

## 十三、11 个提效技巧

1. **CLAUDE.md 要精简**：100-200 行，放架构、技术栈、编码规范
2. **善用 `/compact`**：在任务边界处压缩，不要在复杂任务中途使用
3. **经常看 `/cost`**：每完成一个主要任务就检查一次消耗
4. **简单任务切 Haiku**：Token 消耗可降约 80%
5. **复杂任务先用 Plan 模式**：设计好方案再动手
6. **MCP 作用域合理选择**：`-s user`（个人全局）、`-s project`（团队共享）
7. **权限最小化原则**：只放行必要的命令
8. **善用 Ctrl+B 后台任务**：长时间任务放到后台
9. **利用 `/add-dir` 引用外部代码**：不必把所有代码放一个仓库
10. **定期 `/doctor` 诊断**：确保环境健康
11. **利用 Git 集成**：让 Claude 自动创建 commit、管理分支

---

## 十四、安全与最佳实践

- 避免在 CLAUDE.md 中写入密钥/Token
- 使用 `deny` 规则阻止危险命令（`rm -rf`、`git push --force`）
- 代码审查仍然需要人工参与
- 注意 MCP 服务器的权限范围
- 在 CI/CD 使用 `--dangerously-skip-permissions` 时确保上下文可信
- 定期审查 `.claude/settings.json` 配置

---

## 十五、课程完整目录（23 章）

### 第一部分：快速入门与配置（7 章）

| 章节 | 内容 |
|------|------|
| 1 | 课程介绍与安装 — Claude Code 概念、安装方式 |
| 2 | 基础操作：命令与配置是起点 — CLI 参数、环境变量、配置文件 |
| 3 | 核心模式：按场景切换，效率拉满 — 三种模式、Shift+Tab 切换 |
| 4 | CLAUDE.md：全局记忆的核心 — 三层记忆架构、/init 初始化 |
| 5 | 会话管理：避免失控，高效推进 — /clear、/compact、/resume |
| 6 | 资源监控与批量任务 — /cost、后台任务 Ctrl+B、Token 管理 |
| 7 | 避坑与进阶：让 Claude 更"听话" — 权限管理、常见问题 |

### 第二部分：官方最佳实践（8 章）

| 章节 | 内容 |
|------|------|
| 8 | 上下文规则配置 — settings.json 详解 |
| 9 | 自定义工具配置 — 斜杠命令、Commands、Skills |
| 10 | MCP 服务器配置 — 安装、管理与实战 |
| 11 | 尝试常见工作流程 — 代码审查、调试、重构、测试 |
| 12 | 优化工作流程 — 最佳实践、提高成功率 |
| 13 | 无头模式自动化 — `claude -p`、CI/CD 集成 |
| 14 | 多 Claude 协作工作流 — Agent Teams、Sub-agents |
| 15 | 实践总结 — 回顾与核心要点 |

### 第三部分：企业级应用实战（8 章）

| 章节 | 内容 |
|------|------|
| 16 | 章节介绍与前言 |
| 17 | 案例一：效率提升 3-5 倍的大型项目改造 |
| 18 | 案例二：会议中的高效编码 |
| 19 | 案例三：Playwright MCP 增强 Bug 修复 |
| 20 | 案例四：快速理解和改造开源项目 |
| 21 | 案例五：多任务并行开发 |
| 22 | 11 个技巧让 Claude Code 成功率翻倍 |
| 23 | 安全风险 & 代码审查新挑战 & 总结 |

---

## 相关链接

- [Claude Code 官方文档](https://code.claude.com/docs)
- [Anthropic 官网](https://www.anthropic.com)
- [MCP 协议规范](https://modelcontextprotocol.io)
- [[欢迎|Obsidian Vault 首页]]

---

> [!summary] 总结
> Claude Code 是当前最强大的终端 AI 编程助手，核心在于：
> 1. **CLAUDE.md** 提供项目上下文记忆
> 2. **MCP** 扩展工具能力边界
> 3. **Hooks** 实现自动化工作流
> 4. **三种模式** 灵活应对不同场景
> 5. **无头模式** 让 CI/CD 也能用上 AI
>
> 掌握这些核心概念，就能从零基础到企业级应用。
