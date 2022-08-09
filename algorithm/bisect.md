# 二分搜索

3.4 二分法1
33 34 35

3.5 二分法2
69 162 81

补3.11（二分法练习）: 275 29 74 153

## implementation

1. 二分法收缩区间的**原理**：

   > 一分为二，排除不可能的一半

2. 中间点mid可以跟左边也可以跟右边，如果r=mid则mid=(l+r)//2, 如果l=mid则需要(l+r+1)//2，偶数长度取右中点，防止死循环。
   https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/
   https://leetcode-cn.com/leetbook/read/learning-algorithms-with-leetcode/xsz9zc/ 
   https://suanfa8.com/binary-search/02/ 

## api  

**+bisect:**

`bisect.bisect_left`: 找insert index，相等时insert到左侧

`bisect.bisect_right/bisect.bisect` 找insert index，相等时insert到右侧

**+sortedcontainers.SortedList：**

`a.bisect_left` 找insert index，相等时insert到左侧

`a.bisect_right 找insert index，相等时insert到右侧`

---------

也可以理解为：

> bisect_left: 找第一个>=的位置
> bisect_right: 找第一个>的位置