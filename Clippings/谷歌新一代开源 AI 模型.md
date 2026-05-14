---
title: "谷歌新一代开源 AI 模型"
source: "https://gemma4.cn/"
author:
  - "[[Gemma 4]]"
published:
created: 2026-04-07
description: "Gemma 4 是谷歌 DeepMind 推出的开源多模态模型系列，8 款模型采用 Apache 2.0 许可证，覆盖边缘到数据中心，支持文本、图像、视频和音频。"
tags:
  - "clippings"
---
## Gemma 4开放的力量

谷歌 DeepMind 新一代开源多模态模型。8 款模型覆盖手机到数据中心，基于 Gemini 3 同源技术打造，Apache 2.0 完全免费商用。

![Gemma 4 官方主视觉 — 谷歌 DeepMind 新一代开源多模态模型](https://gemma4.cn/img/hero.png)

8 款

开源模型

256K

最长上下文

89.2%

AIME 2026

#3

开源全球排名

模型矩阵

## 4 种架构 × 2 个版本 = 8 款模型

每种架构均提供 **预训练版（base）** 和 **指令微调版（-it）** ，共 8 款 Gemma 4 模型。预训练版适合二次微调，指令版开箱即用。

Edge

E2B

超轻量端侧模型

**激活** 2.3B  
**总量** 5.1B  
**上下文** 128K  
**显存** ~9.6 GB

文本图像音频

gemma-4-e2b / gemma-4-e2b-it

Edge

E4B

移动端均衡之选

**激活** 4.5B  
**总量** 8B  
**上下文** 128K  
**显存** ~15 GB

文本图像音频

gemma-4-e4b / gemma-4-e4b-it

MoE

26B-A4B

混合专家高效推理

**激活** 4B  
**总量** 26B  
**上下文** 256K  
**显存** ~48 GB

文本图像视频

gemma-4-26b-a4b / gemma-4-26b-a4b-it

旗舰

31B

稠密架构性能之巅

**激活** 30.7B  
**总量** 31B  
**上下文** 256K  
**显存** ~58 GB

文本图像视频

gemma-4-31b / gemma-4-31b-it

### 边缘层：E2B 和 E4B

采用 **PLE（逐层嵌入）** 技术，第二个嵌入表为每个解码器层提供残差信号，让小参数达到大模型 97% 的推理质量。独有 **音频输入** 能力，可做本地语音助手。E2B 量化后仅 1.5GB，树莓派 5 也能跑。

### 工作站层：26B-A4B 和 31B

26B 是混合专家架构，128 个专家仅激活 4B 参数，推理速度比同能力稠密模型快约 2.5 倍。31B 是全密集旗舰，LMArena 开源排名全球第三。两款均支持 **视频理解** （最长 60 秒），1024 token 滑动窗口注意力。

核心特性

## 为什么选择 Gemma 4

从架构到许可证，每一处都经过重新设计。

M

#### 原生多模态

文本、图像、视频、音频在同一 Transformer 空间统一处理，架构级融合而非外挂拼接。

A

#### Agent 原生支持

内置函数调用、结构化 JSON、多步规划和扩展思维链，开箱即用构建 AI Agent。

E

#### 端侧到云端

E2B 量化后不到 1.5GB 跑在树莓派上，31B 在 H100 上释放全部性能。一套模型覆盖所有场景。

L

#### Apache 2.0

无月活限制、无使用策略强制条款。商用、再分发、私有部署——做你想做的，不问许可。

C

#### 256K 超长上下文

双重 RoPE 位置编码，「大海捞针」测试准确率 99%+。滑动窗口 + 全局注意力交替工作。

K

#### 共享 KV 缓存

后 N 层复用前面层的 Key/Value 张量，显著降低显存占用，单卡推理成为可能。

![新特性一览 — 多模态、Agent 支持、256K 长上下文](https://gemma4.cn/img/feature-a.png) 基准测试

## Gemma 4 性能实测

数据来自谷歌官方技术报告。

![Gemma 4 模型在 LMArena ELO 评分与参数规模对比图](https://gemma4.cn/img/benchmark.svg)

LMArena ELO 评分 vs 模型参数规模 · 数据来源：Google DeepMind

### 推理与知识

| 基准 | 31B | 26B-A4B | E4B | E2B |
| --- | --- | --- | --- | --- |
| MMLU Pro | 85.2% | 82.6% | 69.4% | 60.0% |
| AIME 2026 | 89.2% | 88.3% | 42.5% | 37.5% |
| GPQA Diamond | 84.3% | 82.3% | 58.6% | 43.4% |
| BigBench Hard | 74.4% | 64.8% | 33.1% | 21.9% |

### 代码能力

| 基准 | 31B | 26B-A4B | E4B | E2B |
| --- | --- | --- | --- | --- |
| LiveCodeBench v6 | 80.0% | 77.1% | 52.0% | 44.0% |
| Codeforces ELO | 2150 | 1718 | 940 | 633 |

### 视觉理解

| 基准 | 31B | 26B-A4B | E4B | E2B |
| --- | --- | --- | --- | --- |
| MMMU Pro | 76.9% | 73.8% | 52.6% | 44.2% |
| MATH-Vision | 85.6% | 82.4% | 59.5% | 52.4% |

#### 与上代 Gemma 3 的跨越

AIME 数学推理

20.8% → 89.2%

旗舰模型推理能力跃升超过 4 倍

LiveCodeBench 代码

29.1% → 80.0%

代码生成实现推倒重来级跃迁

### 与竞品对比

Llama 4 使用 Meta 社区许可证，月活超 7 亿有限制。该系列的 Apache 2.0 没有任何门槛，对商业团队更友好。社区评测显示，在同等参数规模下性能更强——有评测直言「干掉了 13 倍体量的 Qwen 3.5」。

部署方案

## 快速部署指南

发布首日即获主流框架全面支持。

### 硬件需求一览

| 模型 | BF16 显存 | 推荐设备 |
| --- | --- | --- |
| E2B | ~9.6 GB | 手机、树莓派、Apple Silicon |
| E4B | ~15 GB | Jetson、消费级显卡 |
| 26B-A4B | ~48 GB | A100 / 双卡 4090 |
| 31B | ~58 GB | H100 / 多卡配置 |

### 支持框架

Hugging Face Transformers、vLLM、llama.cpp、Ollama、MLX、LM Studio、Google AI Studio、transformers.js (WebGPU) 等均已原生支持。

### 端侧实测

![边缘端部署 — 手机与芯片端侧推理示意图](https://gemma4.cn/img/feature-c.png)

E2B 2-bit 量化仅 **1.5GB** 。树莓派 5 实测预填充 133 tok/s、解码 7.6 tok/s。Android 和 iOS 通过 Google AI Edge Gallery 直接体验。4-bit 量化可将 31B 压缩到 20GB 以下。

#### 架构创新简述

**交替注意力** ——局部滑动窗口和全局注意力交替使用，平衡速度与长文本理解。 **双重 RoPE** ——让 256K 上下文不退化。 **PLE 逐层嵌入** ——小模型达到大模型 97% 质量的秘密。 **MoE 路由** ——128 个专家仅激活 8+1 个，效率之王。

## 7 种方式本地运行

国内网络可直接下载模型权重，从零代码到完全离线，选择适合你的方案。

#### 国内直接下载

以下平台均已同步全部 8 款模型，国内网络直连，速度快。

#### 方式一：ModelScope（魔搭社区）· 推荐

阿里云运营，国内速度最快，直连高速下载。

```
# 安装 ModelScope
pip install modelscope

# 下载旗舰模型（31B 指令版，约 62.5GB）
modelscope download --model google/gemma-4-31b-it --local_dir ./gemma-4-31b-it

# 下载边缘模型（E2B 指令版，最小）
modelscope download --model google/gemma-4-e2b-it --local_dir ./gemma-4-e2b-it

# 下载 MoE 模型
modelscope download --model google/gemma-4-26b-a4b-it --local_dir ./gemma-4-26b-a4b-it

# 下载 E4B
modelscope download --model google/gemma-4-e4b-it --local_dir ./gemma-4-e4b-it
```

```
from modelscope import snapshot_download

# 一行代码下载，自动缓存
model_dir = snapshot_download("google/gemma-4-e4b-it")
print(model_dir)  # 输出本地路径
```

#### 方式二：HF-Mirror（Hugging Face 镜像）

HuggingFace 官方仓库的国内镜像，模型最全。部分模型需要 HF Token。

```
# 设置镜像源环境变量
export HF_ENDPOINT=https://hf-mirror.com

# 安装 huggingface CLI
pip install huggingface_hub

# 下载模型
huggingface-cli download google/gemma-4-31B-it --local-dir ./gemma-4-31b-it

# 如果需要 Token（首次需在 huggingface.co 同意许可协议）
export HF_TOKEN=your_token_here
huggingface-cli download google/gemma-4-e4b-it --local-dir ./gemma-4-e4b-it
```

#### 方式三：Ollama 离线导入

先从镜像站下载 GGUF 量化文件，再导入 Ollama，绕过 Ollama 官方源。

```
# 1. 从 HF 镜像下载 GGUF 文件
export HF_ENDPOINT=https://hf-mirror.com
huggingface-cli download unsloth/gemma-4-E4B-it-GGUF \
    --include "*.gguf" --local-dir ./gguf

# 2. 创建 Modelfile
echo 'FROM ./gguf/gemma-4-E4B-it-Q8_0.gguf' > Modelfile

# 3. 导入并运行
ollama create gemma4-e4b -f Modelfile
ollama run gemma4-e4b
```

#### 全部模型国内链接

| 模型 | 大小 | ModelScope | HF 镜像 |
| --- | --- | --- | --- |
| E2B-it | ~10 GB | [下载](https://modelscope.cn/models/google/gemma-4-e2b-it) | [下载](https://hf-mirror.com/google/gemma-4-e2b-it) |
| E4B-it | ~16 GB | [下载](https://modelscope.cn/models/google/gemma-4-e4b-it) | [下载](https://hf-mirror.com/google/gemma-4-e4b-it) |
| 26B-A4B-it | ~48 GB | [下载](https://modelscope.cn/models/google/gemma-4-26b-a4b-it) | [下载](https://hf-mirror.com/google/gemma-4-26b-a4b-it) |
| 31B-it | ~62 GB | [下载](https://modelscope.cn/models/google/gemma-4-31b-it) | [下载](https://hf-mirror.com/google/gemma-4-31B-it) |

ModelScope 国内直连速度最快，推荐首选。HF 镜像模型更全但部分需要 Token。预训练版（base）将模型名中的 -it 去掉即可。

#### 安装 Ollama

Ollama 是最简单的本地部署方式，一行命令即可运行。

```
# Linux
curl -fsSL https://ollama.com/install.sh | sh

# macOS
brew install ollama

# Windows：从 ollama.com 下载安装包
```

#### 拉取并运行

```
# 默认模型（E4B，9.6GB）
ollama run gemma4

# 指定模型
ollama run gemma4:e2b    # 边缘模型，7.2GB
ollama run gemma4:26b    # MoE 模型，18GB
ollama run gemma4:31b    # 旗舰模型，20GB

# 图片理解
ollama run gemma4 "描述这张图片 /path/to/photo.png"
```

#### API 调用

Ollama 启动后自动监听 11434 端口，兼容 OpenAI API 格式。

```
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

response = client.chat.completions.create(
    model="gemma4",
    messages=[{"role": "user", "content": "你好"}]
)
print(response.choices[0].message.content)
```

推荐内存：E2B ≥ 8GB · E4B ≥ 10GB · 26B ≥ 20GB · 31B ≥ 24GB

#### 安装依赖

```
pip install -U transformers torch accelerate
pip install bitsandbytes  # 可选，用于量化
```

#### 快速推理 — Pipeline

```
from transformers import pipeline

pipe = pipeline("any-to-any", model="google/gemma-4-e4b-it", device_map="auto")

messages = [{
    "role": "user",
    "content": [{"type": "text", "text": "解释量子计算"}],
}]

output = pipe(messages, max_new_tokens=200, return_full_text=False)
print(output[0]["generated_text"])
```

#### 图片理解

```
messages = [{
    "role": "user",
    "content": [
        {"type": "image", "image": "https://example.com/photo.jpg"},
        {"type": "text", "text": "描述这张图片"},
    ],
}]

output = pipe(messages, max_new_tokens=200, return_full_text=False)
```

#### 4-bit 量化（节省显存）

```
from transformers import AutoModelForImageTextToText, BitsAndBytesConfig

config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
)

model = AutoModelForImageTextToText.from_pretrained(
    "google/gemma-4-31b-it",
    quantization_config=config,
    device_map="auto",
)
```

#### 启用思维链推理

```
inputs = processor.apply_chat_template(
    messages, tokenize=True, return_dict=True,
    return_tensors="pt", add_generation_prompt=True,
    enable_thinking=True,  # 开启思维链
).to(model.device)
```

HuggingFace 模型 ID：google/gemma-4-e2b-it · google/gemma-4-e4b-it · google/gemma-4-26b-a4b-it · google/gemma-4-31b-it

#### 安装 vLLM

vLLM 是高吞吐生产级推理引擎，适合需要并发的 API 服务。

```
pip install -U vllm
pip install transformers==5.5.0
```

#### 启动服务

```
# E4B 单卡
vllm serve google/gemma-4-E4B-it \
    --max-model-len 131072

# 26B MoE 单卡（24GB+ VRAM）
vllm serve google/gemma-4-26B-A4B-it \
    --max-model-len 32768 \
    --gpu-memory-utilization 0.90

# 31B 旗舰双卡并行
vllm serve google/gemma-4-31B-it \
    --tensor-parallel-size 2 \
    --max-model-len 32768
```

#### 调用 API

vLLM 原生兼容 OpenAI API，默认监听 8000 端口。

```
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")

response = client.chat.completions.create(
    model="google/gemma-4-26B-A4B-it",
    messages=[{"role": "user", "content": "你好"}],
    max_tokens=512,
    temperature=0.7
)
```

#### NVIDIA FP4 量化（H100 推荐）

```
vllm serve nvidia/Gemma-4-31B-IT-NVFP4 \
    --quantization modelopt \
    --tensor-parallel-size 8
```

vLLM 适合高并发场景，支持连续批处理（Continuous Batching），吞吐量显著高于原生 Transformers。

#### 编译 llama.cpp

llama.cpp 是纯 C++ 推理引擎，支持 CPU + GPU 混合推理，适合无 NVIDIA 显卡的设备。

```
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j
```

#### 下载 GGUF 量化模型

Unsloth 提供了优化的 GGUF 量化权重，推荐使用。

```
# 小模型用 Q8_0 量化
./llama.cpp/build/bin/llama-cli \
    -hf unsloth/gemma-4-E4B-it-GGUF:Q8_0 \
    --temp 1.0 --top-p 0.95 --top-k 64

# 大模型用 Dynamic 4-bit 量化
./llama.cpp/build/bin/llama-cli \
    -hf unsloth/gemma-4-26B-A4B-it-GGUF:UD-Q4_K_XL \
    --temp 1.0 --top-p 0.95 --top-k 64

# 31B 旗舰
./llama.cpp/build/bin/llama-cli \
    -hf unsloth/gemma-4-31B-it-GGUF:UD-Q4_K_XL \
    --temp 1.0 --top-p 0.95 --top-k 64
```

#### 启动 API 服务

```
./llama.cpp/build/bin/llama-server \
    -hf unsloth/gemma-4-26B-A4B-it-GGUF:UD-Q4_K_XL \
    --temp 1.0 --top-p 0.95 --top-k 64 \
    --chat-template-kwargs '{"enable_thinking":true}'
```

Google 官方推荐参数：temperature=1.0 · top\_p=0.95 · top\_k=64。GGUF 模型来源：unsloth/gemma-4-\*-GGUF

#### 零配置云端体验

Google AI Studio 是最快的体验方式——无需 GPU，无需安装任何东西。

#### 使用步骤

- 打开 **aistudio.google.com**
- 在模型选择中切换到该系列（支持 31B 和 26B）
- 直接开始对话，支持文本和图片输入
- 支持 Function Calling 和思维链模式
- 可一键导出 API 调用代码

#### 通过 API 调用

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemma-4-31b-it",
    contents="用一句话解释相对论",
)
print(response.text)
```

#### 国内下载渠道

- **ModelScope** — modelscope.cn/models/google（推荐，国内直连）
- **HF 镜像** — hf-mirror.com/google（HuggingFace 国内镜像）
- **Ollama** — 可从镜像站下载 GGUF 后手动导入

AI Studio 在国内访问可能受限。建议从 ModelScope 或 HF 镜像下载权重后本地部署。

#### Google AI Edge Gallery

在手机上完全离线运行模型，无需联网，零延迟。

#### 下载 App

- **Android** — Google Play 搜索「AI Edge Gallery」
- **iOS** — App Store 搜索「Google AI Edge Gallery」

#### 支持机型

- **E2B** ：2-bit 量化后仅 1.5GB，大部分中端手机可运行
- **E4B** ：需要 6GB+ 可用内存，旗舰手机推荐

#### 功能亮点

- 完全离线，数据不出设备
- 支持 140+ 语言
- 128K 上下文窗口
- Thinking Mode：可查看模型逐步推理过程
- Agent Skills：支持多步骤自主工作流

#### 开发者集成 — LiteRT-LM

想在自己的 App 中集成该模型，可使用 Google 提供的 LiteRT-LM SDK，支持 CPU + GPU 混合推理和结构化输出。

```
// build.gradle
implementation("com.google.ai.edge.litert:litert-lm:latest")

// 初始化并推理
val model = LlmInference.create(context, "gemma-4-e2b-it")
val result = model.generateResponse("你好")
```

E2B 在树莓派 5 实测：预填充 133 tok/s、解码 7.6 tok/s。手机端体验与桌面几乎无差别。

FAQ

## 常见问题

### Gemma 4 是什么？

谷歌 DeepMind 于 2026 年 4 月发布的开源多模态模型系列。基于 Gemini 3 同源技术，4 种架构各有 base 和 it 版本，共 8 款模型，采用 Apache 2.0 许可证。

### Gemma 4 有多少款模型？

共 8 款。E2B、E4B、26B-A4B、31B 四种架构，每种提供预训练版和指令微调版（-it）两个权重文件。

### Gemma 4 支持哪些模态？

全部模型支持文本和图像。26B 与 31B 额外支持视频（60 秒），E2B 与 E4B 额外支持音频输入（语音识别/翻译）。

### 可以商用吗？

完全可以。Apache 2.0 没有月活限制、没有强制使用策略，允许商用、再分发、嵌入产品和私有部署。

### 在哪里下载？

推荐 ModelScope（魔搭社区）直接下载，国内高速直连。也可通过 hf-mirror.com（HuggingFace 国内镜像）获取。海外用户可用 Hugging Face、Kaggle 或 Ollama。

### Gemma 4 可以在手机上运行吗？

可以。E2B 量化后不到 1.5GB，Android 和 iOS 均可通过 Google AI Edge Gallery 体验。

## 现在就开始构建

Apache 2.0 开源，免费商用，从本地到生产环境——没有门槛。