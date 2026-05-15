命令行环境
>[!note]- 前言
>As we covered in the previous lecture, most shells are not a mere launcher to start up other programs, but in practice they provide an entire programming language full of common patterns and abstractions. However, unlike the majority of programming languages, in shell scripting everything is designed around running programs and getting them to communicate with each other simply and efficiently.
>
>
>Shell scripting is tightly bound by _conventions_. For a command line interface (CLI) program to play nicely within the broader shell environment there are some common patterns that it needs to follow. We will now cover many of the concepts required to understand how command line programs work as well as ubiquitous conventions on how to use and configure them.
>==L1: Some basic commands;L2: See how it operates as a whole!==
>

communicte between different program

- Arguements: plain strings in shell, and it is ==up to the program how to interpret them==
     1. e.g:`ls -l folder/`, we are executing the program `/bin/ls` with arguments `['-l', 'folder/']`
     2. consist of a mixture of _flags_ and regular strings;Flag: are preceded by a dash (`-`) or double-dash (`--`); optional  rule:modify program behavior
     3. `ls -a`=`la --all`;   can group: `ls -l -a` and `ls -la` are also equivalent ;  results may be the same:  `ls -la` and `ls -al` produce the same result
     4. e.g: `ls -h`/ `cat -h`: `-h`: a flag that detimine the fution of the programme: show the instructions!
     5.  same type variables are accepted
     ==6. Globbing


* Streams: running programmes in parealle but the output and input are connected
    -  demonstration of parallel:
    -  Two types of output one types of input; output: stdout (when programme ran normally, down to labeld stdin) and stderr (when programme go wrong, will not be parsed by the next command, but can be directed to a file)
		```bash
		$ ls /nonexistent
		ls: cannot access '/nonexistent': No such file or directory
		$ ls /nonexistent | grep "pattern"
		ls: cannot access '/nonexistent': No such file or directory
		# The error message still appears because stderr is not piped
		$ ls /nonexistent 2>/dev/null
		# No output - stderr was redirected to /dev/null
		```

    -  unification of pipe input and command: some programms only accept arguements while others can also accept stdin
> 	[!explanation]-
> 	### 1. “天生合群”型（两者都支持）
> 	这类程序通常是**数据处理工具**。它们遵循 Unix 哲学：既能处理硬盘上的文件（通过参数），也能处理来自管道的数据（通过 stdin）。
> 	
> 	* **代表工具**：`grep`, `cat`, `sort`, `wc`, `sed`, `awk`。
> 	* **用法示例**：
> 	    * **参数模式**：`grep "error" log.txt`（直接从文件读）。
> 	    * **Stdin 模式**：`ls | grep "py"`（从管道读）。
> 	
> 	---
> 	
> 	### 2. “高冷”型（主要只接受参数）
> 	这类程序通常是**系统操作工具**。它们执行的是“动作”（如删除、移动、创建），而不是“处理文字”。它们默认不看 stdin。
> 	
> 	* **代表工具**：`rm`, `cp`, `mv`, `mkdir`, `touch`, `chmod`。
> 	* **痛点**：你不能直接 `ls | rm`。
> 	* **解决方案**：必须使用 `$( )` 将输入转为参数，或者请 `xargs` 出来当翻译官。
> 	
> 	---
> 	
> 	### 3. “只说不听”型（主要是产生输出）
> 	这类程序通常处于管道的最左端。它们负责产生数据供别人使用，但自己不怎么接受数据输入。
> 	
> 	* **代表工具**：`ls`, `pwd`, `whoami`, `date`。
> 	* **特点**：它们通常只接受“配置类”的参数（比如 `ls -l`），但不处理别人传给它的数据流。
> 	
> 	---
> 	
> 	### 如何判断一个程序是否接受 Stdin？
> 	
> 	1. **看 Manual (man)**：
> 	   如果在说明文档里看到 `[FILE]...` 且后面写着 *"With no FILE, or when FILE is -, read standard input"*, 那它就支持 stdin。
> 	2. **盲测**：
> 	   直接在终端输入命令（不加任何参数）然后按回车。
> 	   * 如果程序立即结束或报错（如 `rm`），说明它不支持 stdin。
> 	   * 如果程序卡在那里不动，说明它正在等待你从键盘输入数据（stdin），你可以试着打几个字，最后按 `Ctrl+D` 结束输入。
> 	1. **万能翻译官 xargs**：
> 	   如果你想让一个原本不支持 stdin 的程序支持它，就在前面加 `xargs`。

    
    - 

	    
    
    
	    


```bash
echo "hello" | grep "hello"
echo "hello" | grep "hello" - #labeled stdin goes in from -
grep "hello" numbers.txt#unifiy with line 2! 
```

4. redirect data to files/from files(先前：programme to programme)
5. 
	```bash
# Redirect stdout to a file (overwrite)
echo "hello" > output.txt
# Redirect stdout to a file (append)
echo "world" >> output.txt
# Redirect stderr to a file
ls foobar 2> errors.txt
# Redirect both stdout and stderr to the same file
ls foobar &> all_output.txt
# Redirect stdin from a file
grep "pattern" < input.txt
# Discard output by redirecting to /dev/null
cmd > /dev/null 2>&1 # cmd > /dev/null:让 stdout (1) 指向了黑洞(/dev/null:消除一切数据)  接着让sderr(2)指向(1)的位置；
cmd > /dev/null 2>&1  (>: 给正常运行的stdout的出口；2>: 给sderr的出口)
	```

5. `fzf`: an interactive interface to filter and select
```bash
$ ls | fzf
$ cat ~/.bash_history | fzf
```

- Environment variables&Local shell variables
  Local var:
	  *assign*: foo=bar; Shell variables do not have types they are all strings
>[!tips]-
> `foo = bar` is invalid syntax as the shell will parse it as calling the program `foo` with arguments `['=', 'bar']`. In shell scripting the role of the space character is to perform argument splitting


*access*: $foo; can add "" (but not ' 'which is seen as literal strings) since space may easily be seen as seperates!
	    
```bash
files=$(ls) # put the results of programms to a variable
# $(): command subsitution: 先执行括号内的命令，然后将命令输出的结果捕捉并替换到当前的行中。
echo "$files" | grep README
```


 