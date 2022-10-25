# 子数组与子序列
***子数组(subarray)***：
> 必须连续, 例：[53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/)

***子序列(subsequence)***：
> 可以不连续, 例：[300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)


# 子数组问题

## 解法1：前缀和（动态规划）
[560. 和为 K 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/)
```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int) 
        d[0] = 1 #sum:count
        s, count = 0, 0
        for i in range(1, len(nums)+1):
            s += nums[i-1]
            if s-k in d: #s-(s-k) = k, [j...]i区间和为k
                count += d[s-k] #不重不漏：加以nums[i-1]结尾的合法区间个数
            d[s] += 1

        return count
```
[cite](https://lfool.github.io/LFool-Notes/algorithm/%E7%A7%92%E6%9D%80%E5%AD%90%E6%95%B0%E7%BB%84%E7%B1%BB%E9%A2%98%E7%9B%AE.html )

## 解法2：动态规划

[53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/)
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        dp = 0 # only care about dp[0]=0 so dp[1] = max(dp[0], dp[0])
        result = nums[0] # b/c: first time compare result with dp[1]
        for i in range(l):
            dp = max(dp+nums[i], nums[i])
            result = max(result, dp)
        return result
```

优化：
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [0 for n in range(l+1)] # only care about dp[0]=0 so dp[1] = max(dp[0], dp[0])
        result = nums[0] # b/c: first time compare result with dp[1]
        for i in range(l):
            dp[i+1] = max(dp[i]+nums[i], nums[i])
            result = max(result, dp[i+1])
        return result
```

## 解法3：滑动窗口
[713. 乘积小于 K 的子数组](https://leetcode.cn/problems/subarray-product-less-than-k/) 

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1: return 0
        i,j = 0, 0
        total = 0
        curProd = 1
        while j<len(nums):
            curProd *= nums[j]
            j += 1

            while curProd >= k: #illegal
                curProd /= nums[i]
                i+=1
            
            #[i...j-1] now legal, update
            total += j-i
        return total
```
[cite](https://lfool.github.io/LFool-Notes/algorithm/%E5%AD%90%E6%95%B0%E7%BB%84%E4%B9%8B%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E7%AF%87.html)
# 子序列问题
**子序列** 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
> 例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

## 最长子序列（LIS）
----
[300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)
### 动态规划：
> dp[i]表示以i结尾（必须包含i）最长子序列长度。 \
> 状态转移方程：
> $$ dp[i] = max(dp[j]), \ j<i \ and \  nums[j]<nums[i] $$
```python
# dp[i]:以i结尾最长子序列长度
# dp[i] = max(dp[j] for j in range(i) if nums[j]<nums[i])
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        max_len = 1
        for i in range(len(nums)):
            prev = [dp[j] for j in range(i) if nums[j]<nums[i]]
            if prev:
                dp[i] = max(prev)+1
                max_len = max(max_len, dp[i])
        return max_len

```
### 动态规划+二分查找

> 我们希望每个靠前的值尽量小，来给后面值留出空间，比如：2,3,7优于2,3,101，因此遍历时替换第一个比当前值大的值，这样在不影响当前子序列长度的情况下优化了序列；如果比所有当前值大，则直接加在队尾（长度加一）。

```python
# dp是严格递增的单调队列，遍历nums替换第一个比num大的值，比所有都大就加到队尾。
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            if not dp or dp[-1] < num:
                dp.append(num)
            else:
                i = bisect.bisect_left(dp, num) # 第一个>=dp的数
                # 注意这里不能用bisect_right, 是因为出现末尾等于num的情况会index溢出
                dp[i] = num
        return len(dp)
```
## 最长公共子序列（LCS）
### 二维动态规划
[1143. 最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/)
> $dp[i][j]$表示$text1[:i], text2[:j]$的最长公共子序列长度，不一定包含$i$.
> $$
> dp[i][j] = 
> \begin{cases}
> dp[i-1][j-1]+1 & \quad if \ text1[i-1]==text2[j-1] \\
> max(dp[i-1][j], dp[i][j-1]) & \quad if \ text1[i-1]!=text2[j-1]
> \end{cases}
> $$

> 注意：可以选择dp[i][j]表示 \
> (1)text1[:i]:前i个。\
> (2)text1[...i]:到i为止。\
> 表示(1)需要注意dp长度为n+1(0表示没有字符)，且从1开始遍历; 表示(2)需要处理dp[i-1][j-1]和类似的index溢出情况。这里优先选择(1)表示方法，更简洁。

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1)+1, len(text2)+1
        dp = [[0] * n2 for _ in range(n1)]
        for i in range(1, n1):
            for j in range(1, n2):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
```