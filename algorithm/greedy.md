# 贪心算法

## 原理

1. 实现一个最原始的暴力解法X
2. 脑补多个贪心策略（如果找到确定是最优策略可以直接实现）
3. 对于每个贪心策略，用暴力解法X检测哪个是最优贪心策略

*在做笔试时不要试图证明哪个策略是最优的，因为没有时间纠结。*

比较常用的方法

1. 排序
2. 堆

## 贪心策略

### 哈夫曼树

 [Huffman Coding | Greedy Algo-3 - GeeksforGeeks](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/) 

哈夫曼树是WPL最小的二叉树

> **<u>WPL(Weighted Path Length):</u>** 树的带权路径长度，即所有叶子结点的**带权路径长度**之和
>
> **<u>结点的带权路径</u>** = 路径长度*节点的权

例: [切金条](###切金条的代价)

## 例题

##### 加油问题

 [Greedy Algorithms — The Car Fueling Problem | by Ayran Olckers | Medium](https://medium.com/@TheGeekiestOne/greedy-algorithms-the-car-fueling-problem-a35ccc9bb011) 

##### 戳气球问题

[435. 无重叠区间](https://leetcode.cn/problems/non-overlapping-intervals/) 

[452. 用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/) 

[757. 设置交集大小至少为2](https://leetcode.cn/problems/set-intersection-size-at-least-two/) 

##### 相关：会议室问题

[253. 会议室 II](https://leetcode.cn/problems/meeting-rooms-ii/)

##### 切金条的代价

解法：哈夫曼树

