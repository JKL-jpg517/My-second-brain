calculation can be achived in sql
![](../../2026/附件们/0148a491-51db-406b-a0b3-b689079fe1db.png)

/ sum
```SQL
-- 创建城市表
CREATE TABLE cities AS
  SELECT 38 AS latitude, 122 AS longitude, "Berkeley" AS name UNION
  SELECT 42, 71, "Cambridge" UNION
  SELECT 45, 93, "Minneapolis" UNION
  SELECT 33, 117, "San Diego" UNION
  SELECT 26, 80, "Miami" UNION
  SELECT 90, 0, "North Pole";

-- 自连接查询：计算距离并按距离排序
CREATE TABLE distances AS
  SELECT a.name AS first, b.name AS second,
         60 * (b.latitude - a.latitude) AS distance
  FROM cities AS a, cities AS b;

-- 运行结果查询
SELECT second FROM distances 
WHERE first = "Minneapolis" 
ORDER BY distance;  # 按照距离排序
```


#### String Expressions
 ![](../../2026/附件们/f06f3618-db3b-46a8-b2ec-7b03bfd3e01c.png)
 `||` combine strings together
 ![](../../2026/附件们/258b2017-48d1-4568-b495-ced2b7b36802.png)
 
 