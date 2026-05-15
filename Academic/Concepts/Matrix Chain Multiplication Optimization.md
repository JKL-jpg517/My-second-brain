>[!Homework] an introduction problem
>![introduction-to-linear-algebra-6nbsped-1733146679-9781733146678_compress, p.37](Academic/Sources/数学/教辅/introduction-to-linear-algebra-6nbsped-1733146679-9781733146678_compress.pdf#page=47&rect=73,58,474,102)
>M1 :32 M2 :18 (two multipications add them up respectively)
>**Key Insight**
    >在 $A(BC)$ 的路径中，因为 $C$ 是一个极窄的矩阵（向量），你先让 $B$ 和 $C$ 乘，相当于**第一时间把数据“降维”压扁成了一个向量**。随后 $A$ 再乘以这个向量，整个过程都是“矩阵乘向量”，这是非常轻量级的操作。
    >在 $(AB)C$ 的路径中，你先让 $A$ 和 $B$ 两个“胖子”硬碰硬，做了一次高昂的“矩阵乘矩阵”操作， 生成了一个更大的中间矩阵，最后才去乘那个小向量 $C$。这种做法没有利用到 $C$ 很窄的优势，白白浪费了算力。
    >The same results to a m$\times$n matrix  but may be m-->p--->n or m--->(p+100)-->n
    
    
