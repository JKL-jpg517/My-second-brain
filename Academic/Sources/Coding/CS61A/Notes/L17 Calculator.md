### Exceptions
**Raise Statements**
python exceptions are raised with a raise statement
`raise <expression>` 常放if结构中 标明符合语法的特殊情况 
`<expression>` must evaluate to a subclass of BaseException or an instance of one! the `<expression>` are instances of the classes below:
e.g:
![](../../../../../2026/附件们/7b89292c-0c85-4652-bece-9287c04e3b2b.png)
e.g
```python
def double(x):
	if isinstance(x,str):
		raise TypeError('double takes only numbers')
	return 2*x
```
![](../../../../../2026/附件们/3bc12e75-3d63-4fa9-a73c-796153741363.png)

**Try Statemnets**
handles exceptions: place it in an outer function  which handles the error situation 当有语法错误的时候跳转
```python
try: 
	<try suite>
except <exception class> as name:
	<except suite>
```
rule:
`<try suite>` is executed first
if during `<try suite>` an exception is raised and its the class of the exception inherits from `<exception class>` then:
`<except suite>` is executed! with `<name>` bound to the exception
![](../../../../../2026/附件们/2edfdae5-51a5-4232-b21c-89c82c5eb9ab.png)

### e.g Reduce
 ![](../../../../../2026/附件们/ace4a9b0-4668-4e66-bd47-9f1bb2265974.png)
 ```python
 from operator import add, mul, truediv

def divide_all(n, ds): # it does not have to know how it is calculated  it only handles the error situation
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')

def reduce(f, s, initial):
    for x in s:
        initial = f(initial, x)
    return initial

def reduce(f, s, initial):
    if not s:
        return initial
    else:
        return reduce(f, s[1:], f(initial, s[0])) # 这是截图底部缺失的一行
 ```

### Programming Lanugages
A computer typically executes programs written in many diffferent programming languages
**Machine languages** : statements are interpreted by the hardware itself(difficult to understand by human)
**High-level languages**: statement&expressions are interpreted ==by another program== or complied into another language
- provide means of abstraction such as naming/function defination/objects
- Absract away details to be independent of different hardware and operating system


A powerful form of abstraction can define a new languange to solve a particular type of appication 

![](../../../../../2026/附件们/7cbe0647-db40-4ae7-ae6c-cc6403235aea.png)

### e.g Calculator
a sublanguage of scheme, created by abstractions of python
#### Calculator Syntax
![](../../../../../2026/附件们/177c97a3-3314-4c0a-863d-beb76b4856d2.png)
#### Calculator Semantics
![](../../../../../2026/附件们/602b2478-21ef-4ddd-a724-1d18557a2faf.png)
recursive: 想要算出这个大表达式的最终结果，你必须先用完全相同的规则，去算出它内部嵌套的小表达式的结果/ 不断套对应的python函数抽象
e.g:The process
![](../../../../../2026/附件们/e9a292d0-10d3-4a8c-9274-567848c5606d.png)
[calculator]([Scalc](https://www.composingprograms.com/examples/scalc/scalc.html))
[3.4 Interpreters for Languages with Combination](https://www.composingprograms.com/pages/34-interpreters-for-languages-with-combination.html)