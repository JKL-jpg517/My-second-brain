>[!abstract]- One-Sentence Intuition 
>**Inner product** is about "compression" (two vectors collide and collapse into a single scalar).
>**Outer product** is about "expansion" (a column and a row cross paths to span a full matrix space).     
>**Rank-1 matrices** are the fundamental "building blocks" of all complex matrices in the universe.



![p.34](Academic/Sources/数学/教辅/introduction-to-linear-algebra-6nbsped-1733146679-9781733146678_compress.pdf#page=44&rect=62,483,449,582&color=note)

 - outer products: determine the size$\implies$ add$\implies$ result
     - $a_{n}b_{n}^{*}$ : all rank 1 matricies (according to Method 1&2)
     - proves: rank=$r$ matrix can be factorized into sums of matricies of rank 1  
- the form of outer product: col$\times$row natrually allows matrix multiplication
- the form of inner productL row$\times$col needs the size of the matrix same


>[!Homework] rank1 matrix factorization:
>![introduction-to-linear-algebra-6nbsped-1733146679-9781733146678_compress, p.37](Academic/Sources/数学/教辅/introduction-to-linear-algebra-6nbsped-1733146679-9781733146678_compress.pdf#page=47&rect=77,371,457,410)
>$A$, $B$ rank 1 matrix: assume $A=uv^{T}$ $B=xy^{T}$
>$AB=uv^{T}xy^{T}=u(v^{T}x)y^{T}$
>$v^{T}x$: 1$\times$ 1 matrix
>$\implies$ $AB=up^{T}$(p is still a column matrix)
>$\implies$ $AB$ is a resulet of a outer product
>So $R_{AB}=1$

^0872dd

>


