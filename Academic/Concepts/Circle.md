[problem](https://cs61a.org/disc/disc03/#:~:text=with%20your%20TA.-,Q5%3A%20Sevens,-The%20Game%20of)

### 繁琐_code
```python
def sevens(n, k):

    """Return the (clockwise) position of who says n among k players.

  

    >>> sevens(2, 5)

    2

    >>> sevens(6, 5)

    1

    >>> sevens(7, 5)

    2

    >>> sevens(8, 5)

    1

    >>> sevens(9, 5)

    5

    >>> sevens(18, 5)

    2

    """

    def f(i, who, direction):

        if i == n:

            return who

        else:

            if i%7==0 or has_seven(i)==True:

                direction=(-1)*direction

                who=who+direction

                i=i+1

                if who<=0:

                    who=k
                elif who>k:
	                who=1

                return f(i,who,direction)

            else:

                i=i+1

                who=who+direction

                if who>k:

                    who=1
                elif who<=0:
	                who=k
             

                return f(i,who,direction)

  
  

    return f(1, 1, 1)

  

def has_seven(n):

    if n == 0:

        return False

    elif n % 10 == 7:

        return True

    else:

        return has_seven(n // 10)
```


### Simplified_code
solve the problem in blocks
```python
def f(i, who, direction):
            if i == n:
                return who
            
            # 第一步：专心判定逢七。如果是，就掉头；如果不是，什么都不用做
            if i % 7 == 0 or has_seven(i):
                direction = -direction
                
            # 第二步：计算下一个玩家
            next_who = who + direction
            
            # 第三步：统一处理绕圈越界（不管当前是顺时针还是逆时针，全覆盖）
            if next_who < 1:
                next_who = k
            elif next_who > k:
                next_who = 1
                
            # 第四步：数字 +1，带着新状态进入下一轮
            return f(i + 1, next_who, direction)
```