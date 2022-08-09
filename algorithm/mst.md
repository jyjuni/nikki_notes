# 最小生成树



## 概念

**<u>连通图</u>**：在无向图中，若任意两个顶点$v_i$与$v_j$都有路径相通，则称该无向图为连通图。

**<u>生成树</u>**：无向图 *G* 的**生成树**是具有 *G* 的全部顶点，但边数最少的连通子图

> 一棵生成树含有图中全部n个顶点，有且仅有n-1条边。

**<u>最小生成树</u>**：带权图的生成树中，总权重最小的称为**最小生成树 (Minimum Spanning Tree, or MST)**。



**求取最小生成树的算法**： 

- **Kruskal算法** - 一种贪心算法，复杂度是 $O(E\log {E}) $

- **Prim算法** - 另一种贪心算法，用二叉堆优化时复杂度是 $O(E+V\log {V}) $. 当边数远远大于点数，可近似认为是 $O(E)$.

  

## Kruskal算法

 [Kruskal最小生成树算法](https://lfool.github.io/LFool-Notes/algorithm/Kruskal%E6%9C%80%E5%B0%8F%E7%94%9F%E6%88%90%E6%A0%91%E7%AE%97%E6%B3%95.html) 



## Prim算法

 [Prim最小生成树算法](https://lfool.github.io/LFool-Notes/algorithm/Prim%E6%9C%80%E5%B0%8F%E7%94%9F%E6%88%90%E6%A0%91%E7%AE%97%E6%B3%95.html) 





**参考**

- [生成树 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E7%94%9F%E6%88%90%E6%A0%91) 

- [算法导论--最小生成树（Kruskal和Prim算法）_勿在浮砂筑高台的博客-CSDN博客_最小生成树](https://blog.csdn.net/luoshixian099/article/details/51908175) 