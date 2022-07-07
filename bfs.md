# BFS
https://leetcode-cn.com/leetbook/read/bfs/e6occ6/ 
例题：树的bfs遍历

130 22 1136
例题：二维搜索bfs、抽象成图bfs问题
## BFS总结：
- BFS用queue(deque: append+popleft)，DFS用stack栈(list: append+pop)/回溯（优先，可读性强且不需要考虑栈溢出问题）
- 优先考虑BFS：搜索最短路径
- 不一定需要单独helper函数，除非要调用多次(参考130）
## 拓扑排序
