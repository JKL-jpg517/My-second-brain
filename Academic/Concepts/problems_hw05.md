[problem1](https://cs61a.org/hw/hw04/#:~:text=%E2%9C%82%EF%B8%8F-,Q4%3A%20Balanced,-Implement%20the%20balanced)
```python
def balanced(m):

    if is_planet(m)==True:  # 注意这个刹车条件！ 高度递归！

        return True

    right_end=end(right(m))

    left_end=end(left(m))

    left_t=length(left(m))*total_mass(left(m))

    right_t=length(right(m))*total_mass(right(m))

    return left_t==right_t and balanced(right_end) and balanced(left_end)
'''
    left_t=total_mass(end(left(m)))*length(left(m))
    right_t=total_mass(end(right(m)))*length(right(m))
    if left_t!=right_t:

        return False

    else:

        if is_planet(end(left(m)))==True:

            left_balanced=True

        else:

            left_balanced=balanced(end(left(m)))

        if is_planet(end(right(m)))==True:

            right_balanced=True

        else:

            right_balanced=balanced(end(right(m)))

        if right_balanced and left_balanced:

            return True

        else:

            return False
'''
```

[problem2](https://cs61a.org/hw/hw04/#:~:text=Trees-,Q5%3A%20Pruning%20Leaves,-Implement%20prune_leaves%2C%20which)
```python
def prune_leaves(t, vals):

    if is_leaf(t):    #依旧是难想的初始条件！

        if label(t) in vals:

            return None

        else:

            return t

    kept_branches=[]

    for b in branches(t):    # 高度难想象！！！细品！

        pruned_b=prune_leaves(b,vals)

        if pruned_b is not None:

            kept_branches.append(pruned_b)

    return tree(label(t),kept_branches)
```