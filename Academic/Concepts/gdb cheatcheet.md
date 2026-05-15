
1.
编译代码（关键步骤）
在 Linux 终端运行以下命令。**必须加上 `-g` 参数**，否则 GDB 找不到源代码行号：

```bash
g++ -g debug_demo.cpp(file name) -o debug_demo(where the complied file is placed)
```
2.
进入 GDB 调试会话

```bash
gdb ./debug_demo
```
or:
 直接运行程序（看运行日志）
输入以下命令并回车：
```bash
./debug_demo
```

这时你就能看到你在 C++ 代码里写的 `std::cout` 或者 `printf` 输出的内容了。


3.
common commands
- `run` - Start the program
- `b {function}` or `b {file}:{line}` - Set a breakpoint
- `c` - Continue execution
- `step` / `next` / `finish` - Step in / step over / step out
- `p {variable}` - Print value of variable
- `bt` - Show backtrace (call stack)
- `watch {expression}` - ==Break when the value changes=== 

> Consider using GDB’s TUI mode (`gdb -tui` or press `Ctrl-x a` inside GDB) for a split-screen view showing source code alongside the command prompt.
> 