### Interpreting Scheme
 The Structure of an Interpreter: *Eval-Apply loop*
 ![](../../../../../2026/附件们/b841593d-e005-45ae-9199-4fc0e7794ce0.png)
Eval: responsible for reading and comprehension; 拆解代码; gives the results to `Apply` 
e.g recursive calls: `(+ (* 2 3) 4)`
Apply: responsible for calculation, gives the results back to `Eval` to understand

### Special Forms
**Scheme Evaluation**
The scheme_eval function dispatches on expression form:
- Symbols are bound to values in the current environment( base cases)
- Self-evaluating expressions(我就是我e.g 5) (base cases)
- All other legal expressions are represented as Scheme Lists, called *combinations* (recursive calls)
	e.g: Special forms/Call expressions

### Quotation
 The `quote` special form evaluates to the quoted expression, but it is not evaluated
 `(quote <expression>)`: the `<expression>` itself is the value of the expression
 `'<expression>`: is a shorthand for it!; before going to  `eval`  it goes to the `scheme_read` parser and converts int into `quote`
 
 ### Lambda expressions
 ![](../../../../../2026/附件们/b33a6bfb-e0dc-4882-b284-5a9116fca44d.png)
 **Frames and Environments**
 A frame represents an environment by having a parent frame
 Frames are python instances with methods `lookup` and `define`
 e.g
 ```python
 g=Frame(None)# create global frame
 f1=Frame(g) # g is the parent frame
 g.define('y',3)
 g.define('z',5)
 g.lookup('y') # 3
 f1.define('x',2) # {x:2}-><Global Frame>
 ```
### Define Expressions
![](../../../../../2026/附件们/1b1c139c-e52e-4b0a-a0b9-37f033d156a8.png)
**Applying User-defined Procedures**
![](../../../../../2026/附件们/db8c0317-bed1-4823-a5d7-e5abc9ef3ce5.png)
a new environment is created!

### Dynamic Scope
![](../../../../../2026/附件们/d0d59695-caa7-4883-b48b-6635fc1acaf3.png)
redult: 13

do not mix Lexical Scope with Dynamic Scope!
Most languages are Lexical Scope!