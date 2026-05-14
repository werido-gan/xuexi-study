# 🧠 大模型训练与开发终极学习手册
> 从零基础 → 工程级专家的完整路线图
> 版本：2026 | 覆盖最新架构（Transformer / MoE / 多模态 / 推理模型）

---

## 📋 目录

1. [🗺️ 学习路线图](#学习路线图)
2. [🔢 数学基础](#数学基础)
   - 线性代数
   - 概率论
   - 信息论
   - 优化算法
3. [🧩 深度学习基础](#深度学习基础)
   - 神经网络MLP
   - CNN / RNN / LSTM
   - Attention机制
   - Loss函数
4. [⚡ Transformer核心（最重要）](#transformer核心)
   - Self-Attention逐公式推导
   - Multi-Head Attention
   - Positional Encoding
   - Encoder/Decoder结构
   - 完整PyTorch实现
5. [🏗️ 大模型架构演进](#大模型架构演进)
   - GPT系列 / BERT / T5
   - MoE架构
   - 多模态模型
   - 推理模型 / Mamba / RWKV
6. [🔥 训练体系](#训练体系)
   - Tokenizer
   - 数据处理Pipeline
   - Pretraining / SFT / RLHF
   - Scaling Law
7. [⚙️ 工程系统](#工程系统)
   - PyTorch / DeepSpeed / FSDP
   - 分布式训练 DDP / ZeRO
   - 混合精度 / 显存优化
8. [🚀 推理与部署](#推理与部署)
   - KV Cache
   - vLLM / TensorRT
   - 量化 INT8 / GGUF
   - LoRA / QLoRA
9. [📊 数据工程](#数据工程)
10. [🔭 前沿技术（2025+）](#前沿技术)
11. [🛠️ 实战项目集](#实战项目集)
12. [📚 参考资料](#参考资料)

---

# 🗺️ 学习路线图

```
┌─────────────────────────────────────────────────────────────────────┐
│                    大模型工程师学习路线图                              │
│                                                                     │
│  阶段1: 基础 (4-6周)                                                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │ 线性代数  │→│  概率论   │→│  信息论   │→│  优化算法  │          │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘          │
│                          ↓                                          │
│  阶段2: 深度学习 (4-6周)                                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │   MLP    │→│ CNN/RNN   │→│ Attention │→│   Loss    │          │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘          │
│                          ↓                                          │
│  阶段3: Transformer (3-4周) ← 核心中的核心                          │
│  ┌──────────────────────────────────────────────────────┐         │
│  │  Self-Attn → MHA → PE → Encoder → Decoder → GPT实现  │         │
│  └──────────────────────────────────────────────────────┘         │
│                          ↓                                          │
│  阶段4: 大模型架构 (3-4周)                                           │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │  GPT系列  │→│   MoE    │→│  多模态   │→│  推理模型  │          │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘          │
│                          ↓                                          │
│  阶段5: 训练体系 (4-6周)                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │Tokenizer │→│Pretraining│→│   SFT    │→│   RLHF   │          │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘          │
│                          ↓                                          │
│  阶段6: 工程系统 (3-4周)                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                        │
│  │DeepSpeed │→│  ZeRO    │→│ 混合精度  │                        │
│  └──────────┘  └──────────┘  └──────────┘                        │
│                          ↓                                          │
│  阶段7: 部署 (2-3周)                                                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                        │
│  │  vLLM   │→│   量化    │→│ LoRA/部署 │                        │
│  └──────────┘  └──────────┘  └──────────┘                        │
│                          ↓                                          │
│  阶段8: 前沿 (持续)                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │  Agent   │→│   RAG    │→│  Mamba   │→│ 最新论文  │          │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘          │
└─────────────────────────────────────────────────────────────────────┘
```

**总时长估计：4-6个月（全职学习）**

---

# 🔢 数学基础

## 1.1 线性代数

### ✔ 通俗解释

把**向量**理解为"一列数字"，比如 [1, 2, 3] 代表三维空间中的一个点。
**矩阵**就是"一堆向量摞在一起"，比如图像可以用像素值矩阵表示。
**神经网络本质上就是一堆矩阵乘法**。

### ✔ 数学原理

**向量内积（点积）：**
```
a · b = Σᵢ aᵢbᵢ = |a||b|cos(θ)
```
意义：衡量两个向量的相似度，这正是Attention的基础！

**矩阵乘法：**
```
C = A × B
其中 C[i,j] = Σₖ A[i,k] × B[k,j]

A: (m, k)  B: (k, n)  →  C: (m, n)
```

**特征值/特征向量：**
```
Av = λv
A：矩阵，v：特征向量，λ：特征值
```
意义：矩阵对特征向量只做"拉伸"，不改变方向。用于PCA降维。

**SVD分解（矩阵压缩/LoRA的数学基础）：**
```
A = UΣVᵀ
U: 左奇异向量, Σ: 奇异值对角矩阵, V: 右奇异向量
```

### ✔ ASCII图解

```
矩阵乘法示意：

     B (3×2)
   ┌─────┐
   │b b  │
   │b b  │
   │b b  │
   └─────┘
A(2×3)  C(2×2)
┌───┐   ┌───┐
│a a│ × │c c│
│a a│   │c c│
└───┘   └───┘

每个c[i,j] = A的第i行 · B的第j列
```

### ✔ 代码实现

```python
import torch
import numpy as np

# 基础向量操作
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])

# 点积（Attention的核心运算）
dot = torch.dot(a, b)  # = 32.0

# 矩阵乘法
A = torch.randn(2, 3)
B = torch.randn(3, 4)
C = A @ B  # shape: (2, 4)
# 或者
C = torch.matmul(A, B)

# 批量矩阵乘法（实际模型中最常用）
# batch_size=8, seq_len=10, d_model=64
Q = torch.randn(8, 10, 64)
K = torch.randn(8, 10, 64)
# Attention中的QK^T
scores = Q @ K.transpose(-2, -1)  # shape: (8, 10, 10)

# 特征值分解
A_square = torch.randn(4, 4)
eigenvalues, eigenvectors = torch.linalg.eig(A_square)

# SVD分解（LoRA的基础）
U, S, Vh = torch.linalg.svd(A, full_matrices=False)
print(f"U: {U.shape}, S: {S.shape}, Vh: {Vh.shape}")
# 低秩近似（取前k个奇异值）
k = 2
A_approx = U[:, :k] @ torch.diag(S[:k]) @ Vh[:k, :]
```

### ✔ 常见错误 + 面试考点

**常见错误：**
- `A @ B` 和 `A * B` 混淆：前者是矩阵乘法，后者是逐元素乘法
- 维度顺序错误：PyTorch默认 `(batch, seq, feature)`，转置时用 `transpose(-2, -1)`

**面试考点：**
- Q：为什么Self-Attention用点积而不是其他相似度？
  A：计算高效（可并行），且有清晰的梯度，经实验效果最好。
- Q：矩阵乘法的时间复杂度？
  A：O(n³) 对于 n×n 矩阵，实际通过GPU并行大幅加速。

---

## 1.2 概率论

### ✔ 通俗解释

**概率**就是"某件事发生的可能性"。语言模型的本质是：给定前面的词，预测下一个词的概率分布。

### ✔ 数学原理

**概率分布：**
- **均匀分布**：所有结果等概率
- **高斯分布（正态分布）**：`N(μ, σ²)`，权重初始化常用
- **Softmax输出的是概率分布**

**贝叶斯定理：**
```
P(A|B) = P(B|A) × P(A) / P(B)

后验 = 似然 × 先验 / 证据
```

**最大似然估计（MLE）：**
```
θ* = argmax P(数据 | θ)

对于语言模型：
L(θ) = Σᵢ log P(xᵢ | x₁,...,xᵢ₋₁; θ)
```
这就是为什么语言模型的训练目标是"最大化训练数据的概率"。

**KL散度（衡量分布差异）：**
```
KL(P || Q) = Σₓ P(x) log(P(x)/Q(x)) ≥ 0
```
RLHF中用KL散度防止模型偏离太远。

### ✔ 代码实现

```python
import torch
import torch.nn.functional as F

# Softmax：将logits转为概率分布
logits = torch.tensor([2.0, 1.0, 0.1])
probs = F.softmax(logits, dim=-1)
# tensor([0.6590, 0.2424, 0.0986])  ← 加起来=1

# 采样（Temperature控制随机性）
def sample_with_temperature(logits, temperature=1.0):
    logits = logits / temperature
    probs = F.softmax(logits, dim=-1)
    return torch.multinomial(probs, num_samples=1)

# temperature=0.1: 更确定（趋向greedy）
# temperature=2.0: 更随机（更有创意但可能不连贯）

# 高斯初始化（神经网络权重初始化）
linear = torch.nn.Linear(512, 512)
torch.nn.init.normal_(linear.weight, mean=0, std=0.02)
# std=0.02 是GPT系列的标准初始化
```

### ✔ 面试考点

- Q：为什么语言模型训练用cross entropy而不是MSE？
  A：语言建模是分类问题（从词表中选词），cross entropy对概率分布建模更自然，且梯度更稳定。

---

## 1.3 信息论

### ✔ 通俗解释

**熵**衡量"不确定性"。抛均匀硬币的熵最高（最不确定），结果已知时熵为0。

### ✔ 数学原理

**香农熵：**
```
H(P) = -Σₓ P(x) log₂ P(x)
```

**交叉熵（训练损失的基础）：**
```
H(P, Q) = -Σₓ P(x) log Q(x)

语言模型中：
P = 真实分布（one-hot标签）
Q = 模型预测分布
loss = -log Q(正确词)
```

**关系：**
```
交叉熵 = 真实熵 + KL散度
H(P, Q) = H(P) + KL(P || Q)
```
所以最小化交叉熵 = 最小化KL散度 = 让模型分布逼近真实分布。

**困惑度（Perplexity）：**
```
PPL = exp(H(P, Q)) = exp(平均cross entropy)
```
PPL越低，模型越好。GPT-2的PPL约18，GPT-4约个位数。

### ✔ 代码实现

```python
import torch
import torch.nn.functional as F

# 交叉熵损失（语言模型训练核心）
# logits: (batch_size, seq_len, vocab_size)
# labels: (batch_size, seq_len)

logits = torch.randn(4, 128, 50257)  # GPT-2 vocab_size
labels = torch.randint(0, 50257, (4, 128))

# 方法1：直接用CrossEntropyLoss
loss_fn = torch.nn.CrossEntropyLoss()
loss = loss_fn(logits.view(-1, 50257), labels.view(-1))

# 方法2：手动计算（理解原理）
log_probs = F.log_softmax(logits, dim=-1)  # (4, 128, 50257)
# 取出正确标签的log概率
nll = -log_probs.gather(-1, labels.unsqueeze(-1)).squeeze(-1)
loss_manual = nll.mean()  # 和方法1相同

# 困惑度
import math
ppl = math.exp(loss.item())
print(f"Loss: {loss.item():.4f}, PPL: {ppl:.2f}")
```

---

## 1.4 优化算法

### ✔ 通俗解释

训练神经网络就是"在一座山上找最低点"。
- **SGD**：随机向下走一步
- **Adam**：记住之前走的方向，自适应调整步长

### ✔ 数学原理

**梯度下降：**
```
θ ← θ - η × ∇L(θ)

η: 学习率, ∇L: 梯度（损失函数对参数的偏导）
```

**SGD with Momentum：**
```
v ← β×v + ∇L(θ)
θ ← θ - η×v

β通常=0.9（记住90%的历史方向）
```

**Adam（自适应矩估计）：**
```
m ← β₁×m + (1-β₁)×g         ← 一阶矩（梯度均值）
v ← β₂×v + (1-β₂)×g²        ← 二阶矩（梯度方差）
m̂ = m/(1-β₁ᵗ)               ← 偏差修正
v̂ = v/(1-β₂ᵗ)               ← 偏差修正
θ ← θ - η × m̂/(√v̂ + ε)

β₁=0.9, β₂=0.999, ε=1e-8（典型值）
```

**AdamW（Adam + Weight Decay）：**
```
θ ← θ - η × [m̂/(√v̂ + ε) + λ×θ]
```
大模型标准优化器，L2正则化防止过拟合。

**学习率调度（Cosine Decay with Warmup）：**
```
                 /\
学习率          /  \
            warmup  \ cosine decay
                     \____________
                                  min_lr
```

### ✔ 代码实现

```python
import torch
import torch.optim as optim
from torch.optim.lr_scheduler import CosineAnnealingLR

model = torch.nn.Linear(512, 512)

# AdamW（大模型标准配置）
optimizer = optim.AdamW(
    model.parameters(),
    lr=3e-4,
    betas=(0.9, 0.95),    # GPT-3使用的值
    eps=1e-8,
    weight_decay=0.1      # 重要！防止过拟合
)

# Cosine LR调度器
total_steps = 100000
scheduler = CosineAnnealingLR(optimizer, T_max=total_steps, eta_min=1e-5)

# 带Warmup的调度（实际大模型训练必备）
def get_lr_with_warmup(step, warmup_steps, max_lr, min_lr, total_steps):
    if step < warmup_steps:
        return max_lr * step / warmup_steps
    progress = (step - warmup_steps) / (total_steps - warmup_steps)
    return min_lr + 0.5 * (max_lr - min_lr) * (1 + math.cos(math.pi * progress))

# 梯度裁剪（防止梯度爆炸，大模型必用）
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

# 训练循环示意
for step, batch in enumerate(dataloader):
    optimizer.zero_grad()
    loss = model(batch)
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
    optimizer.step()
    scheduler.step()
```

### ✔ 常见错误 + 面试考点

**常见错误：**
- 忘记 `optimizer.zero_grad()`，梯度会累积
- learning rate太大导致loss变NaN（先试1e-4，再调）
- 不用gradient clipping导致训练不稳定

**面试考点：**
- Q：Adam为什么比SGD更好？
  A：自适应学习率（每个参数独立调整），对超参数不敏感，训练初期收敛快。
- Q：为什么要用AdamW而不是Adam？
  A：Adam的weight decay实现有bug（衰减的是归一化后的梯度），AdamW直接对参数做L2，实践效果更好。

---

### 🛠️ 实战项目1：线性回归到神经网络

```python
"""
项目：从零实现一个手写数字识别
目标：理解前向传播、反向传播、梯度下降
"""
import torch
import torch.nn as nn
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 数据准备
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])
train_data = datasets.MNIST('./data', train=True, download=True, transform=transform)
train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

# 模型定义
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(784, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 10)
        )
    
    def forward(self, x):
        x = x.view(-1, 784)  # flatten
        return self.net(x)

model = MLP()
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
criterion = nn.CrossEntropyLoss()

# 训练
for epoch in range(5):
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        
        if batch_idx % 100 == 0:
            print(f'Epoch {epoch}, Step {batch_idx}, Loss: {loss.item():.4f}')
```

---

# 🧩 深度学习基础

## 2.1 神经网络（MLP）

### ✔ 通俗解释

神经网络就是多个"线性变换+非线性激活"堆叠：
```
输入 → [线性层 → 激活函数] × N → 输出
```
"非线性激活"是关键，没有它，无论叠多少层都只是一个线性变换。

### ✔ 数学原理

**单层：**
```
z = Wx + b        ← 线性变换
a = f(z)          ← 非线性激活
```

**反向传播（链式法则）：**
```
∂L/∂W = ∂L/∂a × ∂a/∂z × ∂z/∂W

梯度从输出层逐层往回传
```

**常用激活函数：**
```
ReLU:    f(x) = max(0, x)          ← 最常用，简单高效
GeLU:    f(x) = x × Φ(x)          ← Transformer标配
SiLU:    f(x) = x × sigmoid(x)     ← LLaMA使用
Sigmoid: f(x) = 1/(1+e^(-x))       ← 二分类输出
```

**为什么用GeLU？**
GeLU相比ReLU更平滑（x<0时不完全截断），实验上大模型表现更好。

### ✔ 代码实现

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class TransformerMLP(nn.Module):
    """Transformer中FFN层的标准实现"""
    def __init__(self, d_model=768, d_ff=3072, dropout=0.1):
        super().__init__()
        self.fc1 = nn.Linear(d_model, d_ff)
        self.fc2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, x):
        # x: (batch, seq_len, d_model)
        x = self.fc1(x)          # → (batch, seq_len, d_ff)
        x = F.gelu(x)            # 激活函数
        x = self.dropout(x)
        x = self.fc2(x)          # → (batch, seq_len, d_model)
        return x

# SwiGLU（LLaMA使用，性能更好）
class SwiGLU(nn.Module):
    def __init__(self, d_model, d_ff):
        super().__init__()
        self.w1 = nn.Linear(d_model, d_ff, bias=False)
        self.w2 = nn.Linear(d_ff, d_model, bias=False)
        self.w3 = nn.Linear(d_model, d_ff, bias=False)
    
    def forward(self, x):
        # SwiGLU: silu(Wx) * Vx
        return self.w2(F.silu(self.w1(x)) * self.w3(x))
```

---

## 2.2 Attention机制（核心基础）

### ✔ 通俗解释

Attention就是："当我处理这个词时，我需要关注句子中哪些其他位置？"

类比：读"猫坐在**垫子**上，**它**很舒服"——理解"它"时，你的注意力会自动关注"猫"。

### ✔ 数学原理

```
Attention(Q, K, V) = softmax(QKᵀ/√dₖ) × V

Q (Query):  "我想查询什么"
K (Key):    "我能提供什么索引"  
V (Value):  "实际的内容"
√dₖ:        缩放因子，防止点积值过大导致softmax梯度消失
```

**为什么除以√dₖ？**
当维度dₖ很大时，QK的点积会很大，softmax后梯度趋近0，训练困难。

---

# ⚡ Transformer核心

> **来源：** Vaswani et al., "Attention is All You Need", NeurIPS 2017

## 3.1 Self-Attention（逐步推导）

### ✔ 通俗解释

**Self-Attention的三步：**
1. 把每个词映射成Q、K、V三个向量
2. 计算每对词之间的相关性分数（Q·K）
3. 用分数对V做加权求和，得到新的词表示

### ✔ 数学原理（完整推导）

**Step 1：生成Q/K/V**
```
输入 X: (seq_len, d_model)  ← 比如 (10, 512)

Q = X @ W_Q    W_Q: (d_model, d_k)  → Q: (seq_len, d_k)
K = X @ W_K    W_K: (d_model, d_k)  → K: (seq_len, d_k)
V = X @ W_V    W_V: (d_model, d_v)  → V: (seq_len, d_v)
```

**Step 2：计算注意力分数**
```
scores = Q @ Kᵀ / √d_k    → (seq_len, seq_len)

例如 seq_len=4, d_k=64:
scores[i,j] = Q[i]·K[j]/8  ← 词i对词j的注意力
```

**Step 3：Mask（Decoder中必须）**
```
# 因果掩码（Causal Mask）防止看到未来词
mask = [
    [0,  -inf, -inf, -inf],
    [0,   0,  -inf, -inf],
    [0,   0,   0,  -inf],
    [0,   0,   0,   0  ]
]
scores = scores + mask
```

**Step 4：Softmax + 加权求和**
```
weights = softmax(scores)    → (seq_len, seq_len)，每行加起来=1
output = weights @ V          → (seq_len, d_v)
```

### ✔ 完整图解

```
        输入序列: ["The", "cat", "sat"]

               ↓ 线性投影 (W_Q, W_K, W_V)
        
        Q:  [q1]      K:  [k1]      V:  [v1]
            [q2]          [k2]          [v2]
            [q3]          [k3]          [v3]
        
               ↓ Q @ Kᵀ / √d_k
        
        注意力分数矩阵 (3×3):
        ┌────────────┬────────────┬────────────┐
        │ The→The    │ The→cat    │ The→sat    │
        ├────────────┼────────────┼────────────┤
        │ cat→The    │ cat→cat    │ cat→sat    │
        ├────────────┼────────────┼────────────┤
        │ sat→The    │ sat→cat    │ sat→sat    │
        └────────────┴────────────┴────────────┘
        
               ↓ Softmax (每行)
        
        注意力权重 (每行和为1)
        
               ↓ @ V
        
        输出: 每个位置 = Σ(权重 × V)
        [out1]  ← The的新表示（融合了全局信息）
        [out2]  ← cat的新表示
        [out3]  ← sat的新表示
```

### ✔ PyTorch实现（逐行注释）

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class SelfAttention(nn.Module):
    """
    单头Self-Attention完整实现
    输入 x: (batch_size, seq_len, d_model)
    输出:   (batch_size, seq_len, d_model)
    """
    def __init__(self, d_model=512, d_k=64):
        super().__init__()
        self.d_k = d_k
        
        # 线性投影层（不含bias是常见做法）
        self.W_Q = nn.Linear(d_model, d_k, bias=False)
        self.W_K = nn.Linear(d_model, d_k, bias=False)
        self.W_V = nn.Linear(d_model, d_k, bias=False)
        self.W_O = nn.Linear(d_k, d_model, bias=False)
    
    def forward(self, x, mask=None):
        batch_size, seq_len, d_model = x.shape
        
        # Step 1: 生成Q/K/V
        Q = self.W_Q(x)  # (batch, seq_len, d_k)
        K = self.W_K(x)  # (batch, seq_len, d_k)
        V = self.W_V(x)  # (batch, seq_len, d_k)
        
        # Step 2: 计算注意力分数
        scores = Q @ K.transpose(-2, -1)   # (batch, seq_len, seq_len)
        scores = scores / math.sqrt(self.d_k)  # 缩放
        
        # Step 3: 应用mask（可选）
        if mask is not None:
            scores = scores.masked_fill(mask == 0, float('-inf'))
        
        # Step 4: Softmax
        weights = F.softmax(scores, dim=-1)  # (batch, seq_len, seq_len)
        
        # Step 5: 加权求和
        output = weights @ V  # (batch, seq_len, d_k)
        
        # 输出投影
        output = self.W_O(output)  # (batch, seq_len, d_model)
        return output, weights

# 测试
batch_size, seq_len, d_model = 2, 10, 512
x = torch.randn(batch_size, seq_len, d_model)
attn = SelfAttention(d_model=512, d_k=64)
output, weights = attn(x)
print(f"输入 shape: {x.shape}")          # (2, 10, 512)
print(f"输出 shape: {output.shape}")     # (2, 10, 512)
print(f"注意力权重 shape: {weights.shape}")  # (2, 10, 10)
```

---

## 3.2 Multi-Head Attention（多头注意力）

### ✔ 通俗解释

单头Attention像用一种角度理解句子，**多头Attention**是同时用多种角度（"头"）理解，然后拼接结果。

- 第1个头：关注语法关系（主谓宾）
- 第2个头：关注语义关系（近义词）
- 第n个头：关注其他模式

### ✔ 数学原理

```
head_i = Attention(Q_i, K_i, V_i)    i = 1,...,h

MultiHead(Q,K,V) = Concat(head_1,...,head_h) @ W_O

维度：
- d_model = 512, h = 8 heads
- 每个头的d_k = d_model/h = 64
- 每个头输出: (seq_len, 64)
- 拼接后: (seq_len, 512)
- 经W_O后: (seq_len, 512)  ← 维度不变！
```

### ✔ 完整图解

```
输入 X (seq_len × d_model=512)
    │
    ├──W_Q₁──→ Q₁ ─┐
    ├──W_K₁──→ K₁ ─┤→ Head₁ = Attn(Q₁,K₁,V₁) → (seq,64)
    ├──W_V₁──→ V₁ ─┘
    │
    ├──W_Q₂──→ Q₂ ─┐
    ├──W_K₂──→ K₂ ─┤→ Head₂ = Attn(Q₂,K₂,V₂) → (seq,64)
    ├──W_V₂──→ V₂ ─┘
    │                                 ↓
    ...                         Concat all heads
    │                                 ↓
    └──W_Q₈..V₈→ Head₈ ────────→ (seq, 512) @ W_O → (seq, 512)
```

### ✔ PyTorch实现

```python
class MultiHeadAttention(nn.Module):
    """
    多头注意力（高效实现版本）
    """
    def __init__(self, d_model=512, n_heads=8, dropout=0.1):
        super().__init__()
        assert d_model % n_heads == 0
        
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_k = d_model // n_heads  # 每个头的维度
        
        # 合并投影（比分别定义h个投影更高效）
        self.W_Q = nn.Linear(d_model, d_model, bias=False)
        self.W_K = nn.Linear(d_model, d_model, bias=False)
        self.W_V = nn.Linear(d_model, d_model, bias=False)
        self.W_O = nn.Linear(d_model, d_model, bias=False)
        self.dropout = nn.Dropout(dropout)
    
    def split_heads(self, x):
        """(batch, seq, d_model) → (batch, n_heads, seq, d_k)"""
        batch, seq, _ = x.shape
        x = x.view(batch, seq, self.n_heads, self.d_k)
        return x.transpose(1, 2)  # (batch, n_heads, seq, d_k)
    
    def forward(self, x, mask=None):
        batch_size = x.shape[0]
        
        # 投影并分头
        Q = self.split_heads(self.W_Q(x))  # (batch, n_heads, seq, d_k)
        K = self.split_heads(self.W_K(x))
        V = self.split_heads(self.W_V(x))
        
        # 每个头计算注意力
        scores = Q @ K.transpose(-2, -1) / math.sqrt(self.d_k)
        
        if mask is not None:
            scores = scores.masked_fill(mask == 0, float('-inf'))
        
        weights = self.dropout(F.softmax(scores, dim=-1))
        output = weights @ V  # (batch, n_heads, seq, d_k)
        
        # 合并多头
        output = output.transpose(1, 2)  # (batch, seq, n_heads, d_k)
        output = output.contiguous().view(batch_size, -1, self.d_model)
        
        return self.W_O(output)  # (batch, seq, d_model)

# 或使用PyTorch内置（推荐生产使用）
mha = nn.MultiheadAttention(embed_dim=512, num_heads=8, batch_first=True)
x = torch.randn(2, 10, 512)
output, weights = mha(x, x, x)
```

---

## 3.3 Positional Encoding（位置编码）

### ✔ 通俗解释

Attention是"全局"的，它不知道词的顺序（"猫吃鱼"和"鱼吃猫"的Attention值相同！）。Position Encoding给每个位置加一个"标记"。

### ✔ 数学原理

**原始Transformer使用正弦位置编码：**
```
PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))

pos: 位置（0,1,2,...）
i:   维度索引（0,1,...,d_model/2）
```

**为什么这样设计？**
- 每个位置有唯一编码
- 任意两个位置之间的差只与相对距离有关（可推广到未见过的长度）
- 值域在[-1,1]，不影响模型训练稳定性

**现代LLM使用RoPE（旋转位置编码）：**
```
更好地处理长上下文，LLaMA/GPT-NeoX等使用
```

### ✔ 代码实现

```python
class PositionalEncoding(nn.Module):
    """原始Transformer正弦位置编码"""
    def __init__(self, d_model=512, max_len=5000, dropout=0.1):
        super().__init__()
        self.dropout = nn.Dropout(dropout)
        
        # 预计算位置编码表
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        
        # 频率项
        div_term = torch.exp(
            torch.arange(0, d_model, 2).float() * 
            (-math.log(10000.0) / d_model)
        )
        
        pe[:, 0::2] = torch.sin(position * div_term)  # 偶数维度
        pe[:, 1::2] = torch.cos(position * div_term)  # 奇数维度
        
        pe = pe.unsqueeze(0)  # (1, max_len, d_model)
        self.register_buffer('pe', pe)  # 不参与训练
    
    def forward(self, x):
        # x: (batch, seq_len, d_model)
        x = x + self.pe[:, :x.size(1), :]
        return self.dropout(x)


# RoPE（现代大模型标准）
class RotaryEmbedding(nn.Module):
    """旋转位置编码 - 来源：RoFormer (Su et al., 2021)"""
    def __init__(self, dim):
        super().__init__()
        inv_freq = 1.0 / (10000 ** (torch.arange(0, dim, 2).float() / dim))
        self.register_buffer('inv_freq', inv_freq)
    
    def forward(self, seq_len, device):
        t = torch.arange(seq_len, device=device).float()
        freqs = torch.outer(t, self.inv_freq)
        emb = torch.cat((freqs, freqs), dim=-1)
        return emb.cos(), emb.sin()

def rotate_half(x):
    x1, x2 = x.chunk(2, dim=-1)
    return torch.cat((-x2, x1), dim=-1)

def apply_rope(q, k, cos, sin):
    q_rot = (q * cos) + (rotate_half(q) * sin)
    k_rot = (k * cos) + (rotate_half(k) * sin)
    return q_rot, k_rot
```

---

## 3.4 完整Transformer实现

### ✔ 结构图解

```
                    Transformer Block (×N层)
                    
输入 → Embedding + PE
         │
         ▼
    ┌────────────────────────────┐
    │ ┌──────────────────────┐   │
    │ │   Multi-Head Attn    │   │
    │ └──────────────────────┘   │
    │          │                 │
    │    + x (残差连接)           │
    │          │                 │
    │    LayerNorm               │
    │          │                 │
    │ ┌──────────────────────┐   │
    │ │   Feed Forward (MLP) │   │
    │ └──────────────────────┘   │
    │          │                 │
    │    + x (残差连接)           │
    │          │                 │
    │    LayerNorm               │
    └────────────────────────────┘
         │
         ▼
    Linear + Softmax → 下一个词的概率
```

### ✔ 完整GPT风格Transformer（PyTorch逐行实现）

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class LayerNorm(nn.Module):
    """带可学习参数的LayerNorm"""
    def __init__(self, d_model, eps=1e-5):
        super().__init__()
        self.weight = nn.Parameter(torch.ones(d_model))
        self.bias = nn.Parameter(torch.zeros(d_model))
        self.eps = eps
    
    def forward(self, x):
        mean = x.mean(-1, keepdim=True)
        std = x.std(-1, keepdim=True)
        return self.weight * (x - mean) / (std + self.eps) + self.bias


class CausalSelfAttention(nn.Module):
    """GPT风格的因果自注意力（只能看到过去）"""
    def __init__(self, config):
        super().__init__()
        self.n_heads = config.n_heads
        self.d_k = config.d_model // config.n_heads
        
        self.qkv = nn.Linear(config.d_model, 3 * config.d_model, bias=False)
        self.proj = nn.Linear(config.d_model, config.d_model, bias=False)
        self.dropout = nn.Dropout(config.dropout)
        
        # 因果mask（注册为buffer，不参与训练）
        max_len = config.max_seq_len
        mask = torch.tril(torch.ones(max_len, max_len))
        self.register_buffer('mask', mask.view(1, 1, max_len, max_len))
    
    def forward(self, x):
        B, T, C = x.shape  # batch, seq_len, d_model
        
        # 一次性计算QKV
        qkv = self.qkv(x)  # (B, T, 3*C)
        Q, K, V = qkv.split(C, dim=-1)
        
        # 分头
        def split_head(t):
            return t.view(B, T, self.n_heads, self.d_k).transpose(1, 2)
        Q, K, V = split_head(Q), split_head(K), split_head(V)
        # 现在: (B, n_heads, T, d_k)
        
        # 注意力计算
        scores = Q @ K.transpose(-2, -1) / math.sqrt(self.d_k)
        scores = scores.masked_fill(self.mask[:,:,:T,:T] == 0, float('-inf'))
        weights = self.dropout(F.softmax(scores, dim=-1))
        
        out = weights @ V  # (B, n_heads, T, d_k)
        out = out.transpose(1, 2).contiguous().view(B, T, C)
        return self.proj(out)


class TransformerBlock(nn.Module):
    """完整的Transformer Block（Pre-LN风格，更稳定）"""
    def __init__(self, config):
        super().__init__()
        self.ln1 = LayerNorm(config.d_model)
        self.attn = CausalSelfAttention(config)
        self.ln2 = LayerNorm(config.d_model)
        self.mlp = nn.Sequential(
            nn.Linear(config.d_model, 4 * config.d_model),
            nn.GELU(),
            nn.Linear(4 * config.d_model, config.d_model),
            nn.Dropout(config.dropout)
        )
    
    def forward(self, x):
        # 残差连接 + Pre-LN（先归一化再计算，更稳定）
        x = x + self.attn(self.ln1(x))
        x = x + self.mlp(self.ln2(x))
        return x


class GPT(nn.Module):
    """完整GPT模型"""
    def __init__(self, config):
        super().__init__()
        self.config = config
        
        self.transformer = nn.ModuleDict({
            'wte': nn.Embedding(config.vocab_size, config.d_model),    # token embedding
            'wpe': nn.Embedding(config.max_seq_len, config.d_model),   # position embedding
            'drop': nn.Dropout(config.dropout),
            'blocks': nn.ModuleList([TransformerBlock(config) for _ in range(config.n_layers)]),
            'ln_f': LayerNorm(config.d_model)
        })
        self.lm_head = nn.Linear(config.d_model, config.vocab_size, bias=False)
        
        # 权重绑定（embedding和lm_head共享权重，减少参数量）
        self.transformer.wte.weight = self.lm_head.weight
        
        # 初始化权重
        self.apply(self._init_weights)
    
    def _init_weights(self, module):
        if isinstance(module, nn.Linear):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)
            if module.bias is not None:
                torch.nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)
    
    def forward(self, idx, targets=None):
        B, T = idx.shape
        
        # Token + Position Embedding
        tok_emb = self.transformer.wte(idx)           # (B, T, d_model)
        pos = torch.arange(T, device=idx.device)
        pos_emb = self.transformer.wpe(pos)            # (T, d_model)
        x = self.transformer.drop(tok_emb + pos_emb)
        
        # 通过所有Transformer层
        for block in self.transformer.blocks:
            x = block(x)
        
        x = self.transformer.ln_f(x)
        logits = self.lm_head(x)  # (B, T, vocab_size)
        
        # 计算损失
        loss = None
        if targets is not None:
            loss = F.cross_entropy(
                logits.view(-1, logits.size(-1)),
                targets.view(-1),
                ignore_index=-1  # padding位置不计算损失
            )
        return logits, loss
    
    @torch.no_grad()
    def generate(self, idx, max_new_tokens, temperature=1.0, top_k=None):
        """自回归生成"""
        for _ in range(max_new_tokens):
            # 截断到最大序列长度
            idx_cond = idx[:, -self.config.max_seq_len:]
            logits, _ = self(idx_cond)
            logits = logits[:, -1, :] / temperature  # 只取最后一个位置
            
            if top_k is not None:
                v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
                logits[logits < v[:, [-1]]] = float('-inf')
            
            probs = F.softmax(logits, dim=-1)
            next_token = torch.multinomial(probs, num_samples=1)
            idx = torch.cat((idx, next_token), dim=1)
        return idx


# 配置
from dataclasses import dataclass

@dataclass
class GPTConfig:
    vocab_size: int = 50257
    max_seq_len: int = 1024
    d_model: int = 768
    n_layers: int = 12
    n_heads: int = 12
    dropout: float = 0.1

# 实例化GPT-2 small
config = GPTConfig()
model = GPT(config)
total_params = sum(p.numel() for p in model.parameters())
print(f"参数量: {total_params/1e6:.1f}M")  # 约125M

# 前向传播测试
idx = torch.randint(0, 50257, (2, 128))  # batch=2, seq_len=128
targets = torch.randint(0, 50257, (2, 128))
logits, loss = model(idx, targets)
print(f"Logits shape: {logits.shape}")  # (2, 128, 50257)
print(f"Loss: {loss.item():.4f}")
```

---

# 🏗️ 大模型架构演进

## 4.1 GPT系列演进

```
GPT-1 (2018)    GPT-2 (2019)    GPT-3 (2020)    GPT-4 (2023)
  117M params      1.5B params    175B params    ~1.8T (估计MoE)
  BooksCorpus      更多网络数据    CommonCrawl    多模态输入
  12层Decoder      48层Decoder    96层Decoder    RLHF对齐
  
关键进步：规模 + 数据 + RLHF对齐
```

| 模型 | 参数量 | 关键创新 | 局限 |
|------|--------|---------|------|
| GPT-1 | 117M | Decoder-only预训练 | 小规模，能力有限 |
| GPT-2 | 1.5B | 大规模预训练，zero-shot | 无对齐，可能生成有害内容 |
| GPT-3 | 175B | In-context learning，few-shot | 推理成本高，无法微调 |
| InstructGPT | 175B | RLHF对齐 | 创始了现代对话AI |
| GPT-4 | ~1.8T? | 多模态，更强推理 | 闭源，成本高 |

## 4.2 BERT vs GPT对比

```
BERT (Encoder)                  GPT (Decoder)
─────────────────────────────────────────────
双向上下文（看全文）              单向（只看过去）
适合：分类、NER、QA              适合：文本生成、对话
[MASK] 预训练目标                 下一词预测目标
BERT-base: 110M参数              GPT-2: 117M-1.5B
```

## 4.3 T5 (Text-to-Text Transfer Transformer)

**关键思想：所有NLP任务统一为Text→Text格式**
```
翻译: "translate English to French: The cat sat"
摘要: "summarize: Long article..."
QA:   "question: What is... context: ..."
```

## 4.4 MoE架构（Mixture of Experts）

### ✔ 通俗解释

MoE就是"多个专家，每次只请几个"。模型有N个FFN（专家），每个token只激活Top-K个专家，大幅降低计算量。

### ✔ 数学原理

```
MoE输出 = Σᵢ gate_i(x) × Expert_i(x)

其中：
gate(x) = softmax(x @ W_gate)   ← 路由网络
Top-K(gate) ← 只取前K个，其余设为0

计算量：密集模型的 K/N（K=2, N=8 → 25%计算量）
但参数量是密集模型的N倍
```

### ✔ MoE图解

```
输入 token
    │
    ▼
┌─────────┐
│  Router │  → [0.1, 0.6, 0.05, 0.25, ...]  Top-2选择
└─────────┘           ↓         ↓
               ┌──────────┐  ┌──────────┐
               │ Expert 2 │  │ Expert 4 │
               └──────────┘  └──────────┘
                    ↓              ↓
               0.6×out₂ + 0.25×out₄ = 最终输出
```

### ✔ DeepSeek MoE架构

**来源：DeepSeek-V2/V3 (2024)**

DeepSeek创新：
1. **细粒度专家**：将标准专家切分为更细粒度（更多但更小的专家）
2. **共享专家**：部分专家被所有token共享（处理通用知识）
3. **无辅助损失负载均衡**：通过偏置项平衡专家负载
4. **MLA（Multi-head Latent Attention）**：KV缓存压缩

```python
class MoELayer(nn.Module):
    """简化的MoE层实现"""
    def __init__(self, d_model=512, n_experts=8, top_k=2, d_ff=2048):
        super().__init__()
        self.n_experts = n_experts
        self.top_k = top_k
        
        # 路由网络
        self.router = nn.Linear(d_model, n_experts, bias=False)
        
        # 专家网络（每个专家是一个FFN）
        self.experts = nn.ModuleList([
            nn.Sequential(
                nn.Linear(d_model, d_ff),
                nn.GELU(),
                nn.Linear(d_ff, d_model)
            ) for _ in range(n_experts)
        ])
    
    def forward(self, x):
        B, T, C = x.shape
        x_flat = x.view(-1, C)  # (B*T, C)
        
        # 路由得分
        router_logits = self.router(x_flat)  # (B*T, n_experts)
        
        # Top-K路由
        top_k_scores, top_k_indices = torch.topk(
            torch.softmax(router_logits, dim=-1), 
            self.top_k, 
            dim=-1
        )
        # 归一化权重
        top_k_scores = top_k_scores / top_k_scores.sum(dim=-1, keepdim=True)
        
        # 调用选中的专家
        output = torch.zeros_like(x_flat)
        for i in range(self.top_k):
            expert_idx = top_k_indices[:, i]  # (B*T,)
            for e in range(self.n_experts):
                mask = (expert_idx == e)
                if mask.any():
                    expert_out = self.experts[e](x_flat[mask])
                    output[mask] += top_k_scores[mask, i:i+1] * expert_out
        
        return output.view(B, T, C)
    
    def load_balancing_loss(self, router_logits):
        """辅助损失：防止所有token都路由到同一个专家"""
        probs = torch.softmax(router_logits, dim=-1)
        # 每个专家被选中的频率
        freq = probs.mean(dim=0)
        # 鼓励均匀分布
        return self.n_experts * (freq * freq).sum()
```

## 4.5 多模态模型

### CLIP（对比语言-图像预训练）

**来源：Radford et al., OpenAI 2021**

```
图像编码器 (ViT/ResNet)      文本编码器 (Transformer)
         │                           │
         ▼                           ▼
    图像特征向量              文本特征向量
         │                           │
         └──────── 对比学习 ─────────┘
                      │
              相似图文拉近，不相似拉远
```

```python
# CLIP风格对比损失
def clip_loss(image_features, text_features, temperature=0.07):
    # 归一化
    image_features = F.normalize(image_features, dim=-1)
    text_features = F.normalize(text_features, dim=-1)
    
    # 相似度矩阵
    logits = (image_features @ text_features.T) / temperature
    
    # 对角线是正样本
    n = logits.shape[0]
    labels = torch.arange(n, device=logits.device)
    
    # 双向对比损失
    loss_i = F.cross_entropy(logits, labels)       # 图→文
    loss_t = F.cross_entropy(logits.T, labels)     # 文→图
    return (loss_i + loss_t) / 2
```

### GPT-4V / LLaVA架构

```
图像 → Vision Encoder (ViT) → Image tokens
                                    │
                                    ▼
文本 → Tokenizer → Text tokens → LLM Decoder → 输出
```

## 4.6 Mamba（状态空间模型）

**来源：Gu & Dao, "Mamba: Linear-Time Sequence Modeling with Selective State Spaces", 2023**

### ✔ 为什么出现Mamba？

Transformer的痛点：
- 注意力计算复杂度：O(N²)，长序列很慢
- KV Cache随上下文增长无限增大

Mamba的解决：
- 线性复杂度 O(N)
- 固定大小的状态（状态空间模型）
- 选择性机制：根据输入决定记忆什么、忘记什么

```python
# SSM核心公式
# h'(t) = Ah(t) + Bx(t)   ← 状态更新
# y(t) = Ch(t) + Dx(t)    ← 输出

# Mamba的创新：A, B, C 是输入的函数（选择性）
# 而不是固定参数
```

## 4.7 RWKV（RNN + Transformer混合）

**特点：**
- 训练像Transformer（并行），推理像RNN（高效）
- 线性注意力，无二次复杂度
- 适合超长序列和资源受限环境

```
         Transformer   RWKV/Mamba   RNN
训练速度      快          快          慢
推理复杂度   O(N²)       O(N)        O(N)
长序列性能    好          好          差（梯度消失）
```

---

# 🔥 训练体系

## 5.1 Tokenizer（分词器）

### ✔ 通俗解释

Tokenizer把文本切成模型能理解的"碎片"（token）。不是按字或词切，而是基于统计的子词切分。

```
"unbelievable" → ["un", "believ", "able"]
"ChatGPT是最好的" → ["Chat", "G", "PT", "是", "最好", "的"]
```

### ✔ BPE算法（Byte-Pair Encoding）

**来源：Sennrich et al., 2015，GPT/LLaMA使用**

```
算法步骤：
1. 初始词表：所有字符
2. 统计最高频的相邻字符对
3. 合并最高频对为新符号
4. 重复步骤2-3直到词表达到目标大小

例：
初始: ["l","o","w"] ["l","o","w","e","r"] ["n","e","w"]
频率最高对: (l,o) → "lo"
合并后: ["lo","w"] ["lo","w","e","r"] ["n","e","w"]
继续合并: (lo,w) → "low"
最终词表包含: "low", "lower", "new"...
```

### ✔ 代码实现（使用tiktoken/tokenizers库）

```python
# 使用HuggingFace tokenizers
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace

# 训练BPE tokenizer
tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
tokenizer.pre_tokenizer = Whitespace()
trainer = BpeTrainer(
    vocab_size=32000,  # LLaMA词表大小
    special_tokens=["[UNK]", "[BOS]", "[EOS]", "[PAD]"]
)
# 从文件训练
# tokenizer.train(files=["corpus.txt"], trainer=trainer)

# 使用tiktoken（GPT系列）
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")  # GPT-4的tokenizer

text = "Hello, world! 你好世界"
tokens = enc.encode(text)
print(f"Token IDs: {tokens}")
print(f"Token数量: {len(tokens)}")
decoded = enc.decode(tokens)

# 使用transformers库
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
output = tokenizer("Hello, world!", return_tensors="pt")
print(output.input_ids)  # tensor([[1, 15043, 29892, 3186, 29991]])
```

---

## 5.2 Pretraining（预训练）

### ✔ 完整数据处理Pipeline

```
原始网络数据
    │
    ▼
1. 语言检测 (fasttext)
    │
    ▼
2. URL/内容过滤
    ├── 去掉色情/暴力内容
    ├── 去掉低质量内容（短文本/乱码）
    └── 去掉重复内容
    │
    ▼
3. 质量过滤
    ├── 困惑度过滤（用小模型打分）
    └── 规则过滤（标点比例/行长度等）
    │
    ▼
4. 去重（MinHash/精确去重）
    │
    ▼
5. Tokenize + 打包
    └── 多个文档拼接到固定长度（如2048 tokens）
    │
    ▼
6. 存储为二进制格式（.bin / memmap）
```

### ✔ 代码实现

```python
from datasets import load_dataset
from transformers import AutoTokenizer
import numpy as np

# 数据处理示例
tokenizer = AutoTokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

def tokenize_and_group(examples, block_size=1024):
    """将文本tokenize并打包成固定长度"""
    tokenized = tokenizer(
        examples["text"],
        truncation=False,
        return_special_tokens_mask=False
    )
    
    # 连接所有token
    concatenated = {k: sum(tokenized[k], []) for k in tokenized.keys()}
    total_length = len(concatenated["input_ids"])
    
    # 截断到block_size的整数倍
    total_length = (total_length // block_size) * block_size
    
    # 分块
    result = {
        k: [t[i:i+block_size] for i in range(0, total_length, block_size)]
        for k, t in concatenated.items()
    }
    # 语言模型的标签 = 输入右移一位
    result["labels"] = result["input_ids"].copy()
    return result

# 加载OpenWebText（GPT-2预训练数据）
dataset = load_dataset("openwebtext", split="train")
tokenized_dataset = dataset.map(
    tokenize_and_group,
    batched=True,
    remove_columns=dataset.column_names,
    num_proc=8  # 多进程加速
)
```

---

## 5.3 SFT（监督微调）

### ✔ 通俗解释

预训练模型"知道很多"但"不懂得听指令"。SFT用高质量指令数据（问题+答案对）微调，让模型学会"回答问题"。

```
预训练模型: 文本接龙机器
SFT之后: 能理解指令的助手
```

### ✔ 指令数据格式

```
# Alpaca格式
{
  "instruction": "给下面的文章写一个摘要",
  "input": "文章正文...",
  "output": "这篇文章主要讲述了..."
}

# ChatML格式（OpenAI/LLaMA使用）
<|im_start|>system
你是一个有用的助手。<|im_end|>
<|im_start|>user
帮我写一首关于春天的诗<|im_end|>
<|im_start|>assistant
春风轻拂柳丝长...<|im_end|>
```

### ✔ SFT训练代码

```python
from transformers import (
    AutoModelForCausalLM, 
    AutoTokenizer, 
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from datasets import load_dataset

# 加载基础模型
model_name = "meta-llama/Llama-2-7b-hf"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,  # 节省显存
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# 准备数据
def format_instruction(example):
    """格式化成指令微调格式"""
    text = f"### 指令:\n{example['instruction']}\n\n"
    if example.get('input'):
        text += f"### 输入:\n{example['input']}\n\n"
    text += f"### 回答:\n{example['output']}"
    return {"text": text}

dataset = load_dataset("tatsu-lab/alpaca")
dataset = dataset.map(format_instruction)

def tokenize(example):
    result = tokenizer(
        example["text"],
        truncation=True,
        max_length=2048,
        padding=False
    )
    result["labels"] = result["input_ids"].copy()
    return result

tokenized = dataset.map(tokenize, remove_columns=dataset["train"].column_names)

# 训练配置
training_args = TrainingArguments(
    output_dir="./sft-output",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=8,    # 有效batch=32
    learning_rate=2e-5,
    lr_scheduler_type="cosine",
    warmup_ratio=0.03,
    bf16=True,                        # BF16训练
    logging_steps=10,
    save_steps=500,
    report_to="wandb"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized["train"],
    data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False)
)
trainer.train()
```

---

## 5.4 RLHF（基于人类反馈的强化学习）

### ✔ 三阶段流程

```
阶段1: SFT（前面已讲）
    │
    ▼
阶段2: 奖励模型训练（RM）
    - 人类对多个回答进行排名
    - 训练RM预测人类偏好分数
    │
    ▼
阶段3: PPO强化学习
    - SFT模型作为策略（Policy）
    - RM给反馈信号
    - KL散度防止偏离太远
```

### ✔ 奖励模型

```python
class RewardModel(nn.Module):
    """奖励模型：输出一个标量分数"""
    def __init__(self, base_model):
        super().__init__()
        self.base = base_model
        d_model = base_model.config.hidden_size
        self.reward_head = nn.Linear(d_model, 1)
    
    def forward(self, input_ids, attention_mask):
        outputs = self.base(input_ids, attention_mask=attention_mask)
        # 取最后一个token的hidden state
        last_hidden = outputs.last_hidden_state[:, -1, :]
        return self.reward_head(last_hidden).squeeze(-1)  # (batch,)

# Bradley-Terry偏好损失
def preference_loss(chosen_reward, rejected_reward):
    """人类选择chosen比rejected好的概率"""
    return -F.logsigmoid(chosen_reward - rejected_reward).mean()
```

### ✔ DPO（直接偏好优化，更简单）

**来源：Rafailov et al., "Direct Preference Optimization", NeurIPS 2023**

DPO无需单独训练奖励模型，直接在偏好数据上优化，更简单稳定。

```python
def dpo_loss(policy_chosen_logps, policy_rejected_logps,
             ref_chosen_logps, ref_rejected_logps, beta=0.1):
    """
    DPO损失函数
    policy_*: 当前策略的log概率
    ref_*: 参考模型（SFT模型）的log概率
    beta: 控制偏离参考模型的程度
    """
    # 策略比率（相对于参考模型）
    pi_logratios = policy_chosen_logps - policy_rejected_logps
    ref_logratios = ref_chosen_logps - ref_rejected_logps
    
    logits = pi_logratios - ref_logratios
    loss = -F.logsigmoid(beta * logits).mean()
    
    # 胜率统计
    chosen_rewards = beta * (policy_chosen_logps - ref_chosen_logps)
    rejected_rewards = beta * (policy_rejected_logps - ref_rejected_logps)
    reward_acc = (chosen_rewards > rejected_rewards).float().mean()
    
    return loss, chosen_rewards.mean(), rejected_rewards.mean(), reward_acc
```

---

## 5.5 Scaling Law

### ✔ 通俗解释

**规模定律**：损失和参数量/数据量/算力之间有可预测的幂律关系，告诉你"花多少钱买多少性能"。

### ✔ Chinchilla定律（核心）

**来源：Hoffmann et al., "Training Compute-Optimal LLMs", DeepMind 2022**

```
最优训练：数据量(D) ≈ 20 × 参数量(N)

之前：GPT-3有175B参数，只训练了300B tokens（数据不足！）
Chinchilla：70B参数 + 1.4T tokens ≈ 性能超过175B GPT-3

Scaling Law公式：
L(N, D) = A/N^α + B/D^β + C

其中α≈0.34, β≈0.28
```

**实际意义：**
```
给定计算预算C（FLOPs）：
最优参数量: N* ∝ C^0.5
最优数据量: D* ∝ C^0.5

即：增加算力时，模型和数据应该等比例增长
```

---

# ⚙️ 工程系统

## 6.1 分布式训练

### ✔ 数据并行（DDP）

```
┌────────────────────────────────────────┐
│           数据并行 (DDP)                │
│                                        │
│  GPU0: batch[0-32]   GPU1: batch[32-64]│
│  模型副本               模型副本        │
│     ↓                      ↓          │
│  梯度计算               梯度计算        │
│     └──── AllReduce (平均梯度) ────┘   │
│              ↓                         │
│         更新参数（所有GPU同步）          │
└────────────────────────────────────────┘
```

### ✔ ZeRO优化（显存杀手锏）

**来源：Rajbhandari et al., ZeRO: Memory Optimizations Toward Training Trillion Parameter Models, Microsoft 2020**

```
ZeRO-1: 分片优化器状态 → 4x显存节省
ZeRO-2: + 分片梯度     → 8x显存节省
ZeRO-3: + 分片参数     → N×（GPU数）显存节省

175B模型内存需求：
FP32权重: 700GB
梯度:     700GB
优化器状态(Adam): 2×700GB = 1400GB
总计: 约2.8TB

ZeRO-3 with 64 GPUs:
每GPU约 2800GB/64 = 43GB ← A100单卡可以承受！
```

### ✔ 完整分布式训练代码

```python
# train.py - DeepSpeed分布式训练
import torch
import deepspeed
from transformers import AutoModelForCausalLM, AutoTokenizer

# DeepSpeed配置
ds_config = {
    "train_batch_size": 256,
    "train_micro_batch_size_per_gpu": 4,
    "gradient_accumulation_steps": 8,
    
    "optimizer": {
        "type": "AdamW",
        "params": {
            "lr": 3e-4,
            "betas": [0.9, 0.95],
            "weight_decay": 0.1
        }
    },
    
    "scheduler": {
        "type": "WarmupDecayLR",
        "params": {
            "warmup_min_lr": 0,
            "warmup_max_lr": 3e-4,
            "warmup_num_steps": 2000,
            "total_num_steps": 100000
        }
    },
    
    "fp16": {"enabled": False},
    "bf16": {"enabled": True},   # BF16比FP16更稳定
    
    "zero_optimization": {
        "stage": 3,                        # ZeRO-3
        "overlap_comm": True,             # 通信和计算重叠
        "contiguous_gradients": True,
        "reduce_bucket_size": 5e8,
        "stage3_prefetch_bucket_size": 5e8,
        "stage3_param_persistence_threshold": 1e6,
        "offload_optimizer": {            # CPU offload（超大模型用）
            "device": "none"              # 改为"cpu"可节省更多显存
        }
    },
    
    "gradient_clipping": 1.0,
    "steps_per_print": 10
}

# 初始化
model = AutoModelForCausalLM.from_pretrained("gpt2")

model_engine, optimizer, _, scheduler = deepspeed.initialize(
    model=model,
    config=ds_config
)

# 训练循环
for step, batch in enumerate(dataloader):
    input_ids = batch["input_ids"].to(model_engine.device)
    labels = batch["labels"].to(model_engine.device)
    
    outputs = model_engine(input_ids=input_ids, labels=labels)
    loss = outputs.loss
    
    model_engine.backward(loss)         # 替代loss.backward()
    model_engine.step()                 # 替代optimizer.step()
    
    if step % 10 == 0:
        print(f"Step {step}, Loss: {loss.item():.4f}")

# 启动命令：
# deepspeed --num_gpus=8 train.py
```

---

## 6.2 混合精度训练

### ✔ 数值格式对比

```
格式    位数   数值范围            精度      用途
FP32    32     ±3.4×10³⁸         高        传统训练
FP16    16     ±65504            中        训练（可能溢出）
BF16    16     ±3.4×10³⁸         低        LLM训练（推荐！）
FP8     8      ±448 / ±57344     很低      最新GPU推理训练
INT8    8      -128~127          整数       量化推理

BF16 vs FP16：
- BF16指数位更多（8位 vs 5位），数值范围和FP32一样
- 不会像FP16那样溢出
- LLaMA/GPT-3.5等都用BF16训练
```

### ✔ 代码实现

```python
# 方法1：PyTorch原生autocast
from torch.cuda.amp import autocast, GradScaler

model = model.cuda()
scaler = GradScaler()  # FP16需要梯度缩放器

for batch in dataloader:
    with autocast(dtype=torch.bfloat16):  # 前向用BF16
        loss = model(batch)
    
    # BF16不需要scaler，FP16需要
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    optimizer.step()
    optimizer.zero_grad()

# 方法2：transformers自动配置
from transformers import TrainingArguments
args = TrainingArguments(
    bf16=True,  # 一行搞定
    ...
)
```

---

## 6.3 显存优化策略

```
策略                    显存节省    速度影响
───────────────────────────────────────────
梯度检查点(Checkpoint)    ~60-70%    -20-30%速度
混合精度(BF16)            ~50%       +速度
梯度累积                  线性节省   无影响
Flash Attention          节省KV存储  +速度！
ZeRO-3                   N倍节省    轻微通信开销
CPU Offload              极大节省    速度下降明显
```

### ✔ Flash Attention（现代必备）

**来源：Dao et al., "FlashAttention: Fast and Memory-Efficient Exact Attention", 2022**

```python
# 传统Attention：O(N²)显存（存储完整注意力矩阵）
# Flash Attention：O(N)显存（分块计算，不存完整矩阵）

# 使用flash_attn库
from flash_attn import flash_attn_qkvpacked_func, flash_attn_func

# 或直接用torch的scaled_dot_product_attention（PyTorch 2.0+自动用Flash Attn）
with torch.backends.cuda.sdp_kernel(enable_flash=True):
    output = torch.nn.functional.scaled_dot_product_attention(
        query, key, value,
        attn_mask=None,
        dropout_p=0.0,
        is_causal=True  # 因果mask
    )
```

### ✔ 梯度检查点

```python
# 不存储中间激活，反向时重新计算
from torch.utils.checkpoint import checkpoint

class TransformerBlock(nn.Module):
    def forward(self, x):
        if self.training and self.use_checkpoint:
            # 包装函数，反向时重新运算
            x = checkpoint(self._forward, x)
        else:
            x = self._forward(x)
        return x

# HuggingFace一行启用
model.gradient_checkpointing_enable()
```

---

# 🚀 推理与部署

## 7.1 KV Cache

### ✔ 通俗解释

自回归生成每步都重新计算所有K/V很浪费。KV Cache把之前算过的K/V缓存起来，每步只算新token的K/V。

```
没有KV Cache（第t步需要重算前t-1步的KV）：
O(t²) 计算量

有KV Cache（每步只算新token）：
O(t) 计算量
O(t × d) 存储量（但值得！）
```

### ✔ 代码实现

```python
class GPTWithKVCache(nn.Module):
    def generate_with_cache(self, input_ids, max_new_tokens):
        past_key_values = None
        generated = input_ids
        
        for _ in range(max_new_tokens):
            with torch.no_grad():
                outputs = self.model(
                    input_ids=generated[:, -1:] if past_key_values else generated,
                    past_key_values=past_key_values,
                    use_cache=True
                )
            
            logits = outputs.logits[:, -1, :]
            past_key_values = outputs.past_key_values  # 缓存！
            
            next_token = logits.argmax(-1, keepdim=True)
            generated = torch.cat([generated, next_token], dim=-1)
        
        return generated
```

---

## 7.2 vLLM（大规模推理）

**来源：Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention", SOSP 2023**

### ✔ PagedAttention核心思想

```
传统KV Cache：为最大序列长度预分配连续内存 → 大量浪费
PagedAttention：像操作系统分页内存，按需分配页 → 吞吐量↑3-5倍
```

### ✔ vLLM使用

```python
from vllm import LLM, SamplingParams

# 加载模型（自动使用PagedAttention）
llm = LLM(
    model="meta-llama/Llama-2-7b-chat-hf",
    tensor_parallel_size=2,  # 2卡张量并行
    gpu_memory_utilization=0.95,
    max_model_len=4096
)

# 批量推理（高吞吐量）
sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.9,
    max_tokens=512
)

prompts = [
    "解释量子纠缠",
    "写一首关于人工智能的诗",
    "Python如何读取CSV文件？"
]

outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    print(output.outputs[0].text)
```

---

## 7.3 模型量化

### ✔ INT8量化

```
FP16权重（2字节/参数） → INT8（1字节/参数）→ 2x压缩

量化公式：
q = round(x / scale) + zero_point
反量化：x ≈ (q - zero_point) × scale

LLM.int8()（bitsandbytes）：
- 矩阵乘法部分用INT8
- 离群值（outliers）保留FP16
- 几乎无精度损失！
```

### ✔ GGUF量化（本地部署）

```
格式         显存需求(7B模型)  质量
FP16         14GB             最好
Q8_0         7GB              几乎无损
Q5_K_M       4.8GB            很好（推荐）
Q4_K_M       4.1GB            好
Q3_K_M       3.3GB            可用
Q2_K         2.9GB            差
```

### ✔ 代码实现

```python
# bitsandbytes INT8量化（4行搞定）
from transformers import AutoModelForCausalLM
import torch

model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-hf",
    load_in_8bit=True,      # INT8量化
    device_map="auto"
)

# 或NF4量化（更小，QLoRA使用）
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-hf",
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True
)
```

---

## 7.4 LoRA / QLoRA（参数高效微调）

**来源：Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models", ICLR 2022**

### ✔ 核心思想

```
原始权重 W (768×768 = 589824参数) → 冻结！
LoRA：W' = W + ΔW = W + BA

B: (768×r)  A: (r×768)   r=16
参数量：768×16 + 16×768 = 24576 → 只有原来的4%！
```

### ✔ 为什么有效？

权重更新 ΔW 具有低秩特性（实验验证），所以可以用低秩矩阵近似。

### ✔ 代码实现

```python
from peft import LoraConfig, get_peft_model, TaskType
from transformers import AutoModelForCausalLM

# 加载基础模型
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-hf",
    torch_dtype=torch.bfloat16
)

# LoRA配置
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=16,                    # 秩（rank）
    lora_alpha=32,           # 缩放系数（通常=2r）
    target_modules=[         # 在哪些层应用LoRA
        "q_proj", "v_proj",  # 只在QV投影（常见选择）
        # "k_proj", "o_proj", "gate_proj", "up_proj", "down_proj"
    ],
    lora_dropout=0.05,
    bias="none"
)

# 应用LoRA
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()
# trainable params: 4,194,304 || all params: 6,742,609,920 || trainable%: 0.0622

# QLoRA = 4bit量化 + LoRA
from transformers import BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-hf",
    quantization_config=bnb_config,
    device_map="auto"
)
model = get_peft_model(model, lora_config)
# 7B模型只需约8GB显存！
```

---

# 📊 数据工程

## 8.1 数据质量对模型的影响

```
"Garbage in, garbage out"

数据质量 > 数据数量

关键指标：
- 多样性：覆盖多种主题/风格/语言
- 准确性：事实正确，无矛盾
- 指令遵循性：回答真正回答了问题
- 无偏见：不含歧视性内容
```

## 8.2 数据清洗流程

```python
import re
from datasets import Dataset

def clean_text(text: str) -> str | None:
    """文本清洗流水线"""
    # 1. 去掉HTML标签
    text = re.sub(r'<[^>]+>', '', text)
    
    # 2. 去掉重复空白
    text = re.sub(r'\s+', ' ', text).strip()
    
    # 3. 长度过滤
    words = text.split()
    if len(words) < 20 or len(words) > 10000:
        return None
    
    # 4. 语言过滤（需要langdetect）
    # from langdetect import detect
    # if detect(text) != 'zh-cn':
    #     return None
    
    # 5. 质量分数（字母比例）
    alpha_ratio = sum(c.isalpha() for c in text) / len(text)
    if alpha_ratio < 0.5:
        return None
    
    # 6. 去掉明显的垃圾内容
    spam_patterns = [
        r'click here', r'subscribe now', r'buy now',
        r'\d{4}-\d{4}-\d{4}-\d{4}'  # 信用卡号
    ]
    for pattern in spam_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return None
    
    return text

# MinHash去重
from datasketch import MinHash, MinHashLSH

def get_minhash(text, num_perm=128):
    m = MinHash(num_perm=num_perm)
    for word in text.lower().split():
        m.update(word.encode('utf8'))
    return m

# LSH去重
lsh = MinHashLSH(threshold=0.8, num_perm=128)
unique_docs = []
for i, doc in enumerate(documents):
    m = get_minhash(doc)
    result = lsh.query(m)
    if not result:  # 没有相似文档
        lsh.insert(f"doc_{i}", m)
        unique_docs.append(doc)
```

## 8.3 合成数据生成

```python
# 使用强模型生成指令数据（Self-Instruct方法）
import anthropic

client = anthropic.Anthropic()

def generate_instruction_data(seed_tasks: list[str], n: int = 100):
    """用LLM自动生成指令数据"""
    generated = []
    
    for _ in range(n):
        # 从种子任务中采样几个示例
        import random
        examples = random.sample(seed_tasks, min(3, len(seed_tasks)))
        
        prompt = f"""请生成一个新的AI助手指令-回复对，格式如下：

参考示例：
{chr(10).join(examples)}

请生成一个新的、有用的、多样的指令和对应的高质量回复。
格式：
指令：[具体的用户指令]
回复：[AI的详细、准确、有帮助的回复]"""
        
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        response = message.content[0].text
        # 解析指令和回复
        # ...
        generated.append(response)
    
    return generated
```

---

# 🔭 前沿技术（2025+）

## 9.1 推理模型（Chain-of-Thought）

### ✔ 通俗解释

普通模型直接输出答案。推理模型"先思考再回答"，像人做数学题先打草稿。

```
普通模型：问题 → 答案
推理模型：问题 → <think>一步步思考...</think> → 答案
```

### ✔ o1/DeepSeek-R1实现方式

**来源：DeepSeek-R1, 2025**

```
训练方法：GRPO（Group Relative Policy Optimization）

1. 让模型生成多个解答
2. 对正确解答给正奖励
3. 用强化学习强化"先思考再回答"的模式
4. 模型自发学会使用<think>标签

关键发现：无需监督思维链数据，
纯RL训练就能涌现出推理能力！
```

```python
# 简化的推理模型提示格式
def format_reasoning_prompt(question: str) -> str:
    return f"""<|User|>{question}<|Assistant|><think>
让我一步步思考这个问题："""

# 使用DeepSeek-R1
from transformers import pipeline

pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B")
response = pipe(format_reasoning_prompt("9.9和9.11哪个大？"))
```

---

## 9.2 RAG（检索增强生成）

### ✔ 通俗解释

让模型在回答时能"查资料"，解决知识截止日期和幻觉问题。

```
问题 → 向量化 → 向量数据库检索相关文档 → 文档+问题 → LLM → 答案
```

### ✔ 完整RAG实现

```python
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
import torch

# 1. 加载文档
loader = DirectoryLoader("./docs/", glob="**/*.txt")
documents = loader.load()

# 2. 切分文档
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(documents)

# 3. 嵌入 + 存入向量数据库
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",  # 多语言嵌入模型
    model_kwargs={"device": "cuda"}
)
vectordb = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory="./chroma_db"
)

# 4. 配置检索器
retriever = vectordb.as_retriever(
    search_type="mmr",  # Maximum Marginal Relevance（多样性+相关性）
    search_kwargs={"k": 5}
)

# 5. 问答链
qa_chain = RetrievalQA.from_chain_type(
    llm=your_llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

result = qa_chain("你的问题")
print(result["result"])
print("来源：", [doc.metadata["source"] for doc in result["source_documents"]])
```

---

## 9.3 Agent系统

### ✔ ReAct框架

**来源：Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models", ICLR 2023**

```
循环执行：
Thought: 我需要查一下XXX
Action: search("XXX")
Observation: 搜索结果...
Thought: 根据结果，我需要...
Action: calculate(...)
Observation: 计算结果
Thought: 现在我可以回答了
Answer: 最终答案
```

### ✔ 代码实现

```python
import anthropic
import json

client = anthropic.Anthropic()

# 定义工具
tools = [
    {
        "name": "web_search",
        "description": "搜索网络获取最新信息",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "搜索词"}
            },
            "required": ["query"]
        }
    },
    {
        "name": "calculator",
        "description": "执行数学计算",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {"type": "string", "description": "数学表达式"}
            },
            "required": ["expression"]
        }
    }
]

def run_agent(user_message: str) -> str:
    messages = [{"role": "user", "content": user_message}]
    
    while True:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            tools=tools,
            messages=messages
        )
        
        if response.stop_reason == "end_turn":
            # 提取最终文本回复
            return next(block.text for block in response.content 
                       if block.type == "text")
        
        # 处理工具调用
        messages.append({"role": "assistant", "content": response.content})
        tool_results = []
        
        for block in response.content:
            if block.type == "tool_use":
                # 执行工具
                if block.name == "calculator":
                    result = str(eval(block.input["expression"]))
                elif block.name == "web_search":
                    result = f"搜索结果：{block.input['query']}的相关信息..."
                
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result
                })
        
        messages.append({"role": "user", "content": tool_results})

# 使用
answer = run_agent("计算2023年全球GDP总量除以世界人口的结果")
print(answer)
```

---

## 9.4 知识蒸馏

### ✔ 通俗解释

用大模型（Teacher）教小模型（Student），让小模型也能有接近大模型的能力。

```
Teacher (175B GPT-3)
    │
    │ 软标签（概率分布）
    ↓
Student (1B模型)
    │
    │ 模仿Teacher的输出分布
    ↓
小而强的模型！
```

### ✔ 蒸馏损失

```python
def distillation_loss(student_logits, teacher_logits, labels, 
                      temperature=4.0, alpha=0.7):
    """
    蒸馏损失 = α × KL散度(Teacher||Student) + (1-α) × 交叉熵(真实标签)
    """
    # 软标签损失（向Teacher学习）
    soft_student = F.log_softmax(student_logits / temperature, dim=-1)
    soft_teacher = F.softmax(teacher_logits / temperature, dim=-1)
    distill_loss = F.kl_div(soft_student, soft_teacher, reduction='batchmean')
    distill_loss *= temperature ** 2  # 温度补偿
    
    # 硬标签损失（向真实标签学习）
    hard_loss = F.cross_entropy(student_logits, labels)
    
    return alpha * distill_loss + (1 - alpha) * hard_loss
```

---

# 🛠️ 实战项目集

## 项目1：手写GPT（Transformer实战）

```
项目目标：实现并训练一个小型GPT语言模型
技术栈：PyTorch, tiktoken
数据集：Shakespeare文本 / 中文小说
预计时间：2-3天
```

**完整代码结构：**
```
gpt-from-scratch/
├── model.py          # GPT模型（前面已实现）
├── train.py          # 训练脚本
├── tokenizer.py      # 简单字符级tokenizer
├── data/
│   └── shakespeare.txt
└── generate.py       # 文本生成
```

**train.py：**
```python
import torch
from model import GPT, GPTConfig
from torch.utils.data import Dataset, DataLoader

class TextDataset(Dataset):
    def __init__(self, text, block_size=256):
        # 字符级tokenize
        chars = sorted(set(text))
        self.stoi = {c: i for i, c in enumerate(chars)}
        self.itos = {i: c for i, c in enumerate(chars)}
        
        data = torch.tensor([self.stoi[c] for c in text])
        self.data = data
        self.block_size = block_size
    
    def __len__(self):
        return len(self.data) - self.block_size
    
    def __getitem__(self, idx):
        x = self.data[idx:idx+self.block_size]
        y = self.data[idx+1:idx+self.block_size+1]
        return x, y

# 训练
with open('data/shakespeare.txt') as f:
    text = f.read()

dataset = TextDataset(text)
loader = DataLoader(dataset, batch_size=64, shuffle=True)

config = GPTConfig(
    vocab_size=len(dataset.stoi),
    max_seq_len=256,
    d_model=384,
    n_layers=6,
    n_heads=6
)
model = GPT(config).cuda()
optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4)

for epoch in range(10):
    for x, y in loader:
        x, y = x.cuda(), y.cuda()
        logits, loss = model(x, y)
        optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()
    print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

# 运行：python train.py
```

---

## 项目2：LoRA微调自己的助手

```
项目目标：用LoRA在自定义数据上微调LLaMA
技术栈：transformers, peft, bitsandbytes
硬件要求：16GB显存（单卡）
预计时间：3-5天
```

**完整运行步骤：**
```bash
# 1. 安装依赖
pip install transformers peft bitsandbytes datasets accelerate

# 2. 准备数据（jsonl格式）
# {"instruction": "...", "output": "..."}

# 3. 运行微调
python finetune.py \
  --model_name meta-llama/Llama-2-7b-hf \
  --data_path data/my_data.jsonl \
  --output_dir ./lora-output \
  --num_epochs 3 \
  --batch_size 4 \
  --learning_rate 2e-4 \
  --lora_r 16

# 4. 合并LoRA权重
python merge_lora.py --base_model llama-7b --lora_weights ./lora-output

# 5. 部署测试
python chat.py --model ./merged-model
```

---

## 项目3：RAG知识库系统

```
项目目标：搭建一个基于私有文档的问答系统
技术栈：LangChain, Chroma, Ollama（本地LLM）
预计时间：2-3天
```

**项目结构：**
```
rag-system/
├── ingest.py        # 文档入库
├── query.py         # 查询
├── app.py           # Gradio界面
├── docs/            # 你的文档
└── chroma_db/       # 向量数据库
```

```python
# app.py - Gradio界面
import gradio as gr
from query import RAGSystem

rag = RAGSystem()

def chat(message, history):
    response = rag.query(message)
    return response["answer"]

demo = gr.ChatInterface(
    fn=chat,
    title="我的AI知识库",
    description="基于私有文档的智能问答"
)
demo.launch()
```

---

## 项目4：从头训练小型中文LLM

```
项目目标：训练一个1B参数的中文语言模型
技术栈：PyTorch, DeepSpeed, HuggingFace
硬件要求：8×A100 (80GB) 或等效
预计时间：1-2周（训练时间取决于数据量）
```

**关键配置：**
```
数据：20B中文tokens（CC100/WuDaoCorpora等）
模型：1B参数，24层，16头，2048维
训练：100B tokens，cosine LR
时长：约3-5天（8×A100）
```

---

## 项目5：多模态图文问答

```
项目目标：搭建LLaVA风格的图文对话系统
技术栈：transformers, CLIP, LLaMA
预计时间：1周
```

```python
# 使用现成的LLaVA
from transformers import LlavaNextProcessor, LlavaNextForConditionalGeneration
from PIL import Image
import requests

processor = LlavaNextProcessor.from_pretrained("llava-hf/llava-v1.6-mistral-7b-hf")
model = LlavaNextForConditionalGeneration.from_pretrained(
    "llava-hf/llava-v1.6-mistral-7b-hf",
    torch_dtype=torch.float16,
    device_map="auto"
)

image = Image.open("your_image.jpg")
conversation = [
    {
        "role": "user",
        "content": [
            {"type": "image"},
            {"type": "text", "text": "这张图片里有什么？"}
        ]
    }
]

prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)
inputs = processor(images=image, text=prompt, return_tensors="pt").to(model.device)
output = model.generate(**inputs, max_new_tokens=512)
print(processor.decode(output[0], skip_special_tokens=True))
```

---

# 📚 参考资料

## 核心论文（按重要性排序）

| 论文 | 年份 | 贡献 |
|------|------|------|
| Attention is All You Need (Vaswani et al.) | 2017 | Transformer架构 |
| BERT (Devlin et al.) | 2018 | 双向预训练 |
| GPT-2 (Radford et al.) | 2019 | 大规模语言模型 |
| Scaling Laws (Kaplan et al.) | 2020 | 规模定律 |
| GPT-3 (Brown et al.) | 2020 | Few-shot学习 |
| InstructGPT (Ouyang et al.) | 2022 | RLHF对齐 |
| Chinchilla (Hoffmann et al.) | 2022 | 最优训练规模 |
| LoRA (Hu et al.) | 2022 | 参数高效微调 |
| FlashAttention (Dao et al.) | 2022 | 高效注意力 |
| LLaMA (Touvron et al.) | 2023 | 开源大模型 |
| QLoRA (Dettmers et al.) | 2023 | 量化LoRA |
| Mixtral MoE (Jiang et al.) | 2024 | 开源MoE |
| DeepSeek-V3 (DeepSeek AI) | 2024 | 高效MoE训练 |
| DeepSeek-R1 (DeepSeek AI) | 2025 | 推理模型RL |
| Mamba (Gu & Dao) | 2023 | 状态空间模型 |
| DPO (Rafailov et al.) | 2023 | 直接偏好优化 |

## 官方文档

- **PyTorch**: https://pytorch.org/docs/
- **DeepSpeed**: https://deepspeed.readthedocs.io/
- **HuggingFace Transformers**: https://huggingface.co/docs/transformers/
- **PEFT (LoRA)**: https://huggingface.co/docs/peft/
- **vLLM**: https://docs.vllm.ai/
- **LangChain**: https://docs.langchain.com/

## 优质学习资源

- **Andrej Karpathy - "Let's build GPT"**: YouTube完整实现视频
- **Andrej Karpathy - nanoGPT**: GitHub最简洁GPT实现
- **fast.ai**: 实践优先的深度学习课程
- **Stanford CS224N**: NLP with Deep Learning
- **Lilian Weng's Blog (lilianweng.github.io)**: 最好的技术博客之一

---

## 🎯 附录：常见面试题汇总

### Transformer相关
1. **Self-Attention的时间复杂度是多少？** O(n²d)，n是序列长度，d是维度
2. **为什么用Multi-Head而不是单头？** 不同头关注不同子空间的模式
3. **LayerNorm放在哪？** Pre-LN（更稳定）vs Post-LN（原始论文）
4. **Transformer的位置编码可以用学习的embedding吗？** 可以，GPT-2就用的
5. **Attention mask有哪些类型？** Causal mask（GPT）, Padding mask, 全局attention mask（Longformer）

### 训练相关
1. **为什么用BF16而不是FP16？** BF16数值范围更大，不容易溢出
2. **梯度裁剪的作用？** 防止梯度爆炸，threshold通常1.0
3. **为什么要Gradient Accumulation？** 模拟更大batch size，解决显存不足
4. **Warmup的作用？** 训练初期学习率过大会破坏预训练权重
5. **ZeRO-2和ZeRO-3的区别？** ZeRO-3连模型参数也分片

### 架构相关
1. **MoE的负载均衡问题如何解决？** 辅助loss（z-loss）或token choice策略
2. **KV Cache的显存占用公式？** 2 × layers × heads × d_head × seq_len × batch × 2bytes
3. **Flash Attention为什么省显存？** 不存储完整的注意力矩阵，分块计算
4. **LoRA的r选多少？** 通常8-64，任务越复杂r越大
5. **量化会损失精度吗？** INT8几乎无损，INT4有少量损失，Q4_K_M是好的平衡点

---

> **最后更新：2026年**  
> 本手册持续更新，跟踪最新大模型技术进展

---

*"The only way to learn is to build." — 动手实践是唯一的学习之道*