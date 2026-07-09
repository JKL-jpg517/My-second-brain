这些函数大多属于 Python 中对**可迭代对象（iterable）**进行处理的工具，经常和 iterator（迭代器）、generator（生成器）、lambda 表达式一起使用。

先理解一个概念：

```python
nums = [1, 2, 3, 4, 5]
```

`nums` 是一个 iterable。

---

# 1. map()

对序列中的每个元素执行同一个函数。

## 语法

```python
map(function, iterable)
```

## 例子

全部平方：

```python
nums = [1, 2, 3, 4]

result = map(lambda x: x**2, nums)

print(list(result))
```

输出：

```python
[1, 4, 9, 16]
```

等价于：

```python
[x**2 for x in nums]
```

---

## 多个 iterable

```python
a = [1,2,3]
b = [4,5,6]

result = map(lambda x,y: x+y, a, b)

print(list(result))
```

输出：

```python
[5,7,9]
```

---

# 2. filter()

筛选满足条件的元素。

## 语法

```python
filter(function, iterable)
```

函数返回 True 保留。

返回 False 删除。

---

## 例子

保留偶数：

```python
nums = [1,2,3,4,5,6]

result = filter(lambda x: x % 2 == 0, nums)

print(list(result))
```

输出：

```python
[2,4,6]
```

---

等价于：

```python
[x for x in nums if x % 2 == 0]
```

---

# 3. list()

把 iterable 转成列表。

很多 iterator 看不到内容：

```python
result = map(lambda x: x+1, [1,2,3])

print(result)
```

输出：

```python
<map object at ...>
```

因为 map 返回的是迭代器。

需要：

```python
list(result)
```

得到：

```python
[2,3,4]
```

---

# 4. any()

只要有一个 True 就返回 True。

## 例子

```python
nums = [False, False, True]

print(any(nums))
```

输出：

```python
True
```

---

### 实际应用

判断是否存在偶数：

```python
nums = [1,3,5,8]

print(any(x % 2 == 0 for x in nums))
```

输出：

```python
True
```

因为 8 是偶数。

---

# 5. all()

全部为 True 才返回 True。

```python
nums = [True, True, True]

print(all(nums))
```

输出：

```python
True
```

---

### 实际应用

判断是否全为正数：

```python
nums = [1,2,3,4]

print(all(x > 0 for x in nums))
```

输出：

```python
True
```

---

如果：

```python
nums = [1,2,-3,4]
```

输出：

```python
False
```

---

# 6. sum()

求和。

```python
nums = [1,2,3,4]

print(sum(nums))
```

输出：

```python
10
```

---

和 generator 配合：

```python
sum(x*x for x in range(5))
```

结果：

```python
30
```

因为：

```python
0+1+4+9+16
```

---

# 7. max() 和 min()

```python
nums = [3,7,1,9]

print(max(nums))
```

输出：

```python
9
```

```python
print(min(nums))
```

输出：

```python
1
```

---

可以指定比较规则：

```python
words = ["apple", "banana", "cat"]

print(max(words, key=len))
```

输出：

```python
banana
```

---

# 8. sorted()

排序。

```python
nums = [5,2,7,1]

print(sorted(nums))
```

输出：

```python
[1,2,5,7]
```

---

按长度排序：

```python
words = ["apple", "cat", "banana"]

print(sorted(words, key=len))
```

输出：

```python
['cat', 'apple', 'banana']
```

---

# 9. zip()

把多个 iterable 打包。

```python
names = ["Tom", "Alice", "Bob"]
scores = [90, 85, 100]

result = zip(names, scores)

print(list(result))
```

输出：

```python
[
 ('Tom',90),
 ('Alice',85),
 ('Bob',100)
]
```

---

常见遍历：

```python
for name, score in zip(names, scores):
    print(name, score)
```

---

# 10. enumerate()

同时获得下标和元素。

```python
fruits = ["apple","banana","orange"]

for i, fruit in enumerate(fruits):
    print(i, fruit)
```

输出：

```python
0 apple
1 banana
2 orange
```

---

# 11. reduce()

来自：

```python
from functools import reduce
```

把整个序列压缩成一个值。

---

求和：

```python
from functools import reduce

nums = [1,2,3,4]

result = reduce(
    lambda x,y: x+y,
    nums
)

print(result)
```

过程：

```python
((1+2)+3)+4
```

结果：

```python
10
```

---

求乘积：

```python
reduce(lambda x,y:x*y,[1,2,3,4])
```

结果：

```python
24
```

---

# 这些函数与 Iterator 的关系

重点：

```python
map()
filter()
zip()
```

返回的都不是列表，而是 **iterator**。

例如：

```python
m = map(lambda x:x+1,[1,2,3])

print(next(m))
```

输出：

```python
2
```

再：

```python
print(next(m))
```

输出：

```python
3
```

再：

```python
print(next(m))
```

输出：

```python
4
```

继续：

```python
next(m)
```

会抛出：

```python
StopIteration
```

因为迭代器已经耗尽。

---

## 现代 Python 最常见写法

很多老教材会大量使用：

```python
map(...)
filter(...)
reduce(...)
```

但现在更推荐：

```python
# map
[x*x for x in nums]

# filter
[x for x in nums if x%2==0]

# reduce(sum)
sum(nums)
```

原因是：

- 可读性更好
    
- 调试更方便
    
- Pythonic
    

不过：

```python
any(...)
all(...)
zip(...)
enumerate(...)
```

至今仍然是日常开发中的高频工具，尤其是 `zip` 和 `enumerate`，几乎每天都会见到。