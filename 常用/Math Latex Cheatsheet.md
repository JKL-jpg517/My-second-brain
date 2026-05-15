---
tags:
  - "#指南/latex"
---



- **行内公式**：使用 `$公式内容$`，公式会嵌入在文字中间。
    
- **块级公式**：使用 `$$公式内容$$`，公式会独占一行并居中。



- ### ==1. 基础运算与符号==

| **描述** | **LaTeX 语法**                   | **渲染效果**                   |
| ------ | ------------------------------ | -------------------------- |
| 上标（幂）  | `$a^{n}$`                      | $a^{n}$                    |
| 下标     | `$a_{i}$`                      | $a_{i}$                    |
| 分式     | `$\frac{分子}{分母}$`              | $\frac{a}{b}$              |
| 根号     | `$\sqrt{x}$` 或 `$\sqrt[n]{x}$` | $\sqrt{x}$ 或 $\sqrt[n]{x}$ |
| 乘号     | `$\times$`                     | $\times$                   |
| 除号     | `$\div$`                       | $\div$                     |
- ### ==2. 希腊字母（理工科高频)==

希腊字母通常只需输入 `\` 后接字母的英文拼写。**首字母大写即为大写形式。**

|**字母**|**语法**|**字母**|**语法**|
|---|---|---|---|
|$\alpha$|`$\alpha$`|$\beta$|`$\beta$`|
|$\gamma$|`$\gamma$`|$\Delta$|`$\Delta$`|
|$\theta$|`$\theta$`|$\pi$|`$\pi$`|
|$\sigma$|`$\sigma$`|$\Omega$|`$\Omega$`|
- ### ==3. 算术运算符（求和、积分、极限）==

这些在 CS 的算法复杂度分析（Big O）和金融模型中非常常用。

- **累加求和**：`$\sum_{i=1}^{n}$` $\rightarrow$ $\sum_{i=1}^{n}$
    
- **累乘**：`$\prod_{i=1}^{n}$` $\rightarrow$ $\prod_{i=1}^{n}$
    
- **积分**：`$\int_{a}^{b} f(x)dx$` $\rightarrow$ $\int_{a}^{b} f(x)dx$
    
- **极限**：`$\lim_{x \to \infty}$` $\rightarrow$ $\lim_{x \to \infty}$
- **微分**： **一阶导数**：`$\frac{dy}{dx}$` $\rightarrow \frac{dy}{dx}$
       **偏导数**:使用 `\partial` 命令，`$\frac{\partial y}{\partial x}$` $\rightarrow \frac{\partial y}{\partial x}$
       **一阶导数**：`$f'(x)$` $\rightarrow f'(x)$
       **二阶导数**：`$f''(x)$` $\rightarrow f''(x)$
       **n阶导数**：`$\frac{d^{n}y}{dx^{n}}$` $\rightarrow \frac{d^{n}y}{dx^{n}}$
             `$f^{(n)}(x)$` $\rightarrow f^{(n)}(x)$
       
- ### ==4. 矩阵与括号（线性代数基础）==

  在线性代数和编码中经常用到矩阵。

  **带中括号的矩阵：**

```
$$
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$
```
    渲染效果：

$$\begin{bmatrix} a & b \\ c & d \end{bmatrix}$$
行内：这是两个列向量：$$ 和 $\begin{bmatrix} d \\ e \\ f \end{bmatrix}$。

### ==5. 逻辑与集合（CS 离散数学必备）==

- **属于/不属于**：`$\in$` , `$\notin$` ($\in, \notin$)
    
- **蕴含/推导**：`$\implies$` ($\implies$)
    
- **且/或**：`$\land$` , `$\lor$` ($\land, \lor$)
    
- **任意/存在**：`$\forall$` , `$\exists$` ($\forall, \exists$)
- **等价于**: '$A \iff B$'



\ldots  省略号！
\cdot: 点乘

|**函数**|**LaTeX 代码**|**效果**|
|---|---|---|
|正弦|`\sin \theta`|$\sin \theta$|
|余弦|`\cos \alpha$|$\cos \alpha$|
|正切|`\tan \phi$|$\tan \phi$|
|余切|`\cot \beta$|$\cot \beta$|
|正割|`\sec x`|$\sec x$|
|余割|`\csc y`|$\csc y$|