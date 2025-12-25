# CSS 选择器详细解析

在 `06-real-world-project/__main__.py` 中，使用了多种 CSS 选择器来定位页面元素。以下是每个选择器的详细语法解释：

## 1. 后代选择器 (Descendant Selector)

**代码**: `.product-meta h1` (第 20 行)

* **语法**: `A B` (空格分隔)
* **含义**: 选择所有位于 `A` 元素内部的 `B` 元素（无论嵌套多深）。
* **本例解析**:
  * `.product-meta`: 找到所有 `class` 属性包含 `product-meta` 的元素。
  * `h1`: 在上述元素内部，找到所有的 `<h1>` 标签。
  * **目标**: 获取商品详情页中的商品标题。

## 2. 标签+类选择器 (Tag + Class Selector)

**代码**: `span.product-meta__sku-number` (第 22 行)

* **语法**: `tag.classname` (无空格)
* **含义**: 选择同时满足“是 `tag` 标签”且“`class` 包含 `classname`”的元素。
* **本例解析**:
  * `span`: 必须是 `<span>` 标签。
  * `.product-meta__sku-number`: `class` 属性必须包含 `product-meta__sku-number`。
  * **目标**: 获取商品详情页中的 SKU 编号（例如 "SKU-12345"）。这种写法比单纯写 `.product-meta__sku-number` 更精确，因为它限定了标签类型。

## 3. 子元素选择器 (Child Selector)

**代码**: `.product-item > a` (第 34 行)

* **语法**: `A > B` (大于号分隔)
* **含义**: 选择所有是 `A` 元素**直接子元素**的 `B` 元素（只向下一层）。
* **本例解析**:
  * `.product-item`: 找到商品卡片容器。
  * `> a`: 选中该容器直接包裹的 `<a>` 链接。
  * **区别**: 如果写成 `.product-item a` (后代选择器)，它会选中容器内所有的链接（包括可能存在的“添加到购物车”、“收藏”等其他链接）。使用 `>` 是为了**精准定位**到商品详情的主链接。

## 4. 类选择器 (Class Selector)

**代码**: `.collection-block-item` (第 59 行)

* **语法**: `.classname`
* **含义**: 选择所有 `class` 属性包含 `classname` 的元素。
* **本例解析**:
  * 这是最基础的选择器。
  * **目标**: 在首页找到所有代表“品类集合”的区块。因为 `enqueue_links` 会自动从这些区块中提取 `href` 属性，所以这里只需要定位到包含链接的容器（或链接本身）即可。

## 5. 另一个标签+类选择器

**代码**: `a.pagination__next` (第 45 行)

* **语法**: `tag.classname`
* **本例解析**:
  * `a`: 必须是 `<a>` 标签（超链接）。
  * `.pagination__next`: `class` 包含 `pagination__next`。
  * **目标**: 找到列表页底部的“下一页”按钮。限定 `a` 标签是为了确保我们找到的是可以点击跳转的链接，而不是某个样式相同的 `div` 或 `span`。

---

### 总结对照表

| 语法 | 示例 | 名称 | 作用 |
| :--- | :--- | :--- | :--- |
| `.class` | `.collection-block-item` | 类选择器 | 选中指定类的所有元素 |
| `tag.class` | `a.pagination__next` | 标签指定类 | 选中指定类的特定标签 |
| `A B` | `.product-meta h1` | 后代选择器 | 选中 A 内部的所有 B (不管多深) |
| `A > B` | `.product-item > a` | 子元素选择器 | **仅**选中 A 的直接子元素 B |
