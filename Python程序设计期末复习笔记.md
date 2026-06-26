# Python 程序设计期末复习笔记

> **课程来源**：外教课件 Lectures 1-11（2026年春季学期）
> **整理说明**：本笔记整合了11讲课件内容，包含中文翻译与解释、思维导图、代码示例、拓展知识和练习题，帮助你在期末考试中掌握Python编程。

---

# 目录

1. [Python基础与环境](#1-python基础与环境)
2. [分支程序与条件语句](#2-分支程序与条件语句)
3. [while循环](#3-while循环)
4. [for循环与序列迭代](#4-for循环与序列迭代)
5. [一维数组——列表](#5-一维数组列表)
6. [二维数组——列表的列表](#6-二维数组列表的列表)
7. [自定义函数](#7-自定义函数)
8. [高级函数与递归](#8-高级函数与递归)
9. [字符串处理](#9-字符串处理)
10. [列表进阶与元组](#10-列表进阶与元组)
11. [文件处理](#11-文件处理)

---

# 1. Python基础与环境

> 对应课件：Lecture 1

## 1.1 编程新时代

```
编程的演变：
1980s PC早期 → 桌面应用主导
1990s-现在 → 互联网改变一切 → 网站、Web应用、移动App主导

为什么选Python？
  → 简洁易读、语法优雅
  → 排名最高的编程语言之一
  → 应用广泛：Web开发、数据科学、AI、自动化、网络安全
```

## 1.2 什么是编程？

> **编程**：创建一组指令告诉计算机如何完成特定任务。
> **算法（Algorithm）**：有限、定义明确、无歧义的指令序列。

### 算法的四大特性

| 特性 | 含义 |
|------|------|
| **离散性** (Discreteness) | 由独立步骤组成，顺序执行 |
| **确定性** (Determinacy) | 每个指令清晰，相同输入→相同输出 |
| **有穷性** (Finiteness) | 有限步后必须终止 |
| **通用性** (Mass applicability) | 适用于一整类问题，而非单个实例 |

### 算法的三种表示方式

```
1. 流程图（Flowchart）：几何图形+箭头 → 可视化控制流
2. 伪代码（Pseudocode）：人类可读的逻辑描述，不关心语法
3. 编程语言：从低级(汇编)到高级(Python)
```

## 1.3 Python的执行方式

```
Python采用混合方式：
  源代码(.py) → 编译为字节码(.pyc) → 解释器逐行执行

  解释执行的好处：开发调试快
  编译为字节码的好处：跨平台、一定程度的性能优化
```

## 1.4 Python环境搭建

```
安装：
  - python.org 下载 Python 3.x
  - Windows必须勾选"Add Python to PATH"

推荐IDE：
  - VS Code + Python扩展（本课程推荐）
  - PyCharm Community Edition
  - IDLE（Python自带，适合入门）

第一个程序：
  print("Hello, World!")
```

## 1.5 基本数据类型

```python
# 数值类型
int     # 整数，Python 3中任意精度
float   # 浮点数，IEEE 754双精度

# 字符串
'单引号'  "双引号"  '''三引号（多行）'''
```

## 1.6 算术运算

```python
# 运算符（按优先级从高到低）
()      # 括号
**      # 指数运算
* / // %  # 乘、除、整除、取模
+ -     # 加、减

# 关键区别：
5 / 2   # = 2.5（总是返回float）
5 // 2  # = 2（整除，截断小数）
5 % 2   # = 1（取余数）
```

## 1.7 变量与输入

```python
# 变量命名规则：
# - 以字母或下划线开头，后接字母/数字/下划线
# - 区分大小写
# - PEP 8：小写+下划线 (snake_case)
# - 动态类型：同一变量可存储不同类型

# input() 总是返回字符串！
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # 必须转换

# 线性程序：从上到下顺序执行，无分支无循环
```

---

## 📝 基础练习题

**Q1**：写出以下代码的输出：
```python
print(17 / 3)
print(17 // 3)
print(17 % 3)
print(2 ** 10)
```

**Q2**：以下代码有什么问题？
```python
number = input("Enter a number: ")
result = number * 2
print(result)
```

<details>
<summary>点击查看答案</summary>

**A1**：
```
5.666666666666667
5
2
1024
```

**A2**：`input()` 返回字符串，所以 `number * 2` 是字符串重复。输入"5"会输出"55"而非10。应该用 `int(input(...))` 或 `float(input(...))`。
</details>

---

# 2. 分支程序与条件语句

> 对应课件：Lecture 2

## 2.1 布尔类型与比较运算符

```python
# bool 类型：True / False（首字母大写，大小写敏感）

# 比较运算符（返回bool）：
==    # 等于（不是 =！= 是赋值）
!=    # 不等于
<     # 小于
>     # 大于
<=    # 小于等于
>=    # 大于等于

# 字符串按字典序比较（Unicode码点）
# 大写字母 < 小写字母
# 不同类型比较会抛出 TypeError
```

## 2.2 逻辑运算符

```python
# 真值表
# and（与）：全真才真
True and True   # True
True and False  # False
False and True  # False
False and False # False

# or（或）：有真即真
True or True    # True
True or False   # True
False or True   # True
False or False  # False

# not（非）：取反
not True  # False
not False # True
```

### 短路求值（Short-circuit Evaluation）

```python
# and：第一个为False，不再计算第二个
# or：第一个为True，不再计算第二个

# 实用例子：避免除零错误
if x != 0 and y / x > 5:  # 若x=0，不会计算y/x
    print("OK")
```

### 运算符优先级

```
比较运算符 > 逻辑运算符
用括号()明确复杂表达式！
```

## 2.3 if / elif / else

```python
# 基本语法
if condition:
    # 条件为True时执行（必须缩进4个空格！）
    statement
elif other_condition:  # 可选，0个或多个
    statement
else:                  # 可选
    statement

# 关键规则：
# 1. 条件从上到下依次检查
# 2. 第一个为True的块被执行
# 3. 执行完一个块后，其余全部跳过
# 4. 缩进是强制的（Python不用{}）
```

### 经典示例：成绩评级

```python
score = int(input("Enter score: "))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

# 为什么从高到低检查？
# 若先检查 score >= 60，95分会被错误地评为'D'！
```

### 嵌套条件

```python
# 条件可以嵌套（但不要过深，用逻辑运算符简化）
# 闰年判断：
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
# 闰年规则：能被4整除，但能被100整除时还必须能被400整除
```

---

## 📝 条件语句练习题

**Q3**：写出以下代码的输出（输入为85）：
```python
score = int(input())
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

**Q4**：以下代码在 x=0 时会报错吗？为什么？
```python
x = 0
if x != 0 and 10 / x > 2:
    print("Yes")
```

<details>
<summary>点击查看答案</summary>

**A3**：输出 "B"（85满足 >=80，执行后跳过其余条件）

**A4**：不会报错！因为 `x != 0` 为 `False`，短路求值使得 `10 / x > 2` 根本不会执行。
</details>

---

# 3. while 循环

> 对应课件：Lecture 3

## 3.1 循环的核心概念

```
循环（Loop）：指令序列反复执行，直到满足停止条件
  ├─ 循环体（Loop Body）：每次迭代执行的语句
  ├─ 条件（Condition）：控制循环继续或终止
  └─ 迭代变量（Iteration Variable）：循环前初始化、条件中检查、体内更新
```

## 3.2 while 循环语法

```python
counter = 1          # 1. 初始化
while counter <= 5:  # 2. 条件检查
    print(counter)   # 循环体
    counter += 1     # 3. 更新（忘了会导致无限循环！）
# 输出: 1 2 3 4 5

# 停止无限循环：Ctrl + C
```

### 三条铁律
1. **初始化**：循环开始前设置变量初值
2. **条件检查**：while后跟布尔条件+冒号
3. **更新**：体内改变变量 → 否则无限循环

## 3.3 累加器模式（Accumulator Pattern）

```python
# 累加和（Running Total）—— 初始化为0
total = 0
while ...:
    total += value

# 累乘积（Running Product）—— 初始化为1
fact = 1
n = 1
while n <= N:
    fact *= n
    n += 1

# 计数器（Counter）—— 初始化为0
count = 0
while ...:
    if condition:
        count += 1
```

## 3.4 break 和 continue

```python
# break：立即退出循环（不管条件）
while True:
    val = int(input())
    if val == target:
        break  # 找到了，退出

# continue：跳过本次迭代剩余部分，进入下一次条件检查
while ...:
    if num % 2 != 0:
        continue  # 跳过奇数
    total += num  # 只处理偶数
```

## 3.5 经典算法应用

```python
# 1. 输入验证
n = int(input("Enter positive number: "))
while n <= 0:
    print("Invalid!")
    n = int(input("Enter positive number: "))

# 2. 欧几里得算法求GCD
# GCD(a,b)：反复用(b, a%b)替换，直到b=0
while b != 0:
    a, b = b, a % b
print(a)  # a就是最大公约数

# 3. 数字提取（从右到左）
while n > 0:
    digit = n % 10   # 取最后一位
    print(digit)
    n //= 10         # 去掉最后一位
```

---

## 📝 while 循环练习题

**Q5**：以下代码输出什么？
```python
n = 10
while n > 0:
    n -= 3
    print(n, end=' ')
```

**Q6**：用while循环计算1到100的和。

<details>
<summary>点击查看答案</summary>

**A5**：`7 4 1 -2`（依次减3直到n≤0）

**A6**：
```python
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)  # 5050
```
</details>

---

# 4. for 循环与序列迭代

> 对应课件：Lecture 4

## 4.1 while vs for

```
while：条件驱动 —— "只要条件成立就一直做"
  → 不知道具体迭代多少次

for：数据驱动 —— "对集合中每个元素都做一次"
  → 迭代次数 = 集合大小
```

## 4.2 range() 函数

```python
range(stop)          # 0, 1, 2, ..., stop-1
range(start, stop)   # start, start+1, ..., stop-1
range(start, stop, step)  # 以step为步长

# 注意：stop是开区间（不包含）
range(5)       # → 0, 1, 2, 3, 4
range(3, 8)    # → 3, 4, 5, 6, 7
range(0, 10, 2) # → 0, 2, 4, 6, 8
range(10, 0, -1) # → 10, 9, 8, 7, 6, 5, 4, 3, 2, 1（反向）

# range() 返回range对象，惰性生成，不占内存
```

## 4.3 遍历字符串和序列

```python
# 字符串是可迭代的
for char in "Python":
    print(char)  # P y t h o n

# 列表、元组同理
for item in [10, 20, 30, 40]:
    print(item)

# 需要索引时用 enumerate()
for i, value in enumerate(my_list):
    print(f"index {i}: {value}")

# 或用 range(len())
for i in range(len(my_list)):
    print(f"index {i}: {my_list[i]}")
```

## 4.4 嵌套循环

```python
# 外层循环每执行1次，内层循环完整执行一遍
for i in range(3):      # 外循环3次
    for j in range(2):  # 内循环2次
        print(f"({i},{j})", end=' ')
    print()
# 输出：
# (0,0) (0,1)
# (1,0) (1,1)
# (2,0) (2,1)
# 总共 3×2 = 6 次迭代

# 经典例子：九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}×{i}={i*j}", end='\t')
    print()
```

## 4.5 循环 + 条件判断

```python
# 找最大值
max_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num

# 过滤数据
evens = []
for x in numbers:
    if x % 2 == 0:
        evens.append(x)

# 旗标变量（Flag Variable）
found = False
for item in data:
    if item == target:
        found = True
        break
if found:
    print("找到了")
```

---

## 📝 for 循环练习题

**Q7**：写出 `range(2, 11, 3)` 生成的序列。

**Q8**：用 for 循环打印以下图案：
```
*
**
***
****
*****
```

<details>
<summary>点击查看答案</summary>

**A7**：`2, 5, 8`

**A8**：
```python
for i in range(1, 6):
    print('*' * i)
```
</details>

---

# 5. 一维数组——列表（Lists）

> 对应课件：Lecture 5

## 5.1 为什么需要列表？

```
场景：存储30个学生的考试成绩
  不用列表：score1, score2, ..., score30（噩梦！）
  用列表：scores = [85, 92, 78, ...]（一句话搞定）

数组（Array）：存储固定大小、同类型元素的顺序集合
Python列表（List）：更灵活——动态大小、可混合类型
```

## 5.2 列表基础

```python
# Python列表 = 有序 + 可变
# 有序：元素保持插入顺序，可按索引访问
# 可变：可以增删改元素

# 创建列表
numbers = [10, 20, 30, 40, 50]
empty = []
zeros = [0] * 10     # 10个0的列表
chars = list("hello") # ['h','e','l','l','o']
nums = list(range(5))  # [0, 1, 2, 3, 4]

# 列表推导式（Python特有！）
squares = [x**2 for x in range(10)]   # [0,1,4,9,16,25,36,49,64,81]
evens = [x for x in range(20) if x % 2 == 0]  # 带过滤
```

## 5.3 索引与切片

```python
lst = [10, 20, 30, 40, 50]

# 索引（0开始，越界报 IndexError）
lst[0]   # 10（第一个）
lst[-1]  # 50（最后一个）
lst[-2]  # 40（倒数第二个）

# 切片 [start:stop:step]（左闭右开，返回新列表）
lst[0:3]   # [10, 20, 30]
lst[:3]    # [10, 20, 30]（省略start=从头）
lst[2:]    # [30, 40, 50]（省略stop=到尾）
lst[:]     # 浅拷贝整个列表
lst[::2]   # [10, 30, 50]（隔一个取一个）
lst[::-1]  # [50, 40, 30, 20, 10]（反转）
```

## 5.4 列表方法速查表

```python
# 添加
lst.append(x)       # 末尾添加x（原地修改，返回None）
lst.extend(iter)    # 末尾添加所有元素（同 lst += iter）
lst.insert(i, x)    # 在索引i处插入x

# 删除
lst.remove(x)       # 删除第一个x（不存在则 ValueError）
lst.pop(i)          # 删除并返回索引i的元素（默认最后一个，实现栈）
del lst[i]          # 按索引删除
del lst[1:3]        # 按切片删除

# 查找
lst.index(x)        # 返回x第一次出现的位置
lst.count(x)        # 统计x出现次数
x in lst            # 成员检查（返回bool）
len(lst)            # 元素个数（函数，非方法）

# 排序
lst.sort()          # 原地排序（返回None）
lst.sort(reverse=True)  # 降序
sorted(lst)         # 返回新排序列表（原列表不变）
lst.reverse()       # 原地反转
```

## 5.5 经典列表算法

```python
# 线性查找
def linear_search(lst, target):
    for i, val in enumerate(lst):
        if val == target:
            return i
    return -1  # 未找到

# 冒泡排序 O(n²)
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break  # 已排好，提前退出

# 选择排序 O(n²)比较，O(n)交换
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
```

---

## 📝 列表练习题

**Q9**：写出以下代码的输出：
```python
lst = [1, 2, 3, 4, 5]
lst.append(6)
lst.pop(2)
print(lst)
```

**Q10**：用列表推导式生成 [0, 4, 16, 36, 64]（0到8之间偶数的平方）。

<details>
<summary>点击查看答案</summary>

**A9**：`[1, 2, 4, 5, 6]`（添加6到末尾，删除索引2的元素3）

**A10**：`[x**2 for x in range(0, 9, 2)]` 或 `[x**2 for x in range(9) if x % 2 == 0]`
</details>

---

# 6. 二维数组——列表的列表

> 对应课件：Lecture 6

## 6.1 概念

```
真实世界的二维数据：
  - 电子表格（行×列）
  - 数字图像（像素网格）
  - 棋盘（行×列坐标）
  - 数学矩阵

Python表示：list of lists
  matrix[i][j] → 第i行第j列
```

## 6.2 创建二维列表

```python
# 错误方式！（常见陷阱）
matrix = [[0] * 4] * 3
# 这会创建3个对同一内层列表的引用！
matrix[0][0] = 1  # 所有行都会变！

# 正确方式：列表推导式
matrix = [[0 for _ in range(4)] for _ in range(3)]
# 每个内层列表都是独立的对象

# 初始化特定值
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = i * j
```

## 6.3 遍历二维列表

```python
# 行优先遍历（row-major order）
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        process(matrix[i][j])

# 求所有元素的和
total = 0
for row in matrix:
    for elem in row:
        total += elem

# 每行的和
row_sums = [sum(row) for row in matrix]

# 每列的和
col_sums = [sum(row[j] for row in matrix) for j in range(cols)]
```

## 6.4 矩阵运算

```python
# 矩阵加法（同维度）
C[i][j] = A[i][j] + B[i][j]

# 矩阵乘法 A(m×n) × B(n×p) = C(m×p)
for i in range(m):
    for j in range(p):
        C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))

# 矩阵转置
transposed = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
# 或用 zip 技巧：
transposed = list(zip(*matrix))

# 单位矩阵
identity = [[1 if i==j else 0 for j in range(n)] for i in range(n)]

# 对称矩阵：A[i][j] = A[j][i]
```

## 6.5 实际应用

```python
# 图像处理（灰度图 = 二维矩阵，0黑→255白）
negative = [[255 - pixel for pixel in row] for row in image]

# 井字棋（3×3）
board = [[' ' for _ in range(3)] for _ in range(3)]
board[0][1] = 'X'  # 第一行第二列落子
```

---

## 📝 二维列表练习题

**Q11**：创建一个3×3的幻方验证器，检查每行、每列、两条对角线的和是否相等。

<details>
<summary>点击查看答案</summary>

```python
def is_magic_square(square):
    n = len(square)
    target = sum(square[0])  # 以第一行为目标
    
    # 检查行
    for row in square:
        if sum(row) != target:
            return False
    
    # 检查列
    for j in range(n):
        if sum(square[i][j] for i in range(n)) != target:
            return False
    
    # 检查主对角线
    if sum(square[i][i] for i in range(n)) != target:
        return False
    
    # 检查副对角线
    if sum(square[i][n-1-i] for i in range(n)) != target:
        return False
    
    return True
```
</details>

---

# 7. 自定义函数

> 对应课件：Lecture 7

## 7.1 为什么需要函数？

```
函数的四大好处：
  1. 消除重复代码（写一次，反复用）
  2. 模块化（复杂问题拆成小问题）
  3. 抽象化（只需知道做什么，不关心怎么做）
  4. 可测试性（独立验证后再集成）
```

## 7.2 函数定义语法

```python
def function_name(param1, param2):  # def关键字 + 函数名 + 参数列表 + 冒号
    """文档字符串（docstring）：描述函数功能"""
    # 函数体（必须缩进）
    result = param1 + param2
    return result  # 返回值，同时结束函数

# 调用
result = function_name(10, 20)
```

### 函数名规范（PEP 8）
- 小写字母 + 下划线（snake_case）
- 描述函数做什么：`calculate_bmi`, `find_max`

## 7.3 参数传递机制

```python
# Python使用"传对象引用"（pass-by-object-reference）
# 不可变对象（数字、字符串）：函数内修改不影响外部
# 可变对象（列表、字典）：函数内修改会影响外部！

def modify_list(lst):
    lst.append(100)  # 会改变原列表

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 100] ← 变了！
```

## 7.4 参数类型

```python
# 1. 位置参数（Positional）—— 最常见
def describe(name, age):
    pass
describe("Alice", 25)  # 按顺序绑定

# 2. 默认参数（Default）—— 有默认值的参数必须在无默认值之后
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
greet("Bob")        # "Hello, Bob!"
greet("Bob", "Hi")  # "Hi, Bob!"

# 3. 关键字参数（Keyword）—— 按名字传参，提高可读性
describe(age=25, name="Alice")
# 关键字参数必须在位置参数之后

# 4. 可变长度参数
def sum_all(*args):     # *args → 接收任意多个位置参数→元组
    return sum(args)
sum_all(1, 2, 3, 4, 5)  # 15

def print_info(**kwargs):  # **kwargs → 接收任意多个关键字参数→字典
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Bob", age=30, city="Moscow")

# 解包
my_list = [1, 2, 3]
sum_all(*my_list)  # 解包列表为位置参数
```

## 7.5 变量作用域（Scope）

```python
# LEGB规则（Local → Enclosing → Global → Built-in）

x = 10  # 全局变量

def func():
    x = 5       # 局部变量（同名，遮蔽全局）
    print(x)    # 5（使用局部变量）

def func2():
    global x    # 声明要修改全局x
    x = 20

def outer():
    y = 10
    def inner():
        nonlocal y  # 修改外层（非全局）变量
        y = 20
    inner()
    print(y)  # 20
```

## 7.6 文档字符串（Docstring）与测试

```python
def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index.

    Parameters:
        weight_kg (float): Weight in kilograms.
        height_m (float): Height in meters.

    Returns:
        float: The BMI value, rounded to one decimal place.
    """
    return round(weight_kg / (height_m ** 2), 1)

# 访问文档
help(calculate_bmi)
print(calculate_bmi.__doc__)

# 简单测试
assert calculate_bmi(70, 1.75) == 22.9
```

---

## 📝 函数练习题

**Q12**：写一个函数 `is_prime(n)` 判断一个数是否为质数。

**Q13**：以下代码输出什么？
```python
def f(a, lst=[]):
    lst.append(a)
    return lst

print(f(1))
print(f(2))
print(f(3))
```

<details>
<summary>点击查看答案</summary>

**A12**：
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

**A13**：
```
[1]
[1, 2]
[1, 2, 3]
```
这是Python经典陷阱！默认参数在函数定义时只初始化一次，所以每次调用共享同一个列表。正确写法是 `def f(a, lst=None): if lst is None: lst = []`
</details>

---

# 8. 高级函数与递归

> 对应课件：Lecture 8

## 8.1 函数是一等对象（First-Class Objects）

```python
# Python中函数可以：
# 1. 赋值给变量
def square(x): return x * x
f = square       # f 现在引用同一个函数
f(5)             # 25

# 2. 作为参数传递
def apply(func, value):
    return func(value)
apply(square, 5)  # 25

# 3. 作为返回值
def make_adder(n):
    def adder(x):
        return x + n
    return adder
add5 = make_adder(5)
add5(10)  # 15
```

## 8.2 Lambda 表达式

```python
# 匿名函数，用于简短操作
# 语法：lambda 参数: 表达式

sorted(words, key=lambda w: w.lower())
list(map(lambda x: x**2, numbers))
list(filter(lambda x: x > 0, numbers))
```

### 函数式编程工具

```python
# map() —— 对每个元素应用函数
list(map(str.upper, ['hello', 'world']))  # ['HELLO', 'WORLD']

# filter() —— 保留函数返回True的元素
list(filter(lambda x: x > 0, [-2, -1, 0, 1, 2]))  # [1, 2]

# reduce() —— 归约到单个值（from functools import reduce）
from functools import reduce
reduce(lambda a, b: a * b, [1, 2, 3, 4])  # 24 (1*2*3*4)
```

## 8.3 闭包（Closure）

> **闭包**：嵌套函数"记住"外层作用域的变量值

```python
def make_multiplier(factor):
    def multiplier(x):
        return x * factor  # factor被"捕获"
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(10))  # 20  ← factor=2 被记住
print(triple(10))  # 30  ← factor=3 被记住
# 每个闭包捕获的factor是独立的！
```

## 8.4 装饰器（Decorator）

> **装饰器**：接受函数、扩展其行为、返回新函数

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)  # 保留原函数的元数据
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@timer  # 等价于 slow_function = timer(slow_function)
def slow_function():
    total = sum(range(1000000))
    return total
```

## 8.5 递归（Recursion）

> **递归**：函数调用自身。把大问题分解为同类型的小问题。

```python
# 递归两个要素：
# 1. 基本情况（Base Case）：停止条件
# 2. 递归步骤（Recursive Step）：向基本情况靠近

# 阶乘
def factorial(n):
    if n == 0:        # 基本情况
        return 1
    return n * factorial(n - 1)  # 递归步骤

# 斐波那契数列
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### 递归的应用

```
- 汉诺塔（Tower of Hanoi）
- 二分查找（Binary Search）
- 分形（Koch雪花、Sierpinski三角）
- 深度优先搜索（DFS）
- JSON/XML解析
```

### 递归 vs 迭代

|  | 递归 | 迭代 |
|------|------|------|
| **可读性** | 优美，接近数学定义 | 自相似问题不够直观 |
| **性能** | 较慢，占用调用栈 | 更快，更省内存 |
| **限制** | Python递归深度约1000 | 无深度限制 |
| **适用** | 树、图、数学定义 | 大数据量、性能关键 |

---

## 📝 递归练习题

**Q14**：写一个递归函数 `sum_digits(n)` 求一个非负整数各位数字之和。例如 `sum_digits(1234) = 10`。

**Q15**：写一个装饰器，在函数调用前后打印"开始执行"和"执行完毕"。

<details>
<summary>点击查看答案</summary>

**A14**：
```python
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)
```

**A15**：
```python
def announce(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"开始执行 {func.__name__}")
        result = func(*args, **kwargs)
        print(f"执行完毕 {func.__name__}")
        return result
    return wrapper
```
</details>

---

# 9. 字符串处理

> 对应课件：Lecture 9

## 9.1 字符串基础

```python
# Python 3字符串 = Unicode字符的不可变序列
# Unicode：为每种书写系统的每个字符分配唯一码点

# 创建字符串
'text'    # 单引号
"text"    # 双引号（等价）
'''多行'''  # 三引号 → 多行文本和docstring

# 特殊字符
\n    # 换行
\t    # 制表符
\\    # 反斜杠
\' \"  # 嵌套引号

# raw字符串（忽略转义）
r"C:\Users\name"  # 反斜杠不被转义

# f-string（Python 3.6+，最推荐！）
name = "Alice"
age = 25
f"My name is {name}, age {age}"  # "My name is Alice, age 25"
f"Sum: {2 + 3}"                  # "Sum: 5"
f"Pi: {3.14159:.2f}"             # "Pi: 3.14"
```

## 9.2 字符串操作

```python
# 拼接与重复
"Hello, " + "world!"  # "Hello, world!"
"-" * 40               # 40个短横线

# 成员检查
"world" in "Hello, world!"  # True

# 切片（同列表）
s[0:5]    # 前5个字符
s[::-1]   # 反转

# 不可变
s[0] = 'x'  # TypeError！字符串不可原地修改
```

## 9.3 字符串方法速查

```python
# 大小写转换
s.upper()       # 全大写
s.lower()       # 全小写
s.title()       # 标题首字母大写
s.capitalize()  # 句首字母大写

# 空白处理
s.strip()       # 去除两端空白
s.lstrip()      # 去除左侧空白
s.rstrip()      # 去除右侧空白

# 查找
s.find(sub)         # 返回第一次出现的索引（-1未找到）
s.count(sub)        # 非重叠出现次数
s.startswith(pre)   # 检查前缀
s.endswith(suf)     # 检查后缀

# 拆分与连接
s.split()           # 按空白分割→列表
s.split(',')        # 按逗号分割→列表
', '.join(['a','b','c'])  # "a, b, c"
```

## 9.4 三种字符串格式化

```python
name, age = "Alice", 30

# 1. % 运算符（老式，不推荐）
"Name: %s, Age: %d" % (name, age)

# 2. str.format() 方法
"Name: {}, Age: {}".format(name, age)
"{name}, {age}".format(name="Bob", age=25)
"{:.2f}".format(3.14159)  # "3.14"

# 3. f-string（最推荐！）
f"Name: {name}, Age: {age}"
f"{3.14159:.2f}"     # "3.14"
f"{'hi':>10}"        # 右对齐10字符宽度: "        hi"
f"{'hi':^10}"        # 居中: "    hi    "
```

## 9.5 经典字符串算法

```python
# 回文检测
def is_palindrome(s):
    # 清洗：去除非字母数字，转小写
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# 变位词检测
def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

# 凯撒密码
def caesar_encode(text, shift):
    result = ''
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result
```

## 9.6 正则表达式入门

```python
import re

# 基本符号
.     # 任意字符
\d    # 数字
\w    # 单词字符（字母+数字+下划线）
+     # 一个或多个
*     # 零个或多个
[]    # 字符类

# 主要函数
re.search(pattern, text)   # 找第一个匹配（返回Match或None）
re.findall(pattern, text)  # 返回所有不重叠匹配的列表
re.sub(pattern, repl, text) # 替换所有匹配
re.split(pattern, text)    # 按模式分割

# 简单正则优先，复杂场景才用正则
```

---

## 📝 字符串练习题

**Q16**：以下代码输出什么？
```python
s = "  Hello, World!  "
print(s.strip().lower().replace('world', 'Python'))
```

**Q17**：写一个函数 `count_vowels(s)` 统计字符串中元音字母（a, e, i, o, u）的个数。

<details>
<summary>点击查看答案</summary>

**A16**：`hello, Python!`

**A17**：
```python
def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')
```
</details>

---

# 10. 列表进阶与元组

> 对应课件：Lecture 10

## 10.1 列表的底层行为

```python
# Python列表在CPython中实现为动态数组
# O(1) 按索引访问
# O(1) 追加（均摊）
# O(n) 在开头插入或删除

# 赋值的真相
a = [1, 2, 3]
b = a         # b和a指向同一个列表！
b[0] = 99     # a也变了！
print(a)      # [99, 2, 3]

# 创建独立副本
b = a[:]           # 浅拷贝
b = a.copy()       # 浅拷贝
b = list(a)        # 浅拷贝
import copy
b = copy.deepcopy(a)  # 深拷贝（嵌套结构也用这个）
```

## 10.2 列表推导式与生成器

```python
# 列表推导式 = 声明式语法
[expr for item in iterable]
[expr for item in iterable if condition]

# 替代 map 和 filter
[x**2 for x in numbers]                          # 替代 map
[x for x in numbers if x % 2 == 0]               # 替代 filter

# 生成器表达式（用圆括号）—— 惰性求值
(x**2 for x in range(1000000))  # 不立即计算，按需生成
# 特点：惰性、一次性使用、不能索引
```

## 10.3 高级列表操作

```python
# sort() 的 key 参数
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
sorted(students, key=lambda s: s[1])  # 按成绩排序
sorted(students, key=lambda s: (s[1], s[0]))  # 复合排序

# any() 和 all()
any([False, False, True])  # True（有真即真）
all([True, True, False])   # False（全真才真）
# 都具有短路求值 + 惰性求值

# zip() 并行迭代
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# 解压缩
pairs = list(zip(names, scores))
names2, scores2 = zip(*pairs)
```

## 10.4 列表经典算法

```python
# 二分查找（O(log n)，要求有序）
import bisect
idx = bisect.bisect_left(sorted_list, target)

# 去重同时保持顺序
def deduplicate(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# 两数之和问题（O(n)哈希表解法）
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# 合并两个有序列表（双指针）
def merge_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

# 列表旋转k位 O(n) time, O(1) space
def rotate(lst, k):
    k %= len(lst)
    lst.reverse()
    lst[:k] = reversed(lst[:k])
    lst[k:] = reversed(lst[k:])
```

## 10.5 多维列表处理

```python
# 展平（Flatten）
flat = [item for sublist in nested for item in sublist]
# 或用 itertools.chain.from_iterable(nested)

# 按某列排序（重排行）
matrix.sort(key=lambda row: row[col_index])

# 转置
transposed = list(zip(*matrix))
```

## 10.6 元组（Tuple）

```python
# 元组 = 不可变序列
t = (1, 2, 3)
t = 1, 2, 3    # 括号可省略
single = (1,)   # 单元素元组必须有逗号！

# 不可变性 → 可哈希 → 可作为字典键和集合元素（列表不能！）
locations = {(0, 0): "origin", (1, 0): "right"}

# 适用场景
# - 坐标 (x, y)、RGB颜色 (255, 128, 0)、数据库记录
# - 函数返回多个值（本质是返回元组）
def min_max(lst):
    return min(lst), max(lst)  # 返回元组

# 元组解包
x, y, z = (1, 2, 3)   # 一一对应
a, b = b, a            # 交换值（无需临时变量！）
```

---

## 📝 列表进阶练习题

**Q18**：以下代码输出什么？
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

**Q19**：用一行代码（列表推导式）展平 `[[1,2], [3,4], [5,6]]`。

<details>
<summary>点击查看答案</summary>

**A18**：`[1, 2, 3, 4]`（a和b指向同一个列表对象）

**A19**：`[x for sub in [[1,2], [3,4], [5,6]] for x in sub]` → `[1,2,3,4,5,6]`
</details>

---

# 11. 文件处理

> 对应课件：Lecture 11

## 11.1 文件概念

```
文件 = 持久化存储（程序结束后数据不丢失）
  ├─ 文本文件：人类可读（.txt, .py, .csv, .json）
  └─ 二进制文件：机器可读（.png, .mp3, .exe）

Python通过文件对象提供统一接口
open() 指定模式，with 语句自动关闭
```

## 11.2 文件打开模式

| 模式 | 含义 |
|------|------|
| `'r'` | 只读（默认） |
| `'w'` | 写入（覆盖已有内容） |
| `'a'` | 追加（在末尾添加） |
| `'x'` | 创建新文件（文件存在则报错） |
| `'b'` | 二进制模式（如 `'rb'`） |
| `'+'` | 读写（如 `'r+'`） |

## 11.3 读取文件

```python
# 推荐：使用 with 语句（自动关闭）
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()       # 整个文件（大文件慎用）
    # 或
    for line in f:           # 逐行迭代（最省内存！）
        print(line.strip())

# 其他读取方法
with open('file.txt', 'r') as f:
    line = f.readline()        # 读一行（含换行符）
    lines = f.readlines()      # 所有行→列表（小文件适用）
```

## 11.4 写入文件

```python
# write() —— 写字符串（不会自动加换行！）
with open('output.txt', 'w') as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

# print() 写入文件
with open('output.txt', 'w') as f:
    print("Hello", file=f)

# writelines() —— 写字符串序列（每项需自带\n）
lines = ["line1\n", "line2\n", "line3\n"]
with open('output.txt', 'w') as f:
    f.writelines(lines)

# 追加模式
with open('log.txt', 'a') as f:
    f.write("New log entry\n")
```

## 11.5 文件系统操作

```python
import os
from pathlib import Path

# 路径检查
os.path.exists(path)      # 是否存在
os.path.isfile(path)      # 是否是文件
os.path.isdir(path)       # 是否是目录

# 目录操作
os.mkdir('new_dir')                 # 创建目录（父目录必须存在）
os.makedirs('a/b/c', exist_ok=True) # 递归创建
os.rmdir('empty_dir')               # 删除空目录

# 文件操作
import shutil
shutil.copy('src', 'dst')           # 复制
shutil.move('src', 'dst')           # 移动/重命名
os.remove('file.txt')               # 删除
os.rename('old', 'new')             # 重命名

# 元数据
os.path.getsize(path)               # 文件大小
os.path.getmtime(path)              # 最后修改时间
```

## 11.6 常用文件格式

```python
# JSON
import json
data = {'name': 'Alice', 'age': 25}
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)     # 写入
with open('data.json', 'r') as f:
    data = json.load(f)              # 读取

# CSV
import csv
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 25])
```

---

## 📝 文件处理练习题

**Q20**：写一个程序，读取 `input.txt` 中的每一行，将行号添加到每行前面，然后写入 `output.txt`。

**Q21**：以下代码有什么问题？
```python
f = open('file.txt', 'r')
data = f.read()
# ... 处理数据 ...（可能抛异常）
f.close()
```

<details>
<summary>点击查看答案</summary>

**A20**：
```python
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for i, line in enumerate(infile, 1):
        outfile.write(f"{i}: {line}")
```

**A21**：如果在 `f.read()` 和处理之间抛出异常，`f.close()` 不会被执行，导致文件未被关闭。应使用 `with` 语句：`with open('file.txt', 'r') as f:`
</details>

---

# 期末复习总纲

## 知识体系

```
Python 程序设计
├── 基础语法
│   ├── 变量、数据类型（int, float, str, bool, list, tuple）
│   ├── 算术/比较/逻辑运算符与优先级
│   └── input() + 类型转换（str → int/float）
│
├── 控制流
│   ├── if / elif / else + 条件嵌套
│   ├── while 循环 + break/continue + 累加器模式
│   └── for 循环 + range() + 嵌套循环
│
├── 数据结构
│   ├── 列表 → 索引/切片/方法/推导式/排序算法
│   ├── 二维列表 → 矩阵运算/遍历
│   ├── 元组 → 不可变/解包/字典键
│   └── 字符串 → Unicode/方法/f-string/正则
│
├── 函数
│   ├── def + return + 参数类型（位置/默认/关键字/*args/**kwargs）
│   ├── 作用域 LEGB + global/nonlocal
│   ├── lambda + map/filter/reduce
│   ├── 闭包 + 装饰器
│   └── 递归（base case + recursive step）
│
└── 文件
    ├── open() + 模式（r/w/a/b）+ with语句
    ├── read/readline/readlines + write/writelines
    ├── os/pathlib 文件系统操作
    └── JSON/CSV 格式处理
```

## 考试常见代码陷阱

| 陷阱 | 说明 |
|------|------|
| `input()`返回str | 忘记 `int()` / `float()` 转换 |
| `=` vs `==` | 赋值 vs 比较 |
| `5 / 2 = 2.5` | 除法总是返回float |
| `[[0]*n]*m` | 创建了引用的复制，不是独立行 |
| `lst.sort()`返回None | 原地修改，不返回新列表 |
| 默认参数可变对象 | `def f(a, lst=[])` 共享同一列表 |
| 忘记关闭文件 | 使用 `with` 语句 |
| 递归无base case | 导致 RecursionError |

## 考试策略

```
1. 读代码题 → 手动模拟执行，特别注意缩进和变量变化
2. 写代码题 → 先搭框架，逐步细化，不要一次写完全部
3. 改错题 → 关注常见陷阱（见上表）
4. 检查 → 边界情况（空列表、0、负数、大输入）
```

---

> **祝你期末考试顺利！** 🎯

*笔记整理日期：2026年5月18日*
*覆盖课件：Lecture 1-11（完整Python课程）*
