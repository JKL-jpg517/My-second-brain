---
tags:
  - "#coding/CS61A"
---

# L5d Tree Recursion

## Definition

A function calls itself **more than once** per invocation — the call graph branches like a tree.

Computational cost grows **exponentially** with input size.

## Example 1: Fibonacci

```python
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)
```

One call spawns two sub-calls, each spawns two more... forming a binary tree.

## Example 2: Counting Partitions

How many ways to write $n$ as a sum of positive integers $\leq m$?

```python
def count_partitions(n, m):
    if n == 0:
        return 1       # one way: the empty partition
    elif n < 0:
        return 0       # invalid
    elif m == 0:
        return 0       # no parts available
    else:
        return count_partitions(n - m, m) + count_partitions(n, m - 1)
```

The key insight — split into two **mutually exclusive, collectively exhaustive** groups:

- **Use at least one $m$:** `count_partitions(n-m, m)` — consume one $m$, remaining sum is $n-m$
- **Use no $m$ at all:** `count_partitions(n, m-1)` — only parts $\leq m-1$

## The Core Mindset

Don't think about *how* sub-problems are solved — just ask:

> How do I decompose the current problem into two non-overlapping, complete sub-problems?

This is exactly case analysis in mathematical proofs.

---

← [[L5c Recursion in Body vs Return Value|L5c Body vs Return Value Recursion]]
← [[UCB CS61A|CS61A MOC]]
