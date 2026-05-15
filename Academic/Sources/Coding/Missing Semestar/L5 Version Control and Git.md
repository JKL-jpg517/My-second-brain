Version control systems (VCSs) are tools used to track changes to source code; maintain history, facilitate colaborate
>[!tip]- What it can do&why useful
>VCSs track changes to a folder and its contents in a series of _snapshots_, where each snapshot encapsulates the entire state of files/folders within a top-level directory
>VCSs also maintain metadata like who created each snapshot, messages associated with each snapshot, and so on
> it can let you look at old snapshots of a project, keep a log of why certain changes were made, work on parallel branches of development, and much more
> it’s an invaluable tool for seeing what other people have changed, as well as resolving conflicts in concurrent development

can answer questions like this:
- Who wrote this module?
- When was this particular line of this particular file edited? By whom? Why was it edited?
- Over the last 1000 revisions, when/why did a particular unit test stop working?

 Git’s interface is a leaky abstraction(Git 的interface是一个经常有底层泄露的抽象)
 
>[!conclution]-
>While Git admittedly has an ugly interface, its underlying design and ideas are beautiful. While an ugly interface has to be _memorized_, a beautiful design can be _understood_. For this reason, we give a bottom-up explanation of Git, starting with its data model and later covering the command-line interface

## Git's data model
--- the ingenutiy of Git, enabling  maintaining history, supporting branches, and enabling collaboration.
everything has a hash value

### Snapshots

in terms of Git: *a file* is called a “blob”, and it’s just a bunch of bytes with a unique hash value: blob*
.*A directory* is called a “tree”; tree 有一个键值映射(==内部身份==)： 文件名---》blob的哈希值or other tree的哈希值 (只是记录键 而非文件本身); ==在外部也会被给一个哈希值： tree*==
$$文件名 (Name) \xrightarrow{映射} 内部文件的哈希值 (Hash) \xrightarrow{索引} 实际内容 (Blob/Tree)$$

$\implies$ A snapshot is ==the top-level tree(root) that is being tracked(still an id)==；only has trees and the hash value of blobs . For example 
```
<root> (tree)
|
+- foo (tree)
|  |
|  + bar.txt (blob, contents = "hello world")
|
+- baz.txt (blob, contents = "git is wonderful")
```

git history: a bunch of snapshats related through parent relationship
### Git's model of history
not: list snapshots in time order
but: its history is a directed acyclic graph(有向无环图) (DAG) of snapshots：(snapshot+历史指针)
1. each commit refers to(有一个指向历史的指针) a set of parents(its previous commits)(每个快照都有一个指针指向它的父辈：Git 记录的不是“接下来要做什么”，而是“我是从哪个状态演变而来的”)
$$Commit = Snapshot + Metadata + Parent\ Pointers(prevous commits)$$
```
o <-- o <-- o <-- o
            ^
             \
              --- o <-- o
```



2.  for parallel jobs seperated into independent tasks; because of (1.) it only record its father $\implies$ they r independent!
3. Merging(合并)： Merging commit: form two fathers
```
o <-- o <-- o <-- o <---- o
            ^            /
             \          v
              --- o <-- o
```

Commit can not be undo  they can only be abolished!
4. branch: a reference pointing to a commit; muttable; to types of deletion!
when u delete a branch, it delets the reference, not the commits/object on it$\implies$  only for simplifying logic
two types of deletion
- **`git branch -d <name>` (小写 d = Safe)**： Git 会先做一个逻辑判断：这个分支里的内容是否已经合并（Merge）到其他分支了？如果没合并，Git 会拒绝删除，并提示你：“兄弟，这里面的代码还没合呢，删了你就找不到这些 Commit 的入口了！”
    
- **`git branch -D <name>` (大写 D = Force)**： 这是强行删除。它不管你合没合，直接把指针文件扬了。 if not merged: the comitts on the brach will be totally isolated; no regerence can get it but its still there!




the code of history/data model
```
// a file is a bunch of bytes
type blob = array<byte> 
# in git  every file is a byte，given a hash value blob*

// a directory contains named files and directories
type tree = map<string, tree* | blob*>
 # string: tree name; its content: can be another tree* or a blob* or both; but it is only a pointer to the trees and the blobl; the tree is given a hash value；文件名和哈希值的组合

// a commit has parents, metadata, and the top-level tree
type commit = struct {
    parents: array<commit*> # an array of pointers of former commits；Normal commit: one hash value in the array(the former hash); Merge commit: 2 or more hash numbers in the array; Initial commit: 0 hash numbers
    author: string
    message: string
    snapshot: tree*  # bytes
}  # commit itself has a hash value too;commit中包含有其它object的哈希值；并且commit自己也被赋予了一个哈希值？
```


### Objects and content addressing
object(not objects): blob, tree or commit
```
type object = blob | tree | commit
```

*objects*(not object) unify these by giving a hash value to them
```
objects = map<string, object>  # the string here is the hash value!

def store(object):
    id = sha1(object)
    objects[id] = object

def load(id):
    return objects[id]
```
They don’t actually _contain_ them in their on-disk representation, but have a reference to them by their hash

objects: immutable:  actually can change,but if changed, everything behind it will be changed; 
or add a new commit that reverses the  commit u want to delete

### references
SHA-1 hash help identify all snapshot, but the numbers are hard to remenber $\implies$ give human-readable names(references) for hash values.
Unlike objects, which are immutable, references are ==mutable== (can be updated to (point to) a new commit). For example, the `master` reference usually points to the latest commit in the main branch of development.

```
references = map<string, string># the foemer: human readable names; the latter: hash values
def update_reference(name, id):
    references[name] = id
def read_reference(name):
    return references[name]
def load_reference(name_or_id):
    if name_or_id in references:
        return load(references[name_or_id])
    else:
        return load(name_or_id)
```


a notion of "where we are currently at": take a new snapshot,  and name it as HEAD

### Staging area
snapshot--->in staging area, confirm what do u want to control -----> commit!


### Repositoties(仓库)
Finally, we can define what (roughly) is a Git _repository_: it is the data `objects` and `references`.

>[! tip]- the function of git commands
>: All `git` commands map to some manipulation of the commit DAG by adding objects and adding/updating references.
>Whenever you’re typing in any command, think about what manipulation the command is making to the underlying graph data structure.


##### github
git: free and opensouce distributed version tool.
github: software/ service provider let u host git respitories





### Git command-line interface
[[Git Command Cheatsheet]]

