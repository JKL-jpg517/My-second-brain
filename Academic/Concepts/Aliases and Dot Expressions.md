Dot expressions: distinguish whichn column
Aliases: ditinguish tables `AS`( same as giving new names to a column)
often used together: when we need to use a same table twice

often we need to combine two same tables
```SQL
CREATE TABLE siblings AS

  SELECT a.child AS first, b.child AS second 
  From parents AS a, parents AS b 
  WHERE a.parent=b.parent and a.child<b.child; # remove duplicates
```
![](../../2026/附件们/5cd34475-6dc5-4056-b461-26bf8f47ec67.png)

find grandparents
```SQL
SELECT a.parent,b.chile FROM parents AS a, parents AS b WHERE a.child=b.parent;
```

**Join Multiple Tables**
![](../../2026/附件们/04ab7788-281a-4195-8948-44e71b4a5106.png)
WHERE 后面两行： 在毛里找granddog 和grandpup的名字！！！
