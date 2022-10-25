# 排序算法


## 快速排序
快排1.0：每次分为<=和>，每次可以确定中间一个

快排2.0（荷兰国旗问题）：每次分为<，=和>，可以确定中间全部相等的

时间复杂度：$O(N^2)$，最差情况按顺序排列，每次partition出的两个数组一边是0，一边是n-1。

优化：pivot使用随机数，最差情况的期望值为NlogN级别。

时间复杂度：O(NlogN)

### 分治法（partition）

奇数放在数组左边，偶数放在数组右边，还要求原始的相对次序不变（稳定）。0-1 stable sort和快排是等效的：快排分为<=和>，奇偶分为奇数和偶数，都是0-1状态。最好的情况能做到稳定，O(NlogN),O(logN)。



### 实现

```python
# 快速排序
import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(nums, start, end):
            if start >= end:
                return 
            i = partition(nums, start, end)
            quickSort(nums, start, i-1)
            quickSort(nums, i+1, end)
            return

        def partition(nums, start, end):
            ra = random.randint(start,end)
            nums[start], nums[ra] = nums[ra], nums[start]
            pivot = nums[start]
            l, r = start, end
            while l<r:
                while l<r and nums[r]>= pivot:
                    r-=1
                while l<r and nums[l]<= pivot:
                    l+=1
                nums[l], nums[r] = nums[r], nums[l]
                # print(nums, nums[l], nums[r])
            nums[start], nums[l] = nums[l], nums[start]
            # print(start, end, nums[start:end+1])
            return l


        quickSort(nums, 0, len(nums)-1)
        return nums
```



## 归并排序

### 实现

```python
# 归并排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(l, r):
            if l >= r:
                return
            m = (l+r)//2
            mergeSort(l, m)
            mergeSort(m+1, r)
            merge(l, m, r)
            # print(nums)
            return

        def merge(l, m, r):
            #first [l...m], second [m+1...r]
            tmp1, tmp2 = nums[l:m+1], nums[m+1:r+1] 
            i, j = 0, 0 #index for tmp1, tmp2
            for k in range(l, r+1):
                if i == len(tmp1): #nums1 depleted
                    nums[k] = tmp2[j]
                    j+=1
                elif j == len(tmp2): #nums2 depleted
                    nums[k] = tmp1[i]
                    i+=1
                elif tmp1[i] < tmp2[j]: #append smaller: num1
                    nums[k] = tmp1[i]
                    i+=1
                else: 
                    nums[k] = tmp2[j]
                    j+=1
            return 

        mergeSort(0, len(nums)-1)
        return nums
```



### 归并法扩展（递归）

在归并的基础上，通过改变归并排序的merge操作，记录需要的信息，达到O(NlogN)复杂度的计算。

**小和问题**

>  在一个数组中，在每一个数左侧比当前数小的数累加和，叫做这个数组的小和。给定一个数组，求数组的小和。

[315. 计算右侧小于当前元素的个数 - 力扣（LeetCode）](https://leetcode.cn/problems/count-of-smaller-numbers-after-self/) 

merge时：

- 只有在左边指向数小（拷贝左侧）时加`(r+1-p2)`个小数和，挪右侧则不用加
  - 利用右侧数组下标位置可以计算有几个更大的数，不用遍历右侧数组；

- 左右相等时保证右组先拷贝（因为要计算右侧有多少元素**严格大于**左侧元素，如果右侧有相等则不应该计入小和个数，快速跳过不影响左边）

return：左半小和总数+ 右半小和总数 + 当前merge小和总数

不重不漏：只有合并时会产生以a为base的小和，一旦合并就变成了一个数组内了，数组内不会再计算小和

**逆序对问题**

[315. 计算右侧小于当前元素的个数](https://leetcode.cn/problems/count-of-smaller-numbers-after-self/) 

>  在一个数组中，左边的数如果比右边的数大，则这两个数构成一个逆序对。打印所有逆序对。

和小和问题思路类似：小和求的是右侧比左侧大的个数，逆序对求的是右侧比左侧小的个数。merge时如果右侧<左侧则累加个数，相等时左侧先加（因为算p2-l，需要保证当前位置和它前边不包含相等值）。 

### 

## 不基于比较的排序

### 桶排序

#614

将待排序元素划分到不同的桶。先扫描一遍序列求出最大值 maxV 和最小值 minV ，设桶的个数为 k ，则把区间 [minV, maxV] 均匀划分成 k 个区间，每个区间就是一个桶。将序列中的元素分配到各自的桶。

### 计数排序

计数排序本质上是一种特殊的桶排序，当桶的个数最大的时候（maxValue-minValue+1），就是计数排序。

举例：公司员工年龄排序统计

时间复杂度：O(N)

局限性：需要知道数据分布状况，且数据范围有限制

### 基数排序

先根据个位数字排序，再根据十位排序，再根据百位排序...

从低位到高位，因为高位是最后排序的，所以优先级高。

- 相比计数排序：节省桶数（十进制-10个桶）
- 有多少位就进出几次：最大值的十进制位数 = 所有数字入桶出桶的次数

实现

<img src="sort.assets/Screen Shot 2022-10-14 at 12.37.41 AM.png" alt="Screen Shot 2022-10-14 at 12.37.41 AM" style="zoom:50%;" />

- 优化：词频表的前缀和+辅助数组
  - 原数组从右往左，根据词频前缀和-1输出到辅助数组的对应位置
  - 巧妙的利用了先进先出原则

## 堆排序

见[堆实现](heap.md###堆实现)。

## 总结

工程上对排序的改进

1. 充分利用$O(logN)$ 和 $O(N^2)$排序各自的优势

   - 样本量小(<60)，插入排序快

   - 大样本量，快排

   - 小样本量，直接插入排序

2. 稳定性的考虑  

   - 基础类型 - 稳定性没用，快排

   - 非基础类型 - 可能需要稳定，归并

## 例题

##### TopK

 [215. 数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/) 

##### 排序链表

 [148. 排序链表](https://leetcode.cn/problems/sort-list/) 

##### 其他例题

169 274

