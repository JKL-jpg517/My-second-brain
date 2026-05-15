命令行环境
>[!note]- 前言
>As we covered in the previous lecture, most shells are not a mere launcher to start up other programs, but in practice they provide an entire programming language full of common patterns and abstractions. However, unlike the majority of programming languages, in shell scripting everything is designed around running programs and getting them to communicate with each other simply and efficiently.
>
>
>Shell scripting is tightly bound by _conventions_. For a command line interface (CLI) program to play nicely within the broader shell environment there are some common patterns that it needs to follow. We will now cover many of the concepts required to understand how command line programs work as well as ubiquitous conventions on how to use and configure them.
>==L1: Some basic commands;L2: See how it operates as a whole!==
>

### Arguements
plain strings in shell, and it is ==up to the program how to interpret them==
    1. e.g:`ls -l folder/`, we are executing the program `/bin/ls` with arguments `['-l', 'folder/']`
     2. consist of a mixture of _flags_ and regular strings;Flag: are preceded by a dash (`-`) or double-dash (`--`); optional  rule:modify program behavior
     3. `ls -a`=`la --all`;   can group: `ls -l -a` and `ls -la` are also equivalent ;  results may be the same:  `ls -la` and `ls -al` produce the same result
     4. e.g: `ls -h`/ `cat -h`: `-h`: a flag that detimine the fution of the programme: show the instructions!
     5.  same type variables are accepted
     ==6. Globbing


### Streams
running programmes in parealle but the output and input are connected
-  demonstration of parallel:
-  Two types of output one type of input; 
    - output: stdout (when programme ran normally, down to labeld stdin) and stderr (when programme go wrong, will not be parsed by the next command, but can be directed to a file)
    - input:stdin
    ```bash
    $ ls /nonexistent
	ls: cannot access '/nonexistent': No such file or directory
	$ ls /nonexistent | grep "pattern"
	ls: cannot access '/nonexistent': No such file or directory
	# The error message still appears because stderr is not piped
	$ ls /nonexistent 2>/dev/null
	# No output - stderr was redirected to /dev/null
    ```
- unification of pipe input and command: some programms only accept arguements while others can also accept stdin
>[!explanation]-
>### 1. “天生合群”型（两者都支持）
> 这类程序通常是**数据处理工具**。它们遵循 Unix 哲学：既能处理硬盘上的文件（通过参数），也能处理来自管道的数据（通过 stdin）。
> 
> * **代表工具**：`grep`, `cat`, `sort`, `wc`, `sed`, `awk`。
> * **用法示例**：
>     * **参数模式**：`grep "error" log.txt`（直接从文件读）。
>     * **Stdin 模式**：`ls | grep "py"`（从管道读）。
> 
> ---
> 
> ### 2. “高冷”型（主要只接受参数）
> 这类程序通常是**系统操作工具**。它们执行的是“动作”（如删除、移动、创建），而不是“处理文字”。它们默认不看 stdin。
> 
> * **代表工具**：`rm`, `cp`, `mv`, `mkdir`, `touch`, `chmod`。
> * **痛点**：你不能直接 `ls | rm`。
> * **解决方案**：必须使用 `$( )` 将输入转为参数，或者请 `xargs` 出来当翻译官。
> 
> ---
> 
> ### 3. “只说不听”型（主要是产生输出）
> 这类程序通常处于管道的最左端。它们负责产生数据供别人使用，但自己不怎么接受数据输入。
> 
> * **代表工具**：`ls`, `pwd`, `whoami`, `date`。
> * **特点**：它们通常只接受“配置类”的参数（比如 `ls -l`），但不处理别人传给它的数据流。
> 
> ---
> 
> ### 如何判断一个程序是否接受 Stdin？
> 
> 1. **看 Manual (man)**：
>    如果在说明文档里看到 `[FILE]...` 且后面写着 *"With no FILE, or when FILE is -, read standard input"*, 那它就支持 stdin。
> 2. **盲测**：
>    直接在终端输入命令（不加任何参数）然后按回车。
>    * 如果程序立即结束或报错（如 `rm`），说明它不支持 stdin。
>    * 如果程序卡在那里不动，说明它正在等待你从键盘输入数据（stdin），你可以试着打几个字，最后按 `Ctrl+D` 结束输入。
> 3. **万能翻译官 xargs**：
>    如果你想让一个原本不支持 stdin 的程序支持它，就在前面加 `xargs`。
o

one example of unification:
```bash
echo "hello" | grep "hello"
echo "hello" | grep "hello" - #labeled stdin goes in from -
grep "hello" numbers.txt#unifiy with line 2! 
```
- redirect data from file
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
	cmd > /dev/null 2>&1  (>: 给正常运行的stdout的出口；2>: 给sderr的出口) 相当于消除了任意command 的结果
	```

[[Stream grammar tips]]


- `fzf`: an interactive interface to filter and select


## Environment variables&Local shell variables
- local var:
    - *assign*: foo=bar ; Shell variables do not have types they are all strings
    
    > [!tips]-
    > `foo = bar` is invalid syntax as the shell will parse it as calling the program `foo` with arguments `['=', 'bar']`. In shell scripting the role of the space character is to perform argument splitting
    
    - *access*: $foo ; can add "" (but not ' 'which is seen as literal strings) since space may easily be seen as seperates!
	```bash
	files=$(ls) # put the results of programms to a variable
	# $(): command subsitution: 先执行括号内的命令，然后将命令输出的结果捕捉并替换到当前的行中。
	echo "$files" | grep README
	```

- environment variables:
	When the shell program calls another program it passes along a set of variables, which is *envrionment variables*
	- find the current environment variables by running `printenv`
	- modify current environment: `export`&`unset`
		```bash
		export DEBUG=1
		# All programs from this point onwards will have DEBUG=1 in their environment
		bash -c 'echo $DEBUG'
		# prints 1
		unset DEBUG # delete a variable
		```

- *local variables* v.s *environment variables*
	![](../../../../2026/附件们/c80d5f37-2e82-4933-9d2b-b28a2734ffa8.png)
	*local varables*: only vaild when u don't need to 创建新进程 ; like the personal brochure of the boss, only valid when the boss don't need employees to finish jobs
	>[!example]-
	>这类操作被称为 **Shell 内建命令 (Built-ins)**。它们不是硬盘上的程序 而是**直接写在 Shell 本身源代码里的功能**。经理不需要招人，自己一抬手就干了。
	>- **`cd` (切换目录)：** 这是一个极其经典的例子。试想一下，如果 `cd` 是个外部程序，你让一个“临时工”去隔壁房间（切换了目录），然后临时工下班了，你这个经理不还是留在原地吗？所以 `cd` 必须是经理亲自走过去，属于内建命令。
	>- **变量赋值：** 你之前学的 `foo=bar` 或者 `export DEBUG=1`。这是经理在自己本子上写字，不创建新进程。
	>- **`echo`, `pwd`, `history`：** 这些是非常基础的命令，通常也被优化为内建命令。
	>- **`exit`：** 经理自己辞职下班。
	
	*environment variables*: like the regulation of the company---eveyone knows!
	still valid when programs that create new operation:
	>[!example]-
	>只要你是调用了**硬盘上的独立程序**，或者**开辟了新的工作流**，就会创建新进程。
	>- **所有的外部命令：** 比如 `ls`, `grep`, `python`, `git`, `vim`, `cat`。当你输入 `ls` 时，Shell 会去硬盘上找 `ls` 这个执行文件，启动它作为一个子进程运行。
	>- **执行 Shell 脚本（最常见）：** 当你运行 `./myscript.sh` 或 `bash myscript.sh` 时，系统会**新建一个纯净的 Bash 子进程**去跑这个脚本。脚本跑完，子进程销毁。这就是为什么你在脚本里写的“局部变量”，脚本运行完后你就找不到了。
	>- **管道 `|` ：** 你之前学过的 `ls | grep "py"`。管道两边的命令，会同时启动两个平行的子进程，通过管道通信。
	>- **子 Shell 语法 `( )`：** 如果你把命令用括号括起来，比如 `(cd /tmp && ls)`，这叫显式开启一个子进程。执行完后，你原来窗口的目录**不会改变**。

	
## Return Codes
- return of a shell script
	- exit code 0: no bug
	- nonzero: were issues
	- To return a nonzero exit code we have to use the `exit NUM` shell built-in. We can access the return code of the last command that was run by accessing the special variable `$?`.
	- `if` and `while` also uses it for decision
- logistics:`&&`:and; `||`: or
	>[!code]-
>	```bash
>	# echo will only run if grep succeeds (finds a match)
grep -q "pattern" file.txt && echo "Pattern found"
>	# echo will only run if grep fails (no match)
grep -q "pattern" file.txt || echo "Pattern not found"
>	# true is a shell program that always succeeds
true && echo "This will always print"
>	# and false is a shell program that always fails
false || echo "This will always print"
>	```


## Signals:
special communication mechanism; a process stops its execution and deals with it e.g `Ctrl-C`$\implies$ prompts the shell to deliver a `SIGINT` signal to the process

>[!example]- Cope with signals
>In our case, when typing `Ctrl-C` this prompts the shell to deliver a `SIGINT` signal to the process. Here’s a minimal example of a Python program that captures `SIGINT` and ignores it, no longer stopping. To kill this program we can now use the `SIGQUIT` signal instead, by typing `Ctrl-\`.
>```python
>import signal, time
def handler(signum, time):
    >print("\nI got a SIGINT, but I am not stopping")
>signal.signal(signal.SIGINT, handler)
>i = 0
>while True:
   > time.sleep(.1)
    >print("\r{}".format(i), end="")
    >i += 1
>```
>result
>```
$ python sigint.py
24^C    # 在t=24时 按下了无效键cntrl+C
I got a SIGINT, but I am not stopping
26^C
I got a SIGINT, but I am not stopping
30^\[1]    39913 quit       python sigint.py
>```

- typing `Ctrl-Z` will prompt the shell to send a `SIGTSTP` signal, which pauses a process
	- when paused:The [`jobs`](https://www.man7.org/linux/man-pages/man1/jobs.1p.html) command lists the unfinished jobs associated with the current terminal session
-  continue the paused job in the foreground or in the background using [`fg`](https://www.man7.org/linux/man-pages/man1/fg.1p.html) or [`bg`](https://man7.org/linux/man-pages/man1/bg.1p.html), respectively.(`fg` more common)

- ==directly kill a process by signal== : use the [`kill`](https://www.man7.org/linux/man-pages/man1/kill.1.html) command, with the syntax `kill -TERM <PID>`.
	- get pid: open a new terminal and use:  [`pgrep`](https://www.man7.org/linux/man-pages/man1/pgrep.1.html) to find that out;**`pgrep -a [名字]`**：列出 PID 的同时显示**完整的启动命令和参数**
	>[!tips]-
	> `kill` 命令的本质是**发送信号**。
	> `kill -TERM <PID>`（等同于 `kill -15 <PID>`）是**最推荐的关闭程序方式**。它给程序留出时间存盘、清理垃圾、优雅退出。
	> 只有当程序彻底卡死、不听指挥时，才使用强制手段 `kill -KILL <PID>`（即 `kill -9 <PID>`）

- **After recieving signal**:
	Within shell scripts, you can use the `trap` built-in to execute commands when signals are received. This is useful for cleanup operations:
	```bash
	#!/usr/bin/env
	cleanup() {
	    echo "Cleaning up temporary files..."
	    rm -f /tmp/mytemp.*
	}
	trap cleanup EXIT  # Run cleanup when script exits
	trap cleanup SIGINT SIGTERM  # Also on Ctrl-C or kill
	```
- You can learn more about these and other signals [here](https://en.wikipedia.org/wiki/Signal_\(IPC\)) or typing [`man signal`](https://www.man7.org/linux/man-pages/man7/signal.7.html) or `kill -l`.

## Background Job** : (后台运行)
- `command`+`&` : change the command into background job
	```bash
	jhj@LAPTOP-SKRHIUC1:/mnt/c/Users/HW/Desktop$ sleep 1000 &
	[2] 8002  # [2]:job number 8002:PID
	jhj@LAPTOP-SKRHIUC1:/mnt/c/Users/HW/Desktop$ echo $!
	8002

	```
- ==background an already running program== you can do `Ctrl-Z` followed by `bg`.(==if the program has to wait for too long)
	```bash
	jhj@LAPTOP-SKRHIUC1:/mnt/c/Windows/system32$ sleep 1000
	^Z
	[1]+  Stopped                 sleep 1000
	jhj@LAPTOP-SKRHIUC1:/mnt/c/Windows/system32$ bg
	[1]+ sleep 1000 &
	```
- ==foreground an background program== : `fg %<job number>`
	```bash
	jhj@LAPTOP-SKRHIUC1:/mnt/c/Windows/system32$ bg
	[1]+ sleep 1000 &
	jhj@LAPTOP-SKRHIUC1:/mnt/c/Windows/system32$ fg %1
	sleep 1000
	```
>[!code]- examples
> ```bash
> $ sleep 1000
> ^Z
> [1]  + 18653 suspended  sleep 1000
> 
> $ nohup sleep 2000 &
> [2] 18745
> appending output to nohup.out
> 
> $ jobs
> [1]  + suspended  sleep 1000
> [2]  - running    nohup sleep 2000
> 
> $ kill -SIGHUP %1
> [1]  + 18653 hangup     sleep 1000
> 
> $ kill -SIGHUP %2   # nohup protects from SIGHUP
> 
> $ jobs
> [2]  + running    nohup sleep 2000
> 
> $ kill %2
> [2]  + 18745 terminated  nohup sleep 2000
> ```






## Remote Machines:
common tool: SSH; connect to a remote server&provide the shell interace
>[!example]-
> ```
> ssh alice@server.mit.edu
> ```
> Here we are trying to ssh as user `alice` in server `server.mit.edu`.

dont leak private key
- running commands remotely
	```bash
	# here ls runs in the remote, and wc runs locally
	ssh alice@server ls | wc -l
	
	# here both ls and wc run in the server
	ssh alice@server 'ls | wc -l'
	```

- transfer to and from local files: [`scp`](https://www.man7.org/linux/man-pages/man1/scp.1.html) is the most traditional tool;  [`rsync`](https://www.man7.org/linux/man-pages/man1/rsync.1.html) improves upon `scp` (the two commands can only be operated in the local shell environment, not on ssh remote server)
	>[!tips]- The edge of `rsync` 
	>detecting identical files in local and remote, and preventing copying them again
	>provides more fine grained control over symlinks, permissions and has extra features like the `--partial` flag that can resume from a previously interrupted copy
	> 真正的镜像同步 以及保留更多院数据
	
	>[!code]- syntax:
> 	```bash
> 	# 上传：格式：scp [本地文件] [远程地址:远程路径]
> 	scp my_script.py alice@server.mit.edu:/home/alice/scripts/
> 	
> 	# 回拉：格式：scp [远程地址:远程文件] [本地路径]
> 	scp alice@server.mit.edu:/home/alice/data.csv . # the final . means the file I am currently located
> 	
> 	scp -r ./my_project alice@server.mit.edu:/var/www/ #(send the whole file: -r: recursive)
> 	
> 	# 进阶版上传
> 	rsync -avP my_project/ alice@server.mit.edu:/home/alice/backup/ 
> 	# -avP:show everything and visualizes prgress ;
> 	also: rsync -avP [location] [remotes:location]
> 	if local location: rsync -av my_dir remote:/ it puts the whole file into the remote; result:/my_dir/file.txt
> 	
> 	else:rsync -av my_dir/ remote:/  put all the content instead of the whole file into the remote server: 结果远程有：`/file.txt`，没有 `my_dir` 这一层
> 	```



## Terminal Multiplexers
[[tmux cheatsheet]]

## Customizing the Shell
 - Dotfiles: e.g `~/.vimc`
    Hidden files, but the shell itself if configured by them( like the setting file of the system )$\implies$ can edit and set them
- Add new loction for the shell to find programs
    (When 调用 a program, it searches $PATH) $\implies$ add a particular location to $PATH so that writing the program name can 调用 it directly instead of searching it [L1 Course overview+Shell](L1%20Course%20overview+Shell.md)


- installing new command-line tools(executable programs)
    require: Package managers(=应用商店) Ubuntu:apt 
	```bash
	sodo apt install [program name] # sodo:切换到管理员模式
	```

- Aliases:
    simplify commands
    >[!example]-
    >```bash
	>alias ll="ls -lh"
	># Save a lot of typing for common commands
	alias gs="git status"
	alias gc="git commit"
	># Save you from mistyping
	alias sl=ls
	># Overwrite existing commands for better defaults
	alias mv="mv -i"           # -i prompts before overwrite
	>```

	limitations:they cannot take arguments in the *middle* of a command. For more complex behavior, you should use [[shell functions instead]]
- dotfile management(for remote/differnt server working easily; so that u can be yin your familiar envionment settings easily) (no need to know now)
	https://missing.csail.mit.edu/2026/command-line-environment/#:~:text=How%20should%20you,on%20the%20topic.



### AI in shell
(1) 本地 AI models that do not rely on API tokens and internet e.g: Ollama(edge local AI: all the comutations are finished on the comuter's CPU & GPU)
(2) need API tokens and internet e.g: calude!

- command generation: `llm -m llama3.2 "command"`/or model: llama is set as default LLm $\implies$ `llm "command"`
	simple coding requirements: use llama3.2
	complex problrems: use models that requires tokens!
- can directly combined with pipelines! e.g:
	```bash
	$ cat users.txt
	Contact: john.doe@example.com
	User 'alice_smith' logged in at 3pm
	Posted by: @bob_jones on Twitter
	Author: Jane Doe (jdoe)
	Message from mike_wilson yesterday
	Submitted by user: sarah.connor
	$ INSTRUCTIONS="Extract just the username from each line, one per line, nothing else"
	$ llm "$INSTRUCTIONS" < users.txt  # "$ ": since INSTRUCTIONS is a variable!
	john.doe
	alice_smith
	bob_jones
	jdoe
	mike_wilson
	sarah.connor
	```

### Terminal Emulators(beautify your interface!)

Along with customizing your shell, it is worth spending some time figuring out your choice of **terminal emulator** and its settings. A terminal emulator is a GUI program that provides the text-based interface where your shell runs. There are many terminal emulators out there.

Since you might be spending hundreds to thousands of hours in your terminal it pays off to look into its settings. Some of the aspects that you may want to modify in your terminal include:

- Font choice
- Color Scheme
- Keyboard shortcuts
- Tab/Pane support
- Scrollback configuration
- Performance (some newer terminals like [Alacritty](https://github.com/alacritty/alacritty) or [Ghostty](https://ghostty.org/) offer GPU acceleration).













