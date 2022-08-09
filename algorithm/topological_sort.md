# 拓扑排序

拓扑排序（Topological Sorting）是一种应用在「有向无环图（DAG，Directed Acyclic Graph）」上，给出结点输出先后顺序的算法。这些结点的输出顺序需要保证：

- 每一个结点输出且仅输出一次；
- 在有向无环图中，如果存在一条从 u 到 v 的路径，那么在拓扑排序的结果中，u 必需保证在 v 的前面。

Notes：

- 拓扑排序应用于 **有向图** 检测是否有环，**有向无环图才存在拓扑序**；

- 拓扑序结果不唯一；

- 拓扑排序的典型实现是「广度优先遍历」，使用「入度数组」和「队列」帮助实现；

> 任何 DAG 具有至少一个拓扑排序，存在算法用于在<u>**线性**</u>时间内构建任何 DAG 的拓扑排序。



## Template

```python
1. 遍历每条边，构建入度表和邻接表
2. bfs建图
```



## 例题

[207. 课程表](https://leetcode.cn/problems/course-schedule/)

本质上是判断有向图是否有环，采用常规拓扑排序template。因为只需要判断是否有环，bfs中每次取出入度为0的元素（即可以上的课），取尽后如果有剩余入度不为0的元素则有环。

```python
# 拓扑排序
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 构建入度表和邻接表
        in_degrees = [0] * numCourses #indegrees[i] - (i-1)th course
        adj = defaultdict(list)
        
        for p in prerequisites:
            in_degrees[p[0]] += 1
            adj[p[1]].append(p[0])
        # print(p, adj)

        # BFS建图，每次取入度为0的一个
        q = deque([i for i,v in enumerate(in_degrees) if v==0]) #入度为0的课
        while q:
            c = q.popleft()
            numCourses -= 1
            for next_c in adj[c]:
                in_degrees[next_c] -= 1
                if in_degrees[next_c] == 0:
                    q.append(next_c)
        
        #入度为0的取尽，还没上完所有课则返回False，上完为True
        return numCourses==0
```



[210. 课程表 II](https://leetcode.cn/problems/course-schedule-ii/) 

和课程表I类似，bfs记录一个result数组，返回即可：

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 构建入度表和邻接表
        in_degrees = [0] * numCourses #indegrees[i] - (i-1)th course
        adj = defaultdict(list)
        
        for p in prerequisites:
            in_degrees[p[0]] += 1
            adj[p[1]].append(p[0])
        # print(p, adj)

        # BFS建图，每次取入度为0的一个
        result = []
        q = deque([i for i,v in enumerate(in_degrees) if v==0]) #入度为0的课
        while q:
            c = q.popleft()
            numCourses -= 1
            result.append(c)
            for next_c in adj[c]:
                in_degrees[next_c] -= 1
                if in_degrees[next_c] == 0:
                    q.append(next_c)
        
        #入度为0的取尽，还没上完所有课则返回False，上完为True
        return result if numCourses==0 else []
```


[444. 序列重建](https://leetcode.cn/problems/sequence-reconstruction/)  [(剑指 Offer II 115. 重建序列)](https://leetcode.cn/problems/ur2n8P/) 

```python
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        # 1. 遍历每条边，构建入度表和邻接表
        # 入度表
        d_in = [0] * (n+1)
				# 邻接表
        adj = defaultdict(list)
        for s in sequences:
            for i, j in pairwise(s):
                d_in[j] += 1
                adj[i].append(j)
        
        print(d_in)

        # 2. bfs建图
        q = deque([i for i in range(1,n+1) if d_in[i]==0])
        while q:
            if len(q)>1:
                return False    
            cur = q.popleft()
            for next in adj[cur]:
                d_in[next] -= 1
                if d_in[next] == 0:
                    q.append(next)

        return True
```



[310. 最小高度树](https://leetcode.cn/problems/minimum-height-trees/) 

[1136. 并行课程](https://leetcode.cn/problems/parallel-courses/) 

[269. 火星词典](https://leetcode.cn/problems/alien-dictionary/) 



[1857. 有向图中最大颜色值](https://leetcode.cn/problems/largest-color-value-in-a-directed-graph/)  

[1591. 奇怪的打印机 II](https://leetcode.cn/problems/strange-printer-ii/) 

[1203. 项目管理](https://leetcode.cn/problems/sort-items-by-groups-respecting-dependencies/) 



