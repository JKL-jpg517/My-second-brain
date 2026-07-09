在 Linux（以及你的 WSL Ubuntu）中，移动文件的核心指令是 **`mv`**（其含义就是 **m**o**v**e）。

这个指令非常强大，因为它不仅用来**移动**文件，还兼职用来**重命名**文件。

### 1. 基本用法

`mv` 指令的基本格式如下：

Bash

```
mv [选项] 源文件 目标位置
```

#### 场景 A：移动文件到另一个文件夹

如果你想把 `documentationtry.py` 移动到名为 `Labs` 的文件夹里：

Bash

```
mv documentationtry.py Labs/
```

#### 场景 B：重命名文件

在 Linux 中，重命名其实就是“把文件移动到一个新的名字下”。如果你想把 `documentationtry.py` 改名为 `math_tools.py`：

Bash

```
mv documentationtry.py math_tools.py
```

#### 场景 C：移动并重命名

你想把文件移到 `Labs` 文件夹的同时顺便改个名：

Bash

```
mv documentationtry.py Labs/math_tools.py
```

### 2. 常用参数（防止手抖）

`mv` 是个“狠角色”，默认情况下如果目标位置有同名文件，它会**直接覆盖**而不提醒。建议配合以下参数使用：

|**参数**|**说明**|
|---|---|
|**`-i`**|**交互模式**：如果目标文件已存在，会询问你是否覆盖（输入 `y` 确认）。|
|**`-n`**|**不覆盖**：如果目标文件已存在，则不执行移动，安全第一。|
|**`-v`**|**可视化**：运行后会告诉你它具体做了什么（例如：`'a.py' -> 'Labs/a.py'`）。|

### 3. 进阶技巧：批量移动

如果你想把当前目录下所有的 `.py` 文件都移到 `Labs` 文件夹：

Bash

```
mv *.py Labs/
```

_这里的 `*` 是通配符，代表“任何内容”。_

### 💡 一个关于 WSL 的小提醒

既然你在用 WSL，你可能会想在 Linux 终端里把文件移动到 Windows 的桌面。在 WSL 中，你的 Windows 硬盘通常挂载在 `/mnt/` 目录下。

例如，移动文件到 **Windows 桌面**（假设用户名是 `YourName`）：

Bash

```
mv documentationtry.py /mnt/c/Users/YourName/Desktop/
```

你现在是想整理一下你的 `CS61A` 文件夹，还是想给那个拼写错误的 `devide` 文件改个名字？