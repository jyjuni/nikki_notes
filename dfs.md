# DFS

## 图+DFS
200(岛屿问题) 46（全排列） 37（解数独）
1.并查集：
https://leetcode-cn.com/problems/number-of-provinces/solution/python-duo-tu-xiang-jie-bing-cha-ji-by-m-vjdr/ 

## 回溯
51 （n皇后）47（全排列II）39 77 78 （子集I）
dsf与回溯：
https://leetcode-cn.com/leetbook/read/dfs/e3eqfs/ 

## 回溯总结：
不剪枝的回溯就是dfs
https://leetcode-cn.com/problems/subsets/solution/c-zong-jie-liao-hui-su-wen-ti-lei-xing-dai-ni-gao-/ 
子集(90)<->全排序(47)
区别：全排序要每一种顺序组合(permutation)，后面数可以小于前面，子集只要一种顺序(combination)，因此子集需要先排序，且后面数不能小于前面数（因此不用原地置换，直接从当前值val第一个出现位置开始搜索后面的就可以）