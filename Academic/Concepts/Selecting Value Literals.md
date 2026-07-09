A `SELECT` statement always includes a comma-seperated list of column descriptions
*column description*: an expression, optionally followed by `AS` to give it a column name

Selecting literals created a one-row table
`SELECT [expression] AS [name], [expression] AS [name]`

The union of two select statements is a table containing the rows of both of their results: `UNION`: A tabel more than on row



```SQL
  SELECT "daisy" AS parent, "hank" AS child UNION
  SELECT "ace"          , "bella"         UNION
  SELECT "ace"          , "charlie"       UNION
  SELECT "finn"         , "ace"           UNION
  SELECT "finn"         , "dixie"         UNION
  SELECT "finn"         , "ginger"        UNION
  SELECT "ellie"        , "finn";
```
