

# BFS

广度优先遍历 (BFS) 呈现出「一层一层向外扩张」的特点，**先看到的结点先遍历，后看到的结点后遍历**，因此「广度优先遍历」可以借助「队列」实现。

**说明**：遍历到一个结点时，如果这个结点有左（右）孩子结点，依次将它们加入队列。

<img src="bfs.assets/BFS-and-DFS-Algorithms.png" alt="fbfs" style="zoom:75%;" />

### 树的bfs遍历

树的广度优先遍历的写法模式相对固定：

- 使用队列；
- 在队列非空的时候，动态取出队首元素；
- 取出队首元素的时候，把队首元素相邻的结点*（非空）*加入队列。
  - 子结点入队的时候，非空的判断很重要：在队列的队首元素出队的时候，一定要在左（右）子结点非空的时候才将左（右）子结点入队。



### 图的bfs搜索

广度优先遍历作用于「无权图」，得到的是「最短路径」。

**note:** 由于图中可能存在环，bfs作用于图论问题的时候，结点在加入队列以后标记为「已经访问」，否则会出现结点重复入队的情况。

**note2**: bfs只用于求解「无权图」的最短路径。如果是带权图，就需要使用相应的专门的算法去解决它们。事实上，这些「专门」的算法的思想也都基于「广度优先遍历」的思想：

- 带权有向图、且所有权重都非负的单源最短路径问题：Dijkstra 算法
- 带权有向图的单源最短路径问题：Bellman-Ford 算法
- 一个图的所有结点对的最短路径问题：Floy-Warshall 算法



### 抽象成图

广度优先遍历作用于「无权图」，得到的是「最短路径」。如果题目有让求「最小」、「最短」、「最少」，可以考虑这个问题是不是可以建立成一个「图形结构」或者「树形结构」，用「广度优先遍历」的思想求得「最小」、「最短」、「最少」的数值；



### 拓扑排序

拓扑排序（Topological Sorting）是一种应用在「有向无环图（DAG，Directed Acyclic Graph）」上，给出结点输出先后顺序的算法。

拓扑排序的典型实现是「广度优先遍历」，使用「入度数组」和「队列」帮助实现；

详见[拓扑排序](topological_sort.md)。



### caveats for bfs
- BFS用queue(deque: append+popleft)，DFS用stack栈(list: append+pop)/回溯（优先，可读性强且不需要考虑栈溢出问题）
- 优先考虑BFS：搜索最短路径，按层搜索
- 不一定需要单独helper函数，除非要调用多次(参考 [130. 被围绕的区域 ](https://leetcode.cn/problems/surrounded-regions/) ）



### 时间复杂度

$O(N)$，这里 $N$ 是二叉树结点的个数



## Template

```python
# 初始化维护变量
max_s = -float('inf')
visited = {}
q = deque([root])

while q:
    # 本层开始
    s = 0

    for _ in range(len(q)): # 分层用，可以省略
        cur = q.popleft()
        # 处理当前节点
        s += cur.val 
        # 添加子节点
        if cur.left:
            if cur.left not in visited: # memorization，可以省略
                q.append(cur.left)
        if cur.right:
            if cur.right not in visited: # memorization，可以省略
                q.append(cur.right)

    # 本层结束
    max_s = max(s, max_s)
    level += 1
```



## 例题

### 树bfs

[919. 完全二叉树插入器](https://leetcode.cn/problems/complete-binary-tree-inserter/) 

**方法1：直接bfs遍历树**

insert每次bfs遍历判断(1)只有左节点则直接加右节点，返回 (2)左右都没有，如果能遍历到叶子节点说明前面都满了，加左节点返回。

insert: O(N)

init, get_root: O(1)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class CBTInserter:
    def __init__(self, root: TreeNode): 
        self.root = root

    def insert(self, val: int) -> int:
        q = deque([self.root])
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left and cur.right:
                    q.append(cur.left)
                    q.append(cur.right)
                elif cur.left and not cur.right:
                    cur.right = TreeNode(val)
                    return cur.val
                else:
                    cur.left = TreeNode(val)
                    return cur.val
        return None


    def get_root(self) -> TreeNode:
        return self.root
```

**优化：一次bfs+队列**

队列 init:O(N), insert和get_root: O(1)

bfs遍历建队列，存储待用的父节点，insert时从队头开始依次加子节点

>  注意如果加了右节点则子节点满了，需要弹出；如果加左节点则node仍留在队头(为叶子层第一个节点，下一次还是它)

```python
class CBTInserter:
    def __init__(self, root: TreeNode): 
        self.root = root
        q = deque([root])
        parents = deque([])
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                else:
                    parents.append(cur)
        # print(parents)
        self.parents = parents
        return None


    def insert(self, val: int) -> int:
        p = self.parents[0]
        cur = TreeNode(val)
        if p.left:
            p.right = cur
            # 如果对队首节点已经有两个子节点，我们需要将其从队列中移除
            self.parents.popleft()
        else:
            p.left = cur
            
        self.parents.append(cur)
        # print(self.parents)
        return p.val


    def get_root(self) -> TreeNode:
        return self.root
```



### 图bfs

 [130. 被围绕的区域 ](https://leetcode.cn/problems/surrounded-regions/) 



### 抽象成图

 [22. 括号生成](https://leetcode.cn/problems/generate-parentheses/)

本题数据范围很小(n<=8)，可以有n多个解法（DFS/BFS/动态规划/位运算）。bfs的思路很直观，在实现中注意分枝条件即可。

```python
# bfs
# 按长度分层，节点表示一种当前可能的合法状态（l<=n and l>=r)；两种前进的可能：
# 1) l < n: 可以加左括号
# 2) r < l: 可以加右括号
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q = deque([""])
        result = []
        while q:
            for _ in range(len(q)):
                s = q.popleft()
                if len(s)==n*2:
                    result.append(s)
                l,r = s.count('('), s.count(')')
                if l<n:
                    q.append(s + '(')
                if r<l:
                    q.append(s + ')')
        return result
```



[1136. 并行课程](https://leetcode.cn/problems/parallel-courses/) 

拓扑排序题，用入度表+bfs。详见



## **reference**

- https://leetcode-cn.com/leetbook/read/bfs/e6occ6/ 

