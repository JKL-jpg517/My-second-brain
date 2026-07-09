[problem](https://insideempire.github.io/CS61A-Website-Archive/hw/sol-hw06/index.html#:~:text=Optional%20Questions-,Q5%3A%20Two%20List,-Implement%20a%20function)
```python
  

def two_list(vals, counts):  #关键：指针思维
    l=len(vals)

    c=Link(0)  # `Link.empty` 不能被赋值；需要引入“哑节点”（Dummy Node）

    result=c  # 在建一个指针指向这个对象本身，c 作为尾部指针

    for i in range(l):

        item=vals[i]

        for j in range(counts[i]):

            c.rest=Link(item)

            c=c.rest  #c 作为尾部指针

    return result.rest #扣掉dummy node
```