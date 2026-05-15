development environments: a set of tools for developing software
>[!note]- the heart of development environment
> the heart of a development environment is text editing
> functionality,along with accompanying features such as syntax 
> highlighting, type checking, code formatting, and autocomplete

- _Integrated development environments_ (IDEs): e.g VS code brings the heart of development environment altogether with a single application
- *Terminal-based development workflows*: combine tools such as [tmux](https://github.com/tmux/tmux) (a terminal multiplexer), [Vim](https://www.vim.org/) (a text editor), [Zsh](https://www.zsh.org/) (a shell), and language-specific command-line tools, such as [Ruff](https://docs.astral.sh/ruff/) (a Python linter and code formatter) and [Mypy](https://mypy-lang.org/) (a Python type checker)
-  vs the ubuntu on the computer:[relationship between Linux&shell&WSL&ubuntu&terminal](../../../Concepts/relationship%20between%20Linux&shell&WSL&ubuntu&terminal.md)

## Text editing and Vim
[[Vim]]
A text editor optimized for CS related code interaction!(in codes many tasks are distributed); do everything only by keyboard! the interface itself is a coding language;
modal editors: 有不同操作模式对应不同用途；*Normal mode：for moving around a file and making edits; 
Insert Mode： for inserting text;
Replace Mode:for replacing text;
Visual mode: selecting chunks of text;
Command mode:running a command*
>[!note]- mode changing
>You change modes by pressing `<ESC>` (the escape key) to 
>switch from any mode back to Normal mode. From Normal 
>mode, enter Insert mode with `i`, Replace mode with `R`, Visual 
>mode with `v`, Visual Line mode with `V`, Visual Block mode 
>with `<C-v>` (Ctrl-V, sometimes also written `^V`), and 
>Command-line mode with `:`.


### Normal mode
key bindings for:
- movement
- selection
- edits
- counts
- modifiers
>[!code]- basic commands
>Basic movement: `hjkl` (left, down, up, right)
>Words: `w` (next word), `b` (beginning of word), `e` (end of word)   ==对于"end" vim 是为光标也占一个位子 会停在最后一个字母之前的位置，想加载尾部：用ctrl+a替代ctrl+i==
>Lines: `0` (beginning of line), `^` (first non-blank character), `$` (end of line)
>Screen: `H` (top of screen), `M` (middle of screen), `L` (bottom of screen)  是对于行数的中间而言 而非terminal的几何中心
>Scroll: `Ctrl-u` (up), `Ctrl-d` (down) 向上/向下的单位为 0.5$\times$ terminal lines
>File: `gg` (beginning of file), `G` (end of file)
>Line numbers: `:{number}<CR>` or `{number}G` (line {number})  e.g`2G`: go to the second line
>	`<CR>` refers to the carriage return / enter key
>Misc: `%` (matching item, like parenthesis or brace)  e.g : '[ ]' at the first `[`  can jump to ']'
>Find: `f{character}`, `t{character}`, `F{character}`, `T{character}`  e.g f a
  >  - find/to forward/backward {character} on the current line
   > - `,` / `;` for navigating matches  continue to find the priror matches e.g `f,` $\implies$ finds a(from the propor example);   ==都只能在同一行内寻找！==
>Search: `/{regex}`, `n` / `N` for navigating matches ==在全文搜索某个字符 n/N:找下一个贴切的目标==
>u: undo

### Selection
in visual mode:
not only for looking  but also for editing!

- Visual: `v`
- Visual Line: `V`
- Visual Block: `Ctrl-v`

Can use movement keys to make selection.


### Edits
cmds that when used in norml mode: after which automatically changes into insert mode
- `i` enter Insert mode
    - but for manipulating/deleting text, want to use something more than backspace
- `o` / `O` insert line below / above
- `d{motion}` delete {motion}
    - e.g. `dw` is delete word, `d$` is delete to end of line, `d0` is delete to beginning of line
- `c{motion}` change {motion}
    - e.g. `cw` is change word
    - like `d{motion}` followed by `i`
- `x` delete character (equivalent to `dl`)
- `s` substitute character (equivalent to `cl`)
- Visual mode + manipulation
    - select text, `d` to delete it or `c` to change it
- `u` to undo, `<C-r>` to redo
- `y` to copy / “yank” (some other commands like `d` also copy)
- `p` to paste
- Lots more to learn: for example, `~` flips the case of a character, and `J` joins together lines

### Counts
You can combine nouns and verbs with a count, which will perform a given action a number of times.

- `3w` move 3 words forward
- `5j` move 5 lines down
- `7dw` delete 7 words

### Modifiers
==change the meaning of a noun==
Some modifiers are `i`, which means “inner” or “inside”, and `a`, which means “around”.
- `ci(` change the contents inside the current pair of parentheses
- `ci[` change the contents inside the current pair of square brackets
- `da'` delete a single-quoted string, including the surrounding single quotes

>[!Summary] 
>Grammar: [vim Count] + [vim_Verb] + [vim_Modifier] + [vim_Noun]
>in Visual Mode: the noun is already selected!

some additional learning resources:https://missing.csail.mit.edu/2026/development-environment/#:~:text=vimtutor%20is%20a,Vim%20(book)

## Code intelligence and languange servers
IDEs (e.g vscode)  offer lanuguage-specific support for semantic code understanding: can underastand what language u r coding and offer guidance! (e.g:the [Python extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python) relies on [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance), and the [Go extension for VS Code](https://marketplace.visualstudio.com/items?itemName=golang.go) relies on the first-party [gopls](https://go.dev/gopls/).); By installing these extentions, they connect to language servers that implement Langugage Server Protocol(LSP protocol:协议)

[[language complier and extentions]]

spceific jobs: https://missing.csail.mit.edu/2026/development-environment/#:~:text=Code%20completion.%20Better,on%20code%20quality.

when configuring python: the extention should be pointed to spcific envirnments or it will not recognize some packages

can also set and modify the extentions

## AI-powered development
LLMs adoption in coding: autocomplete, inline chat, and coding agents(能力不断进阶的三种形态)
### Autocomplete
vs: LSP: a dictionary; AI autocomplete: guess what u write
AI for vscode: Github Copilot

- guide AI autocomplete by naming appropriately and using 注释 or dotstring(""".......""": placed in the next line of a function!)
- downside: can only help complete contents after the cursor( can still complete tasks suceessfully; but the code may lack aethetic value)

### Inline chat
(行内对话)
select al line or a block, directly prompt AI model to edict the code block:

在 VS Code（安装了 Copilot 之后）或 Cursor 中，你通常按下 **`Ctrl + I`** (Windows) 或 **`Cmd + K`** (Cursor) 就能召唤它。

它会像一个浮动的输入框一样出现在你的光标处：

> **你输入**：“帮我给这个函数加上异常处理，如果路径不存在就报错。” **它执行**：直接在你原来的代码位置进行修改，并用**红绿颜色**（Diff 视图）展示它改了哪里。


### Coding agents
in L7

## Other exploration&extentions:
(1) IDE AI agents: [VS Code extensions sorted by popularity](https://marketplace.visualstudio.com/search?target=VSCode&category=All%20categories&sortBy=Installs)

(2) terminanal based development workflows:  e.g install vim extentions(e.g can help u chek grammar; beautify vim); coding agents in terminals(e.g Aider)
e.g [[Nerdtree extention]]


