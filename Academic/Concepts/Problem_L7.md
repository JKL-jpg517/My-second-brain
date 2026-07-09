[problem1](https://cs61a.org/disc/disc04/#:~:text=Q4%3A%20A%20Perfect,not%20be%20unique.)


```python
def fit(total, n):

    def f(total, n, k):

        if total==0 and n==0:

            return True

        elif total<0 or n==0 or k*k>total:   #注意多重条件！

            return False

        else:

            return f(total-k*k,n-1,k) or f(total,n,k+1)

    return f(total, n, 1)
```

[problem2](https://cs61a.org/disc/disc04/#:~:text=Q3%3A%20Sum%20Fun,3%5D%5D%20start%20with)
```python
  

def sums(n, m):

    if n < 0:

        return []

    if n == 0:

        sums_to_zero = []     # The only way to sum to zero using positives

        return [sums_to_zero] # Return a list of all the ways to sum to zero

    result = []

    for k in range(1, m + 1):

        result = result + [ [k]+rest for rest in sums(n-k,m) if rest == [] or rest[0]!=k ]  # 注意：元素是列表！ rest[0]!=k 保证不相邻

    return result
```

[problem3](https://cs61a.org/disc/disc04/#:~:text=%2C%204%5D-,Q2%3A%20Max%20Product,-Implement%20max_product%2C%20which)
```python
def max_products(s):

    mul=1

    if len(s)==0:

        return 1

    elif len(s)==1:

        return s[0]

    elif len(s)==2:

        return max(s[0],s[1])

    else:

        take_first=s[0]*max_products(s[2:])

        skip_first=max_products(s[1:])

    return max(take_first,skip_first)
```


[Problem](https://cs61a.org/lab/lab04/#:~:text=%E2%9C%82%EF%B8%8F-,Q3%3A%20Buying%20Fruit,-Implement%20the%20buy)
```python
def buy(fruits_to_buy: list[str], prices: dict[str, int], total_amount: int) -> None:

    """Print ways to buy some of each fruit so that the sum of prices is amount.

  

    >>> prices = {'oranges': 4, 'apples': 3, 'bananas': 2, 'kiwis': 9}

    >>> buy(['apples', 'oranges', 'bananas'], prices, 12)  # We can only buy apple, orange, and banana, but not kiwi

    [2 apples][1 orange][1 banana]

    >>> buy(['apples', 'oranges', 'bananas'], prices, 16)

    [2 apples][1 orange][3 bananas]

    [2 apples][2 oranges][1 banana]

    >>> buy(['apples', 'kiwis'], prices, 36)

    [3 apples][3 kiwis]

    [6 apples][2 kiwis]

    [9 apples][1 kiwi]

    """

    def add(fruits: list[str], amount: int, cart: str) -> None:

        if fruits == [] and amount == 0:

            print(cart)

        elif fruits and amount > 0:

            fruit = fruits[0]

            price = prices[fruit]

            for k in range(1,amount//price+1):

                # Hint: The display function will help you add fruit to the cart.

                add(fruits[1:], amount-k*price , cart+display(fruit,k))

    add(fruits_to_buy, total_amount, '')
    
    
    
    or: a better version:
    
    
    def add(fruits, amount, cart):
    # 1. 终点站：无论是否刚好花完，我们都要检查一下
    if not fruits:
        if amount == 0:
            print(cart)
        return # 到了终点，必须停下，不管成没成功 如果fruit没了 但amount!=0 失败 return一个空的值！！

    # 2. 只有当还有水果时，才继续尝试
    fruit = fruits[0]
    price = prices[fruit]
    for k in range(1, (amount // price) + 1):
        add(fruits[1:], amount - k * price, cart + display(fruit, k))

  
  

def display(fruit: str, count: int) -> str:

    """Display a count of a fruit in square brackets.

  

    >>> display('apples', 3)

    '[3 apples]'

    >>> display('apples', 1)

    '[1 apple]'

    >>> print(display('apples', 3) + display('kiwis', 3))

    [3 apples][3 kiwis]

    """

    assert count >= 1 and fruit[-1] == 's'

    if count == 1:

        fruit = fruit[:-1]  # get rid of the plural s

    return '[' + str(count) + ' ' + fruit + ']'    
```
- the result are strings! not lists
- no return value; there are only print that really show what is happening 



[project](https://cs61a.org/proj/cats/#:~:text=Computer%20Aided%20Typing%20Software)
==problem 6==: 将计数器融在return value里面！
```python
def furry_fixes(entered: str, source: str, limit: int) -> int:
    m=limit

    if limit<0:

        return 1

    if len(entered)==0 or len(source)==0:

        return abs(len(entered)-len(source)) 

    if entered[0]!=source[0]:

        return 1+furry_fixes(entered[1:],source[1:],limit-1)  # abs(len(entered)-len(source)) can be returned here!

    else:

        return furry_fixes(entered[1:],source[1:],limit)
```
==problem 7== use of tree recursion!!!
```python

```