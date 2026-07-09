---
tags:
  - "#coding/CS61A"
---

# L5c Recursion in Body vs. Return Value

Where the recursive call sits determines the behavior. These are fundamentally different:

| Location | Behavior | Key trait |
|----------|----------|-----------|
| **In `return`** | Recursive result is used in a computation | Must wait for sub-call to return |
| **In function body** | Recursive call is a step in execution | Code after the call waits for it to return |

## Example: `cascade`

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
20      ← (C) 3rd call resumes
201     ← (C) 2nd call resumes
2013    ← (C) 1st call resumes
```

**Why this order?** Line (C) cannot execute until `cascade(n // 10)` fully returns. The call stack acts as a natural LIFO structure — the last call in is the first to reach line (C).

## One-Sentence Distinction

- **Return-value recursion**: the *result* propagates upward
- **Body recursion**: the *position* of the call creates a "down" phase and an "up" phase, exploiting the call stack

---

← [[L5b Mutual Recursion|L5b Mutual Recursion]]
→ [[L5d Tree Recursion|L5d Tree Recursion]]
← [[UCB CS61A|CS61A MOC]]
