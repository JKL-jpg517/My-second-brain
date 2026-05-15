$$
	A_{m\times n}=C_{m\times p}R_{p\times n}
$$
1. $C$(Columns):Contains the First $r$ Independent Columns of $A$
   >[!Tips]- determin independent cols method&relation between C and A
    >two determination methods of independent columns:![p.30](Academic/Sources/数学/教辅/introduction-to-linear-algebra-6nbsped-1733146679-9781733146678_compress.pdf#page=40&rect=80,175,431,208&color=note)
    >$r$&$n$: ![p.30](Academic/Sources/数学/教辅/introduction-to-linear-algebra-6nbsped-1733146679-9781733146678_compress.pdf#page=40&rect=66,159,372,173&color=note)
    >[[Invertible Matrix Theorem and everything about it]]
2. $R$(Rows): Tells how to produce $A$ from $C$
   >[!Tips]- two parts of $R$
    >Col of $C$: from A $\implies$ $R$ contains an identity matrix
    >Other parts of $R$ : the coefficients of the linear combinations of the columns of $A$

3. relationship between $C,R,A$
    $r=$ the columns of $C$=the rows of $R$ (==the premise of the multiplication of matricies==)$\implies$ column rank of $A$=row rank of $A$
>[!Tip]- Summary
> ![p.31](Academic/Sources/数学/教辅/introduction-to-linear-algebra-6nbsped-1733146679-9781733146678_compress.pdf#page=41&rect=44,231,474,351&color=note)
>$C$ has the same column space as $A$; 
>$R$ has the same row space of $A$ (use another way of multiplication u will see; or in chap3)
 >![p.32](Academic/Sources/数学/教辅/introduction-to-linear-algebra-6nbsped-1733146679-9781733146678_compress.pdf#page=42&rect=68,440,437,535&color=note)


4. How to determine $C R$
     [How to find R and C?](../Sources/数学/MIT%2018.06%20Linear%20Algebra/notes/1.4%20Matrix%20Multipication%20AB%20and%20CR.md#How%20to%20find%20R%20and%20C?)
     
5. Insight &Intuition:
   - **Dimensionality Compression**: It provides a fundamental proof that the **column rank** of a matrix is always equal to its **row rank**.
   - **Information Extraction**: In the context of data processing, $C$ represents the **core features** (the basis), while $R$ represents the **combination weights** (the coefficients) of these features.
   - **Storage Optimization**: If $r \ll n$, the memory required to store $C$ and $R$ ($m \times r + r \times n$) is significantly lower than storing the full matrix $A$ ($m \times n$).
   - **Robotics Application**: When processing massive state matrices returned by sensors, the $A=CR$ logic helps quickly identify which state variables are redundant.

   >[!warning] Boundary Conditions 
    > This factorization offers significant compression benefits only when $A$ is **not full rank** (i.e., it contains linearly dependent columns).
  

