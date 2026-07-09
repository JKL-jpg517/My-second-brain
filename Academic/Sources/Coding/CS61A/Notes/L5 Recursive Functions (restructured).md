---
tags:
  - "#coding/CS61A"
---

# L5 Recursive Functions

> **Core idea:** A function that calls itself — break $f(\text{large})$ into $f(\text{smaller}) + \text{simple work}$. The call stack tracks where you are.

---

## 1. Recursion Basics: Base Case & Recursive Case

Two required pieces:

| Component | Role | Without it |
|-----------|------|------------|
| **Base Case** | Handle the simplest input; stop the recursion | Infinite loop |
| **Recursive Case** | Reduce the problem; call the function itself | Not recursive |

### Sum of Digits

```python
def sum_digits(n):
    if n < 10:
        return n              # base case
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last  # recursive case
```

Breakdown: summing digits of 738 = summing digits of 73, plus 8.

### Factorial

```python
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
```

The recursive function constructs the result directly from $n$ and the result of the simpler problem `fact(n-1)`.

**Abstraction mindset:** don't think about how `fact(n-1)` works — trust it.

### Recursion = Mathematical Induction

![formula](../../../../../2026/附件们/69da45c4-bab0-4284-b86c-3e71e8ee105d.png)

| Induction | Recursion |
|-----------|-----------|
| Base case: prove $n=1$ | Base case |
| Inductive step: assume $n-1$ holds, prove $n$ | Recursive case: trust `f(n-1)`, handle $n$ |
| All cases follow from the base | All calls resolve from the base case upward |

![correction](../../../../../2026/附件们/8b136dd3-2313-477f-addb-48f6e13025c6.png)

> **My words:** Writing recursion is just writing an inductive proof in code. The base case is the base case. The recursive call is the inductive hypothesis. If you can prove it by induction, you can write it recursively.

---

## 2. Mutual Recursion

A recursive procedure split across two functions that call each other.

### Even / Odd

```python
def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n - 1)
```

- 0 is even
- A number is even iff it's one more than an odd number
- A number is odd iff it's one more than an even number

### Pebble Game

$n$ pebbles. Two players take turns removing 1 or 2. Remove the last pebble → win.

- Alice always removes 1
- Bob removes 2 if even number of pebbles remain, otherwise 1

![pebble game](../../../../../2026/附件们/d14a515b-b036-4c46-b91a-cc42b8779c90.png)

```python
def play_alice(n):
    if n == 0:
        return "Bob wins!"
    else:
        return play_bob(n - 1)

def play_bob(n):
    if n == 0:
        return "Alice wins!"
    elif n % 2 == 0:
        return play_alice(n - 2)
    else:
        return play_alice(n - 1)
```

> **My words:** Mutual recursion useful when the problem naturally alternates between two states. Each function models one state. Simpler than a single function with a state variable and branching.

---

## 3. Recursion in Body vs. Return Value

**These are fundamentally different.**

| Location | Behavior | Key trait |
|----------|----------|-----------|
| In `return` | Recursive result used in computation | Wait for sub-call to return |
| In function body | Recursive call is a step; code after it waits | Exploits call stack LIFO |

### Cascade: Body Recursion

```python
def cascade(n):
    if n < 10:
        print(n)          # (A) base case
    else:
        print(n)          # (B) on the way "down"
        cascade(n // 10)
        print(n)          # (C) on the way "up"
```

`cascade(2013)` prints:

```
2013    ← (B) 1st call
201     ← (B) 2nd call
20      ← (B) 3rd call
2       ← (A) base case
20      ← (C) 3rd call resumes  (must wait for cascade to return)
201     ← (C) 2nd call resumes
2013    ← (C) 1st call resumes
```

Line (C) cannot execute until `cascade(n // 10)` **fully returns**. The call stack naturally creates a down-then-up pattern.

> **My words:** Body recursion is what gives you "print before and after" patterns. The stack remembers where you paused. Return-value recursion can't do this — it only passes results upward.

---

## 4. Tree Recursion

A function calls itself **more than once** per invocation. The call graph branches like a tree. Cost grows **exponentially**.

### Fibonacci

```python
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)
```

One call → two sub-calls → four → eight... **Correct but not fast.** `fib(3)` gets recomputed many times.

### Counting Partitions

How many ways to write $n$ as a sum of positive integers $\leq m$?

```python
def count_partitions(n, m):
    if n == 0:
        return 1       # empty partition
    elif n < 0:
        return 0       # invalid
    elif m == 0:
        return 0       # no parts available
    else:
        return count_partitions(n - m, m) + count_partitions(n, m - 1)
```

The split — **mutually exclusive, collectively exhaustive:**

- **Use at least one $m$:** `count_partitions(n-m, m)` — consume one $m$
- **Use no $m$:** `count_partitions(n, m-1)` — only parts $\leq m-1$

> **My words:** Tree recursion is case analysis in code. You don't think about *how* sub-problems solve — you just ask: "What are the two non-overlapping, complete cases?" The rest is the inductive hypothesis. Later, DP fixes the exponential blowup by caching sub-results.

---

## 5. Y Combinator (Bonus)

What if you can't name the function?

```python
fact = lambda n: 1 if n == 1 else mul(n, fact(sub(n, 1)))
```

Without the name `fact`:

```python
def Y(f):
    return f(lambda: Y(f))

def Y_factorization():
    return Y(lambda h: lambda n: 1 if n == 1 else mul(n, h()(sub(n - 1))))
```

`h()` is the symbol that re-invokes the function. The inner lambda takes no argument because it's just re-triggering — no new parameter added.

---

## Connections

- [[L4 Higher-Order Functions]] — recursion and HOFs are two ways to express iteration; HOFs abstract *how*, recursion abstracts *what*
- [[L14 Decomposition]] — tree recursion is problem decomposition made explicit in code
- [[L13 Efficiency]] — tree recursion is elegant but exponential; memoization/DP (later) fixes it
- [[L3 Control]] — recursion replaces `while` loops entirely; this is the functional programming way
- [[is_prime_recursion version]] — recursive primality check
- [[knapsack]] — another tree recursion classic

← [[UCB CS61A|CS61A MOC]]
