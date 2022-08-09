# 并查集(Union-Find/Disjoint-set)

## 原理

并查集是一种特殊数据结构，用于解决图的连通性问题。

并查集维护了一个不相交的动态集的集合$S_1, S_2, ..., S_n$ ，每个连通集合的所有成员拥有共同的root节点，我们不关心集合的哪个成员为root：在开始时，让每个节点构成一个单的集合，然后按一定顺序将属于同一集合的元素合并。


顾名思义，并查集主要就是实现union和find两个函数，具体地：

​	**`__init__(n)`: 初始化，此时每个节点互不连通**

​	**`union(p,q)`: 将p和q连通**

​	**`find(p)`: 返回p的root节点**



### 数据结构

**<u>连通</u>**：如果p和q拥有相同的root节点，则p和q相互连通。方便起见，我们不维护每个元素的root，而维护其父节点，使用find函数查找root。

使用数组`parent[]`维护元素的**父节点**。

判断是否为root节点：

- 如果自己就是根节点，那么`parent[x]==x`
- 如果自己不是根节点，那么`parent[x]==root_id`



### Union

连通p和q：将其中一个的根节点指向另一个的根节点。

```python
def union(p,q):
    """cnnect p,q"""  
    # find roots
    rootP = find(p)
    rootQ = find(q)
		if rootP == rootQ:
        return
    # connect one's root to the other root
    parent[rootP] = rootQ
```

优化：[按秩合并](###按秩合并)

### Find

查找根节点：根节点的特点是自己是自己的parent。因此我们只需递归地找，直到parent指向自己。

```python
def find(x):
    """find root"""
    # iterate until x is the parent of itself
    while parent[x] != x: # not root
      	x = parent[x]
    return x
```

优化：[路径压缩](###路径压缩)



### 瓶颈分析

分析上述实现的方法，`find()`是决定并查集时间复杂度的重要因素。抛开`find()`因素，其他方法的时间复杂度均可视为`O(1)`。所以如果要优化算法的时间复杂度，需要从`find()`入手

- 最坏情况：链表 (`O(n)`)
- 最好情况：n - 1 叉树 (`O(1)`)



## 优化

### 按秩合并

思路：使用`rank[]`维护每个连通分量的树的深度，每次将深度小的合并到深度大的。

```python
def union(self, p, q):
    rootP, rootQ = self.find(p), self.find(q)
    if rootP == rootQ:
        return
    # 深度小的root接在深度大的root下
    if self.rank[rootP] > self.rank[rootQ]:
        self.parent[rootQ] = rootP
    elif self.rank[rootP] < self.rank[rootQ]:
        self.parent[rootP] = rootQ
    else: #深度相同
        self.parent[rootP] = rootQ
        self.rank[rootP] += 1
```



### 路径压缩

思路：使树高始终保持为常数，向上迭代遍历，依次把root直接作为parent。

```python
def find(x):
    if parent[x] != x: # not root
      	parent[x] = find(parent[x])
    return parent[x]
```

使用上面的递归，可以直接把链表拉平成n-1叉树~

- 可以结合使用
- 「路径压缩优化」比「平衡性优化（按秩合并）」更为常用；但当使用了「路径压缩优化」后，「平衡性优化（按秩合并）」也可以不使用。

- 但是可以在某些题目中使用「平衡性优化（按秩合并）」的思想，**如 [最长连续序列](https://leetcode-cn.com/problems/longest-consecutive-sequence/)**



### 时间复杂度

同时使用路径压缩和按秩合并优化的并查集，每个查询和合并操作的平均（和最坏）时间复杂度仅为$O(\alpha (n))$，$\alpha$是[反阿克曼函数](https://zh.m.wikipedia.org/zh-hans/%E9%98%BF%E5%85%8B%E6%9B%BC%E5%87%BD%E6%95%B8)。

> 由于阿克曼函数$A$增加极度迅速，所以$\alpha$ 增长极度缓慢，对于任何在实践中有意义的元素数目n，$\alpha(n)$均小于5。
>
> 因此，也可以粗略地认为，并查集的操作有*常数*的时间复杂度。



## Template

按秩合并+路径压缩：

```python
class UnionFind:  
    def __init__(self, n):
        self.parent = range(n)
        self.rank = [1] * n
    
    def find(self, x):
        """find root (with path compression)"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, p, q):
        """cnnect p,q (with union by rank)"""  
        rootP, rootQ = self.find(p), self.find(q)
        if rootP == rootQ:
            return
        # 深度小的root接在深度大的root下
        if self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        elif self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        else: #深度相同
            self.parent[rootP] = rootQ
            self.rank[rootP] += 1
```

 [UnionFind.py](../code/UnionFind.py) 



## 例题

[990. 等式方程的可满足性](https://leetcode-cn.com/problems/satisfiability-of-equality-equations/)

[130. 被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/)

[128. 最长连续序列](https://leetcode-cn.com/problems/longest-consecutive-sequence/)

[952. 按公因数计算最大组件大小](https://leetcode.cn/problems/largest-component-size-by-common-factor/) 

[547. 省份数量](https://leetcode.cn/problems/number-of-provinces/) 

[[Python/C++/Java] 多图详解并查集 - 省份数量 - 力扣（LeetCode）](https://leetcode.cn/problems/number-of-provinces/solution/python-duo-tu-xiang-jie-bing-cha-ji-by-m-vjdr/) 



## Reference

[Lfool's Notes](https://lfool.github.io/LFool-Notes/algorithm/%E5%B9%B6%E6%9F%A5%E9%9B%86-Union-Find.html) 

[GeeksforGeeks](https://www.geeksforgeeks.org/disjoint-set-data-structures/) 

[并查集各种情况下的时间复杂度](http://t.zoukankan.com/FengZeng666-p-14447989.html) 

[wikipedia](https://zh.m.wikipedia.org/zh-hans/%E5%B9%B6%E6%9F%A5%E9%9B%86)  

