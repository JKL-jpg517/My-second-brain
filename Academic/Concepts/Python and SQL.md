python can interact with databases
e.g
```python
import sqlite3

# 1. 连接数据库, n.db: a database
db = sqlite3.Connection("n.db") #Python 本身并不懂 SQL，它只负责把这串字符像运货一样，通过 `sqlite3` 这个接口，“原封不动”地运送给底层的数据库引擎

# 2. 创建表
db.execute("CREATE TABLE nums AS SELECT 2 UNION SELECT 3;")

# 3. 插入新数据
db.execute("INSERT INTO nums VALUES (?), (?), (?);", range(4, 7))

# 4. 执行查询并打印
print(db.execute("SELECT * FROM nums;").fetchall())

# 5. 保存并关闭
db.commit()
```


python vs SQL:
|**特性**|**Python (宿主语言)**|**SQL (查询语言)**|
|---|---|---|
|**职能**|**大脑**：负责写业务逻辑、循环、条件判断、做计算。|**管理员**：只负责存储、筛选、归档和查找数据。|
|**思维模式**|**指令式**：告诉程序“第一步做什么，第二步做什么，遇到循环怎么跳”。|**声明式**：只告诉数据库“我要这个结果，你看着办”。|
|**处理对象**|变量、函数、类、复杂的逻辑流。|数据表、关系、行列匹配。|
|**运行位置**|在内存中动态运行。|在数据存储层（磁盘/数据库文件）运行。|