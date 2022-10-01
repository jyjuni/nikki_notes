# 巧妙解法

#### 巧用str.count

 [1408. 数组中的字符串匹配](https://leetcode.cn/problems/string-matching-in-an-array/) 

题目求`words`数组 中是其他单词的subword的所有单词。

常规解法是暴力遍历筛查。

一种巧妙的解法是把字符串数组串联成单个长字符串，用str.count()找出出现过一次以上的字符串。注意单词之间使用空格（或其他占位符）连接，避免数到跨单词的pattern。

```python
# 模拟
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s = " ".join(words) #避免跨单词的subwords
        return [subword for subword in words if s.count(subword)>1]
      ## 常规解法：暴力遍历
      # return [s for s in words if any(o for o in words if s!=o and s in o)]

```



#### 哈希的哈希

**note：**维护哈希表的哈希表（即d.values()的出现频率）其实非常简单，可以在建哈希表同时进行，只需要额外常数复杂度。

 [1224. 最大相等频率](https://leetcode.cn/problems/maximum-equal-frequency/) 

可以通过*找规律*:cry: 推出满足条件的前缀(即d.values())分布有三种情况：

1. [1,1,1,1] 全部是1

2. [3,3,3,1] 最小为1，剩下的都是x

3. [3,2,2,2] 最大为x+1, 其他为x

除了不重、不漏地找出所有合法情况以外，本题的难点在于快速判断当前频率是否属于情况2或情况3。这里使用了一个trick：利用目前前缀长度l==sum(d.values())的特点，维护每个频率出现的次数cnt，就可以列出判断等式：

情况1：`max_freq == 1`

情况2：`l == max_freq * cnt[max_freq] +1`

情况3：`l == max_freq + cnt[max_freq-1] * (max_freq-1)`

```python
# 哈希表+哈希表的哈希表
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        d = defaultdict(int)
        cnt = defaultdict(int)
        max_freq = 0
        max_len = 1
        for l, num in enumerate(nums, start=1):
            d[num] += 1
            max_freq = max(max_freq, d[num])
            # 维护d.values().count的哈希表
            cnt[d[num]] += 1
            cnt[d[num]-1] -= 1

            # 情况1: [1,1,1,1] 全部是1
            if max_freq == 1:
                max_len = max(max_len, l)
            # 情况2: [3,3,3,1] 最小为1，剩下的都是x 
            # 或情况3: [3,2,2,2] 最大为x+1, 其他为x
            elif l == 1 + max_freq * cnt[max_freq] or l == max_freq + cnt[max_freq-1] * (max_freq-1):
                max_len = max(max_len, l)
                
        return max_len
```

