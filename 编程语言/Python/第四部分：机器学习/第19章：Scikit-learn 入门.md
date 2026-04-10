## 第19章：Scikit-learn 入门 🛠️

### 19.1 Scikit-learn 简介

Scikit-learn 是 Python 中最流行的机器学习库，它提供了简单且高效的工具用于数据挖掘和数据分析。

> **特点**：
> - 简单易用的API
> - 包含多种机器学习算法
> - 与 NumPy、Pandas、Matplotlib 无缝集成
> - 提供完整的机器学习工作流程支持

### 19.2 安装 Scikit-learn

```bash
pip install scikit-learn
```

### 19.3 基本使用流程

1. **导入库**
2. **加载数据**
3. **数据预处理**
4. **模型选择**
5. **模型训练**
6. **模型评估**
7. **模型预测**

### 19.4 数据加载

#### 19.4.1 内置数据集

Scikit-learn 提供了一些内置数据集，方便快速上手。

```python
from sklearn.datasets import load_iris, load_digits, load_wine, load_breast_cancer, load_boston, fetch_california_housing

# 分类数据集
iris = load_iris()
digits = load_digits()
wine = load_wine()
breast_cancer = load_breast_cancer()

# 回归数据集
boston = load_boston()  # 已弃用
california = fetch_california_housing()

# 查看数据
print(iris.data.shape)  # 特征数据
print(iris.target.shape)  # 目标数据
print(iris.feature_names)  # 特征名称
print(iris.target_names)  # 目标类别名称
```

#### 19.4.2 自定义数据

```python
import numpy as np
import pandas as pd

# 从 NumPy 数组创建
X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([0, 1, 0])

# 从 Pandas DataFrame 创建
data = pd.DataFrame({
    'feature1': [1, 3, 5],
    'feature2': [2, 4, 6],
    'target': [0, 1, 0]
})
X = data[['feature1', 'feature2']]
y = data['target']
```

### 19.5 数据预处理

#### 19.5.1 特征缩放

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# 标准化（均值为0，标准差为1）
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 归一化（缩放到0-1之间）
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# 鲁棒缩放（对异常值不敏感）
scaler = RobustScaler()
X_scaled = scaler.fit_transform(X)
```

#### 19.5.2 特征编码

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# 标签编码（将类别转换为整数）
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# 独热编码（将类别转换为二进制向量）
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# 假设第0列是类别特征
ct = ColumnTransformer([
    ('onehot', OneHotEncoder(), [0])
], remainder='passthrough')
X_encoded = ct.fit_transform(X)
```

#### 19.5.3 缺失值处理

```python
from sklearn.impute import SimpleImputer

# 填充缺失值
imputer = SimpleImputer(strategy='mean')  # 也可以是 'median', 'most_frequent', 'constant'
X_imputed = imputer.fit_transform(X)
```

#### 19.5.4 数据分割

```python
from sklearn.model_selection import train_test_split

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

### 19.6 模型训练与预测

#### 19.6.1 分类模型

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# 逻辑回归
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)

# 决策树
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 随机森林
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 支持向量机
model = SVC()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# K最近邻
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

#### 19.6.2 回归模型

```python
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

# 线性回归
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Ridge 回归（L2正则化）
model = Ridge(alpha=1.0)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Lasso 回归（L1正则化）
model = Lasso(alpha=0.1)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 决策树回归
model = DecisionTreeRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 随机森林回归
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

### 19.7 模型评估

#### 19.7.1 分类评估

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

# 准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# 精确率、召回率、F1分数
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")

# 混淆矩阵
cm = confusion_matrix(y_test, y_pred)
print(f"Confusion Matrix:\n{cm}")

# 分类报告
report = classification_report(y_test, y_pred)
print(f"Classification Report:\n{report}")

# ROC AUC（二分类）
if len(np.unique(y)) == 2:
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, y_pred_proba)
    print(f"ROC AUC: {auc}")
    
    # 绘制 ROC 曲线
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
    plt.plot(fpr, tpr, label=f'AUC = {auc:.2f}')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend()
    plt.show()
```

#### 19.7.2 回归评估

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 均方误差
mse = mean_squared_error(y_test, y_pred)
print(f"MSE: {mse}")

# 均方根误差
rmse = np.sqrt(mse)
print(f"RMSE: {rmse}")

# 平均绝对误差
mae = mean_absolute_error(y_test, y_pred)
print(f"MAE: {mae}")

# R² 分数
r2 = r2_score(y_test, y_pred)
print(f"R² Score: {r2}")
```

### 19.8 交叉验证

```python
from sklearn.model_selection import cross_val_score, cross_val_predict

# K折交叉验证
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')  # 分类
# scores = cross_val_score(model, X, y, cv=5, scoring='r2')  # 回归
print(f"Cross-validation scores: {scores}")
print(f"Mean score: {scores.mean()}")

# 交叉验证预测
y_pred_cv = cross_val_predict(model, X, y, cv=5)
```

### 19.9 超参数调优

#### 19.9.1 网格搜索

```python
from sklearn.model_selection import GridSearchCV

# 定义参数网格
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [3, 5, 7, None],
    'min_samples_split': [2, 5, 10]
}

# 网格搜索
grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1  # 使用所有CPU核心
)

grid_search.fit(X_train, y_train)

# 最佳参数和分数
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_}")

# 使用最佳模型
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
```

#### 19.9.2 随机搜索

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

# 定义参数分布
param_dist = {
    'n_estimators': randint(100, 500),
    'max_depth': [3, 5, 7, None],
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 10)
}

# 随机搜索
random_search = RandomizedSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_distributions=param_dist,
    n_iter=10,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    random_state=42
)

random_search.fit(X_train, y_train)

# 最佳参数和分数
print(f"Best parameters: {random_search.best_params_}")
print(f"Best score: {random_search.best_score_}")
```

### 19.10 特征重要性

```python
from sklearn.ensemble import RandomForestClassifier

# 训练模型
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 获取特征重要性
feature_importances = model.feature_importances_

# 可视化特征重要性
import matplotlib.pyplot as plt

features = X.columns if hasattr(X, 'columns') else [f'feature_{i}' for i in range(X.shape[1])]
sorted_indices = np.argsort(feature_importances)[::-1]
sorted_features = [features[i] for i in sorted_indices]
sorted_importances = feature_importances[sorted_indices]

plt.figure(figsize=(10, 6))
plt.barh(sorted_features, sorted_importances)
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Feature Importance')
plt.show()
```

### 19.11 模型保存与加载

```python
import joblib

# 保存模型
joblib.dump(model, 'model.pkl')

# 加载模型
loaded_model = joblib.load('model.pkl')

# 使用加载的模型
y_pred = loaded_model.predict(X_test)
```

### 19.12 管道（Pipeline）

管道可以将多个预处理步骤和模型训练步骤组合成一个完整的工作流。

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# 创建管道
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

# 训练管道
pipeline.fit(X_train, y_train)

# 评估管道
accuracy = pipeline.score(X_test, y_test)
print(f"Accuracy: {accuracy}")

# 保存管道
joblib.dump(pipeline, 'pipeline.pkl')
```

### 19.13 示例：完整的机器学习工作流

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# 1. 加载数据
iris = load_iris()
X, y = iris.data, iris.target

# 2. 数据分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 创建管道
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC())
])

# 4. 定义参数网格
param_grid = {
    'svm__C': [0.1, 1, 10, 100],
    'svm__gamma': [0.001, 0.01, 0.1, 1]
}

# 5. 网格搜索
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# 6. 最佳模型
best_model = grid_search.best_estimator_
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best cross-validation score: {grid_search.best_score_}")

# 7. 模型评估
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Test accuracy: {accuracy}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 8. 保存模型
import joblib
joblib.dump(best_model, 'iris_model.pkl')
print("\nModel saved as 'iris_model.pkl'")
```