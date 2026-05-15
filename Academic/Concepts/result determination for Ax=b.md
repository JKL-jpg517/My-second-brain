## equation perspective:
- $Ax=b$ is n equations for n unknowns
    - **one solution**: $A$ has independent columns([[Inverse&independent&rank&determinant&pibots]])
     - **no solution**: $A$ has dependent columns([Inverse&independent&rank&determinant&pibots](Inverse&independent&rank&determinant&pibots.md) ) while $b$ is **not in the columns space of B**
     - **infinate solutions** : $A$ has dependent columns([Inverse&independent&rank&determinant&pibots](Inverse&independent&rank&determinant&pibots.md) ) while $b$ is **in the column space of B**
>[!tip]- How the solutions look like?
>$A$ independent $\implies$ $AX=0$ infinate solutions for $X$
>$\implies$ $A(x+\alpha X)=b$ ($\alpha$ is a random number)
>$\implies$ pick a random $x$and ${X}$  solution: x+$\alpha X$ 
    
## A to U & back substitution persepctive
a more systematic way
![introduction-to-linear-algebra-6nbsped-1733146679-9781733146678_compress, p.41](Academic/Sources/数学/教辅/introduction-to-linear-algebra-6nbsped-1733146679-9781733146678_compress.pdf#page=51&rect=47,185,473,209)
#### $A$ to $U$: row elimation
- elimation to $U$: ==use the $i$ equation to produce zeros below piviot $i$ in column$i$==
 - tool: elimation matrix $E_{{ij}}$  to turn the number in row $i$ column $j$ into 0
   $\implies$ $E_{ij}E_{mn}E_{pq}\dots A=U$$\implies$ $EA=U=Eb=c$
 - piviot: the first non-zero element in a row of a matrix that is ==used to eliminate (make zero) the entries below it in its column during Gaussian elimination.==
 >[!bug] Possible breakdown
> *zero can appear in a pivot position*
>1. row exchage via matrix $P$ use the rows below to provide pivots
>2. or: no potential piviots available$\implies A$ do not have full rank$\implies$ no or inf solutions

#### Back substitution and diagnal of $U$
- $U=EPA$  when its diagonal has no zeros$\iff$ full rank$\iff$ one solution for $Ax=b$ ==The diagonal of $U$ tells us everthing!!==

## Geography prespective
- row picture: 在$x-y$ 坐标中($n$-dimention 坐标) draw the graph by the rows of $A$
>[!tips]- example
>![introduction-to-linear-algebra-6nbsped-1733146679-9781733146678_compress, p.44](Academic/Sources/数学/教辅/introduction-to-linear-algebra-6nbsped-1733146679-9781733146678_compress.pdf#page=54&rect=53,332,462,492)
 
- column picture: split $A$ into columns m column vectors$\implies$ the linear combinations of the column vectors 

>[!tips]- example
>![introduction-to-linear-algebra-6nbsped-1733146679-9781733146678_compress, p.44](Academic/Sources/数学/教辅/introduction-to-linear-algebra-6nbsped-1733146679-9781733146678_compress.pdf#page=54&rect=50,64,458,185)

