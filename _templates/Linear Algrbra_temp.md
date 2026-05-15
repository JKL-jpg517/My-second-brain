---
title: "Lec 01: 矩阵乘法与列空间"
date: 2026-04-24  # 你可以手动修改或通过插件自动填充
course: "MIT 18.06 Linear Algebra"
type: "Lecture Notes"

---


### 🧠 Index&Summary
- **A = CR 分解**：矩阵乘法的列观察法。矩阵 $A$ 可以分解为独立列矩阵 $C$ 和行梯阵 $R$。
- **[[列空间 (Column Space)]]**：矩阵 $A$ 所有列的线性组合形成的集合 $C(A)$。
- **线性独立 (Linear Independence)**：列向量之间不包含多余的信息，即没有任何一列可以由其他列线性组合得到。

---

# 🎓 MIT 18.06: Linear Algebra
## Lec 01: 

> **[Quick Access]**
> 📥 **手写笔记原文：** ![[MIT1806_L1_手写.pdf]]
> 🎥 **课程视频：** [Lecture 1 - MIT OCW](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-1-the-geometry-of-linear-equations/)

---

### 📐 深度推导 (Deep Dive)

#### 1. 矩阵乘法的本质：$A = CR$
从**列视角**（Column Perspective）理解矩阵乘法：
$$
A = \begin{bmatrix} | & | \\ c_1 & c_2 \\ | & | \end{bmatrix} \begin{bmatrix} r_1 \\ r_2 \end{bmatrix} = c_1 r_{11} + c_2 r_{21} \dots
$$
- **核心直觉：** $A$ 的每一列都是 $C$ 中各列的线性组合，组合系数记录在 $R$ 中。
- **Key Idea:** $C$ 的列构成了 $A$ 的列空间的“基”（Basis）。

#### 2. 列空间 $C(A)$ 的几何诠释
- **定义：** 方程 $Ax = b$ 中，所有可能产生的 $b$ 构成的集合。
- **维度：** 如果 $A$ 中有 $r$ 个线性独立的列，则 $C(A)$ 是 $\mathbb{R}^m$ 空间中的一个 $r$ 维子空间（过原点的线、面或高维体）。

---

### ✍️ 手写笔记映射 (Handwriting Mapping)
*建议将 iPad 笔记中的精华推导过程截图贴在这里，实现“手写直觉”与“文档检索”的结合。*

| 关键截图 | 对应考点 / 疑问 | 补充说明 |
| :--- | :--- | :--- |
| ![[Pasted Image 1.png]] | 线性组合的系数分布 | 对应 $A=CR$ 中 $R$ 矩阵的构造。 |
| ![[Pasted Image 2.png]] | 3D 空间的平面 | 列空间在三维空间中的几何表示（过原点）。 |

---

### 💡 洞察与 Q&A (Insights)
- **Insight:** 矩阵分解（Factorization）其实就是在给数据“瘦身”，找出最核心的向量。
- **我的困惑：** - [ ] 既然 $A=CR$ 这么直觉，在算法竞赛或工程实践中，为什么计算库（如 NumPy）更多使用 $QR$ 或 $SVD$？
    - *思考：* 可能是因为数值稳定性（Numerical Stability）。

---

### 💻 编程实现 (Computational Link)
*使用 Python 验证矩阵的秩（Rank）和列空间直觉。*

```python
import numpy as np

# 定义矩阵 A
A = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])

# 计算矩阵的秩（线性独立列的数量）
rank = np.linalg.matrix_rank(A)
print(f"Matrix Rank: {rank}")

# 验证：如果秩小于列数，说明存在线性相关的列
if rank < A.shape[1]:
    print("存在线性相关的列，列空间维度小于矩阵列数。")