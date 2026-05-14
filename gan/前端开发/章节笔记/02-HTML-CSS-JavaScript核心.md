---
title: HTML CSS JavaScript核心
tags: [前端, HTML, CSS, JavaScript, 基础]
category: 前端开发
---

## 2. HTML / CSS / JavaScript 核心三件套

### 2.1 HTML 结构与语义化

#### HTML 文档基本结构

```html
<!DOCTYPE html>           <!-- 告诉浏览器这是HTML5文档 -->
<html lang="zh-CN">      <!-- 根元素，lang属性指定语言 -->
  <head>
    <!-- 头部：不显示在页面上，但对浏览器和搜索引擎很重要 -->
    <meta charset="UTF-8">                    <!-- 字符编码 -->
    <meta name="viewport"                     <!-- 移动端适配关键！ -->
          content="width=device-width, initial-scale=1.0">
    <meta name="description" content="页面描述">  <!-- SEO -->
    <title>页面标题</title>                   <!-- 标签页标题 -->
    <link rel="stylesheet" href="style.css">  <!-- 引入CSS -->
  </head>
  <body>
    <!-- 页面内容 -->
    <script src="app.js"></script>  <!-- JS放在body底部，防止阻塞渲染 -->
  </body>
</html>
```

#### 语义化标签（Semantic HTML）

**为什么要语义化？**
1. 对搜索引擎友好（SEO），爬虫能理解内容结构
2. 对残障用户友好（屏幕阅读器依赖语义）
3. 代码可读性强，团队协作更容易

```
[非语义化 vs 语义化对比]

❌ 非语义化（全用div，无意义）
<div class="header">
  <div class="nav">
    <div class="nav-item">首页</div>
  </div>
</div>
<div class="main">
  <div class="article">文章内容</div>
  <div class="sidebar">侧边栏</div>
</div>
<div class="footer">版权信息</div>

✅ 语义化（标签即意义）
<header>
  <nav>
    <a href="/">首页</a>
  </nav>
</header>
<main>
  <article>文章内容</article>
  <aside>侧边栏</aside>
</main>
<footer>版权信息</footer>
```

**常用语义化标签速查：**

| 标签 | 语义 | 用途 |
|-----|------|-----|
| `<header>` | 页头 | 网站Logo、导航 |
| `<nav>` | 导航 | 菜单链接 |
| `<main>` | 主内容 | 页面核心内容（每页只用一次） |
| `<article>` | 文章 | 独立完整的内容（博客文章） |
| `<section>` | 章节 | 内容分区 |
| `<aside>` | 旁白 | 侧边栏、广告 |
| `<footer>` | 页脚 | 版权、联系方式 |
| `<figure>` | 图表 | 图片、图表及说明 |
| `<time>` | 时间 | 日期时间（有datetime属性） |
| `<address>` | 地址 | 联系信息 |

#### HTML 元素类型

```
[元素分类]

块级元素（Block）          行内元素（Inline）
独占一行，可设宽高          不独占一行，宽高由内容决定

<div>   <p>              <span>  <a>
<h1~h6> <ul/ol>          <strong> <em>
<table> <form>           <img>   <input>
<header> <section>       <button> <label>
```

> **实际开发中的坑**：`<img>` 是行内元素，底部默认有 4px 空白（基线对齐问题）。解决方法：`img { display: block; }` 或 `img { vertical-align: bottom; }`

---

### 2.2 CSS 布局（Flex / Grid / 响应式）

#### 盒子模型（Box Model）

**类比**：每个 HTML 元素就像一个礼品盒。内容是礼物本身，padding 是内部填充物，border 是盒子壁，margin 是盒子之间的距离。

```
[CSS 盒子模型]

┌──────────────────────────────────────┐
│              margin（外边距）         │
│  ┌────────────────────────────────┐  │
│  │          border（边框）         │  │
│  │  ┌──────────────────────────┐  │  │
│  │  │       padding（内边距）   │  │  │
│  │  │  ┌────────────────────┐  │  │  │
│  │  │  │   content（内容）   │  │  │  │
│  │  │  │   width × height   │  │  │  │
│  │  │  └────────────────────┘  │  │  │
│  │  └──────────────────────────┘  │  │
│  └────────────────────────────────┘  │
└──────────────────────────────────────┘

⚠️ 重要：box-sizing 属性
- content-box（默认）：width = 内容宽度（不含padding、border）
- border-box（推荐）：width = 内容 + padding + border
  → 所有项目建议设置：* { box-sizing: border-box; }
```

#### Flexbox 布局（一维布局）

**类比**：Flex 像一排可伸缩的弹簧座位，座位可以自动调整大小来填满空间。

```
[Flexbox 核心概念]

容器（container）设置 display: flex
  │
  ├── 主轴方向（flex-direction）
  │     row（←→ 水平，默认）
  │     column（↑↓ 垂直）
  │
  ├── 主轴对齐（justify-content）
  │     flex-start  | ● ● ● |
  │     flex-end    |       ● ● ●|
  │     center      |   ● ● ●   |
  │     space-between| ●   ●   ● |
  │     space-around| ○●○ ○●○ ○●○|
  │     space-evenly| ○ ● ○ ● ○ ● ○|
  │
  └── 交叉轴对齐（align-items）
        stretch（默认，撑满容器高度）
        center（垂直居中）
        flex-start / flex-end
```

**常用 Flex 布局示例：**

```css
/* 水平垂直居中（面试高频题） */
.container {
  display: flex;
  justify-content: center;  /* 水平居中 */
  align-items: center;      /* 垂直居中 */
}

/* 导航栏：左侧Logo，右侧菜单 */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* 弹性子元素 */
.flex-item {
  flex: 1;          /* 等分剩余空间 */
  flex-grow: 1;     /* 放大比例 */
  flex-shrink: 0;   /* 不缩小 */
  flex-basis: 200px; /* 初始大小 */
}
```

#### CSS Grid 布局（二维布局）

**类比**：Grid 像一个 Excel 表格，可以精确控制行和列。

```
[Grid 布局示意]

grid-template-columns: 1fr 2fr 1fr
grid-template-rows: 100px auto 60px

┌──────────┬────────────────────┬──────────┐
│  1fr     │       2fr          │   1fr    │ ← 100px
├──────────┼────────────────────┼──────────┤
│          │                    │          │ ← auto
│  left    │      main          │  right   │
│          │                    │          │
├──────────┴────────────────────┴──────────┤
│              footer                      │ ← 60px
└──────────────────────────────────────────┘
```

```css
/* 典型页面布局 */
.layout {
  display: grid;
  grid-template-areas:
    "header header header"
    "sidebar main aside"
    "footer footer footer";
  grid-template-columns: 200px 1fr 200px;
  grid-template-rows: 60px 1fr 60px;
  min-height: 100vh;
}

.header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main    { grid-area: main; }
.aside   { grid-area: aside; }
.footer  { grid-area: footer; }
```

#### 响应式设计

**核心思想**：同一套代码，在手机、平板、桌面上都能好看地显示。

```
[响应式断点设计]

320px ─── 480px ─── 768px ─── 1024px ─── 1440px
  │           │          │           │         │
手机竖屏    手机横屏    平板       桌面      大屏
```

```css
/* 移动优先（Mobile First）策略（推荐） */

/* 基础样式：手机 */
.container {
  width: 100%;
  padding: 0 16px;
}

/* 平板：768px以上 */
@media (min-width: 768px) {
  .container {
    max-width: 720px;
    margin: 0 auto;
  }
}

/* 桌面：1024px以上 */
@media (min-width: 1024px) {
  .container {
    max-width: 960px;
  }
}

/* 大屏：1440px以上 */
@media (min-width: 1440px) {
  .container {
    max-width: 1200px;
  }
}
```

> **最佳实践**：始终采用 Mobile First（移动端优先）策略。原因：移动端用户占全球 60%+ ；且移动端限制更多，优先考虑限制反而能做出更简洁的设计。

---

### 2.3 JavaScript 核心概念

#### 变量与作用域

```javascript
// 三种声明方式
var x = 1;   // 函数作用域，存在变量提升（不推荐）
let y = 2;   // 块级作用域（推荐）
const z = 3; // 块级作用域，不可重赋值（优先使用）

// 作用域链示意
function outer() {
  const outerVar = 'outer';
  
  function inner() {
    const innerVar = 'inner';
    console.log(outerVar); // ✅ 可以访问外层变量
    console.log(innerVar); // ✅ 可以访问自身变量
  }
  
  console.log(innerVar); // ❌ 不能访问内层变量
}
```

```
[作用域链示意图]

全局作用域（Global Scope）
  └── window.x = 1
  
  函数作用域（outer）
    └── outerVar = 'outer'
    
    函数作用域（inner）
      └── innerVar = 'inner'
      
查找变量时：inner → outer → global（向上查找，不能向下）
```

#### 闭包（Closure）

**类比**：闭包就像一个"带记忆的函数"。函数执行完了，但它记住了自己诞生时的环境。

```javascript
// 经典闭包示例：计数器
function createCounter() {
  let count = 0;  // 这个变量被"封闭"在闭包中
  
  return {
    increment: () => ++count,
    decrement: () => --count,
    getCount: () => count
  };
}

const counter = createCounter();
counter.increment(); // 1
counter.increment(); // 2
counter.decrement(); // 1
counter.getCount();  // 1

// count 变量外部无法直接访问，实现了"私有变量"
```

**闭包的实际应用场景：**

```javascript
// 1. 函数工厂（生产不同配置的函数）
function multiplyBy(n) {
  return (x) => x * n;  // n 被闭包捕获
}
const double = multiplyBy(2);
const triple = multiplyBy(3);
double(5); // 10
triple(5); // 15

// 2. 防抖（Debounce）- 防止频繁触发
function debounce(fn, delay) {
  let timer;
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

// 3. 模块化（在ES6之前）
const myModule = (function() {
  const private = 'private data';
  
  return {
    getPrivate: () => private  // 外部只能通过这个方法访问
  };
})();
```

> **实际开发中的坑**：闭包会导致内存泄漏！如果闭包引用了大对象且长期不释放，内存会一直被占用。解决方案：不用时将引用变量设为 null。

#### 原型与原型链

**类比**：原型就像"遗传基因"。孩子（对象）会继承父母（原型）的特征（方法）。

```
[原型链示意图]

let arr = [1, 2, 3]

arr 对象
  │
  │ __proto__（原型指针）
  ▼
Array.prototype
  ├── push()
  ├── pop()
  ├── map()
  └── filter()
  │
  │ __proto__
  ▼
Object.prototype
  ├── toString()
  ├── hasOwnProperty()
  └── valueOf()
  │
  │ __proto__
  ▼
  null（原型链终点）
```

```javascript
// 原型继承实现
function Animal(name) {
  this.name = name;
}
Animal.prototype.speak = function() {
  return `${this.name} makes a sound`;
};

function Dog(name, breed) {
  Animal.call(this, name);  // 调用父类构造函数
  this.breed = breed;
}
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;
Dog.prototype.bark = function() {
  return `${this.name} barks!`;
};

// 现代写法：ES6 Class（本质还是原型）
class Animal {
  constructor(name) {
    this.name = name;
  }
  speak() {
    return `${this.name} makes a sound`;
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name);           // 调用父类构造函数
    this.breed = breed;
  }
  bark() {
    return `${this.name} barks!`;
  }
}
```

#### 异步编程（非常重要！）

**类比**：同步就像去餐厅点餐，站在柜台等厨师做好；异步就像下单后拿号，去找位置坐，等叫号再去取餐。

```
[同步 vs 异步]

同步（阻塞）:
任务1 ── 任务2 ── 任务3 ──► 时间
(任务1完成才能开始任务2)

异步（非阻塞）:
任务1 ──────────────────► 完成回调
任务2 ─────────► 完成回调
任务3 ──► 完成回调
         ↑
       不等待，并行执行
```

**异步的三个时代：**

```javascript
// === 时代1: 回调函数（Callback）===
// 问题：回调地狱，代码难以维护
fs.readFile('a.txt', (err, dataA) => {
  fs.readFile('b.txt', (err, dataB) => {
    fs.readFile('c.txt', (err, dataC) => {
      // 横向增长，难以阅读
    });
  });
});

// === 时代2: Promise ===
// 优点：链式调用，避免嵌套
fetch('/api/user')
  .then(res => res.json())
  .then(user => fetch(`/api/posts/${user.id}`))
  .then(res => res.json())
  .then(posts => console.log(posts))
  .catch(err => console.error(err));  // 统一错误处理

// === 时代3: async/await（推荐）===
// 优点：像写同步代码一样写异步，可读性极强
async function getUserPosts(userId) {
  try {
    const userRes = await fetch(`/api/user/${userId}`);
    const user = await userRes.json();
    
    const postsRes = await fetch(`/api/posts/${user.id}`);
    const posts = await postsRes.json();
    
    return posts;
  } catch (error) {
    console.error('获取数据失败:', error);
    throw error;
  }
}

// 并行请求（不要串行等待可以并行的请求）
async function getMultipleData() {
  // ❌ 错误写法：串行，浪费时间
  const user = await fetchUser();
  const config = await fetchConfig();  // 等user完成才开始
  
  // ✅ 正确写法：并行，节省时间
  const [user, config] = await Promise.all([
    fetchUser(),
    fetchConfig()
  ]);
}
```

> **实际开发中的坑**：`await` 只能在 `async` 函数内使用。忘记 `await` 会拿到 Promise 对象而不是值，这是非常常见的Bug！

---

### 2.4 第二章总结

```
[HTML/CSS/JS 核心知识导图]

核心三件套
├── HTML
│   ├── 文档结构（DOCTYPE/head/body）
│   ├── 语义化标签（header/main/article）
│   └── 块级 vs 行内元素
│
├── CSS
│   ├── 盒子模型（content/padding/border/margin）
│   ├── Flexbox（一维，主轴+交叉轴）
│   ├── Grid（二维，行+列）
│   └── 响应式（@media，移动优先）
│
└── JavaScript
    ├── 作用域与作用域链
    ├── 闭包（带记忆的函数）
    ├── 原型链（遗传基因）
    └── 异步（回调→Promise→async/await）
```

---
