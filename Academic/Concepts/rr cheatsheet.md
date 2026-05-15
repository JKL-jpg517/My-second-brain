Basic usage:

```
# Record a program execution
rr record ./my_program

# Replay the recording (opens GDB)
rr replay
```

The magic happens during replay. Because the execution is deterministic, you can use **reverse debugging** commands(when u debug: pick out the place where there is a bug; reverse up the line to check and determine a more specific scope(像二分法)):

- `reverse-continue` (`rc`) - Run backwards until hitting a breakpoint
- `reverse-step` (`rs`) - Step backwards one line
- `reverse-next` (`rn`) - Step backwards, skipping function calls
- `reverse-finish` - Run backwards until entering the current function

This is incredibly powerful for debugging. Say you have a crash—instead of guessing where the bug is and setting breakpoints, you can:

1. Run to the crash
2. Inspect the corrupted state
3. Set a watchpoint on the corrupted variable
4. `reverse-continue` to find exactly where it was corrupted

`bt` 是用来查看“函数调用链”的。它让你知道程序是怎么一步步从 `main` 钻到当前这一行代码的，是排查崩溃和内存篡改的头号神器

**When to use rr:**

- Flaky tests that fail intermittently
- Race conditions and threading bugs
- Crashes that are hard to reproduce
- Any bug where you wish you could “go back in time”

> Note: rr only works on Linux and requires hardware performance counters. It doesn’t work in VMs that don’t expose these counters, such as on most AWS EC2 instances, and it doesn’t support GPU access. For macOS, check out [Warpspeed](https://warpspeed.dev/).

> **rr and concurrency**: Because rr records execution deterministically, it serializes thread scheduling. This means some race conditions may not manifest under rr if they depend on specific timing. rr is still useful for debugging races—once you capture a failing run, you can replay it reliably—but you may need multiple recording attempts to catch an intermittent bug. For bugs that don’t involve concurrency, rr shines brightest: you can always reproduce the exact execution and use reverse debugging to hunt down corruption.