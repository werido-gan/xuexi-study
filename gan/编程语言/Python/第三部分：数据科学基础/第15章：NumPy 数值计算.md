## 第15章：NumPy 数值计算 🔢

### 15.1 NumPy 简介

NumPy（Numerical Python）是 Python 中用于科学计算的核心库，提供了高效的多维数组操作和数学函数。

```python
import numpy as np

# 创建数组
# 从列表创建
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # [1 2 3 4 5]
print(type(arr))  # <class 'numpy.ndarray'>

# 创建多维数组
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)  # [[1 2 3]
              #  [4 5 6]]

# 创建特殊数组
zeros = np.zeros((3, 4))  # 全0数组
ones = np.ones((2, 3))    # 全1数组
full = np.full((2, 2), 7)  # 填充指定值
range_arr = np.arange(0, 10, 2)  # 类似range
linspace = np.linspace(0, 1, 5)  # 等间隔
random_arr = np.random.rand(2, 3)  # 0-1随机数

# 数组属性
print(arr.shape)  # 形状
print(arr.ndim)   # 维度
print(arr.dtype)  # 数据类型
print(arr.size)   # 元素个数

# 数据类型
arr_int = np.array([1, 2, 3], dtype=np.int32)
arr_float = np.array([1, 2, 3], dtype=np.float64)
```

### 15.2 数组操作

```python
import numpy as np

# 索引和切片
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])      # 1
print(arr[1:4])    # [2 3 4]
print(arr[::-1])   # [5 4 3 2 1]

# 多维数组索引
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0, 1])     # 2
print(arr2d[1:, 1:])   # [[5 6]
                       #  [8 9]]

# 布尔索引
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 3
print(arr[mask])  # [4 5]

# 花式索引
arr = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]
print(arr[indices])  # [10 30 50]

# 数组运算
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 + arr2)  # 对应元素相加
print(arr1 - arr2)  # 对应元素相减
print(arr1 * arr2)  # 对应元素相乘
print(arr1 / arr2)  # 对应元素相除
print(arr1 ** 2)    # 平方

# 广播
arr = np.array([1, 2, 3])
print(arr + 10)  # [11 12 13]

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d + arr)  # 广播

# 聚合函数
arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr))    # 15
print(np.mean(arr))   # 3.0
print(np.min(arr))    # 1
print(np.max(arr))    # 5
print(np.std(arr))    # 标准差
print(np.median(arr)) # 中位数

# 多维数组聚合
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(arr2d, axis=0))  # 按列求和 [5 7 9]
print(np.sum(arr2d, axis=1))  # 按行求和 [6 15]

# 数组变形
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.reshape(2, 3))  # 2行3列
print(arr.reshape(3, -1))  # 3行，列数自动计算

# 数组拼接
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(np.concatenate([arr1, arr2], axis=0))  # 垂直拼接
print(np.concatenate([arr1, arr2], axis=1))  # 水平拼接

# 分割数组
arr = np.array([1, 2, 3, 4, 5, 6])
print(np.split(arr, 3))  # 分成3份

# 转置
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d.T)  # 转置
```

### 15.3 线性代数

```python
import numpy as np

# 矩阵乘法
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))  # 矩阵乘法
print(A @ B)         # 矩阵乘法（Python 3.5+）

# 矩阵求逆
A = np.array([[1, 2], [3, 4]])
A_inv = np.linalg.inv(A)
print(A_inv)

# 行列式
print(np.linalg.det(A))

# 特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)
print(eigenvectors)

# 解线性方程组
# Ax = b
A = np.array([[2, 1], [1, 1]])
b = np.array([4, 3])
x = np.linalg.solve(A, b)
print(x)  # [1 2]
```

### 15.4 随机数生成

```python
import numpy as np

# 设置随机种子
np.random.seed(42)

# 均匀分布
print(np.random.rand(3))  # 0-1之间
print(np.random.uniform(0, 10, 3))  # 0-10之间

# 正态分布
print(np.random.randn(3))  # 标准正态分布
print(np.random.normal(10, 2, 3))  # 均值10，标准差2

# 整数随机数
print(np.random.randint(1, 10, 5))  # 1-9之间的整数

# 随机选择
arr = [1, 2, 3, 4, 5]
print(np.random.choice(arr, size=3, replace=False))  # 无放回

# 打乱数组
np.random.shuffle(arr)
print(arr)
```