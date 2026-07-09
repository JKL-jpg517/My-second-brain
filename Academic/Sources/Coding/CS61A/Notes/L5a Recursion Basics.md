---
tags:
  - "#coding/CS61A"
---

# L5a Recursion Basics: Base Case & Recursive Case

## What Is a Recursive Function?

A function that calls itself — directly or indirectly.

Essence: simplify $f(\text{large})$ into $f(\text{smaller}) + \text{simple work}$.

The call stack keeps track of where we are in the computation.

## Two Required Components

| Component | Role | Without it |
|-----------|------|------------|
| **Base Case** | Defines behavior for the simplest input; terminates recursion | Infinite recursion |
| **Recursive Case** | Reduces the problem; calls the function itself | No recursion |

## Example 1: Sum of Digits

```python
def sum_digits(n):
    if n < 10:
        return n              # base case
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last  # recursive case
```

Breakdown: summing the digits of 738 = summing the digits of 73, plus 8.

## Example 2: Factorial

```python
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
```

## Recursion = Mathematical Induction

| Induction | Recursion |
|-----------|-----------|
| Base case (prove $n=1$) | Base case |
| Inductive step (assume $n-1$ true, prove $n$) | Recursive case: trust `fact(n-1)`, handle $n$ |
| All cases follow from the base | All calls resolve from the base case upward |

When writing recursion, trust the recursive call. Don't unfold it in your head.

---

→ [[L5b Mutual Recursion|L5b Mutual Recursion]]
← [[UCB CS61A|CS61A MOC]]
