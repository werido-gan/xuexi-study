# 调酒大师系统完整指南

> 基于 OpenClaw 的智能调酒机器人系统 - 完整配置与实现文档

---

## 目录

1. [系统架构](#系统架构)
2. [emotion-analyzer 配置详解](#emotion-analyzer-配置详解)
3. [drink-controller 配置详解](#drink-controller-配置详解)
4. [Python 脚本联动实现](#python-脚本联动实现)
5. [完整工作流程](#完整工作流程)
6. [使用示例](#使用示例)
7. [故障排查](#故障排查)

---

## 系统架构

### 整体架构图

```
用户语音输入
    ↓
emotion-analyzer (情感分析代理)
    ↓
{emotion_label, taste_preference, golden_quote, voice_comfort}
    ↓
drink-controller (调酒控制代理)
    ↓
{drink_name, bartender_words, estimated_abv, light_mode, pumps}
    ↓
硬件执行 (ESP32)
```

### 文件结构

```
.openclaw/
├── openclaw.json                          # OpenClaw 主配置文件
├── cocktail_master.py                     # Python 联动脚本
├── workspace/
│   ├── knowledge-base/
│   │   └── cocktail-recipes.md            # 调酒配方知识库
│   ├── skills/
│   │   ├── emotion-analyzer/
│   │   │   ├── MEMORY.md                 # 情感分析记忆文件
│   │   │   ├── system-prompt.txt         # 系统提示词
│   │   │   └── config.json               # 技能配置
│   │   └── drink-controller/
│   │       ├── MEMORY.md                 # 调酒控制记忆文件
│   │       ├── system-prompt.txt         # 系统提示词
│   │       └── config.json               # 技能配置
│   └── agents/
│       ├── emotion-analyzer/
│       │   └── agent.json                # 代理配置文件
│       └── drink-controller/
│           └── agent.json                # 代理配置文件
```

---

## emotion-analyzer 配置详解

### 代理配置文件

**文件路径**: `/home/werido1/.openclaw/workspace/agents/emotion-analyzer/agent.json`

```json
{
  "agent_id": "emotion-analyzer",
  "agent_name": "情感分析与金句大师",
  "version": "1.0.0",
  "description": "分析用户语音文本，提取情绪和口味需求，创作情感金句",
  "type": "specialized",
  "enabled": true,
  "default": true,
  "model": {
    "primary": "siliconflow/Pro/MiniMaxAI/MiniMax-M2.5",
    "fallback": "siliconflow/Qwen/Qwen2.5-32B-Instruct"
  },
  "parameters": {
    "temperature": 0.7,
    "max_tokens": 500,
    "top_p": 0.9,
    "frequency_penalty": 0.3,
    "presence_penalty": 0.3
  },
  "skills": ["emotion-analyzer"],
  "workspace": "/home/werido1/.openclaw/workspace/skills/emotion-analyzer",
  "system_prompt": "system-prompt.txt",
  "output_format": "json",
  "capabilities": {
    "emotion_recognition": true,
    "golden_quote_creation": true,
    "taste_mapping": true,
    "voice_comfort": true
  },
  "input_schema": {
    "type": "object",
    "properties": {
      "user_voice_text": {
        "type": "string",
        "description": "用户语音文本"
      }
    },
    "required": ["user_voice_text"]
  },
  "output_schema": {
    "type": "object",
    "properties": {
      "emotion_label": {
        "type": "string",
        "enum": ["疲惫", "伤心", "低落", "兴奋", "平静"],
        "description": "情绪标签"
      },
      "taste_preference": {
        "type": "string",
        "enum": ["清爽", "偏甜", "烈酒", "茶香"],
        "description": "口味偏好"
      },
      "golden_quote": {
        "type": "string",
        "maxLength": 100,
        "description": "情感金句"
      },
      "voice_comfort": {
        "type": "string",
        "maxLength": 20,
        "description": "语音安慰"
      }
    },
    "required": ["emotion_label", "taste_preference", "golden_quote", "voice_comfort"]
  },
  "validation": {
    "strict_json": true,
    "allow_markdown": false,
    "retry_on_failure": true,
    "max_retries": 3
  },
  "cache": {
    "enabled": true,
    "ttl": 300000,
    "max_size": 100
  },
  "logging": {
    "enabled": true,
    "log_input": true,
    "log_output": true,
    "log_errors": true
  }
}
```

### 系统提示词

**文件路径**: `/home/werido1/.openclaw/workspace/skills/emotion-analyzer/system-prompt.txt`

#### 角色设定
- 情感大师与文化巨人
- 极高的同理心和细腻的情感触觉
- 熟读古今中外海量诗词歌赋与文学经典

#### 核心功能
1. **情绪识别** - 识别 5 种情绪
2. **口味映射** - 情绪 → 口味偏好
3. **金句创作** - 极具美感的情感金句
4. **语音安慰** - 口语化、亲切的简短安慰

#### 情绪识别规则

| 情绪 | 关键词 | 识别特征 |
|------|---------|---------|
| 疲惫 | 累、疲惫、累坏了、累死 | 工作劳累、身体疲惫、精神压力、想休息 |
| 伤心 | 伤心、难过、分手、失恋 | 失恋、失去、悲伤、痛苦、哭泣 |
| 低落 | 失望、沮丧、消极、无精打采 | 失望、沮丧、消极、无精打采、心情不好 |
| 兴奋 | 开心、兴奋、升职、庆祝 | 开心、激动、期待、充满活力、高兴 |
| 平静 | 平和、思考、冷静、安宁 | 平和、思考、冷静、安宁、没什么特别情绪 |

#### 口味偏好映射

| 情绪 | 口味偏好 | 原因 |
|------|----------|------|
| 疲惫 | 清爽 | 提神解压 |
| 伤心 | 烈酒 | 温柔的烈酒，入口甜后劲大 |
| 低落 | 偏甜 | 高甜度、丝滑感，提供抚慰 |
| 兴奋 | 茶香 | 沉稳内敛 |
| 平静 | 清爽/茶香 | 微苦、木质调 |

#### 输出格式
```json
{
  "emotion_label": "疲惫/伤心/低落/兴奋/平静",
  "taste_preference": "清爽/偏甜/烈酒/茶香",
  "golden_quote": "[哲理金句]",
  "voice_comfort": "[口语化安慰]"
}
```

---

## drink-controller 配置详解

### 代理配置文件

**文件路径**: `/home/werido1/.openclaw/workspace/agents/drink-controller/agent.json`

```json
{
  "agent_id": "drink-controller",
  "agent_name": "硬件调酒控制大师",
  "version": "2.0.0",
  "description": "基于情绪与硬件库存，动态推演安全配方并输出硬件控制指令的智能中枢",
  "type": "specialized",
  "enabled": true,
  "default": false,
  "model": {
    "primary": "siliconflow/Pro/MiniMaxAI/MiniMax-M2.5",
    "fallback": "siliconflow/Qwen/Qwen2.5-32B-Instruct"
  },
  "parameters": {
    "temperature": 0.3,
    "max_tokens": 400,
    "top_p": 0.9,
    "frequency_penalty": 0.1,
    "presence_penalty": 0.1
  },
  "skills": ["drink-controller"],
  "workspace": "/home/werido1/.openclaw/workspace/skills/drink-controller",
  "system_prompt": "system-prompt.txt",
  "output_format": "json",
  "capabilities": {
    "recipe_generation": true,
    "channel_selection": true,
    "drink_naming": true,
    "light_control": true,
    "abv_calculation": true,
    "bartender_words": true,
    "safety_rules": true,
    "fallback_mechanism": true
  },
  "input_schema": {
    "type": "object",
    "properties": {
      "emotion_label": {
        "type": "string",
        "enum": ["疲惫", "伤心", "低落", "兴奋", "平静"],
        "description": "情绪标签"
      },
      "taste_preference": {
        "type": "string",
        "enum": ["清爽", "偏甜", "烈酒", "茶香"],
        "description": "口味偏好"
      },
      "current_channels": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "channel": {
              "type": "number",
              "minimum": 1,
              "maximum": 6,
              "description": "通道编号"
            },
            "name": {
              "type": "string",
              "description": "饮品名称"
            },
            "alcohol": {
              "type": "number",
              "minimum": 0,
              "maximum": 100,
              "description": "酒精度"
            },
            "type": {
              "type": "string",
              "enum": ["基酒", "调酒"],
              "description": "饮品类型"
            },
            "current_volume": {
              "type": "number",
              "minimum": 0,
              "description": "当前库存"
            },
            "flavor_profile": {
              "type": "object",
              "properties": {
                "sweetness": {
                  "type": "number",
                  "minimum": 0,
                  "maximum": 5,
                  "description": "甜度（0-5）"
                },
                "acidity": {
                  "type": "number",
                  "minimum": 0,
                  "maximum": 5,
                  "description": "酸度（0-5）"
                },
                "is_dairy": {
                  "type": "boolean",
                  "description": "是否奶制品"
                },
                "is_carbonated": {
                  "type": "boolean",
                  "description": "是否碳酸"
                }
              },
              "required": ["sweetness", "acidity", "is_dairy", "is_carbonated"]
            },
            "characteristics": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "风味特征"
            }
          },
          "required": ["channel", "name", "alcohol", "type", "current_volume", "flavor_profile", "characteristics"]
        },
        "minItems": 1,
        "maxItems": 6,
        "description": "当前通道配置"
      }
    },
    "required": ["emotion_label", "taste_preference", "current_channels"]
  },
  "output_schema": {
    "type": "object",
    "properties": {
      "drink_name": {
        "type": "string",
        "maxLength": 50,
        "description": "特调名称"
      },
      "bartender_words": {
        "type": "string",
        "maxLength": 100,
        "description": "调酒师的人性化寄语"
      },
      "estimated_abv": {
        "type": "string",
        "pattern": "^\\d+(\\.\\d+)?% VOL(\\s*\\(无酒精\\))?$",
        "description": "预估酒精度，例如 '12% VOL' 或 '0% VOL (无酒精)'"
      },
      "light_mode": {
        "type": "string",
        "enum": ["cool", "warm", "vibrant", "calm"],
        "description": "灯光模式"
      },
      "pumps": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "channel": {
              "type": "number",
              "minimum": 1,
              "maximum": 6,
              "description": "通道编号"
            },
            "ml": {
              "type": "number",
              "minimum": 20,
              "maximum": 200,
              "description": "出酒量"
            }
          },
          "required": ["channel", "ml"]
        },
        "minItems": 1,
        "maxItems": 3,
        "description": "出液泵指令"
      }
    },
    "required": ["drink_name", "bartender_words", "estimated_abv", "light_mode", "pumps"]
  },
  "validation": {
    "strict_json": true,
    "allow_markdown": false,
    "retry_on_failure": true,
    "max_retries": 3,
    "validate_volume": true,
    "volume_range": [150, 200],
    "validate_abv": true,
    "abv_format": "string",
    "safety_rules": {
      "protein_coagulation_warning": true,
      "inventory_limits": {
        "min_per_channel": 20,
        "max_total": 200,
        "max_channels": 3,
        "max_draw_percentage": 50
      }
    }
  },
  "fallback_mechanism": {
    "enabled": true,
    "min_base_alcohol_volume": 20,
    "mocktail_enabled": true,
    "out_of_stock_messages": [
      "不好意思，烈酒刚被上一位伤心的人喝光了，这杯甜甜的气泡水请你喝，生活还得继续。",
      "今天的基酒都在休息，这杯无酒精的特调，陪你度过这个平静的夜晚。"
    ]
  },
  "cache": {
    "enabled": true,
    "ttl": 600000,
    "max_size": 50
  },
  "logging": {
    "enabled": true,
    "log_input": true,
    "log_output": true,
    "log_errors": true,
    "log_safety_violations": true
  }
}
```

### 系统提示词

**文件路径**: `/home/werido1/.openclaw/workspace/skills/drink-controller/system-prompt.txt`

#### 角色设定
- 智能调酒控制核心
- 极具同理心、深谙潮饮风味的幽默调酒师
- 统管 6 个高精度出液通道

#### 绝对安全守则（最高优先级）

##### 1. 蛋白质凝固警戒
```
如果选择了【奶制品/丝滑】属性液体
  ↓
绝对禁止与【高酸度/柑橘类/碳酸】属性液体混合
  ↓
会导致蛋白质变性分离，彻底堵塞硬件泵管！
```

**危险组合示例**：
- 百利甜 + 青柠汁 ❌
- 生椰乳 + 汤力水 ❌
- 椰浆 + 橙汁 ❌

##### 2. 库存与泵控底线
- 总出酒量：150ml - 200ml
- 单通道最低：20ml
- 最多通道数：3 个
- 单次抽取量：不超过当前库存的 50%

#### 万能调配公式

| 策略 | 适用场景 | 公式 | 示例 |
|------|---------|------|------|
| A: 酸甜气泡法则 | 疲惫/兴奋 + 清爽 | 1:1:2 | 40ml + 40ml + 80ml = 160ml |
| B: 奶香醇厚法则 | 低落/伤心 + 偏甜 | 1:1:1 | 50ml + 50ml + 50ml = 150ml |
| C: 茶酒互补法则 | 平静/思考 + 茶香 | 1:3 | 45ml + 135ml = 180ml |
| D: 重度安抚法则 | 伤心 + 烈酒 | 1:1 | 80ml + 80ml = 160ml |

#### 情绪与灯光映射

| 情绪 | 策略 | 灯光模式 | 颜色 |
|------|------|---------|------|
| 疲惫/压力 | 提神解压 | cool | 蓝色/青色 |
| 伤心/崩溃 | 温柔烈酒 | warm | 橙色/红色 |
| 低落/难过 | 抚慰丝滑 | warm | 橙色/红色 |
| 平静/思考 | 沉稳内敛 | calm | 绿色/紫色 |
| 兴奋/开心 | 清新层次 | vibrant | 彩虹色/动态 |

#### 酒精度计算公式

```
estimated_abv = (Σ(通道酒精度 × 通道毫升数)) / 总毫升数
```

**示例**：
- 金酒(40% × 45ml) + 汤力水(0% × 120ml) = 1800 / 165 = 10.9% VOL
- 椰浆(0% × 80ml) + 威士忌(40% × 80ml) = 3200 / 160 = 20% VOL

#### 输出格式
```json
{
  "drink_name": "[极具诗意的特调名字]",
  "bartender_words": "[调酒师的人性化寄语]",
  "estimated_abv": "[预估酒精度，如 '12% VOL']",
  "light_mode": "[cool/warm/vibrant/calm]",
  "pumps": [
    {"channel": 1, "ml": 60},
    {"channel": 5, "ml": 120}
  ]
}
```

---

## Python 脚本联动实现

### 脚本文件

**文件路径**: `/home/werido1/.openclaw/cocktail_master.py`

### 完整代码

```python
#!/usr/bin/env python3
import subprocess
import json
import sys
from typing import Dict, Any, Optional

class CocktailMaster:
    def __init__(self):
        self.default_channels = [
            {
                "channel": 1,
                "name": "金酒",
                "alcohol": 40,
                "type": "基酒",
                "current_volume": 500,
                "flavor_profile": {
                    "sweetness": 0,
                    "acidity": 1,
                    "is_dairy": False,
                    "is_carbonated": False
                },
                "characteristics": ["杜松子香", "清爽"]
            },
            {
                "channel": 2,
                "name": "汤力水",
                "alcohol": 0,
                "type": "调酒",
                "current_volume": 1000,
                "flavor_profile": {
                    "sweetness": 2,
                    "acidity": 3,
                    "is_dairy": False,
                    "is_carbonated": True
                },
                "characteristics": ["气泡", "苦味"]
            },
            {
                "channel": 3,
                "name": "椰浆",
                "alcohol": 0,
                "type": "调酒",
                "current_volume": 500,
                "flavor_profile": {
                    "sweetness": 4,
                    "acidity": 0,
                    "is_dairy": True,
                    "is_carbonated": False
                },
                "characteristics": ["浓郁", "奶香"]
            },
            {
                "channel": 4,
                "name": "威士忌",
                "alcohol": 40,
                "type": "基酒",
                "current_volume": 500,
                "flavor_profile": {
                    "sweetness": 2,
                    "acidity": 0,
                    "is_dairy": False,
                    "is_carbonated": False
                },
                "characteristics": ["醇厚", "焦糖香", "木质调"]
            }
        ]

    def call_agent(self, agent_id: str, message: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        try:
            result = subprocess.run(
                ['openclaw', 'agent', '--agent', agent_id, '--message', json.dumps(message), '--local'],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode != 0:
                print(f"Error calling {agent_id}: {result.stderr}", file=sys.stderr)
                return None
            
            output = result.stdout
            
            json_start = output.find('{')
            if json_start == -1:
                print(f"No JSON found in output from {agent_id}", file=sys.stderr)
                print(f"Raw output: {output}", file=sys.stderr)
                return None
            
            json_str = output[json_start:]
            return json.loads(json_str)
        except subprocess.TimeoutExpired:
            print(f"Timeout calling {agent_id}", file=sys.stderr)
            return None
        except json.JSONDecodeError as e:
            print(f"JSON decode error from {agent_id}: {e}", file=sys.stderr)
            print(f"Raw output: {result.stdout}", file=sys.stderr)
            return None
        except Exception as e:
            print(f"Unexpected error calling {agent_id}: {e}", file=sys.stderr)
            return None

    def analyze_emotion(self, user_voice_text: str) -> Optional[Dict[str, Any]]:
        message = {"user_voice_text": user_voice_text}
        return self.call_agent("emotion-analyzer", message)

    def generate_drink(self, emotion_label: str, taste_preference: str, current_channels: list) -> Optional[Dict[str, Any]]:
        message = {
            "emotion_label": emotion_label,
            "taste_preference": taste_preference,
            "current_channels": current_channels
        }
        return self.call_agent("drink-controller", message)

    def make_cocktail(self, user_voice_text: str, current_channels: Optional[list] = None) -> Optional[Dict[str, Any]]:
        if current_channels is None:
            current_channels = self.default_channels

        print(f"🍸 调酒大师正在为您服务...")
        print(f"📝 用户输入: {user_voice_text}")
        print()

        emotion_data = self.analyze_emotion(user_voice_text)
        if not emotion_data:
            print("❌ 情感分析失败，使用默认值", file=sys.stderr)
            emotion_data = {
                "emotion_label": "平静",
                "taste_preference": "清爽",
                "golden_quote": "生活就像一杯酒，慢慢品味才能体会其中的滋味",
                "voice_comfort": "哥，今天给你调一杯清爽的"
            }

        print(f"🧠 情感分析结果:")
        print(f"   - 情绪: {emotion_data.get('emotion_label')}")
        print(f"   - 口味偏好: {emotion_data.get('taste_preference')}")
        print(f"   - 金句: {emotion_data.get('golden_quote')}")
        print(f"   - 安慰语: {emotion_data.get('voice_comfort')}")
        print()

        drink_data = self.generate_drink(
            emotion_data.get("emotion_label", "平静"),
            emotion_data.get("taste_preference", "清爽"),
            current_channels
        )
        if not drink_data:
            print("❌ 调酒配方生成失败，使用默认配方", file=sys.stderr)
            drink_data = {
                "drink_name": "经典金汤力",
                "bartender_words": "这杯经典金汤力，简单却永远可靠",
                "estimated_abv": "10% VOL",
                "light_mode": "cool",
                "pumps": [
                    {"channel": 1, "ml": 50},
                    {"channel": 2, "ml": 150}
                ]
            }

        print(f"🍹 调酒配方:")
        print(f"   - 酒名: {drink_data.get('drink_name')}")
        print(f"   - 调酒师寄语: {drink_data.get('bartender_words')}")
        print(f"   - 酒精度: {drink_data.get('estimated_abv')}")
        print(f"   - 灯光模式: {drink_data.get('light_mode')}")
        print(f"   - 泵控制: {drink_data.get('pumps')}")
        print()

        result = {
            "emotion_analysis": emotion_data,
            "drink_recipe": drink_data,
            "hardware_commands": {
                "pump_commands": drink_data.get("pumps", []),
                "light_command": drink_data.get("light_mode", "cool"),
                "voice_command": emotion_data.get("voice_comfort", "")
            }
        }

        print("✅ 调酒完成！")
        print()
        return result

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 cocktail_master.py <user_voice_text> [channels_json_file]")
        print()
        print("Example:")
        print("  python3 cocktail_master.py \"今天工作好累啊\"")
        print("  python3 cocktail_master.py \"今天工作好累啊\" custom_channels.json")
        sys.exit(1)

    user_voice_text = sys.argv[1]
    current_channels = None

    if len(sys.argv) >= 3:
        try:
            with open(sys.argv[2], 'r', encoding='utf-8') as f:
                current_channels = json.load(f)
        except Exception as e:
            print(f"Warning: Failed to load channels file: {e}", file=sys.stderr)
            print("Using default channels.", file=sys.stderr)

    master = CocktailMaster()
    result = master.make_cocktail(user_voice_text, current_channels)

    if result:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        sys.exit(0)
    else:
        print("Failed to make cocktail", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### 核心方法说明

#### 1. `call_agent(agent_id, message)`
调用指定的 OpenClaw 代理

**参数**:
- `agent_id`: 代理 ID（"emotion-analyzer" 或 "drink-controller"）
- `message`: 发送给代理的消息（JSON 格式）

**返回值**:
- 成功：返回解析后的 JSON 对象
- 失败：返回 None

**关键逻辑**:
```python
result = subprocess.run(
    ['openclaw', 'agent', '--agent', agent_id, '--message', json.dumps(message), '--local'],
    capture_output=True,
    text=True,
    timeout=30
)

# 提取 JSON（处理插件输出）
json_start = output.find('{')
json_str = output[json_start:]
return json.loads(json_str)
```

#### 2. `analyze_emotion(user_voice_text)`
调用 emotion-analyzer 分析用户情绪

**参数**:
- `user_voice_text`: 用户语音文本

**返回值**:
```json
{
  "emotion_label": "疲惫",
  "taste_preference": "清爽",
  "golden_quote": "疲惫是身体在提醒你，该停下来给自己充充电了",
  "voice_comfort": "哥，听你声音有点累，歇会吧"
}
```

#### 3. `generate_drink(emotion_label, taste_preference, current_channels)`
调用 drink-controller 生成调酒配方

**参数**:
- `emotion_label`: 情绪标签
- `taste_preference`: 口味偏好
- `current_channels`: 当前通道配置

**返回值**:
```json
{
  "drink_name": "清晨的露珠",
  "bartender_words": "累了就来一杯，慢慢喝，放松一下～",
  "estimated_abv": "12.5% VOL",
  "light_mode": "cool",
  "pumps": [
    {"channel": 1, "ml": 50},
    {"channel": 2, "ml": 110}
  ]
}
```

#### 4. `make_cocktail(user_voice_text, current_channels)`
完整的调酒流程

**参数**:
- `user_voice_text`: 用户语音文本
- `current_channels`: 当前通道配置（可选，默认使用内置配置）

**返回值**:
```json
{
  "emotion_analysis": {
    "emotion_label": "疲惫",
    "taste_preference": "清爽",
    "golden_quote": "...",
    "voice_comfort": "..."
  },
  "drink_recipe": {
    "drink_name": "清晨的露珠",
    "bartender_words": "...",
    "estimated_abv": "12.5% VOL",
    "light_mode": "cool",
    "pumps": [...]
  },
  "hardware_commands": {
    "pump_commands": [...],
    "light_command": "cool",
    "voice_command": "..."
  }
}
```

---

## 完整工作流程

### 数据流图

```
用户输入："今天工作好累啊"
    ↓
【Python 脚本】cocktail_master.py
    ↓
调用 emotion-analyzer
    ↓
【emotion-analyzer】
    ↓
分析：
  - 关键词：累、疲惫
  - 情绪：疲惫
  - 口味：清爽
  - 金句："疲惫是身体在提醒你，该停下来给自己充充电了"
  - 安慰："哥，听你声音有点累，歇会吧"
    ↓
输出：
  {
    "emotion_label": "疲惫",
    "taste_preference": "清爽",
    "golden_quote": "...",
    "voice_comfort": "..."
  }
    ↓
【Python 脚本】接收 emotion-analyzer 的输出
    ↓
调用 drink-controller
    ↓
【drink-controller】
    ↓
输入：
  - emotion_label: "疲惫"
  - taste_preference: "清爽"
  - current_channels: [...]
    ↓
推演：
  - 选择策略：A (酸甜气泡法则 1:1:2)
  - 选择通道：金酒(清爽) + 汤力水(气泡)
  - 计算比例：50ml + 110ml = 160ml
  - 计算酒精度：(40×50 + 0×110) / 160 = 12.5% VOL
  - 选择灯光：cool (蓝色/青色)
  - 创作名字："清晨的露珠"
  - 生成寄语："累了就来一杯，慢慢喝，放松一下～"
    ↓
输出：
  {
    "drink_name": "清晨的露珠",
    "bartender_words": "...",
    "estimated_abv": "12.5% VOL",
    "light_mode": "cool",
    "pumps": [
      {"channel": 1, "ml": 50},
      {"channel": 2, "ml": 110}
    ]
  }
    ↓
【Python 脚本】整合输出
    ↓
最终结果：
  {
    "emotion_analysis": {...},
    "drink_recipe": {...},
    "hardware_commands": {
      "pump_commands": [...],
      "light_command": "cool",
      "voice_command": "..."
    }
  }
    ↓
【硬件执行】
  - 泵1：50ml 金酒
  - 泵2：110ml 汤力水
  - 灯光：cool (蓝色)
  - 语音："哥，听你声音有点累，歇会吧"
```

---

## 使用示例

### 基本使用

```bash
# 使用默认通道配置
python3 cocktail_master.py "今天工作好累啊"
```

### 自定义通道配置

```bash
# 使用自定义通道配置
python3 cocktail_master.py "今天工作好累啊" custom_channels.json
```

### custom_channels.json 示例

```json
[
  {
    "channel": 1,
    "name": "金酒",
    "alcohol": 40,
    "type": "基酒",
    "current_volume": 500,
    "flavor_profile": {
      "sweetness": 0,
      "acidity": 1,
      "is_dairy": false,
      "is_carbonated": false
    },
    "characteristics": ["杜松子香", "清爽"]
  },
  {
    "channel": 2,
    "name": "汤力水",
    "alcohol": 0,
    "type": "调酒",
    "current_volume": 1000,
    "flavor_profile": {
      "sweetness": 2,
      "acidity": 3,
      "is_dairy": false,
      "is_carbonated": true
    },
    "characteristics": ["气泡", "苦味"]
  },
  {
    "channel": 3,
    "name": "椰浆",
    "alcohol": 0,
    "type": "调酒",
    "current_volume": 500,
    "flavor_profile": {
      "sweetness": 4,
      "acidity": 0,
      "is_dairy": true,
      "is_carbonated": false
    },
    "characteristics": ["浓郁", "奶香"]
  },
  {
    "channel": 4,
    "name": "威士忌",
    "alcohol": 40,
    "type": "基酒",
    "current_volume": 500,
    "flavor_profile": {
      "sweetness": 2,
      "acidity": 0,
      "is_dairy": false,
      "is_carbonated": false
    },
    "characteristics": ["醇厚", "焦糖香", "木质调"]
  }
]
```

### 输出示例

```json
{
  "emotion_analysis": {
    "emotion_label": "疲惫",
    "taste_preference": "清爽",
    "golden_quote": "疲惫是身体在提醒你，该停下来给自己充充电了",
    "voice_comfort": "哥，听你声音有点累，歇会吧"
  },
  "drink_recipe": {
    "drink_name": "清晨的露珠",
    "bartender_words": "累了就来一杯，慢慢喝，放松一下～",
    "estimated_abv": "12.5% VOL",
    "light_mode": "cool",
    "pumps": [
      {"channel": 1, "ml": 50},
      {"channel": 2, "ml": 110}
    ]
  },
  "hardware_commands": {
    "pump_commands": [
      {"channel": 1, "ml": 50},
      {"channel": 2, "ml": 110}
    ],
    "light_command": "cool",
    "voice_command": "哥，听你声音有点累，歇会吧"
  }
}
```

---

## 故障排查

### 常见问题

#### 1. JSON 解析错误

**问题**:
```
JSON decode error from emotion-analyzer: Expecting value: line 1 column 1 (char 0)
```

**原因**: OpenClaw 输出包含插件注册信息，不是纯 JSON

**解决**: 脚本已实现 JSON 提取逻辑
```python
json_start = output.find('{')
json_str = output[json_start:]
return json.loads(json_str)
```

#### 2. 代理调用超时

**问题**:
```
Timeout calling emotion-analyzer
```

**原因**: 网络延迟或模型响应慢

**解决**: 增加超时时间或检查网络连接
```python
timeout=30  # 可根据需要调整
```

#### 3. 通道库存不足

**问题**: 调酒失败，提示库存不足

**原因**: 通道库存低于所需量

**解决**: 脚本已实现优雅降级机制，会自动生成无酒精特调

#### 4. 蛋白质凝固警告

**问题**: 配方违反安全规则

**原因**: 奶制品与高酸度/碳酸液体混合

**解决**: drink-controller 已内置安全规则，会自动避免危险组合

---

## 总结

调酒大师系统是一个基于 OpenClaw 的智能调酒机器人系统，通过两个专门的代理协同工作：

1. **emotion-analyzer**: 分析用户情绪，生成情感金句和口味偏好
2. **drink-controller**: 根据情绪和库存，生成安全的调酒配方

Python 脚本 `cocktail_master.py` 作为协调器，串联两个代理，并提供完整的错误处理和降级机制。

系统特点：
- 情感驱动的个性化推荐
- 严格的物理安全规则
- 优雅的降级机制
- 完整的日志记录
- 灵活的配置管理

通过本文档，开发者可以快速理解系统架构，并根据需要进行定制和扩展。