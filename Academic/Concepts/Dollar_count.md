[problem](https://cs61a.org/hw/hw03/#:~:text=Tree%20Recursion-,Q4%3A%20Count%20Dollars,-Given%20a%20positive)

```python
def next_smaller_dollar(bill):

    """Returns the next smaller bill in order."""

    if bill == 100:

        return 50

    if bill == 50:

        return 20

    if bill == 20:

        return 10

    elif bill == 10:

        return 5

    elif bill == 5:

        return 1

  

def count_dollars(sum_needed):

    """Return the number of ways to make change.

  

    >>> count_dollars(15)  # 15 $1 bills, 10 $1 & 1 $5 bills, ... 1 $5 & 1 $10 bills

    6

    >>> count_dollars(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills

    4

    >>> count_dollars(20)  # 20 $1 bills, 15 $1 & $5 bills, ... 1 $20 bill

    10

    >>> count_dollars(45)  # How many ways to make change for 45 dollars?

    44

    >>> count_dollars(100) # How many ways to make change for 100 dollars?

    344

    >>> count_dollars(200) # How many ways to make change for 200 dollars?

    3274

    >>> from construct_check import check

    >>> # ban iteration

    >>> check(SOURCE_FILE, 'count_dollars', ['While', 'For'])

    True

    """

    "*** YOUR CODE HERE ***"

    def count(remain,bill):   ### 难点：自己主动定义一个辅助函数！

        if remain==0: # 非remian-bill==0 e.g:对于余下5元 也可以是用5个1元抵掉！！！

            return 1

        elif remain<0 or bill is None:  # bill is none: 一元的终点 代表bill==1的时候 return count(remain-bill,bill)+count(remain,next_smaller_dollar(bill)) 只剩下前一项

            return 0

        else:

            return count(remain-bill,bill)+count(remain,next_smaller_dollar(bill))

    return count(sum_needed,100)
```


**A similar problem***
[problem](https://cs61a.org/lab/lab03/#:~:text=%E2%9C%82%EF%B8%8F-,Q6%3A%20Making%20Onions,-Write%20a%20function)
```python
def make_onion(f, g):


    def can_reach(x, y, limit):

        if limit < 0:

            return False

        elif x == y:

            return True

        else:

            return can_reach(f(x), y, limit - 1) or can_reach(g(x), y, limit - 1)

    return can_reach
```