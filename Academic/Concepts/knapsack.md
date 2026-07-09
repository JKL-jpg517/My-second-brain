[problem](https://cs61a.org/hw/hw03/#:~:text=during%20Office%20Hours.-,Q6%3A%20Knapsack,-You%27re%20a%20thief)
```python
def knapsack(weights,values,c):

    if c==0 or not weights:   #已经取完

        return 0

    elif weights[0]>c: # 没法取

        return knapsack(weights[1:],values[1:],c)  # 数组的迭代

    else:

        take_it=values[0]+knapsack(weights[1:],values[1:],c-weights[0])

        leave_it=knapsack(weights[1:],values,c)

        return max(take_it,leave_it)  # two recursion scenarios（意味着每个都是穷尽到底的方案 代表了多个max! values[0]+max1+max2+... &pick the maximun of them
```