 **Insert**
 ![480](../../2026/附件们/b8b3fa71-0c3c-4759-b198-cd3adf4661cd.png)
 Insert into one column:
 `INSERT INTO t(column) VALUES (value)`;   the others become default values
 Insert into both columns:
 `INSERT INTO t VALUES (value0,value1)`
 e.g:
 ```SQL
 create table primes(n UNIQUE, prime DEFAULT 1); # create empty list
 INSERT INTO prime VALUES (2,1),(3,1);
 
 INSERT INTO primes(n) VALUES (4),(5),(6),(7);
 ```
 ![](../../2026/附件们/8d2ebe49-95d1-4bb8-90ce-76711e1f67dc.png)
 **Update**
 modify the values 
 ![](../../2026/附件们/22c2f9bb-8d30-4453-8132-56f6b436a0b1.png)
 
 e.g
 `UPDATE primes SET prime=0 WHERE n>2 AND n%2=0;`

**Delete**
remuve some rows  but does not delete the table itself
![](../../2026/附件们/9659a4c2-8679-48fb-903e-bbdf6516cfb0.png)
