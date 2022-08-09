# 巧妙解法

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

