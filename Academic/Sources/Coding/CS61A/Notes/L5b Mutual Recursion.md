---
tags:
  - "#coding/CS61A"
---

# L5b Mutual Recursion

## Definition

A recursive procedure split across two functions that call each other.

## Example 1: Even / Odd

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

Logic:
- 0 is even
- A number is even iff it's one more than an odd number
- A number is odd iff it's one more than an even number

## Example 2: Pebble Game

$n$ pebbles on a table. Two players take turns removing 1 or 2 pebbles. The player who takes the last pebble wins.

```python
def play_alice(n):
    if n == 0:
        return "Bob wins!"
    else:
        return play_bob(n - 1)   # Alice always removes 1

def play_bob(n):
    if n == 0:
        return "Alice wins!"
    elif n % 2 == 0:
        return play_alice(n - 2)  # even → remove 2
    else:
        return play_alice(n - 1)  # odd → remove 1
```

## Why Use Mutual Recursion?

Splits a single complex function with many branches into multiple functions, each responsible for one "state" or "perspective." Cleaner logic.

---

← [[L5a Recursion Basics|L5a Recursion Basics]]
→ [[L5c Recursion in Body vs Return Value|L5c Body vs Return Value Recursion]]
← [[UCB CS61A|CS61A MOC]]
