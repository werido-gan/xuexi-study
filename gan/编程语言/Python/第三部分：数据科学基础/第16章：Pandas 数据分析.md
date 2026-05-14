## 第16章：Pandas 数据分析 📊

### 16.1 Pandas 简介

Pandas 是 Python 中用于数据处理和分析的强大库，提供了 DataFrame 和 Series 两种核心数据结构。

```python
import pandas as pd

# 创建 Series
# Series 是一维标记数组
ser = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(ser)

# 创建 DataFrame
# DataFrame 是二维表格数据结构
data = {
    'name': ['小明', '小红', '小强', '小花'],
    'age': [18, 19, 17, 18],
    'score': [90, 85, 92, 88]
}
df = pd.DataFrame(data)
print(df)

# 从文件读取
# 读取 CSV
# df = pd.read_csv('data.csv')

# 读取 Excel
# df = pd.read_excel('data.xlsx')

# 读取 JSON
# df = pd.read_json('data.json')

# 查看数据
df.head()  # 前5行
df.tail()  # 后5行
df.info()  # 数据信息
df.describe()  # 统计信息

# 数据类型
df.dtypes

# 索引
df.index

# 列名
df.columns

# 数据值
df.values
```

### 16.2 数据选择与操作

```python
import pandas as pd

data = {
    'name': ['小明', '小红', '小强', '小花'],
    'age': [18, 19, 17, 18],
    'score': [90, 85, 92, 88],
    'gender': ['男', '女', '男', '女']
}
df = pd.DataFrame(data)

# 选择列
print(df['name'])
print(df[['name', 'score']])

# 选择行
print(df.loc[0])  # 按标签选择
print(df.iloc[0])  # 按位置选择
print(df.loc[0:2])  # 切片

# 条件选择
print(df[df['score'] > 85])
print(df[(df['score'] > 85) & (df['age'] < 19)])

# 修改数据
df['score'] = df['score'] + 5
print(df)

# 添加新列
df['pass'] = df['score'] >= 60
print(df)

# 删除列
df.drop('pass', axis=1, inplace=True)
print(df)

# 删除行
df.drop(0, axis=0, inplace=True)
print(df)

# 排序
df_sorted = df.sort_values('score', ascending=False)
print(df_sorted)

# 分组
grouped = df.groupby('gender')
print(grouped.mean())
print(grouped.count())

# 聚合
df['score'].sum()
df['score'].mean()
df['score'].max()
df['score'].min()

# 缺失值处理
# 检查缺失值
df.isnull().sum()

# 填充缺失值
df.fillna(0, inplace=True)

# 删除缺失值
df.dropna(inplace=True)

# 数据转换
df['age'] = df['age'].astype(str)
df['score'] = df['score'].astype(float)

# 应用函数
df['score'] = df['score'].apply(lambda x: x * 0.8)
print(df)
```

### 16.3 数据合并与连接

```python
import pandas as pd

# 创建两个 DataFrame
df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['小明', '小红', '小强', '小花'],
    'age': [18, 19, 17, 18]
})

df2 = pd.DataFrame({
    'id': [1, 2, 3, 5],
    'score': [90, 85, 92, 88],
    'gender': ['男', '女', '男', '女']
})

# 内连接
inner_join = pd.merge(df1, df2, on='id', how='inner')
print(inner_join)

# 左连接
left_join = pd.merge(df1, df2, on='id', how='left')
print(left_join)

# 右连接
right_join = pd.merge(df1, df2, on='id', how='right')
print(right_join)

# 外连接
outer_join = pd.merge(df1, df2, on='id', how='outer')
print(outer_join)

# 纵向拼接
df3 = pd.DataFrame({
    'id': [6, 7],
    'name': ['小李', '小王'],
    'age': [19, 18]
})

concatenated = pd.concat([df1, df3], axis=0, ignore_index=True)
print(concatenated)

# 横向拼接
df4 = pd.DataFrame({
    'height': [175, 165, 180, 160],
    'weight': [65, 55, 70, 50]
}, index=[0, 1, 2, 3])

merged = pd.concat([df1, df4], axis=1)
print(merged)
```

### 16.4 时间序列处理

```python
import pandas as pd
import numpy as np

# 创建时间序列
# 日期范围
dates = pd.date_range('2024-01-01', periods=7)
print(dates)

# 创建时间序列数据
df = pd.DataFrame({
    'date': dates,
    'value': np.random.randn(7)
})
print(df)

# 设置日期索引
df.set_index('date', inplace=True)
print(df)

# 时间索引操作
df.index.year
df.index.month
df.index.day
df.index.hour

# 重采样
# 按天采样
daily = df.resample('D').mean()

# 按周采样
weekly = df.resample('W').sum()

# 按月采样
monthly = df.resample('M').max()

# 时间偏移
df.shift(1)  # 向后偏移1天
df.shift(-1)  # 向前偏移1天

# 滚动窗口
df.rolling(window=3).mean()  # 3天滚动平均

# 差分
df.diff()  # 一阶差分
```

### 16.5 数据可视化

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建数据
dates = pd.date_range('2024-01-01', periods=30)
df = pd.DataFrame({
    'date': dates,
    'value1': np.random.randn(30).cumsum(),
    'value2': np.random.randn(30).cumsum()
})
df.set_index('date', inplace=True)

# 折线图
df.plot(kind='line')
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()

# 散点图
df.plot(kind='scatter', x='value1', y='value2')
plt.title('Scatter Plot')
plt.show()

# 直方图
df['value1'].plot(kind='hist', bins=10)
plt.title('Histogram')
plt.show()

# 箱线图
df.plot(kind='box')
plt.title('Box Plot')
plt.show()

# 面积图
df.plot(kind='area')
plt.title('Area Plot')
plt.show()
```

### 16.6 数据导出

```python
import pandas as pd

data = {
    'name': ['小明', '小红', '小强', '小花'],
    'age': [18, 19, 17, 18],
    'score': [90, 85, 92, 88]
}
df = pd.DataFrame(data)

# 导出为 CSV
df.to_csv('output.csv', index=False, encoding='utf-8')

# 导出为 Excel
df.to_excel('output.xlsx', index=False)

# 导出为 JSON
df.to_json('output.json', orient='records', force_ascii=False)

# 导出为 HTML
df.to_html('output.html', index=False)
```