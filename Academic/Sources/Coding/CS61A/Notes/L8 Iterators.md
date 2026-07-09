A sequence  can be represented without each element being stored explicitly in the memory of the computer
enables us to compute elements on demand instead of computing the value altogether in advance

e.g `range` : `r = range(10000, 1000000000), r[200]`: computes only one number instead of all numbers in (10000,1000000)

Computing values on demand, rather than retrieving them from an existing representation, is an example of _lazy_ computation(don,t use comuptation in advance/over-amount)




### Iterators
An object that provides sequential access to values one by one
Iterators are obtained by the `iter` function; contents r obtained by the `next` function!

can only be fomed by `iter`/`yield`!

Objects are _iterable_ (an interface) if they have an __iter__ method that returns an _iterator_.
```python
primes = [2, 3, 5, 7]
type(primes)
iterator = iter(primes)
type(iterator) # <class 'list_iterator'>
next(iterator) #2
next(iterator) #3
next(iterator) #5
next(iterator) #7
next(iterator) # error
refine version
try:
		next(iterator)
	except StopIteration:
		print('No more values')
>>> [x + 1 for x in r_iter]

>>> next(r_iter) # 已经到头了
>>> 
>>>prev=next(t)
>>>for curr in t:yield curr-prev
# 位置已经被推进了一位了！！
```
ach time next is called, that position advances. and never goes back!
- Two separate iterators can track two different positions in the same sequence.
- two names for the same iterator will share a position, because they share the same value(`l1=l2`)
- Calling iter on an iterator will return that iterator

>[!significance]-
>An iterator provides a mechanism for considering each of a series of values in turn, but all of those elements do not need to be stored simultaneously. Instead, when the next element is requested from an iterator, that element may be computed on demand instead of being retrieved from an existing memory source.

Enable to transfer sequences(besides ranges) into lazy computation ones 

### Iterables
Any value that can produce iterators is called an _iterable_ value (e.g: strings, lists dictionaries)
e.g dictionaries:
```python
d = {'one': 1, 'two': 2, 'three': 3}
k = iter(d)
v = iter(d.values())
m=iter(d.items())
n=iter(d.keys())
```
if add/delete a paie of items in dictionary: the `next()` becomes invalid
but: only chaning the key will not!

### Built-in Iterators
take interators as arguements and return iterators! also lazy computation！
e.g `map` function!
```python
>>>def double_and_print(x):
        print('***', x, '=>', 2*x, '***')
        return 2*x
>>>s = range(3, 7)
>>>doubled = map(double_and_print, s)  # double_and_print not yet called
>>>next(doubled)
*** 3 => 6 ***
6
>>>next(doubled)
*** 4 => 8 ***
8
>>> list(doubled)                       # double_and_print called twice more
*** 5 => 10 ***
*** 6 => 12 ***
```

other functions: `filter` `zip` `reversed`

[[functions on iterators]]
### For Statement
```python
 counts = [1, 2, 3]
 for item in counts: # changes the count into an iterable value first
	 print(item)
```



### Generator
A generator function is a fuc that yield values insead of returning them(==**A special function**==)
A normal function only returns once; a generator function can yield multiple times
A generator is an iterator created automatically by calling a generator function(**a special iterator**)
When a generator function is called, it returns a generator that iterates over its yields
(it will not run the code inside until u use the next function!==lazy computation!== not a data volt!)

“懒惰的加工流水线”;生成器**肚子里没有囤积任何现成的数据**;它只记住了“下一个数据该怎么造”的规则和当前的状态
e.g
```python
def evens(start,end):
	even=start+start%2
	while even<end:
		yield even
		even=even+2
>>>t=evens(2,10)
>>>next(t)
2
>>>next(t)
4
```
#### Generators&iterators
A `yield from` statement returns all values from an iterator or an iterable

可想象为一个存起来的库 用list呈现出来 list()
function直接跑完了所有的next!
```python
def factory():
    yield 1
    yield 2
def courier_station():
    yield 'A'
    # 直接建立直通管道（委托）
    yield from factory()# 不用 for i in factory(): yield item 了！！！
    yield 'B'
print(list(courier_station()))  # 输出: ['A', 1, 2, 'B']
```



```python
def a_then_b(a,b):
	for x in a:
		yield x
	for y in b:
		yield y
# or another method
def a_then_b(a,b):
	yield from a # yieldfrom= for+ yield
	yield from b
def countdown(k):
	if k>0:
		yield k
		yield from countdown(k-1)
def prefixes(s):# yield from a function!!!
	if s:
		yield from prefixes(s[:-1])
		yield s
	return None # imporant! will not reach the next level until it is called/reached!
>>>list(prefixes(both))
['b','bo','bot',both']: it yields from the yield value; 
def substrings(s):
	if s:
		yield from prefixes(s)
		yield from substrings(s[1:])
# substrings will not be reached until it prefixes are finished
>>>list(substrings('tops')) # 此题是顺的结构： 先抓yield 的prefixes;接下抓下一个substrings yield出的东西
[t,to,top,tops,o,op,ops,ps,s,'s']
t,to,top,tops:prefix(tops); o,op,ops:prefix(o,op,ops)
,ps,s:prefix(ps)
```


e.g partitions
```python
def partitions(n,m):
	if n>0 and m>0:
		if n==m:
			yield str(m)
		for p in partitions(n-m,m): # 用了这个值 左分支
			yield p+'+'+str(m)
		yield from partitions(n,m-1) # 没用这个值 右分支
```


e.g:
```python
next(filter(lambda n: n > 2026, gen_fib()))#get the smallest fib number bigger than 2026
filter(lambda n: n > 2026, gen_fib()) picks from the iterator
 next(iterator): gets the first one
```

[[functions on iterators]]


==disc05== in linux
[[problem_hw05]]