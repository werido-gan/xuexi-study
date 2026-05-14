## 第17章：Matplotlib 数据可视化 📈

### 17.1 Matplotlib 简介

Matplotlib 是 Python 中最常用的数据可视化库，可以创建各种类型的图表，如折线图、散点图、直方图、饼图等。

```python
import matplotlib.pyplot as plt
import numpy as np

# 基本折线图
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sin Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()

# 多个子图
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

x = np.linspace(0, 10, 100)

axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('Sin')

axes[0, 1].plot(x, np.cos(x))
axes[0, 1].set_title('Cos')

axes[1, 0].plot(x, np.tan(x))
axes[1, 0].set_title('Tan')

axes[1, 1].plot(x, np.exp(x))
axes[1, 1].set_title('Exp')

plt.tight_layout()
plt.show()
```

### 17.2 常用图表类型

#### 17.2.1 折线图

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin(x)', color='red', linestyle='-', linewidth=2)
plt.plot(x, y2, label='cos(x)', color='blue', linestyle='--', linewidth=2)

plt.title('Sin and Cos Waves')
plt.xlabel('x')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
```

#### 17.2.2 散点图

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(100)
y = np.random.randn(100)
sizes = np.random.randint(10, 100, 100)
colors = np.random.randn(100)

plt.scatter(x, y, s=sizes, c=colors, alpha=0.5, cmap='viridis')
plt.colorbar()
plt.title('Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
```

#### 17.2.3 直方图

```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.3)
plt.show()
```

#### 17.2.4 饼图

```python
import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [30, 25, 20, 25]
colors = ['red', 'green', 'blue', 'yellow']
explode = (0.1, 0, 0, 0)  # 突出显示第一个扇区

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # 确保饼图是圆形
plt.title('Pie Chart')
plt.show()
```

#### 17.2.5 箱线图

```python
import matplotlib.pyplot as plt
import numpy as np

data = [np.random.randn(100) for _ in range(4)]

plt.boxplot(data, labels=['A', 'B', 'C', 'D'])
plt.title('Box Plot')
plt.xlabel('Group')
plt.ylabel('Value')
plt.grid(axis='y', alpha=0.3)
plt.show()
```

#### 17.2.6 柱状图

```python
import matplotlib.pyplot as plt

x = ['A', 'B', 'C', 'D', 'E']
y = [25, 40, 30, 35, 20]

plt.bar(x, y, color='blue', alpha=0.7)
plt.title('Bar Chart')
plt.xlabel('Category')
plt.ylabel('Value')
plt.grid(axis='y', alpha=0.3)
plt.show()

# 水平柱状图
plt.barh(x, y, color='green', alpha=0.7)
plt.title('Horizontal Bar Chart')
plt.xlabel('Value')
plt.ylabel('Category')
plt.grid(axis='x', alpha=0.3)
plt.show()

# 堆叠柱状图
y1 = [25, 40, 30, 35, 20]
y2 = [15, 25, 20, 15, 10]

plt.bar(x, y1, label='Group 1', color='blue')
plt.bar(x, y2, bottom=y1, label='Group 2', color='red')
plt.title('Stacked Bar Chart')
plt.xlabel('Category')
plt.ylabel('Value')
plt.legend()
plt.show()
```

#### 17.2.7 热力图

```python
import matplotlib.pyplot as plt
import numpy as np

# 创建数据
data = np.random.rand(10, 10)

# 绘制热力图
plt.imshow(data, cmap='viridis')
plt.colorbar()
plt.title('Heatmap')
plt.show()
```

### 17.3 自定义图表

```python
import matplotlib.pyplot as plt
import numpy as np

# 自定义样式
plt.style.use('seaborn-v0_8-whitegrid')

# 基本设置
plt.figure(figsize=(10, 6))

x = np.linspace(0, 10, 100)
y = np.sin(x)

# 绘制
plt.plot(x, y, label='sin(x)', color='purple', linestyle='-', linewidth=2, marker='o', markersize=5, markerfacecolor='white', markeredgecolor='purple')

# 标题和标签
plt.title('Customized Sin Wave', fontsize=16, fontweight='bold')
plt.xlabel('X-axis', fontsize=12)
plt.ylabel('Y-axis', fontsize=12)

# 坐标轴范围
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

# 刻度
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(-1, 1.1, 0.5))

# 网格
plt.grid(True, linestyle='--', alpha=0.7)

# 图例
plt.legend(loc='upper right', fontsize=10, frameon=True, shadow=True)

# 注释
plt.annotate('Peak', xy=(np.pi/2, 1), xytext=(2, 1.2), arrowprops=dict(facecolor='black', shrink=0.05))

# 保存图表
plt.savefig('custom_plot.png', dpi=300, bbox_inches='tight')

plt.show()
```

### 17.4 3D 图表

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 创建 3D 图形
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 生成数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# 绘制 3D 表面图
surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')

# 添加颜色条
fig.colorbar(surf, shrink=0.5, aspect=5)

# 设置标题和标签
ax.set_title('3D Surface Plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

# 3D 散点图
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x = np.random.randn(100)
y = np.random.randn(100)
z = np.random.randn(100)

ax.scatter(x, y, z, c=z, cmap='viridis', s=50, alpha=0.5)

ax.set_title('3D Scatter Plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
```

### 17.5 与 Pandas 结合

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 创建数据
dates = pd.date_range('2024-01-01', periods=30)
df = pd.DataFrame({
    'date': dates,
    'value1': np.random.randn(30).cumsum(),
    'value2': np.random.randn(30).cumsum(),
    'category': ['A']*15 + ['B']*15
})

# 折线图
df.plot(x='date', y=['value1', 'value2'], figsize=(10, 6))
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()

# 散点图
df.plot(kind='scatter', x='value1', y='value2', figsize=(8, 6))
plt.title('Scatter Plot')
plt.show()

# 直方图
df['value1'].plot(kind='hist', bins=10, figsize=(8, 6))
plt.title('Histogram of Value1')
plt.show()

# 箱线图
df.boxplot(column='value1', by='category', figsize=(8, 6))
plt.title('Box Plot by Category')
plt.suptitle('')  # 移除默认标题
plt.show()

# 柱状图
df.groupby('category')['value1'].mean().plot(kind='bar', figsize=(8, 6))
plt.title('Mean Value1 by Category')
plt.ylabel('Mean Value')
plt.show()
```