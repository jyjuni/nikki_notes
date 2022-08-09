# DFS

## 图+DFS
200(岛屿问题) 46（全排列） 37（解数独）

## 回溯
不剪枝的回溯就是dfs，详见 [dsf与回溯](https://leetcode.cn/leetbook/read/dfs/nj8h1e/)

### 子集(Combination)和排序(Permutation)

子集(90)<->全排序(47)
区别：全排序要每一种顺序组合(permutation)，后面数可以小于前面，子集只要一种顺序(combination)，因此子集需要先排序，且后面数不能小于前面数（因此不用原地置换，直接从当前值val第一个出现位置开始搜索后面的就可以）

[90. 子集 II](https://leetcode.cn/problems/subsets-ii/) 

[47. 全排列 II](https://leetcode.cn/problems/permutations-ii/) 



## 例题

[623. 在二叉树中增加一行](https://leetcode.cn/problems/add-one-row-to-tree/)  

51 （n皇后）47（全排列II）39 77 78 （子集I）

## Reference

[总结回溯问题类型](https://leetcode.cn/problems/subsets/solution/c-zong-jie-liao-hui-su-wen-ti-lei-xing-dai-ni-gao-/) 