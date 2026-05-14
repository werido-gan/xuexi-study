# 🐍 Python 学习笔记：

> 📖 **本笔记特点**：通俗易懂、图文并茂、代码完整、覆盖从入门到机器学习/深度学习的全部知识点。字数无上限，只要是能帮你成为大佬的知识，全部收录！

---

## 📚 目录导航

```
第一部分：Python 入门基础
  第1章：认识 Python
  第2章：环境搭建
  第3章：基础语法
  第4章：数据类型
  第5章：控制流程
  第6章：函数
  第7章：面向对象编程

第二部分：Python 进阶
  第8章：模块与包
  第9章：文件操作
  第10章：异常处理
  第11章：高级特性（装饰器/生成器/迭代器）
  第12章：并发编程
  第13章：正则表达式
  第14章：常用标准库

第三部分：数据科学基础
  第15章：NumPy 数值计算
  第16章：Pandas 数据分析
  第17章：Matplotlib 数据可视化

第四部分：机器学习
  第18章：机器学习基础概念
  第19章：Scikit-learn 入门
  第20章：监督学习算法
  第21章：无监督学习算法
  第22章：模型评估与优化

第五部分：深度学习
  第23章：深度学习基础
  第24章：PyTorch 入门
  第25章：神经网络实战
  第26章：CNN / RNN / Transformer

第六部分：算法与数据结构
  第27章：基本数据结构
  第28章：排序算法
  第29章：搜索算法
  第30章：动态规划

第七部分：实战项目与面试
  第31章：综合实战项目
  第32章：面试高频题与技巧
```

---

# 第一部分：Python 入门基础

---

## 第1章：认识 Python 🌟

### 1.1 什么是 Python？

想象一下，你想让电脑帮你做事，但电脑只懂机器语言（一堆0和1），你得"翻译"给它听。**编程语言**就是这个"翻译工具"。

Python 就是一种特别简单、特别接近人类语言的编程语言。

```
人类说：把苹果放进篮子里
Python说：basket.append("apple")
机器语言：010100110100...（一大串0和1）
```

### 1.2 Python 的特点

```
┌─────────────────────────────────────────────┐
│              Python 的特点                    │
├─────────────┬───────────────────────────────┤
│  简单易学   │ 语法接近英语，新手友好         │
│  跨平台     │ Windows/Mac/Linux 都能运行     │
│  库丰富     │ 几乎什么都能做（AI/爬虫/Web）  │
│  开源免费   │ 完全免费，可商业使用           │
│  解释型     │ 写完直接运行，无需编译         │
└─────────────┴───────────────────────────────┘
```

### 1.3 Python 能做什么？

```
Python 的应用领域
│
├── 🤖 人工智能 / 机器学习
│   ├── 图像识别（人脸识别、自动驾驶）
│   ├── 自然语言处理（ChatGPT底层技术）
│   └── 推荐系统（抖音、淘宝推荐算法）
│
├── 📊 数据分析
│   ├── 股票数据分析
│   ├── 用户行为分析
│   └── 科学研究数据处理
│
├── 🕷️ 网络爬虫
│   ├── 抓取网页数据
│   └── 自动化数据采集
│
├── 🌐 Web 开发
│   ├── Django / Flask 框架
│   └── 搭建网站后端
│
└── 🔧 自动化脚本
    ├── 自动处理 Excel
    ├── 定时发送邮件
    └── 批量重命名文件
```

### 1.4 Python 的历史

| 年份 | 事件 |
|------|------|
| 1989 | Guido van Rossum 圣诞节开始写 Python |
| 1991 | Python 0.9.0 发布 |
| 2000 | Python 2.0 发布 |
| 2008 | Python 3.0 发布（现在主流） |
| 2020 | Python 2 正式停止维护 |
| 今天 | Python 是全球最流行的编程语言之一 |

> 💡 **小贴士**：现在学 Python 直接学 **Python 3**，Python 2 已经是历史了！

---

## 第2章：环境搭建 🛠️

### 2.1 安装 Python

**步骤1：下载 Python**
1. 访问官网：https://www.python.org/
2. 点击 "Downloads"，下载最新版本（如 Python 3.12）

**步骤2：安装时注意**
```
⚠️ 重要！安装时务必勾选：
☑ Add Python to PATH
（这样才能在命令行中使用 python 命令）
```

**步骤3：验证安装**
```bash
# 打开命令行/终端，输入：
python --version
# 或
python3 --version

# 看到类似这样说明成功：
# Python 3.12.0
```

### 2.2 推荐开发工具

#### 方案一：VS Code（推荐新手）
- 免费、轻量
- 安装 Python 插件即可
- 下载：https://code.visualstudio.com/

#### 方案二：PyCharm（推荐专业开发）
- 功能强大
- 社区版免费
- 下载：https://www.jetbrains.com/pycharm/

#### 方案三：Jupyter Notebook（推荐数据科学）
- 可以一边写代码一边看结果
- 特别适合机器学习实验
```bash
pip install jupyter
jupyter notebook
```

### 2.3 虚拟环境（重要！）

虚拟环境就像是给每个项目建立一个独立的"小房间"，不同项目的依赖互不干扰。

```bash
# 创建虚拟环境
python -m venv myenv

# 激活（Windows）
myenv\Scripts\activate

# 激活（Mac/Linux）
source myenv/bin/activate

# 退出虚拟环境
deactivate
```

### 2.4 pip 包管理器

pip 是 Python 的"应用商店"，用来安装第三方库。

```bash
# 安装包
pip install numpy

# 安装指定版本
pip install numpy==1.24.0

# 查看已安装的包
pip list

# 卸载包
pip uninstall numpy

# 导出依赖列表（方便分享项目）
pip freeze > requirements.txt

# 根据依赖列表安装
pip install -r requirements.txt
```

---

## 第3章：基础语法 📝

### 3.1 第一个 Python 程序

```python
# 这是一个注释（以 # 开头的行不会被执行）
print("Hello, World!")  # 打印输出
print("你好，世界！")

# 运行结果：
# Hello, World!
# 你好，世界！
```

### 3.2 注释

```python
# 单行注释：以 # 开头

"""
这是多行注释
可以写很多行
通常用来写文档说明
"""

'''
这也是多行注释
单引号和双引号都可以
'''
```

### 3.3 缩进（Python 的灵魂）

**Python 用缩进来表示代码块，不像其他语言用 `{}` 大括号！**

```python
# ✅ 正确写法
if True:
    print("这行有4个空格的缩进")
    print("这行也是")

# ❌ 错误写法（会报错！）
if True:
print("没有缩进，语法错误！")
```

> 💡 **约定**：使用 **4个空格** 作为一级缩进（不要混用 Tab 和空格！）

### 3.4 变量与赋值

```python
# Python 变量不需要声明类型，直接赋值
name = "小明"           # 字符串
age = 18               # 整数
height = 175.5         # 浮点数
is_student = True      # 布尔值

# 多变量赋值
x, y, z = 1, 2, 3

# 交换两个变量（Python 特有的优雅写法）
a, b = 1, 2
a, b = b, a  # 现在 a=2, b=1

# 查看变量类型
print(type(name))   # <class 'str'>
print(type(age))    # <class 'int'>
```

### 3.5 运算符

#### 算术运算符

```python
a = 10
b = 3

print(a + b)   # 13  加法
print(a - b)   # 7   减法
print(a * b)   # 30  乘法
print(a / b)   # 3.333... 除法（结果是浮点数）
print(a // b)  # 3   整除（去掉小数部分）
print(a % b)   # 1   取余（10除以3余1）
print(a ** b)  # 1000  幂运算（10的3次方）
```

#### 比较运算符

```python
print(5 > 3)   # True
print(5 < 3)   # False
print(5 == 5)  # True （注意是两个等号！）
print(5 != 3)  # True
print(5 >= 5)  # True
print(5 <= 4)  # False
```

#### 逻辑运算符

```python
# and：两个都是True才是True（并且）
print(True and True)   # True
print(True and False)  # False

# or：有一个是True就是True（或者）
print(True or False)   # True
print(False or False)  # False

# not：取反
print(not True)   # False
print(not False)  # True

# 实际例子
age = 20
is_student = True
# 年龄大于18 并且 是学生
print(age > 18 and is_student)  # True
```

#### 成员运算符

```python
fruits = ["apple", "banana", "orange"]

print("apple" in fruits)      # True
print("grape" not in fruits)  # True

name = "Hello Python"
print("Python" in name)  # True
```

### 3.6 print 与 input

```python
# print 输出
print("普通输出")
print("分隔符", "hello", "world", sep="-")  # hello-world
print("不换行", end=" ")  # 默认是换行的，改成空格

# 格式化字符串（三种方式）
name = "小明"
age = 18

# 方式1：% 格式化（旧方式）
print("我叫%s，今年%d岁" % (name, age))

# 方式2：format 方法
print("我叫{}，今年{}岁".format(name, age))

# 方式3：f-string（推荐！最简洁）
print(f"我叫{name}，今年{age}岁")
print(f"10 + 5 = {10 + 5}")  # 可以在花括号里写表达式

# input 输入
user_name = input("请输入你的名字：")
print(f"你好，{user_name}！")

# 注意：input 返回的是字符串，需要转换类型
age_str = input("请输入年龄：")
age_num = int(age_str)  # 转换为整数
```

---

## 第4章：数据类型 📦

### 4.1 数字类型

```python
# 整数（int）- 没有大小限制
small = 42
big = 99999999999999999999

# 浮点数（float）- 带小数点
pi = 3.14159
scientific = 1.5e10  # 科学计数法：1.5 × 10^10

# 复数（complex）
z = 3 + 4j
print(z.real)  # 实部：3.0
print(z.imag)  # 虚部：4.0

# 类型转换
print(int(3.7))    # 3（截断，不是四舍五入）
print(float(5))    # 5.0
print(round(3.7))  # 4（四舍五入）

# 数学运算
import math
print(math.sqrt(16))    # 4.0  开平方
print(math.ceil(3.2))   # 4    向上取整
print(math.floor(3.8))  # 3    向下取整
print(math.pi)          # 3.141592653589793
print(abs(-5))          # 5    绝对值
```

### 4.2 字符串（String）

字符串是最常用的数据类型之一，就是一段文字。

```python
# 创建字符串
s1 = "Hello"
s2 = 'World'
s3 = """多行
字符串"""

# 字符串拼接
result = s1 + " " + s2  # "Hello World"

# 字符串重复
print("ha" * 3)  # "hahaha"

# 获取长度
print(len("Python"))  # 6

# 索引（从0开始）
s = "Python"
print(s[0])   # 'P'
print(s[1])   # 'y'
print(s[-1])  # 'n'  负数从末尾开始

# 切片 [start:end:step]
s = "Hello World"
print(s[0:5])    # "Hello"
print(s[6:])     # "World"（到末尾）
print(s[:5])     # "Hello"（从开头）
print(s[::2])    # "HloWrd"（每隔一个取一个）
print(s[::-1])   # "dlroW olleH"（反转字符串）
```

#### 字符串常用方法

```python
s = "  Hello, Python!  "

# 大小写
print(s.upper())       # "  HELLO, PYTHON!  "
print(s.lower())       # "  hello, python!  "
print(s.title())       # "  Hello, Python!  " (首字母大写)

# 去空白
print(s.strip())       # "Hello, Python!"（去两端空格）
print(s.lstrip())      # "Hello, Python!  "（去左边空格）
print(s.rstrip())      # "  Hello, Python!"（去右边空格）

# 查找与替换
s2 = "Hello, World!"
print(s2.find("World"))     # 7（返回位置，找不到返回-1）
print(s2.replace("World", "Python"))  # "Hello, Python!"
print("Python" in s2)      # False

# 分割与合并
words = "apple,banana,orange".split(",")  # ['apple', 'banana', 'orange']
print(",".join(words))  # "apple,banana,orange"

# 判断
print("123".isdigit())   # True（是否全是数字）
print("abc".isalpha())   # True（是否全是字母）
print("Hello".startswith("He"))  # True
print("Hello".endswith("lo"))    # True

# 格式化（f-string 进阶）
pi = 3.14159
print(f"Pi = {pi:.2f}")   # "Pi = 3.14"（保留2位小数）
print(f"{100:>10}")        # "       100"（右对齐，宽度10）
print(f"{100:<10}")        # "100       "（左对齐）
print(f"{100:0>5}")        # "00100"（用0填充）
```

### 4.3 列表（List）— Python 最常用的数据结构

列表就像一个可以随意增删改查的有序容器。

```python
# 创建列表
fruits = ["apple", "banana", "orange"]
mixed = [1, "hello", 3.14, True, [1, 2]]  # 可以混合类型
empty = []

# 访问元素
print(fruits[0])    # "apple"
print(fruits[-1])   # "orange"

# 切片
print(fruits[0:2])  # ["apple", "banana"]

# 修改元素
fruits[0] = "grape"
print(fruits)  # ["grape", "banana", "orange"]

# 常用方法
fruits = ["apple", "banana", "orange"]
fruits.append("mango")          # 末尾添加
fruits.insert(1, "grape")       # 在位置1插入
fruits.remove("banana")         # 删除第一个匹配的元素
popped = fruits.pop()           # 删除并返回最后一个元素
popped2 = fruits.pop(0)         # 删除并返回指定位置的元素

# 排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()                  # 原地排序
numbers.sort(reverse=True)      # 降序排序
sorted_list = sorted(numbers)   # 返回新列表，不修改原列表

# 其他操作
print(len(fruits))              # 长度
print("apple" in fruits)        # 是否包含
fruits.reverse()                # 原地反转
fruits.extend([1, 2, 3])       # 合并另一个列表
print(fruits.count("apple"))    # 计数
print(fruits.index("apple"))    # 查找位置

# 列表推导式（超级好用！）
# 普通写法
squares = []
for i in range(10):
    squares.append(i ** 2)

# 列表推导式写法（更简洁）
squares = [i ** 2 for i in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 带条件的列表推导式
even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
```

### 4.4 元组（Tuple）— 不可变的列表

元组和列表很像，但是**一旦创建就不能修改**。

```python
# 创建元组
point = (3, 4)
colors = ("red", "green", "blue")
single = (42,)    # 单个元素的元组（注意那个逗号！）

# 访问元素（和列表一样）
print(point[0])   # 3

# 元组拆包（很实用！）
x, y = point
print(x, y)  # 3 4

a, b, c = colors
print(a, b, c)  # red green blue

# 元组不能修改
# point[0] = 10  # 报错！TypeError

# 元组可以用于多返回值
def get_min_max(lst):
    return min(lst), max(lst)

minimum, maximum = get_min_max([3, 1, 4, 1, 5, 9])
print(minimum, maximum)  # 1 9

# 元组转列表，列表转元组
lst = list(point)    # [3, 4]
tup = tuple([1, 2, 3])  # (1, 2, 3)
```

### 4.5 字典（Dictionary）— 键值对存储

字典就像现实中的字典：通过"词"（键）来找"解释"（值）。

```python
# 创建字典
person = {
    "name": "小明",
    "age": 18,
    "city": "北京"
}

# 访问值
print(person["name"])          # "小明"
print(person.get("age"))       # 18
print(person.get("email", "没有邮箱"))  # "没有邮箱"（默认值）

# 修改/添加
person["age"] = 19             # 修改
person["email"] = "xm@qq.com" # 添加新键

# 删除
del person["city"]
removed = person.pop("email")  # 删除并返回值

# 遍历
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

for key in person.keys():
    print(key)

for value in person.values():
    print(value)

# 判断键是否存在
print("name" in person)   # True

# 合并字典
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}  # {"a": 1, "b": 2, "c": 3, "d": 4}

# 字典推导式
squares = {x: x**2 for x in range(6)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### 4.6 集合（Set）— 无序、不重复

集合就像数学中的集合概念，自动去重，无序。

```python
# 创建集合
fruits = {"apple", "banana", "orange", "apple"}  # 重复会自动去掉
print(fruits)  # {'apple', 'banana', 'orange'}

empty_set = set()  # 空集合（不能用{}，那是空字典）

# 添加和删除
fruits.add("mango")
fruits.remove("banana")   # 不存在会报错
fruits.discard("grape")   # 不存在不报错

# 集合运算（超有用！）
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a | b)   # 并集：{1, 2, 3, 4, 5, 6, 7}
print(a & b)   # 交集：{3, 4, 5}
print(a - b)   # 差集：{1, 2}
print(a ^ b)   # 对称差集：{1, 2, 6, 7}（只在一个集合中的元素）

# 判断
print(3 in a)       # True
print({1, 2}.issubset(a))  # True（是a的子集）

# 利用集合去重
lst = [1, 2, 3, 2, 1, 4, 3]
unique = list(set(lst))
print(unique)  # [1, 2, 3, 4]（顺序可能不同）
```

### 4.7 布尔类型（Boolean）

```python
# True 和 False（注意首字母大写！）
is_raining = True
is_sunny = False

# 哪些值被认为是 False？
print(bool(0))      # False
print(bool(""))     # False（空字符串）
print(bool([]))     # False（空列表）
print(bool({}))     # False（空字典）
print(bool(None))   # False

# 哪些值被认为是 True？
print(bool(1))      # True
print(bool(-1))     # True（任何非零数）
print(bool("hello"))  # True
print(bool([0]))    # True（非空列表）
```

### 4.8 None 类型

```python
# None 表示"没有值"或"空"
result = None

def greet(name):
    print(f"Hello, {name}!")
    # 没有return语句，默认返回 None

x = greet("小明")
print(x)  # None

# 判断 None
if result is None:
    print("结果为空")

# 注意：要用 is None，不要用 == None
```

---

## 第5章：控制流程 🔀

### 5.1 条件语句

```python
# if / elif / else
age = 20

if age < 18:
    print("未成年")
elif age < 60:
    print("成年人")
else:
    print("老年人")

# 三元表达式（一行写条件）
score = 85
grade = "及格" if score >= 60 else "不及格"
print(grade)  # "及格"

# 嵌套 if
score = 85
if score >= 60:
    if score >= 90:
        print("优秀")
    elif score >= 80:
        print("良好")
    else:
        print("及格")
else:
    print("不及格")
```

### 5.2 循环

#### for 循环

```python
# 遍历列表
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# range 函数
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):    # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8（步长为2）
    print(i)

# enumerate（同时获取索引和值）
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 输出：
# 0: apple
# 1: banana
# 2: orange

# zip（同时遍历多个列表）
names = ["小明", "小红", "小强"]
scores = [90, 85, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}分")

# 遍历字典
person = {"name": "小明", "age": 18}
for key, value in person.items():
    print(f"{key} = {value}")
```

#### while 循环

```python
# 基本 while 循环
count = 0
while count < 5:
    print(count)
    count += 1

# 猜数字游戏
import random
secret = random.randint(1, 100)
while True:
    guess = int(input("猜一个数字(1-100)："))
    if guess < secret:
        print("猜小了")
    elif guess > secret:
        print("猜大了")
    else:
        print("猜对了！")
        break  # 退出循环
```

#### break / continue / pass

```python
# break：立即退出循环
for i in range(10):
    if i == 5:
        break
    print(i)  # 打印 0 1 2 3 4

# continue：跳过本次循环，继续下一次
for i in range(10):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(i)  # 打印 1 3 5 7 9

# pass：占位符，什么都不做
for i in range(5):
    if i == 3:
        pass  # 暂时不做任何事
    print(i)

# for...else / while...else
for i in range(5):
    print(i)
else:
    print("循环正常结束")  # 如果没有break，会执行这里
```

---

## 第6章：函数 ⚙️

### 6.1 函数基础

```python
# 定义函数
def greet(name):
    """
    这是函数的文档字符串（docstring）
    说明函数的作用
    
    参数:
        name: 要问候的人名
    返回:
        问候语字符串
    """
    return f"Hello, {name}!"

# 调用函数
result = greet("小明")
print(result)  # "Hello, 小明!"

# 无返回值的函数
def say_hello():
    print("Hello!")
    # 没有 return，返回 None
```

### 6.2 参数类型

```python
# 1. 位置参数（最基本）
def add(a, b):
    return a + b
print(add(3, 5))  # 8

# 2. 关键字参数
def describe(name, age, city):
    print(f"{name}, {age}岁, 来自{city}")

describe(name="小明", age=18, city="北京")
describe("小红", city="上海", age=20)  # 混合使用

# 3. 默认参数
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("小明")            # "Hello, 小明!"
greet("小明", "你好")    # "你好, 小明!"

# 4. 可变参数 *args（接收任意多个位置参数）
def sum_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(sum_all(1, 2, 3))      # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# 5. 关键字可变参数 **kwargs（接收任意多个关键字参数）
def show_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

show_info(name="小明", age=18, city="北京")

# 6. 完整的参数顺序
def full_func(a, b, *args, default=10, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"default={default}")
    print(f"kwargs={kwargs}")

full_func(1, 2, 3, 4, 5, default=20, x=10, y=20)
```

### 6.3 高阶函数

函数在 Python 中是"一等公民"，可以当参数传递、可以当返回值。

```python
# 函数作为参数
def apply(func, value):
    return func(value)

def double(x):
    return x * 2

print(apply(double, 5))  # 10

# Lambda 匿名函数（小型函数的简洁写法）
# 格式：lambda 参数: 表达式
square = lambda x: x ** 2
print(square(5))  # 25

add = lambda x, y: x + y
print(add(3, 4))  # 7

# 排序时使用 lambda
students = [("小明", 90), ("小红", 85), ("小强", 92)]
students.sort(key=lambda s: s[1])  # 按成绩排序
print(students)

# 内置高阶函数
# map：对每个元素应用函数
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# filter：过滤元素
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# reduce：累积计算
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120 (1*2*3*4*5)
```

### 6.4 作用域

```python
# 全局变量 vs 局部变量
x = 10  # 全局变量

def func():
    y = 20  # 局部变量，只在函数内有效
    print(x)  # 可以访问全局变量
    print(y)

func()
# print(y)  # 报错！y 不在这里的作用域

# 修改全局变量
def change_global():
    global x  # 声明要修改全局变量
    x = 100

change_global()
print(x)  # 100

# 嵌套函数和 nonlocal
def outer():
    count = 0
    
    def inner():
        nonlocal count  # 修改外层函数的变量
        count += 1
        return count
    
    return inner

counter = outer()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

### 6.5 闭包

```python
# 闭包：内层函数记住了外层函数的变量
def make_multiplier(n):
    def multiplier(x):
        return x * n  # 记住了 n 的值
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15

# 实用例子：计数器
def make_counter(start=0):
    count = [start]  # 用列表是为了能被内层修改
    
    def increment():
        count[0] += 1
        return count[0]
    
    return increment

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
```

---

## 第7章：面向对象编程（OOP）🏗️

### 7.1 什么是面向对象？

> 想象你要建造一座城市：
> - **面向过程**：列出所有步骤，一步步执行（打地基 → 建墙 → 装屋顶...）
> - **面向对象**：把城市里的东西分类（建筑、道路、市民），每种东西有自己的属性和行为

```
现实世界的"猫"  →  Python 中的 Cat 类
─────────────────────────────────────────────
属性：                   类的属性：
  名字 → "小白"            name = "小白"
  颜色 → 白色              color = "white"
  年龄 → 2岁               age = 2

行为：                   类的方法：
  叫                       def meow(self)
  吃饭                     def eat(self)
  睡觉                     def sleep(self)
```

### 7.2 类的定义与使用

```python
# 定义类
class Cat:
    # 类变量（所有实例共享）
    species = "猫科动物"
    
    # 构造方法（创建对象时自动调用）
    def __init__(self, name, color, age):
        # 实例变量（每个对象独有）
        self.name = name
        self.color = color
        self.age = age
    
    # 实例方法（self 是当前对象的引用）
    def meow(self):
        return f"{self.name}: 喵~"
    
    def eat(self, food):
        return f"{self.name}正在吃{food}"
    
    def introduce(self):
        return f"我叫{self.name}，{self.color}色，{self.age}岁"
    
    # 字符串表示（print对象时显示）
    def __str__(self):
        return f"Cat({self.name})"

# 创建对象（实例化）
cat1 = Cat("小白", "白", 2)
cat2 = Cat("小黑", "黑", 3)

# 使用对象
print(cat1.name)        # "小白"
print(cat1.meow())      # "小白: 喵~"
print(cat1.eat("鱼"))   # "小白正在吃鱼"
print(cat1.introduce()) # "我叫小白，白色，2岁"
print(cat1)             # "Cat(小白)"（调用__str__）
print(Cat.species)      # "猫科动物"（访问类变量）
```

### 7.3 三大特性

#### 封装（Encapsulation）

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # 私有属性（双下划线）
    
    # 用方法访问私有属性
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"存入{amount}元，余额{self.__balance}元"
        return "金额必须大于0"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"取出{amount}元，余额{self.__balance}元"
        return "余额不足或金额无效"

account = BankAccount("小明", 1000)
print(account.get_balance())     # 1000
print(account.deposit(500))      # 存入500元，余额1500元
print(account.withdraw(200))     # 取出200元，余额1300元
# print(account.__balance)       # 报错！私有属性不能直接访问
```

#### 继承（Inheritance）

```python
# 父类（基类）
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def breathe(self):
        return f"{self.name}在呼吸"
    
    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"

# 子类（派生类）
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # 调用父类构造方法
        self.breed = breed
    
    def bark(self):
        return f"{self.name}: 汪汪汪！"
    
    def fetch(self, item):
        return f"{self.name}去捡了{item}"

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def meow(self):
        return f"{self.name}: 喵~"

# 使用
dog = Dog("旺财", 3, "金毛")
cat = Cat("小白", 2)

print(dog.breathe())       # 继承自Animal："旺财在呼吸"
print(dog.bark())          # 自己的方法："旺财: 汪汪汪！"
print(dog.breed)           # "金毛"
print(dog)                 # "Dog(旺财)"

# isinstance 检查类型
print(isinstance(dog, Dog))    # True
print(isinstance(dog, Animal)) # True
print(isinstance(cat, Dog))    # False
```

#### 多态（Polymorphism）

```python
class Shape:
    def area(self):
        raise NotImplementedError("子类必须实现此方法")
    
    def describe(self):
        return f"这是一个{self.__class__.__name__}，面积为{self.area():.2f}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# 多态：同一接口，不同行为
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
for shape in shapes:
    print(shape.describe())  # 每个形状有自己的area()实现
```

### 7.4 特殊方法（魔术方法）

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):        # str(obj) 和 print(obj) 调用
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):       # repr(obj) 调用，更详细的表示
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other): # + 运算符
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other): # - 运算符
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar): # * 运算符
        return Vector(self.x * scalar, self.y * scalar)
    
    def __len__(self):         # len(obj) 调用
        return int((self.x**2 + self.y**2) ** 0.5)
    
    def __eq__(self, other):   # == 运算符
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):   # < 运算符
        return len(self) < len(other)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)    # Vector(4, 6)
print(v1 - v2)    # Vector(-2, -2)
print(v1 * 3)     # Vector(3, 6)
print(len(v2))    # 5 (3-4-5 勾股定理)
print(v1 == Vector(1, 2))  # True
```

### 7.5 类方法和静态方法

```python
class Student:
    count = 0  # 类变量，记录学生总数
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.count += 1
    
    # 实例方法（通过 self 访问实例）
    def study(self):
        return f"{self.name}在学习"
    
    # 类方法（通过 cls 访问类本身）
    @classmethod
    def get_count(cls):
        return f"学生总数：{cls.count}"
    
    @classmethod
    def create_from_string(cls, student_string):
        """工厂方法：从字符串创建学生"""
        name, grade = student_string.split("-")
        return cls(name, int(grade))
    
    # 静态方法（不访问实例和类，只是相关的工具函数）
    @staticmethod
    def is_passing(score):
        return score >= 60

s1 = Student("小明", 10)
s2 = Student("小红", 11)

print(Student.get_count())            # "学生总数：2"
s3 = Student.create_from_string("小强-12")  # 工厂方法
print(s3.name, s3.grade)             # "小强" 12

print(Student.is_passing(75))        # True
print(Student.is_passing(55))        # False
```

---

# 第二部分：Python 进阶

---

## 第8章：模块与包 📦

### 8.1 import 语句

```python
# 导入整个模块
import math
print(math.pi)          # 3.14159...
print(math.sqrt(16))    # 4.0

# 导入特定内容
from math import pi, sqrt
print(pi)        # 3.14159...
print(sqrt(16))  # 4.0

# 使用别名
import numpy as np         # 常见写法
import pandas as pd        # 常见写法
from datetime import datetime as dt

# 导入所有（不推荐，可能引起命名冲突）
from math import *
```

### 8.2 创建自己的模块

```python
# 文件：my_utils.py
def add(a, b):
    return a + b

def greet(name):
    return f"Hello, {name}!"

PI = 3.14

# 在另一个文件中使用
import my_utils
print(my_utils.add(3, 5))     # 8
print(my_utils.greet("小明"))  # "Hello, 小明!"
```

### 8.3 `__name__` 与 `__main__`

```python
# my_module.py

def my_function():
    print("函数被调用了")

# 这段代码只在直接运行此文件时执行
# 被其他文件 import 时不执行
if __name__ == "__main__":
    print("这是主程序")
    my_function()
```

### 8.4 包（Package）

```
my_package/
│   __init__.py      # 标志这是一个包（可以为空）
│   utils.py
│   math_tools.py
└── sub_package/
    │   __init__.py
    └── helper.py
```

```python
# 导入包中的模块
from my_package import utils
from my_package.math_tools import add_vectors
```

---

## 第9章：文件操作 📁

### 9.1 读写文本文件

```python
# 写文件
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.writelines(["第三行\n", "第四行\n"])

# 读文件
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()       # 读取全部内容
    print(content)

with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()    # 读取所有行，返回列表

with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:           # 逐行读取（内存友好）
        print(line.strip())

# 追加内容
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("追加的内容\n")
```

### 9.2 文件模式

| 模式 | 含义 |
|------|------|
| `r` | 只读（默认） |
| `w` | 只写（覆盖） |
| `a` | 追加 |
| `r+` | 读写 |
| `rb` | 以二进制只读 |
| `wb` | 以二进制只写 |

### 9.3 处理 CSV 文件

```python
import csv

# 写 CSV
data = [
    ["姓名", "年龄", "城市"],
    ["小明", 18, "北京"],
    ["小红", 20, "上海"],
]
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# 读 CSV
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 使用 DictReader（推荐）
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["姓名"], row["年龄"])
```

### 9.4 处理 JSON 文件

```python
import json

# Python 对象转 JSON 字符串
data = {"name": "小明", "age": 18, "hobbies": ["篮球", "编程"]}
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)

# JSON 字符串转 Python 对象
parsed = json.loads(json_str)
print(parsed["name"])  # "小明"

# 写 JSON 文件
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 读 JSON 文件
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
```

### 9.5 os 模块

```python
import os

# 获取当前目录
print(os.getcwd())

# 列出目录内容
print(os.listdir("."))

# 创建目录
os.makedirs("new_folder/sub_folder", exist_ok=True)

# 删除文件
os.remove("test.txt")

# 文件/目录是否存在
print(os.path.exists("data.csv"))  # True/False
print(os.path.isfile("data.csv"))  # 是否是文件
print(os.path.isdir("my_folder")) # 是否是目录

# 路径操作
path = "/home/user/projects/data.csv"
print(os.path.dirname(path))   # "/home/user/projects"
print(os.path.basename(path))  # "data.csv"
print(os.path.splitext(path))  # ('/home/user/projects/data', '.csv')

# 拼接路径（推荐！跨平台安全）
full_path = os.path.join("home", "user", "data.csv")
```

---

## 第10章：异常处理 🛡️

### 10.1 try / except

```python
# 基本异常处理
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"除零错误：{e}")

# 捕获多种异常
try:
    x = int("abc")  # ValueError
    y = 1 / 0       # ZeroDivisionError
except ValueError as e:
    print(f"值错误：{e}")
except ZeroDivisionError as e:
    print(f"除零错误：{e}")
except Exception as e:   # 捕获所有异常
    print(f"其他错误：{e}")
finally:
    print("无论如何都会执行")  # 常用于关闭文件/连接

# try...else（没有异常时执行）
try:
    result = 10 / 2
except ZeroDivisionError:
    print("出错了")
else:
    print(f"结果是：{result}")  # 只有没有异常时执行
```

### 10.2 常见异常类型

```python
# ValueError：值不合适
int("hello")  # ValueError

# TypeError：类型不匹配
"3" + 3       # TypeError

# IndexError：索引越界
lst = [1, 2, 3]
lst[10]       # IndexError

# KeyError：字典键不存在
d = {"a": 1}
d["b"]        # KeyError

# AttributeError：属性不存在
"hello".nonexistent()  # AttributeError

# FileNotFoundError：文件不存在
open("nonexistent.txt")  # FileNotFoundError

# ImportError：导入失败
import nonexistent_module  # ImportError
```

### 10.3 自定义异常

```python
# 定义自定义异常
class AgeError(ValueError):
    def __init__(self, age, message="年龄无效"):
        self.age = age
        self.message = message
        super().__init__(f"{message}: {age}")

class BankError(Exception):
    pass

class InsufficientFundsError(BankError):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"余额不足：需要{amount}，只有{balance}")

# 使用自定义异常
def set_age(age):
    if not 0 <= age <= 150:
        raise AgeError(age, "年龄必须在0-150之间")
    return age

try:
    set_age(200)
except AgeError as e:
    print(e)  # "年龄必须在0-150之间: 200"
```

---

## 第11章：高级特性 🚀

### 11.1 装饰器（Decorator）

装饰器是 Python 的神器，可以在不修改函数的情况下，给函数添加功能。

> 比喻：函数是一杯白开水，装饰器是茶叶/糖/柠檬，可以给白开水"增味"。

```python
# 基本装饰器
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"准备调用 {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} 调用完毕")
        return result
    return wrapper

@my_decorator  # 等同于 greet = my_decorator(greet)
def greet(name):
    print(f"Hello, {name}!")

greet("小明")
# 输出：
# 准备调用 greet
# Hello, 小明!
# greet 调用完毕

# 计时装饰器（非常实用！）
import time
import functools

def timer(func):
    @functools.wraps(func)  # 保留原函数的信息
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 运行耗时：{end - start:.4f}秒")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "完成"

slow_function()
# 输出：slow_function 运行耗时：1.0001秒

# 带参数的装饰器
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
# 输出：
# Hello!
# Hello!
# Hello!
```

### 11.2 生成器（Generator）

生成器是"懒惰"的序列，一次只生成一个元素，节省内存。

```python
# 普通函数 vs 生成器函数
def normal_range(n):
    result = []
    for i in range(n):
        result.append(i)
    return result  # 一次返回所有元素（占内存）

def my_range(n):
    for i in range(n):
        yield i  # 每次只生成一个元素

# 生成器对象
gen = my_range(5)
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2

for x in my_range(5):
    print(x)

# 无限生成器
def count_up(start=0):
    n = start
    while True:
        yield n
        n += 1

counter = count_up(10)
print(next(counter))  # 10
print(next(counter))  # 11

# 生成器表达式（类似列表推导式，但是懒惰的）
# 列表推导式：立即生成所有元素
squares_list = [x**2 for x in range(1000000)]  # 占很多内存

# 生成器表达式：按需生成
squares_gen = (x**2 for x in range(1000000))   # 几乎不占内存
print(sum(squares_gen))  # 可以直接用 sum 等函数
```

### 11.3 迭代器（Iterator）

```python
# 任何实现了 __iter__ 和 __next__ 的对象就是迭代器
class CountDown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # 告诉循环结束了
        self.current -= 1
        return self.current + 1

for n in CountDown(3):
    print(n)
# 输出：3 2 1

# 内置 iter() 和 next()
lst = [1, 2, 3]
it = iter(lst)         # 创建迭代器
print(next(it))        # 1
print(next(it))        # 2

# itertools 模块
import itertools

# 无限计数
for i in itertools.count(10, 2):  # 从10开始，步长2
    if i > 20: break
    print(i)  # 10, 12, 14, 16, 18, 20

# 循环重复
for item in itertools.cycle([1, 2, 3]):
    print(item)  # 1 2 3 1 2 3 ... 无限循环

# 组合
for combo in itertools.combinations([1, 2, 3], 2):
    print(combo)  # (1,2) (1,3) (2,3)

# 排列
for perm in itertools.permutations([1, 2, 3], 2):
    print(perm)  # (1,2) (1,3) (2,1) (2,3) (3,1) (3,2)
```

### 11.4 上下文管理器

```python
# with 语句的本质是上下文管理器
# 实现 __enter__ 和 __exit__ 方法

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False  # 不抑制异常

with FileManager("test.txt", "w") as f:
    f.write("Hello!")

# 使用 contextlib 简化
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("获取资源")
    try:
        yield "资源对象"
    finally:
        print("释放资源")

with managed_resource() as resource:
    print(f"使用{resource}")
```

### 11.5 类型提示（Type Hints）

Python 3.5+ 支持类型提示，帮助 IDE 提供更好的自动补全。

```python
from typing import List, Dict, Tuple, Optional, Union, Any

# 基本类型提示
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}!"

# 复杂类型
def process_data(
    data: List[int],
    config: Dict[str, Any]
) -> Tuple[List[int], float]:
    sorted_data = sorted(data)
    average = sum(data) / len(data)
    return sorted_data, average

# Optional（可以是None）
def find_user(user_id: int) -> Optional[str]:
    users = {1: "小明", 2: "小红"}
    return users.get(user_id)  # 可能返回 None

# Union（多种类型）
def process(value: Union[int, str]) -> str:
    return str(value)

# Python 3.10+ 新语法
def modern(x: int | str | None) -> str:
    return str(x)
```

---

## 第12章：并发编程 ⚡

### 12.1 多线程

```python
import threading
import time

def download_file(filename, duration):
    print(f"开始下载 {filename}")
    time.sleep(duration)  # 模拟下载耗时
    print(f"{filename} 下载完成")

# 普通顺序执行（慢）
# download_file("file1.zip", 3)
# download_file("file2.zip", 2)
# 总耗时：5秒

# 多线程并发执行（快）
t1 = threading.Thread(target=download_file, args=("file1.zip", 3))
t2 = threading.Thread(target=download_file, args=("file2.zip", 2))

t1.start()
t2.start()

t1.join()  # 等待线程完成
t2.join()
# 总耗时：约3秒（取最长的）

# 线程锁（避免竞争条件）
lock = threading.Lock()
counter = 0

def increment():
    global counter
    with lock:  # 加锁，一次只允许一个线程访问
        counter += 1

threads = [threading.Thread(target=increment) for _ in range(1000)]
for t in threads: t.start()
for t in threads: t.join()
print(counter)  # 1000（正确，不会出现竞争问题）
```

### 12.2 多进程

```python
from multiprocessing import Process, Pool
import os

def cpu_task(n):
    """CPU密集型任务（适合用多进程）"""
    total = sum(i * i for i in range(n))
    return total

# 进程池（推荐）
if __name__ == "__main__":
    with Pool(4) as pool:  # 4个进程
        results = pool.map(cpu_task, [10**6, 10**6, 10**6, 10**6])
        print(results)
```

### 12.3 异步编程（asyncio）

```python
import asyncio
import aiohttp  # 需要安装：pip install aiohttp

async def fetch_url(url):
    """异步获取URL内容"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = [
        "https://www.python.org",
        "https://www.github.com",
    ]
    # 并发请求所有URL
    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for url, result in zip(urls, results):
        print(f"{url}: {len(result)} chars")

# 运行异步程序
asyncio.run(main())

# 简单的 async/await 示例
async def say_after(delay, text):
    await asyncio.sleep(delay)
    print(text)

async def simple_main():
    print("开始")
    await asyncio.gather(
        say_after(2, "world"),
        say_after(1, "hello"),
    )
    print("结束")
# 输出：开始 → hello(1秒后) → world(2秒后) → 结束
```

---

## 第13章：正则表达式 🔍

```python
import re

text = "我的手机号是13812345678，邮箱是user@example.com"

# 基本匹配
pattern = r"\d{11}"  # 11位数字
match = re.search(pattern, text)
if match:
    print("找到手机号:", match.group())  # 13812345678

# 查找所有匹配
all_numbers = re.findall(r"\d+", text)
print(all_numbers)  # ['13812345678']

# 替换
result = re.sub(r"\d{11}", "***手机号***", text)
print(result)

# 常用正则模式
patterns = {
    "手机号":   r"1[3-9]\d{9}",
    "邮箱":     r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "身份证":   r"\d{17}[\dX]",
    "IP地址":   r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
    "URL":      r"https?://[^\s]+",
    "中文":     r"[\u4e00-\u9fff]+",
}

# 正则元字符速查
"""
.    任意一个字符（除换行符）
^    字符串开头
$    字符串结尾
*    0个或多个（贪婪）
+    1个或多个
?    0个或1个
{n}  恰好n个
{n,m} n到m个
[]   字符集合，如[abc][a-z]
[^]  否定字符集
|    或
()   分组
\d   数字 [0-9]
\D   非数字
\w   单词字符 [a-zA-Z0-9_]
\W   非单词字符
\s   空白字符（空格、制表符等）
\S   非空白字符
"""

# 分组
pattern = r"(\d{4})-(\d{2})-(\d{2})"
match = re.search(pattern, "今天是2024-01-15")
if match:
    print(match.group(0))  # "2024-01-15"（完整匹配）
    print(match.group(1))  # "2024"（第1组）
    print(match.group(2))  # "01"（第2组）
    print(match.group(3))  # "15"（第3组）
```

---

# 第三部分：数据科学基础

---

## 第15章：NumPy 数值计算 🔢

NumPy 是 Python 数据科学的基础，提供高效的多维数组和数学运算。

### 15.1 NumPy 数组基础

```python
import numpy as np

# 创建数组
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])  # 2D 数组（矩阵）
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # 3D 数组

print(arr2.shape)   # (2, 3)  2行3列
print(arr2.ndim)    # 2       维度数
print(arr2.size)    # 6       元素总数
print(arr2.dtype)   # int64   数据类型

# 常用创建方法
np.zeros((3, 4))         # 全0矩阵，3行4列
np.ones((2, 3))          # 全1矩阵
np.eye(3)                # 3x3单位矩阵
np.full((2, 3), 7)       # 全7矩阵
np.arange(0, 10, 2)      # [0, 2, 4, 6, 8]（类似range）
np.linspace(0, 1, 5)     # [0, 0.25, 0.5, 0.75, 1]（均匀5个点）
np.random.rand(3, 3)     # 0-1随机数
np.random.randn(3, 3)    # 标准正态分布随机数
np.random.randint(1, 10, (3, 3))  # 随机整数
```

### 15.2 数组索引与切片

```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 索引
print(arr[0, 1])      # 2（第0行第1列）
print(arr[1, :])      # [4, 5, 6]（第1行所有列）
print(arr[:, 2])      # [3, 6, 9]（所有行第2列）
print(arr[0:2, 1:3])  # [[2,3],[5,6]]（切片）

# 布尔索引（超级好用！）
arr = np.array([1, 2, 3, 4, 5, 6])
mask = arr > 3
print(arr[mask])      # [4, 5, 6]

# 直接过滤
print(arr[arr % 2 == 0])  # [2, 4, 6]（偶数）

# 花式索引
print(arr[[0, 2, 4]])  # [1, 3, 5]（取特定位置）
```

### 15.3 数组运算

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 元素级运算
print(a + b)    # [5, 7, 9]
print(a * b)    # [4, 10, 18]
print(a ** 2)   # [1, 4, 9]
print(np.sqrt(a))  # [1., 1.41, 1.73]

# 矩阵运算
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A @ B)           # 矩阵乘法
print(np.dot(A, B))    # 同上
print(A.T)             # 转置
print(np.linalg.inv(A))  # 逆矩阵
print(np.linalg.det(A))  # 行列式

# 广播机制（Broadcasting）
# 不同形状的数组可以自动扩展来运算
a = np.array([[1, 2, 3], [4, 5, 6]])   # shape (2, 3)
b = np.array([10, 20, 30])              # shape (3,)
print(a + b)
# [[11, 22, 33],  # b 被广播到每一行
#  [14, 25, 36]]
```

### 15.4 统计运算

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

# 全局统计
print(np.sum(arr))    # 21
print(np.mean(arr))   # 3.5
print(np.std(arr))    # 标准差
print(np.var(arr))    # 方差
print(np.max(arr))    # 6
print(np.min(arr))    # 1

# 沿指定轴统计
print(np.sum(arr, axis=0))   # [5, 7, 9]（列求和）
print(np.sum(arr, axis=1))   # [6, 15]（行求和）
print(np.mean(arr, axis=0))  # [2.5, 3.5, 4.5]（列均值）

# 排序
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print(np.sort(arr))          # 排序
print(np.argsort(arr))       # 排序后的索引
```

### 15.5 数组变形

```python
arr = np.arange(12)
print(arr)  # [0, 1, 2, ..., 11]

# reshape（重塑形状）
matrix = arr.reshape(3, 4)   # 变成3行4列
print(matrix)

# 展平
flat = matrix.flatten()       # 变回1D
flat2 = matrix.ravel()        # 同上，但可能返回视图

# 拼接
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.vstack([a, b]))  # 垂直拼接
print(np.hstack([a, b]))  # 水平拼接
```

---

## 第16章：Pandas 数据分析 📊

Pandas 是 Python 数据分析的核心库，提供 DataFrame 和 Series。

```
DataFrame 就像 Excel 表格：
  ┌──────┬──────┬──────┐
  │ Name │ Age  │ City │
  ├──────┼──────┼──────┤
  │ 小明 │  18  │ 北京 │
  │ 小红 │  20  │ 上海 │
  │ 小强 │  22  │ 广州 │
  └──────┴──────┴──────┘
```

### 16.1 创建 DataFrame

```python
import pandas as pd
import numpy as np

# 从字典创建
data = {
    "姓名": ["小明", "小红", "小强", "小芳"],
    "年龄": [18, 20, 22, 19],
    "城市": ["北京", "上海", "广州", "深圳"],
    "成绩": [90, 85, 92, 88]
}
df = pd.DataFrame(data)
print(df)

# 从CSV读取
df = pd.read_csv("data.csv", encoding="utf-8")

# 从Excel读取
df = pd.read_excel("data.xlsx")

# 查看基本信息
print(df.head())        # 前5行
print(df.tail(3))       # 后3行
print(df.shape)         # (行数, 列数)
print(df.info())        # 列信息、非空数、数据类型
print(df.describe())    # 统计摘要
print(df.columns)       # 列名
print(df.dtypes)        # 数据类型
```

### 16.2 数据访问

```python
# 访问列
print(df["姓名"])           # Series（单列）
print(df[["姓名", "年龄"]]) # DataFrame（多列）

# 访问行
print(df.loc[0])            # 按索引标签
print(df.iloc[0])           # 按整数位置
print(df.loc[0:2])          # 多行（标签切片，包含末端）
print(df.iloc[0:2])         # 多行（位置切片，不包含末端）

# 访问特定位置
print(df.loc[0, "姓名"])    # "小明"
print(df.iloc[0, 0])        # "小明"

# 条件筛选
print(df[df["年龄"] > 19])
print(df[(df["年龄"] > 19) & (df["成绩"] > 88)])
print(df[df["城市"].isin(["北京", "上海"])])
print(df.query("年龄 > 19 and 成绩 > 88"))  # 等价的查询方式
```

### 16.3 数据清洗

```python
# 缺失值处理
df.isnull()              # 检查缺失值（True/False）
df.isnull().sum()        # 每列缺失值数量
df.dropna()              # 删除含缺失值的行
df.dropna(subset=["年龄"])  # 只看特定列
df.fillna(0)             # 用0填充
df.fillna(df.mean())     # 用均值填充
df["年龄"].fillna(df["年龄"].median(), inplace=True)

# 重复值处理
df.duplicated()          # 检查重复行
df.drop_duplicates()     # 删除重复行
df.drop_duplicates(subset=["姓名"])

# 数据类型转换
df["年龄"] = df["年龄"].astype(int)
df["日期"] = pd.to_datetime(df["日期"])

# 字符串操作
df["姓名"].str.upper()
df["城市"].str.contains("京")
df["名字"] = df["姓名"].str.replace("小", "大")
df["城市"] = df["城市"].str.strip()
```

### 16.4 数据变换

```python
# 添加列
df["总分"] = df["成绩"] * 1.1
df["等级"] = df["成绩"].apply(lambda x: "优秀" if x >= 90 else "良好")

# apply 应用函数
def categorize(age):
    if age < 20:
        return "青少年"
    elif age < 30:
        return "青年"
    else:
        return "中年"

df["年龄段"] = df["年龄"].apply(categorize)

# 排序
df.sort_values("成绩", ascending=False)  # 按成绩降序
df.sort_values(["城市", "成绩"])          # 多列排序

# 分组聚合（groupby）
# 按城市分组，计算平均成绩
city_avg = df.groupby("城市")["成绩"].mean()
print(city_avg)

# 多个聚合
result = df.groupby("城市").agg({
    "成绩": ["mean", "max", "min", "count"],
    "年龄": "mean"
})
print(result)

# 数据透视表
pivot = df.pivot_table(
    values="成绩",
    index="城市",
    columns="年龄段",
    aggfunc="mean"
)
```

### 16.5 数据合并

```python
df1 = pd.DataFrame({"id": [1, 2, 3], "name": ["A", "B", "C"]})
df2 = pd.DataFrame({"id": [2, 3, 4], "score": [90, 85, 92]})

# merge（类似SQL的JOIN）
inner = pd.merge(df1, df2, on="id", how="inner")  # 交集
left  = pd.merge(df1, df2, on="id", how="left")   # 左连接
right = pd.merge(df1, df2, on="id", how="right")  # 右连接
outer = pd.merge(df1, df2, on="id", how="outer")  # 并集

# concat（垂直或水平拼接）
vertical   = pd.concat([df1, df1])                     # 垂直拼接
horizontal = pd.concat([df1, df2], axis=1)             # 水平拼接
```

---

## 第17章：Matplotlib 数据可视化 📈

```python
import matplotlib.pyplot as plt
import numpy as np

# 中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows
plt.rcParams['axes.unicode_minus'] = False

# ─────────────────────────────────────
# 1. 折线图
# ─────────────────────────────────────
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
z = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="sin(x)", color="blue", linewidth=2)
plt.plot(x, z, label="cos(x)", color="red", linestyle="--")
plt.title("三角函数")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# ─────────────────────────────────────
# 2. 散点图
# ─────────────────────────────────────
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5

plt.figure()
plt.scatter(x, y, alpha=0.6, c="green")
plt.title("散点图")
plt.show()

# ─────────────────────────────────────
# 3. 柱状图
# ─────────────────────────────────────
cities = ["北京", "上海", "广州", "深圳"]
values = [90, 85, 92, 88]

plt.figure()
plt.bar(cities, values, color=["red", "blue", "green", "orange"])
plt.title("各城市平均成绩")
plt.ylabel("平均分")
for i, v in enumerate(values):
    plt.text(i, v + 0.5, str(v), ha="center")  # 显示数值
plt.show()

# ─────────────────────────────────────
# 4. 饼图
# ─────────────────────────────────────
labels = ["北京", "上海", "广州", "其他"]
sizes = [30, 25, 20, 25]
explode = (0.1, 0, 0, 0)  # 突出显示第一块

plt.figure()
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
plt.title("城市分布")
plt.show()

# ─────────────────────────────────────
# 5. 热力图（常用于相关性分析）
# ─────────────────────────────────────
import pandas as pd

data = np.random.randn(5, 5)
df = pd.DataFrame(data, columns=list("ABCDE"))
corr = df.corr()

import seaborn as sns
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
plt.title("相关性热力图")
plt.show()

# ─────────────────────────────────────
# 6. 子图
# ─────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot([1, 2, 3], [4, 5, 6])
axes[0, 0].set_title("折线图")

axes[0, 1].scatter([1, 2, 3], [4, 5, 6])
axes[0, 1].set_title("散点图")

axes[1, 0].bar(["A", "B", "C"], [4, 5, 6])
axes[1, 0].set_title("柱状图")

axes[1, 1].hist(np.random.randn(1000), bins=30)
axes[1, 1].set_title("直方图")

plt.tight_layout()
plt.show()
```

---

# 第四部分：机器学习

---

## 第18章：机器学习基础概念 🧠

### 18.1 什么是机器学习？

> 传统编程：程序员 → 规则 + 数据 → 计算机 → 答案  
> 机器学习：数据 + 答案 → 机器学习 → 规则（模型）

机器学习就是让计算机从数据中**自动学习规律**，而不是人工编写规则。

### 18.2 机器学习的分类

```
机器学习
│
├── 监督学习（有标签的训练数据）
│   ├── 分类（预测类别）
│   │   ├── 垃圾邮件识别（是/否）
│   │   ├── 图像分类（猫/狗/鸟）
│   │   └── 情感分析（正面/负面）
│   └── 回归（预测连续值）
│       ├── 房价预测
│       ├── 股价预测
│       └── 天气温度预测
│
├── 无监督学习（无标签，自己发现规律）
│   ├── 聚类（K-means）
│   │   └── 用户分群、图像分割
│   └── 降维（PCA）
│       └── 特征压缩、可视化
│
└── 强化学习（通过奖惩机制学习）
    ├── 游戏AI（AlphaGo）
    └── 机器人控制
```

### 18.3 关键概念

```
数据集分割：
┌──────────────────────────────┐
│          全部数据             │
├────────────────┬─────────────┤
│  训练集(70%)   │  测试集(30%) │
└────────────────┴─────────────┘

更好的做法（交叉验证）：
┌──────────────────────────────────────────┐
│              全部数据                     │
├────────────┬────────────┬────────────────┤
│  训练集     │   验证集   │    测试集       │
│   (60%)    │   (20%)    │    (20%)       │
└────────────┴────────────┴────────────────┘
```

**重要术语：**

| 术语 | 解释 |
|------|------|
| 特征（Feature） | 输入变量，比如房子的面积、房间数 |
| 标签（Label） | 要预测的输出，比如房价 |
| 模型 | 从数据中学到的"规则" |
| 过拟合 | 模型在训练集表现好，但新数据表现差 |
| 欠拟合 | 模型连训练集都拟合不好 |
| 超参数 | 训练前设置的参数（学习率、深度等） |
| 损失函数 | 衡量预测值与真实值的差距 |

### 18.4 机器学习工作流程

```
1. 数据收集
   ↓
2. 数据探索 (EDA)
   ↓
3. 数据预处理
   ├── 缺失值处理
   ├── 异常值处理
   ├── 特征工程
   └── 数据标准化
   ↓
4. 选择模型
   ↓
5. 训练模型
   ↓
6. 评估模型
   ↓
7. 调优（调整超参数）
   ↓
8. 部署模型
```

---

## 第19章：Scikit-learn 入门 🔬

### 19.1 Scikit-learn 基本使用模式

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1. 准备数据
from sklearn.datasets import load_iris
data = load_iris()
X = data.data     # 特征
y = data.target   # 标签

# 2. 分割数据
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. 数据预处理（标准化）
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)   # 在训练集上学习并转换
X_test = scaler.transform(X_test)          # 只转换测试集（不重新学习）

# 4. 选择并训练模型
model = LogisticRegression()
model.fit(X_train, y_train)

# 5. 预测
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)  # 预测概率

# 6. 评估
print("准确率:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

### 19.2 数据预处理

```python
from sklearn.preprocessing import (
    StandardScaler, MinMaxScaler, RobustScaler,
    LabelEncoder, OneHotEncoder
)
from sklearn.impute import SimpleImputer

import numpy as np

# ─────────────────────────────────────
# 缺失值处理
# ─────────────────────────────────────
X = np.array([[1, 2, np.nan], [3, np.nan, 5], [np.nan, 7, 8]])

imputer = SimpleImputer(strategy="mean")  # 或 median, most_frequent
X_filled = imputer.fit_transform(X)

# ─────────────────────────────────────
# 特征缩放
# ─────────────────────────────────────
X = np.array([[1, 100], [2, 200], [3, 300]])

# 标准化（均值0，方差1），适合正态分布
scaler = StandardScaler()
print(scaler.fit_transform(X))

# 归一化（压缩到[0,1]），适合分布不均匀的数据
minmax = MinMaxScaler()
print(minmax.fit_transform(X))

# ─────────────────────────────────────
# 分类变量编码
# ─────────────────────────────────────
from sklearn.preprocessing import OrdinalEncoder

# Label 编码（适合有序类别）
le = LabelEncoder()
cities = ["北京", "上海", "广州", "北京", "上海"]
print(le.fit_transform(cities))  # [1, 2, 0, 1, 2]

# One-Hot 编码（适合无序类别）
encoder = OneHotEncoder(sparse_output=False)
data = [["北京"], ["上海"], ["广州"]]
print(encoder.fit_transform(data))
# [[1, 0, 0],
#  [0, 1, 0],
#  [0, 0, 1]]
```

---

## 第20章：监督学习算法 📐

### 20.1 线性回归

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# 生成模拟数据：y = 2x + 1 + 噪声
np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 2 * X.ravel() + 1 + np.random.randn(100)

# 训练
model = LinearRegression()
model.fit(X, y)
print(f"斜率(系数): {model.coef_[0]:.2f}")    # 约2
print(f"截距: {model.intercept_:.2f}")         # 约1

# 评估
y_pred = model.predict(X)
print(f"MSE: {mean_squared_error(y, y_pred):.4f}")  # 均方误差
print(f"R²: {r2_score(y, y_pred):.4f}")             # R²（越接近1越好）
```

> 💡 **理解 R²**：
> - R² = 1：完美预测
> - R² = 0：模型和直接用均值一样好
> - R² < 0：模型比直接用均值还差

### 20.2 逻辑回归（分类）

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score, confusion_matrix

# 生成分类数据
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 训练
model = LogisticRegression()
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

# 混淆矩阵
cm = confusion_matrix(y_test, y_pred)
print("混淆矩阵:")
print(cm)
"""
              预测正类  预测负类
真实正类  [[  TP  ,  FN  ],  
真实负类   [  FP  ,  TN  ]]
"""

# 评估指标
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
```

### 20.3 决策树

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

data = load_iris()
X, y = data.data, data.target

model = DecisionTreeClassifier(
    max_depth=3,          # 最大深度，防止过拟合
    min_samples_split=5,  # 节点分裂最小样本数
    random_state=42
)
model.fit(X, y)

# 查看决策树结构
tree_rules = export_text(model, feature_names=data.feature_names)
print(tree_rules)

# 特征重要性
for name, importance in zip(data.feature_names, model.feature_importances_):
    print(f"{name}: {importance:.4f}")
```

### 20.4 随机森林

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,     # 树的数量
    max_depth=5,          # 每棵树最大深度
    random_state=42,
    n_jobs=-1             # 使用所有CPU核心
)
model.fit(X_train, y_train)
print(f"测试集准确率: {model.score(X_test, y_test):.4f}")
```

> 💡 **随机森林的直觉**：
> 一个人做决策可能出错，但如果让100个人分别做决策，然后多数服从少数，出错的概率就大大降低了。这就是"集成学习"的思想！

### 20.5 支持向量机（SVM）

```python
from sklearn.svm import SVC

model = SVC(
    C=1.0,           # 正则化参数，越大越不容忍错误分类
    kernel="rbf",    # 核函数：linear, poly, rbf, sigmoid
    gamma="scale"    # 核函数的参数
)
model.fit(X_train, y_train)
```

### 20.6 K 近邻（KNN）

```python
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(
    n_neighbors=5,     # K值，取最近的5个邻居
    metric="euclidean" # 距离度量
)
model.fit(X_train, y_train)
```

> 💡 **KNN 的直觉**："物以类聚，人以群分"。找到最相似的K个样本，用他们的标签来预测。

### 20.7 梯度提升（XGBoost）

```python
# pip install xgboost
import xgboost as xgb

model = xgb.XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)
model.fit(X_train, y_train,
          eval_set=[(X_test, y_test)],
          verbose=False)
print(f"准确率: {model.score(X_test, y_test):.4f}")
```

---

## 第21章：无监督学习算法 🔮

### 21.1 K-Means 聚类

```python
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# 生成聚类数据
X, y_true = make_blobs(n_samples=300, centers=4, random_state=42)

# K-Means
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
y_pred = kmeans.fit_predict(X)

# 可视化
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=y_true, cmap="viridis")
plt.title("真实分组")

plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap="viridis")
plt.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1],
            marker="*", s=300, c="red", label="聚类中心")
plt.title("K-Means 聚类结果")
plt.legend()
plt.show()

# 选择最优K值（肘部法则）
inertias = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)

plt.plot(range(1, 11), inertias, marker="o")
plt.xlabel("K值")
plt.ylabel("惯性（越小越好）")
plt.title("肘部法则选择最优K")
plt.show()
```

### 21.2 主成分分析（PCA）

```python
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits

# 加载手写数字数据（64维）
digits = load_digits()
X = digits.data   # shape: (1797, 64)

# 降维到2D
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print(f"原始维度: {X.shape}")       # (1797, 64)
print(f"降维后: {X_reduced.shape}") # (1797, 2)

# 查看保留了多少信息
print(f"方差解释率: {pca.explained_variance_ratio_}")
print(f"总信息保留: {sum(pca.explained_variance_ratio_):.2%}")

# 可视化
plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_reduced[:, 0], X_reduced[:, 1],
                      c=digits.target, cmap="tab10", alpha=0.7)
plt.colorbar(scatter)
plt.title("手写数字 PCA 降维可视化")
plt.show()
```

---

## 第22章：模型评估与优化 🎯

### 22.1 交叉验证

```python
from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold

model = RandomForestClassifier(random_state=42)

# 5折交叉验证
scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
print(f"各折准确率: {scores}")
print(f"平均准确率: {scores.mean():.4f} ± {scores.std():.4f}")
```

### 22.2 超参数调优

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

# 网格搜索（穷举所有组合）
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [3, 5, 7, None],
    "min_samples_split": [2, 5, 10]
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1,
    verbose=1
)
grid_search.fit(X_train, y_train)
print(f"最佳参数: {grid_search.best_params_}")
print(f"最佳得分: {grid_search.best_score_:.4f}")

# 随机搜索（适合大参数空间）
from scipy.stats import randint
param_dist = {
    "n_estimators": randint(50, 500),
    "max_depth": randint(1, 20),
}
random_search = RandomizedSearchCV(
    RandomForestClassifier(),
    param_dist,
    n_iter=50,
    cv=5,
    random_state=42
)
random_search.fit(X_train, y_train)
```

### 22.3 Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# 把预处理和模型打包成流水线
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("svm", SVC(kernel="rbf"))
])

# 流水线可以直接 fit 和 predict
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

# 还可以一起做交叉验证和超参数搜索
param_grid = {
    "svm__C": [0.1, 1, 10],
    "svm__gamma": [0.01, 0.1, 1]
}
grid = GridSearchCV(pipeline, param_grid, cv=5)
grid.fit(X_train, y_train)
```

### 22.4 评估指标详解

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, roc_curve, confusion_matrix
)

# ─────────────────────────────────────────────────
# 分类指标
# ─────────────────────────────────────────────────
"""
混淆矩阵：
                预测正      预测负
真实正   TP(真正例)  FN(假负例)
真实负   FP(假正例)  TN(真负例)

准确率(Accuracy)  = (TP+TN) / (TP+TN+FP+FN)  → 总体预测对了多少比例
精确率(Precision) = TP / (TP+FP)               → 预测为正的中，真的是正的比例
召回率(Recall)    = TP / (TP+FN)               → 真正正例中，被预测出来的比例
F1分数            = 2 * P * R / (P + R)         → 精确率和召回率的调和平均

何时用哪个指标？
- 准确率：类别均衡时
- 精确率：假阳性代价高（如垃圾邮件检测，不想误判正常邮件）
- 召回率：假阴性代价高（如癌症诊断，不想漏诊）
- F1：需要平衡精确率和召回率
"""

# ─────────────────────────────────────────────────
# 回归指标
# ─────────────────────────────────────────────────
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

"""
MAE (平均绝对误差)：简单直观，对异常值不敏感
MSE (均方误差)：对大误差更敏感
RMSE (均方根误差)：MSE的开方，与目标值同单位
R² (决定系数)：越接近1越好，可以理解为"解释了多少方差"
"""
```

---

# 第五部分：深度学习

---

## 第23章：深度学习基础 🧬

### 23.1 神经网络的直觉

```
一个神经元：

输入:  x₁  x₂  x₃
       │   │   │
权重:  w₁  w₂  w₃
        \  │  /
         加权求和
            │
         + 偏置 b
            │
         激活函数 f
            │
          输出 y

数学公式：y = f(w₁x₁ + w₂x₂ + w₃x₃ + b)
```

### 23.2 激活函数

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

# Sigmoid：输出[0,1]，适合二分类输出
sigmoid = 1 / (1 + np.exp(-x))

# Tanh：输出[-1,1]，比Sigmoid梯度更大
tanh = np.tanh(x)

# ReLU：最常用！解决梯度消失问题
relu = np.maximum(0, x)

# Leaky ReLU：解决"死亡ReLU"问题
leaky_relu = np.where(x > 0, x, 0.01 * x)

# Softmax：多分类输出层
def softmax(z):
    e_z = np.exp(z - np.max(z))  # 减最大值防止溢出
    return e_z / e_z.sum()

# 各激活函数的适用场景：
"""
- 隐藏层：ReLU（首选）/ Leaky ReLU（防死亡）/ Tanh
- 二分类输出层：Sigmoid（输出概率）
- 多分类输出层：Softmax（输出概率分布）
- 回归输出层：无激活函数（线性输出）
"""
```

### 23.3 反向传播与梯度下降

```python
"""
训练神经网络的过程：

1. 前向传播：输入 → 各层计算 → 输出预测值
2. 计算损失：损失函数（MSE、交叉熵等）
3. 反向传播：从损失开始，用链式法则计算各参数的梯度
4. 参数更新：w = w - 学习率 × 梯度

优化器对比：
- SGD（随机梯度下降）：简单，收敛慢，容易振荡
- Momentum：加速度机制，减少振荡
- RMSprop：自适应学习率
- Adam：最常用！结合Momentum和RMSprop

常见损失函数：
- MSE（均方误差）：回归问题
- 交叉熵（Cross Entropy）：分类问题
- Binary Cross Entropy：二分类问题
"""
```

---

## 第24章：PyTorch 入门 🔥

### 24.1 张量（Tensor）基础

```python
import torch

# 创建张量
t1 = torch.tensor([1, 2, 3])           # 从列表创建
t2 = torch.zeros(3, 4)                  # 全0
t3 = torch.ones(2, 3)                   # 全1
t4 = torch.rand(2, 3)                   # 均匀随机
t5 = torch.randn(2, 3)                  # 正态分布随机
t6 = torch.arange(0, 10, 2)            # [0, 2, 4, 6, 8]

# 属性
print(t2.shape)   # torch.Size([3, 4])
print(t2.dtype)   # torch.float32
print(t2.device)  # cpu

# GPU（如果有CUDA）
if torch.cuda.is_available():
    t2 = t2.cuda()   # 移到GPU
    t2 = t2.to("cuda:0")

# NumPy互转
import numpy as np
arr = np.array([1, 2, 3])
t = torch.from_numpy(arr)
arr2 = t.numpy()

# 基本运算
a = torch.tensor([[1., 2.], [3., 4.]])
b = torch.tensor([[5., 6.], [7., 8.]])

print(a + b)        # 元素加
print(a @ b)        # 矩阵乘法
print(torch.mm(a, b))  # 同上
print(a.T)          # 转置

# 形状变换
x = torch.arange(12)
print(x.reshape(3, 4))
print(x.view(3, 4))     # 共享内存
print(x.unsqueeze(0))   # 增加维度
print(x.unsqueeze(0).squeeze(0))  # 去掉维度
```

### 24.2 自动微分（Autograd）

```python
import torch

# 需要计算梯度的张量
x = torch.tensor(2.0, requires_grad=True)
y = x ** 3  # y = x³

y.backward()  # 反向传播，计算梯度
print(x.grad)  # dy/dx = 3x² = 3*4 = 12

# 多元函数
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = (x ** 2).sum()  # y = x₁² + x₂² + x₃²
y.backward()
print(x.grad)  # [2*1, 2*2, 2*3] = [2, 4, 6]

# 停止梯度计算（推理时用）
with torch.no_grad():
    result = x * 2  # 不会追踪梯度
```

### 24.3 建立神经网络

```python
import torch
import torch.nn as nn
import torch.optim as optim

# ─────────────────────────────────────
# 方式1：Sequential（简洁）
# ─────────────────────────────────────
model = nn.Sequential(
    nn.Linear(784, 256),   # 输入784维，输出256维
    nn.ReLU(),
    nn.Dropout(0.5),       # Dropout防过拟合
    nn.Linear(256, 128),
    nn.ReLU(),
    nn.Linear(128, 10),    # 输出10分类
)

# ─────────────────────────────────────
# 方式2：继承 nn.Module（灵活）
# ─────────────────────────────────────
class MLP(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(MLP, self).__init__()
        
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.5)
        self.fc2 = nn.Linear(hidden_size, num_classes)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        return x

model = MLP(784, 256, 10)
print(model)

# 查看参数数量
total_params = sum(p.numel() for p in model.parameters())
print(f"总参数量: {total_params:,}")
```

### 24.4 训练循环

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# 准备数据（示例）
X_train = torch.randn(1000, 784)
y_train = torch.randint(0, 10, (1000,))

dataset = TensorDataset(X_train, y_train)
loader = DataLoader(dataset, batch_size=32, shuffle=True)

# 模型、损失函数、优化器
model = MLP(784, 256, 10)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 训练循环
num_epochs = 10
for epoch in range(num_epochs):
    model.train()  # 训练模式（启用Dropout等）
    
    total_loss = 0
    correct = 0
    
    for X_batch, y_batch in loader:
        # 前向传播
        outputs = model(X_batch)
        loss = criterion(outputs, y_batch)
        
        # 反向传播
        optimizer.zero_grad()  # 清零梯度（很重要！）
        loss.backward()
        optimizer.step()       # 更新参数
        
        total_loss += loss.item()
        _, predicted = torch.max(outputs, 1)
        correct += (predicted == y_batch).sum().item()
    
    avg_loss = total_loss / len(loader)
    accuracy = 100 * correct / len(dataset)
    print(f"Epoch [{epoch+1}/{num_epochs}] Loss: {avg_loss:.4f} Acc: {accuracy:.2f}%")

# 保存模型
torch.save(model.state_dict(), "model.pth")

# 加载模型
model = MLP(784, 256, 10)
model.load_state_dict(torch.load("model.pth"))
model.eval()  # 评估模式（关闭Dropout）
```

---

## 第25章：经典网络架构 🏛️

### 25.1 卷积神经网络（CNN）

```python
class CNN(nn.Module):
    def __init__(self, num_classes=10):
        super(CNN, self).__init__()
        
        # 特征提取层
        self.features = nn.Sequential(
            # 卷积层1：输入1通道，输出32通道，3x3卷积核
            nn.Conv2d(1, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),  # 尺寸减半
            
            # 卷积层2
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
        )
        
        # 分类层
        self.classifier = nn.Sequential(
            nn.Linear(64 * 7 * 7, 512),  # 对于28x28的MNIST图片
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(512, num_classes),
        )
    
    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)  # 展平
        x = self.classifier(x)
        return x

"""
CNN 核心概念：
┌─────────────────────────────────────────────────────┐
│  卷积层（Conv2d）                                     │
│  - 用卷积核扫描图像，提取局部特征                      │
│  - 参数少（权重共享），适合处理图像                    │
│                                                      │
│  池化层（MaxPool/AvgPool）                            │
│  - 降低特征图尺寸，减少计算量                         │
│  - 同时增加感受野（看到更大范围）                     │
│                                                      │
│  批归一化（BatchNorm）                                │
│  - 加速训练，减少对初始化的敏感性                     │
│  - 一定程度的正则化效果                              │
└─────────────────────────────────────────────────────┘
"""
```

### 25.2 循环神经网络（RNN/LSTM）

```python
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super(LSTMModel, self).__init__()
        
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,   # 输入格式：(batch, seq_len, input_size)
            dropout=0.2 if num_layers > 1 else 0
        )
        self.fc = nn.Linear(hidden_size, num_classes)
    
    def forward(self, x):
        # x: (batch, seq_len, input_size)
        out, (h_n, c_n) = self.lstm(x)
        
        # 取最后一个时间步的输出
        out = self.fc(out[:, -1, :])
        return out

"""
RNN/LSTM 核心概念：
┌─────────────────────────────────────────────────────┐
│  RNN：有"记忆"的网络，处理序列数据                   │
│  - 文本、语音、时间序列                              │
│                                                      │
│  LSTM 解决了 RNN 的梯度消失问题：                    │
│  - 遗忘门：决定丢掉哪些信息                         │
│  - 输入门：决定存储哪些新信息                        │
│  - 输出门：决定输出什么                             │
│                                                      │
│  GRU：LSTM 的简化版，参数更少，效果也不差            │
└─────────────────────────────────────────────────────┘
"""
```

### 25.3 Transformer（简介）

```python
"""
Transformer 是现代 NLP 的基础架构（GPT、BERT 都基于它）

核心机制：自注意力（Self-Attention）
─────────────────────────────────────
传统 RNN：顺序处理，慢，难以捕捉长距离依赖
Transformer：并行处理，每个位置都能直接关注所有位置

自注意力计算过程：
1. 输入：序列中每个词的向量
2. 计算 Q（查询）、K（键）、V（值）矩阵
3. Attention = softmax(QK^T / √d_k) × V

Transformer 结构：
  ┌─────────────────────┐
  │     编码器          │  ← 理解输入
  │  多头注意力         │
  │  前馈网络           │
  ├─────────────────────┤
  │     解码器          │  ← 生成输出
  │  多头注意力         │
  │  编解码注意力       │
  │  前馈网络           │
  └─────────────────────┘

PyTorch 内置 Transformer
"""
import torch.nn as nn

transformer = nn.Transformer(
    d_model=512,        # 模型维度
    nhead=8,            # 注意力头数
    num_encoder_layers=6,
    num_decoder_layers=6,
    dim_feedforward=2048,
    dropout=0.1
)
```

---

# 第六部分：算法与数据结构

---

## 第27章：基本数据结构 🗂️

### 27.1 栈（Stack）

```python
# 栈：后进先出（LIFO）
# 就像一摞盘子，只能从顶部放和取

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):    # 入栈
        self.items.append(item)
    
    def pop(self):            # 出栈
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):           # 查看栈顶
        if not self.is_empty():
            return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# 应用：括号匹配检测
def is_balanced(s):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty() or stack.peek() != pairs[char]:
                return False
            stack.pop()
    
    return stack.is_empty()

print(is_balanced("([{}])"))   # True
print(is_balanced("([{])"))    # False
```

### 27.2 队列（Queue）

```python
from collections import deque

# 队列：先进先出（FIFO）
class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):  # 入队
        self.items.append(item)
    
    def dequeue(self):         # 出队
        if not self.is_empty():
            return self.items.popleft()
    
    def is_empty(self):
        return len(self.items) == 0

# 优先队列
import heapq

pq = []
heapq.heappush(pq, (1, "任务A"))  # (优先级, 任务)
heapq.heappush(pq, (3, "任务C"))
heapq.heappush(pq, (2, "任务B"))

while pq:
    priority, task = heapq.heappop(pq)
    print(f"执行: {task} (优先级{priority})")
# 输出：任务A, 任务B, 任务C（按优先级从小到大）
```

### 27.3 链表

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))
    
    def delete(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # 1 -> 2 -> 3
```

### 27.4 二叉树

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    # 前序遍历：根 → 左 → 右
    def preorder(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
    
    # 中序遍历：左 → 根 → 右（BST中是升序！）
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=" ")
            self.inorder(node.right)
    
    # 后序遍历：左 → 右 → 根
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=" ")
    
    # 层序遍历（BFS）
    def level_order(self, root):
        if not root:
            return
        queue = deque([root])
        while queue:
            node = queue.popleft()
            print(node.val, end=" ")
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

# 二叉搜索树（BST）
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        self.root = self._insert(self.root, val)
    
    def _insert(self, node, val):
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node
    
    def search(self, val):
        return self._search(self.root, val)
    
    def _search(self, node, val):
        if not node or node.val == val:
            return node
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)
```

### 27.5 哈希表

```python
# Python 的 dict 就是哈希表，底层通过哈希函数实现
d = {}
d["key"] = "value"  # O(1) 的插入和查找

# 手动实现简单哈希表（了解原理）
class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])
    
    def get(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None
```

---

## 第28章：排序算法 🔄

```python
# ─────────────────────────────────────────────────
# 冒泡排序 O(n²)  — 最简单但最慢
# ─────────────────────────────────────────────────
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# ─────────────────────────────────────────────────
# 选择排序 O(n²)
# ─────────────────────────────────────────────────
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# ─────────────────────────────────────────────────
# 插入排序 O(n²)  — 小数组效果好，接近有序时很快
# ─────────────────────────────────────────────────
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# ─────────────────────────────────────────────────
# 归并排序 O(n log n)  — 稳定，适合链表
# ─────────────────────────────────────────────────
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ─────────────────────────────────────────────────
# 快速排序 O(n log n) 平均  — 实践中最快
# ─────────────────────────────────────────────────
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

# 排序算法比较
"""
算法         最好      平均      最坏     空间    稳定
冒泡排序    O(n)     O(n²)    O(n²)    O(1)    是
选择排序    O(n²)    O(n²)    O(n²)    O(1)    否
插入排序    O(n)     O(n²)    O(n²)    O(1)    是
归并排序  O(nlogn) O(nlogn) O(nlogn)  O(n)    是
快速排序  O(nlogn) O(nlogn)  O(n²)    O(logn) 否
堆排序    O(nlogn) O(nlogn) O(nlogn)  O(1)    否

Python 内置的 sort() 使用 Timsort，
结合了插入排序和归并排序，实际性能非常优秀
"""
```

---

## 第29章：搜索算法 🔎

```python
# ─────────────────────────────────────────────────
# 线性搜索 O(n)
# ─────────────────────────────────────────────────
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# ─────────────────────────────────────────────────
# 二分搜索 O(log n)  — 必须先排序！
# ─────────────────────────────────────────────────
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# 递归版本
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid+1, right)
    else:
        return binary_search_recursive(arr, target, left, mid-1)

# BFS（广度优先搜索）
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# DFS（深度优先搜索）
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    result = [node]
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result

# 示例图
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

print("BFS:", bfs(graph, 'A'))  # A B C D E F
print("DFS:", dfs(graph, 'A'))  # A B D E C F
```

---

## 第30章：动态规划（DP）🏆

动态规划是解决最优化问题的利器，核心思想是**把大问题拆成小问题，记录中间结果，避免重复计算**。

```python
# ─────────────────────────────────────────────────
# 斐波那契数列（DP 入门）
# ─────────────────────────────────────────────────
# 方式1：递归（慢！大量重复计算）
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# 方式2：记忆化递归（加速）
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n-1) + fib_memo(n-2)

# 方式3：动态规划（最好）
def fib_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# ─────────────────────────────────────────────────
# 爬楼梯问题（经典 DP）
# 每次可以爬1或2个台阶，爬n级有多少种方法？
# ─────────────────────────────────────────────────
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]  # 从i-1级跨1步 或 从i-2级跨2步
    return dp[n]

# ─────────────────────────────────────────────────
# 0/1 背包问题（经典 DP）
# 有n个物品，各有重量w和价值v，背包容量为W
# 选取物品使总价值最大，每个物品只能选一次
# ─────────────────────────────────────────────────
def knapsack(weights, values, capacity):
    n = len(weights)
    # dp[i][j] = 前i个物品，容量为j时的最大价值
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(capacity + 1):
            # 不选第i个物品
            dp[i][j] = dp[i-1][j]
            # 选第i个物品（如果放得下）
            if j >= weights[i-1]:
                dp[i][j] = max(dp[i][j], 
                               dp[i-1][j-weights[i-1]] + values[i-1])
    
    return dp[n][capacity]

# 测试
weights = [2, 3, 4, 5]
values  = [3, 4, 5, 6]
capacity = 8
print(f"最大价值: {knapsack(weights, values, capacity)}")  # 10

# ─────────────────────────────────────────────────
# 最长公共子序列（LCS）
# ─────────────────────────────────────────────────
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

print(lcs("ABCBDAB", "BDCAB"))  # 4 ("BCAB")
```

---

# 第七部分：实战项目与面试

---

## 第31章：综合实战项目 💼

### 31.1 鸢尾花分类（完整 ML 项目）

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

# ─── 1. 数据加载与探索 ───────────────────────────
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target
df["species"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

print("数据形状:", df.shape)
print("\n前5行:")
print(df.head())
print("\n统计摘要:")
print(df.describe())
print("\n各类别数量:")
print(df["species"].value_counts())

# ─── 2. 数据可视化 ──────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

for i, feature in enumerate(iris.feature_names):
    ax = axes[i // 2, i % 2]
    for species in df["species"].unique():
        data = df[df["species"] == species][feature]
        ax.hist(data, alpha=0.6, label=species, bins=20)
    ax.set_title(feature)
    ax.legend()

plt.tight_layout()
plt.savefig("iris_distribution.png")
plt.show()

# ─── 3. 数据预处理 ──────────────────────────────
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ─── 4. 模型训练 ────────────────────────────────
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", RandomForestClassifier(n_estimators=100, random_state=42))
])

# 交叉验证
cv_scores = cross_val_score(pipeline, X_train, y_train, cv=5)
print(f"\n交叉验证准确率: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

pipeline.fit(X_train, y_train)

# ─── 5. 模型评估 ────────────────────────────────
y_pred = pipeline.predict(X_test)
print("\n分类报告:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 混淆矩阵可视化
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=iris.target_names,
            yticklabels=iris.target_names)
plt.title("混淆矩阵")
plt.ylabel("真实标签")
plt.xlabel("预测标签")
plt.show()

# 特征重要性
rf = pipeline.named_steps["clf"]
importances = rf.feature_importances_
plt.figure(figsize=(8, 5))
plt.barh(iris.feature_names, importances)
plt.title("特征重要性")
plt.xlabel("重要性分数")
plt.show()
```

### 31.2 手写数字识别（PyTorch CNN）

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# ─── 1. 数据准备 ─────────────────────────────────
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

train_dataset = datasets.MNIST("./data", train=True,
                                download=True, transform=transform)
test_dataset = datasets.MNIST("./data", train=False, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader  = DataLoader(test_dataset, batch_size=64, shuffle=False)

# ─── 2. 定义模型 ─────────────────────────────────
class ConvNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_layers = nn.Sequential(
            nn.Conv2d(1, 32, 3, padding=1), nn.ReLU(),
            nn.Conv2d(32, 64, 3, padding=1), nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Dropout(0.25)
        )
        self.fc_layers = nn.Sequential(
            nn.Linear(64 * 14 * 14, 128), nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, 10)
        )
    
    def forward(self, x):
        x = self.conv_layers(x)
        x = x.view(x.size(0), -1)
        return self.fc_layers(x)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = ConvNet().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# ─── 3. 训练 ─────────────────────────────────────
def train(epoch):
    model.train()
    for batch, (X, y) in enumerate(train_loader):
        X, y = X.to(device), y.to(device)
        optimizer.zero_grad()
        output = model(X)
        loss = criterion(output, y)
        loss.backward()
        optimizer.step()
        
        if batch % 200 == 0:
            print(f"Epoch {epoch}, Batch {batch}/{len(train_loader)}, "
                  f"Loss: {loss.item():.4f}")

def test():
    model.eval()
    correct = 0
    with torch.no_grad():
        for X, y in test_loader:
            X, y = X.to(device), y.to(device)
            output = model(X)
            correct += output.argmax(1).eq(y).sum().item()
    accuracy = 100. * correct / len(test_dataset)
    print(f"测试准确率: {accuracy:.2f}%")

for epoch in range(1, 6):
    train(epoch)
    test()

# 保存模型
torch.save(model.state_dict(), "mnist_cnn.pth")
```

---

## 第32章：面试高频题 💡

### 32.1 Python 基础面试题

```python
# ─── Q1：Python 中的可变与不可变类型 ───────────────
"""
不可变：int, float, str, tuple, frozenset
可变：list, dict, set

为什么重要？
- 默认参数陷阱：
"""
def add_item(item, lst=[]):  # ❌ 危险！默认参数是可变的
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2]  ！不是预期的[2]

def add_item_safe(item, lst=None):  # ✅ 正确写法
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# ─── Q2：深拷贝 vs 浅拷贝 ──────────────────────────
import copy

lst = [[1, 2], [3, 4]]

# 浅拷贝：只复制第一层
shallow = copy.copy(lst)
shallow[0].append(9)
print(lst)  # [[1, 2, 9], [3, 4]]  ！原列表被修改

lst = [[1, 2], [3, 4]]
# 深拷贝：完全独立的副本
deep = copy.deepcopy(lst)
deep[0].append(9)
print(lst)  # [[1, 2], [3, 4]]  原列表不受影响

# ─── Q3：GIL（全局解释器锁） ────────────────────────
"""
GIL 是 CPython 中的一个锁，同一时刻只允许一个线程执行 Python 代码。
- 影响：多线程无法利用多核CPU（CPU密集型任务）
- 不影响：I/O密集型任务（等待期间会释放GIL）
- 解决方案：多进程（multiprocessing）或使用C扩展
"""

# ─── Q4：*args 和 **kwargs ──────────────────────────
def show(*args, **kwargs):
    print(f"args: {args}")      # 元组
    print(f"kwargs: {kwargs}")  # 字典

show(1, 2, 3, name="小明", age=18)
# args: (1, 2, 3)
# kwargs: {'name': '小明', 'age': 18}

# ─── Q5：列表推导式 vs map/filter ──────────────────
# 一般推荐列表推导式，更 Pythonic
nums = range(10)

# 传统
even_squares = list(map(lambda x: x**2, filter(lambda x: x%2==0, nums)))

# 列表推导式（更清晰）
even_squares = [x**2 for x in nums if x % 2 == 0]
```

### 32.2 算法面试高频题

```python
# ─── 两数之和 ──────────────────────────────────────
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# ─── 反转字符串 ─────────────────────────────────────
def reverse_string(s):
    return s[::-1]

# ─── 判断回文 ──────────────────────────────────────
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# ─── 有效括号 ──────────────────────────────────────
def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()
    return not stack

# ─── 最大子数组和（Kadane算法）────────────────────
def max_subarray(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# ─── 二叉树最大深度 ─────────────────────────────────
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# ─── 快速幂 ─────────────────────────────────────────
def fast_pow(base, exp):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2
    return result
```

---

## 附录：Python 常用速查表

### 字符串方法速查

| 方法 | 作用 | 示例 |
|------|------|------|
| `upper()` | 转大写 | `"abc".upper()` → `"ABC"` |
| `lower()` | 转小写 | `"ABC".lower()` → `"abc"` |
| `strip()` | 去两端空格 | `"  abc  ".strip()` → `"abc"` |
| `split()` | 分割字符串 | `"a,b,c".split(",")` → `["a","b","c"]` |
| `join()` | 合并列表 | `",".join(["a","b"])` → `"a,b"` |
| `replace()` | 替换子串 | `"hello".replace("l","r")` → `"herro"` |
| `find()` | 查找位置 | `"hello".find("ll")` → `2` |
| `startswith()` | 是否以...开头 | `"hello".startswith("he")` → `True` |
| `format()` | 格式化 | `"{0} + {1}".format(1,2)` → `"1 + 2"` |

### 列表方法速查

| 方法 | 作用 | 示例 |
|------|------|------|
| `append(x)` | 末尾添加 | `[1,2].append(3)` → `[1,2,3]` |
| `insert(i,x)` | 指定位置插入 | `[1,3].insert(1,2)` → `[1,2,3]` |
| `remove(x)` | 删除第一个x | `[1,2,1].remove(1)` → `[2,1]` |
| `pop(i)` | 删除并返回 | `[1,2,3].pop()` → `3` |
| `sort()` | 原地排序 | `[3,1,2].sort()` → `[1,2,3]` |
| `reverse()` | 原地反转 | `[1,2,3].reverse()` → `[3,2,1]` |
| `index(x)` | 查找位置 | `[1,2,3].index(2)` → `1` |
| `count(x)` | 计数 | `[1,2,1].count(1)` → `2` |
| `extend(lst)` | 合并列表 | `[1].extend([2,3])` → `[1,2,3]` |

### 时间复杂度速查

| 数据结构 | 查找 | 插入 | 删除 |
|---------|------|------|------|
| 列表（末尾） | O(n) | O(1) | O(1) |
| 列表（中间） | O(n) | O(n) | O(n) |
| 字典 | O(1) | O(1) | O(1) |
| 集合 | O(1) | O(1) | O(1) |
| 堆 | O(n) | O(log n) | O(log n) |

### 机器学习算法速查

| 算法 | 适用场景 | 优点 | 缺点 |
|------|---------|------|------|
| 线性回归 | 连续值预测 | 简单、可解释 | 只能线性关系 |
| 逻辑回归 | 二分类 | 简单、概率输出 | 线性假设 |
| 决策树 | 分类/回归 | 可解释 | 容易过拟合 |
| 随机森林 | 通用 | 准确、稳健 | 速度慢、黑箱 |
| SVM | 高维、小数据 | 效果好 | 参数敏感 |
| KNN | 小数据集 | 简单无需训练 | 预测慢 |
| XGBoost | 竞赛首选 | 性能优异 | 参数多 |
| K-Means | 聚类 | 简单快速 | 需指定K值 |
| PCA | 降维 | 去噪、压缩 | 线性假设 |

---

## 🎯 学习路线总结

```
阶段1：打好基础（1-2个月）
├── Python 基础语法
├── 数据类型与结构
├── 函数与面向对象
└── 练习：LeetCode 简单题 20道

阶段2：数据科学三件套（1个月）
├── NumPy
├── Pandas
└── Matplotlib

阶段3：机器学习（2个月）
├── 机器学习理论
├── Scikit-learn 实战
└── 项目：Kaggle 入门竞赛

阶段4：深度学习（3个月）
├── 神经网络理论
├── PyTorch 框架
└── 项目：图像分类 / NLP

阶段5：进阶专业方向（持续）
├── 计算机视觉（CV）
├── 自然语言处理（NLP）
├── 强化学习（RL）
└── 大模型应用
```

---

## 📚 推荐学习资源

### 书籍
- 《Python 编程：从入门到实践》— Eric Matthes
- 《利用 Python 进行数据分析》— Wes McKinney
- 《机器学习》— 周志华（西瓜书）
- 《深度学习》— Goodfellow 等（花书）
- 《动手学深度学习》— 李沐（免费在线）

### 在线资源
- 菜鸟教程：https://www.runoob.com/python3/
- 廖雪峰 Python 教程：https://www.liaoxuefeng.com/
- 动手学深度学习：https://zh.d2l.ai/
- Kaggle：https://www.kaggle.com/
- LeetCode：https://leetcode.cn/

### 视频课程
- B站：吴恩达机器学习课程（中文字幕）
- B站：李沐《动手学深度学习》
- Coursera：Andrew Ng Deep Learning Specialization

---

> 🚀 **记住：学编程最重要的是动手！每学一个概念，立刻写代码试验。遇到问题是正常的，解决问题才是成长！加油！** 💪

---

*本笔记版本：2026年 | 适用：Python 3.8+*