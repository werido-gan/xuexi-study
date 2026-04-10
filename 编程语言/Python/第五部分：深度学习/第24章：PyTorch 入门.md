## 第24章：PyTorch 入门 🔥

### 24.1 PyTorch 简介

PyTorch 是 Facebook（现在的 Meta）开发的深度学习框架，它以其动态计算图和易用性而闻名。

> **PyTorch 的优势**：
> - 动态计算图：更灵活，易于调试
> - Python 友好：与 Python 生态系统无缝集成
> - 强大的 GPU 加速：支持 CUDA
> - 丰富的预训练模型
> - 活跃的社区

### 24.2 PyTorch 安装

#### 24.2.1 基本安装

```bash
# 安装 PyTorch (CPU 版本)
pip install torch torchvision torchaudio

# 安装 PyTorch (CUDA 11.7 版本)
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
```

#### 24.2.2 验证安装

```python
import torch
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"CUDA version: {torch.version.cuda}")
    print(f"Number of GPUs: {torch.cuda.device_count()}")
    print(f"Current GPU: {torch.cuda.current_device()}")
    print(f"GPU name: {torch.cuda.get_device_name(0)}")
```

### 24.3 张量（Tensors）

张量是 PyTorch 的基本数据结构，类似于 NumPy 的数组，但支持自动微分和 GPU 加速。

#### 24.3.1 创建张量

```python
import torch
import numpy as np

# 从 Python 列表创建
t1 = torch.tensor([1, 2, 3])
print(f"t1: {t1}")
print(f"t1 shape: {t1.shape}")

# 从 NumPy 数组创建
arr = np.array([[1, 2], [3, 4]])
t2 = torch.from_numpy(arr)
print(f"t2: {t2}")
print(f"t2 shape: {t2.shape}")

# 创建全零张量
t3 = torch.zeros(2, 3)
print(f"t3: {t3}")

# 创建全一张量
t4 = torch.ones(3, 2)
print(f"t4: {t4}")

# 创建随机张量
t5 = torch.rand(2, 2)
print(f"t5: {t5}")

# 创建指定范围的张量
t6 = torch.arange(0, 10, 2)
print(f"t6: {t6}")

# 创建等间隔的张量
t7 = torch.linspace(0, 1, 5)
print(f"t7: {t7}")
```

#### 24.3.2 张量操作

```python
import torch

# 基本操作
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])

print(f"a + b: {a + b}")
print(f"a - b: {a - b}")
print(f"a * b: {a * b}")
print(f"a / b: {a / b}")
print(f"a ** 2: {a ** 2}")

# 矩阵乘法
c = torch.tensor([[1, 2], [3, 4]])
d = torch.tensor([[5, 6], [7, 8]])
print(f"c @ d: {c @ d}")
print(f"torch.matmul(c, d): {torch.matmul(c, d)}")

# 张量属性
print(f"a shape: {a.shape}")
print(f"a dtype: {a.dtype}")
print(f"a device: {a.device}")

# 张量变形
e = torch.tensor([1, 2, 3, 4, 5, 6])
print(f"e: {e}")
print(f"e.reshape(2, 3): {e.reshape(2, 3)}")
print(f"e.view(2, 3): {e.view(2, 3)}")

# 张量拼接
f = torch.tensor([[1, 2], [3, 4]])
g = torch.tensor([[5, 6], [7, 8]])
print(f"torch.cat([f, g], dim=0): {torch.cat([f, g], dim=0)}")  # 按行拼接
print(f"torch.cat([f, g], dim=1): {torch.cat([f, g], dim=1)}")  # 按列拼接

# 张量索引和切片
h = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"h[0, :]: {h[0, :]}")  # 第一行
print(f"h[:, 1]: {h[:, 1]}")  # 第二列
print(f"h[1:3, 1:3]: {h[1:3, 1:3]}")  # 子矩阵
```

#### 24.3.3 自动微分

PyTorch 的自动微分系统允许我们计算张量的梯度。

```python
import torch

# 创建需要梯度的张量
x = torch.tensor(2.0, requires_grad=True)
y = x ** 2 + 2 * x + 1

# 反向传播计算梯度
y.backward()

# 查看梯度
print(f"x.grad: {x.grad}")  # 应为 2*x + 2 = 6

# 多变量情况
x = torch.tensor(1.0, requires_grad=True)
y = torch.tensor(2.0, requires_grad=True)
z = x ** 2 + y ** 2

z.backward()

print(f"x.grad: {x.grad}")  # 2*x = 2
print(f"y.grad: {y.grad}")  # 2*y = 4

# 停止梯度追踪
with torch.no_grad():
    w = x ** 2
    print(f"w: {w}")
    print(f"w.requires_grad: {w.requires_grad}")
```

### 24.4 神经网络基础

#### 24.4.1 神经网络模块

PyTorch 使用 `nn.Module` 类来构建神经网络。

```python
import torch
import torch.nn as nn

class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(2, 3)  # 输入层到隐藏层
        self.fc2 = nn.Linear(3, 1)  # 隐藏层到输出层
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# 创建模型
model = SimpleNN()
print(model)

# 查看模型参数
for name, param in model.named_parameters():
    print(f"{name}: {param.shape}")

# 测试模型
x = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
y_pred = model(x)
print(f"Predictions: {y_pred}")
```

#### 24.4.2 损失函数

```python
import torch
import torch.nn as nn

# 均方误差（回归）
criterion = nn.MSELoss()
y_true = torch.tensor([[0.0], [1.0], [1.0], [0.0]], dtype=torch.float32)
y_pred = torch.tensor([[0.1], [0.9], [0.8], [0.2]], dtype=torch.float32)
loss = criterion(y_pred, y_true)
print(f"MSE Loss: {loss.item()}")

# 交叉熵损失（分类）
criterion = nn.CrossEntropyLoss()
y_true = torch.tensor([0, 1, 2], dtype=torch.long)
y_pred = torch.tensor([[0.9, 0.05, 0.05], [0.05, 0.9, 0.05], [0.05, 0.05, 0.9]], dtype=torch.float32)
loss = criterion(y_pred, y_true)
print(f"Cross Entropy Loss: {loss.item()}")

# 二元交叉熵损失（二分类）
criterion = nn.BCELoss()
y_true = torch.tensor([[0.0], [1.0], [1.0], [0.0]], dtype=torch.float32)
y_pred = torch.tensor([[0.1], [0.9], [0.8], [0.2]], dtype=torch.float32)
loss = criterion(y_pred, y_true)
print(f"Binary Cross Entropy Loss: {loss.item()}")
```

#### 24.4.3 优化器

```python
import torch
import torch.nn as nn
import torch.optim as optim

# 创建模型
model = SimpleNN()

# 创建优化器
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
# optimizer = optim.Adam(model.parameters(), lr=0.001)

# 训练步骤
def train_step(x, y):
    # 前向传播
    y_pred = model(x)
    
    # 计算损失
    criterion = nn.MSELoss()
    loss = criterion(y_pred, y)
    
    # 反向传播
    optimizer.zero_grad()  # 清除之前的梯度
    loss.backward()  # 计算梯度
    optimizer.step()  # 更新参数
    
    return loss.item()

# 测试训练
x = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
y = torch.tensor([[0.0], [1.0], [1.0], [0.0]], dtype=torch.float32)

for epoch in range(1000):
    loss = train_step(x, y)
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss}")

# 测试模型
with torch.no_grad():
    y_pred = model(x)
    print(f"Predictions: {y_pred}")
```

### 24.5 数据加载

PyTorch 提供了 `DataLoader` 和 `Dataset` 类来加载和处理数据。

#### 24.5.1 自定义数据集

```python
import torch
from torch.utils.data import Dataset, DataLoader

class CustomDataset(Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y
    
    def __len__(self):
        return len(self.X)
    
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# 创建数据集
X = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
y = torch.tensor([[0.0], [1.0], [1.0], [0.0]], dtype=torch.float32)

dataset = CustomDataset(X, y)

# 创建数据加载器
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# 遍历数据加载器
for batch_idx, (batch_X, batch_y) in enumerate(dataloader):
    print(f"Batch {batch_idx}: X={batch_X}, y={batch_y}")
```

#### 24.5.2 内置数据集

```python
import torch
import torchvision
import torchvision.transforms as transforms

# 数据变换
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

# 加载 CIFAR-10 数据集
trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = DataLoader(trainset, batch_size=4, shuffle=True, num_workers=2)

# 加载测试集
testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
testloader = DataLoader(testset, batch_size=4, shuffle=False, num_workers=2)

# 类别标签
classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

# 查看数据
import matplotlib.pyplot as plt
import numpy as np

def imshow(img):
    img = img / 2 + 0.5  # 反归一化
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()

# 获取一批数据
dataiter = iter(trainloader)
images, labels = next(dataiter)

# 显示图像
imshow(torchvision.utils.make_grid(images))
# 打印标签
print(' '.join(f'{classes[labels[j]]:5s}' for j in range(4)))
```

### 24.6 模型训练

#### 24.6.1 完整的训练流程

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

# 数据准备
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = DataLoader(trainset, batch_size=4, shuffle=True, num_workers=2)

testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
testloader = DataLoader(testset, batch_size=4, shuffle=False, num_workers=2)

classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

# 定义模型
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)
    
    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# 创建模型
net = Net()

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

# 训练模型
for epoch in range(2):  # 训练 2 个 epoch
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        # 获取输入
        inputs, labels = data
        
        # 清零梯度
        optimizer.zero_grad()
        
        # 前向传播
        outputs = net(inputs)
        
        # 计算损失
        loss = criterion(outputs, labels)
        
        # 反向传播
        loss.backward()
        
        # 更新参数
        optimizer.step()
        
        # 打印统计信息
        running_loss += loss.item()
        if i % 2000 == 1999:  # 每 2000 个 mini-batch 打印一次
            print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
            running_loss = 0.0

print('Finished Training')

# 测试模型
correct = 0
total = 0
with torch.no_grad():
    for data in testloader:
        images, labels = data
        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f'Accuracy of the network on the 10000 test images: {100 * correct / total} %')

# 测试每个类的准确率
class_correct = list(0. for i in range(10))
class_total = list(0. for i in range(10))
with torch.no_grad():
    for data in testloader:
        images, labels = data
        outputs = net(images)
        _, predicted = torch.max(outputs, 1)
        c = (predicted == labels).squeeze()
        for i in range(4):
            label = labels[i]
            class_correct[label] += c[i].item()
            class_total[label] += 1

for i in range(10):
    print(f'Accuracy of {classes[i]}: {100 * class_correct[i] / class_total[i]} %')
```

### 24.7 模型保存和加载

```python
import torch
import torch.nn as nn

# 定义模型
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(2, 3)
        self.fc2 = nn.Linear(3, 1)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# 创建模型
model = Net()

# 保存模型
# 方式 1：保存整个模型
torch.save(model, 'model.pth')

# 方式 2：只保存模型参数
torch.save(model.state_dict(), 'model_state_dict.pth')

# 加载模型
# 方式 1：加载整个模型
loaded_model = torch.load('model.pth')

# 方式 2：加载模型参数
loaded_model = Net()
loaded_model.load_state_dict(torch.load('model_state_dict.pth'))

# 测试加载的模型
x = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
with torch.no_grad():
    print(f"Original model predictions: {model(x)}")
    print(f"Loaded model predictions: {loaded_model(x)}")
```

### 24.8 迁移学习

迁移学习是指利用预训练模型的知识来解决新的任务。

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torchvision.models import resnet18

# 数据准备
transform = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = DataLoader(trainset, batch_size=4, shuffle=True, num_workers=2)

testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
testloader = DataLoader(testset, batch_size=4, shuffle=False, num_workers=2)

# 加载预训练模型
model = resnet18(pretrained=True)

# 冻结所有层
for param in model.parameters():
    param.requires_grad = False

# 替换最后一层
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 10)  # CIFAR-10 有 10 个类别

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
# 只优化最后一层
optimizer = optim.SGD(model.fc.parameters(), lr=0.001, momentum=0.9)

# 训练模型
for epoch in range(2):
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data
        
        optimizer.zero_grad()
        
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
        if i % 2000 == 1999:
            print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
            running_loss = 0.0

print('Finished Training')

# 测试模型
correct = 0
total = 0
with torch.no_grad():
    for data in testloader:
        images, labels = data
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f'Accuracy of the network on the 10000 test images: {100 * correct / total} %')
```

### 24.9 PyTorch 技巧

#### 24.9.1 使用 GPU 加速

```python
import torch

# 检查 GPU 是否可用
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# 将模型移到 GPU
model.to(device)

# 将数据移到 GPU
inputs = inputs.to(device)
labels = labels.to(device)
```

#### 24.9.2 混合精度训练

混合精度训练可以加速模型训练并减少内存使用。

```python
from torch.cuda.amp import autocast, GradScaler

# 创建梯度缩放器
scaler = GradScaler()

# 训练步骤
for epoch in range(epochs):
    for batch in dataloader:
        inputs, labels = batch
        inputs, labels = inputs.to(device), labels.to(device)
        
        optimizer.zero_grad()
        
        # 自动混合精度
        with autocast():
            outputs = model(inputs)
            loss = criterion(outputs, labels)
        
        # 反向传播
        scaler.scale(loss).backward()
        scaler.step(optimizer)
        scaler.update()
```

#### 24.9.3 模型并行

模型并行可以将大型模型分布到多个 GPU 上。

```python
import torch
import torch.nn as nn

# 创建大型模型
class LargeModel(nn.Module):
    def __init__(self):
        super(LargeModel, self).__init__()
        self.part1 = nn.Sequential(
            nn.Linear(10000, 1000),
            nn.ReLU()
        ).to('cuda:0')
        self.part2 = nn.Sequential(
            nn.Linear(1000, 100),
            nn.ReLU(),
            nn.Linear(100, 10)
        ).to('cuda:1')
    
    def forward(self, x):
        x = self.part1(x)
        x = x.to('cuda:1')  # 移到第二个 GPU
        x = self.part2(x)
        return x

# 使用模型
model = LargeModel()
x = torch.randn(64, 10000).to('cuda:0')
y = model(x)
print(f"Output shape: {y.shape}")
```

### 24.10 PyTorch 生态系统

- **TorchVision**：计算机视觉相关的模型和工具
- **TorchText**：自然语言处理相关的模型和工具
- **TorchAudio**：音频处理相关的模型和工具
- **TorchGeo**：地理空间数据处理相关的模型和工具
- **PyTorch Lightning**：高级训练框架，简化训练流程
- **Hugging Face Transformers**：预训练的 NLP 模型
- **PyTorch Ignite**：高性能训练工具

### 24.11 常见问题和解决方案

1. **内存不足**：
   - 减少 batch size
   - 使用混合精度训练
   - 使用梯度累积
   - 清理缓存：`torch.cuda.empty_cache()`

2. **训练速度慢**：
   - 使用 GPU
   - 增加 batch size
   - 使用数据加载器的 `num_workers` 参数
   - 使用 `pin_memory=True`

3. **过拟合**：
   - 数据增强
   - 正则化（L1/L2）
   - Dropout
   - 早停

4. **梯度爆炸/消失**：
   - 使用批量归一化
   - 使用适当的激活函数
   - 梯度裁剪
   - 权重初始化

5. **模型不收敛**：
   - 调整学习率
   - 使用不同的优化器
   - 检查数据预处理
   - 检查模型架构