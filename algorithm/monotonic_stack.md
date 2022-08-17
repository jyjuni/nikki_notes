# 单调栈



**单调栈**是对于数组中的*范围查询*(range query)问题的最佳时间复杂度解决方案。 因为数组中的每个元素只入栈一次，所以时间复杂度是O(N)，N 表示数组的长度。

使用单调栈来维护范围可以节省大量时间。 单调堆栈可以维护范围内的最大/最小元素，同时保持范围内元素的顺序。 因此，我们不再需要一一比较元素来得到范围内的最大/最小值，避免了对现有元素的重复操作。 同时，由于它保留了元素顺序，我们只需要根据最新添加的元素更新堆栈。	

适合用单调栈解决的问题：

1. 数组中的**范围查询**问题
2. **单调性：**范围内元素的最小值/最大值元素，或元素的单调性顺序对于查询很有用。
3. **一次性使用：**每个元素只使用一次（出栈后不会再入栈）。

## 例题

 [768. 最多能完成排序的块 II](https://leetcode.cn/problems/max-chunks-to-make-sorted-ii/) 

上述分析过程中，我们只用到了块的最大值来进行比较，比较过程又是从右到左，符合栈的思想，因此可以用类似单调栈的数据结构来存储块的最大值。

 [84. 柱状图中最大的矩形](https://leetcode.cn/problems/largest-rectangle-in-histogram/) 

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ret = 0
        mono_stack = [] #heights[i]单调递增
        heights.append(0)
        for i, v in enumerate(heights):
            while mono_stack and heights[mono_stack[-1]] > v:
                height = heights[mono_stack.pop()]
                # 对于每一个height, 求length即找到左右两侧最近的高度小于 height 的柱子
                # 左边界：d[-1]或0
                # 右边界：i-1
                if mono_stack: 
                  	#以height为高度的区间，d[-1]+1...i-1都是可以构成底的宽度
                    length = i-1 - mono_stack[-1] 
                else:
                  	#以height为高度的区间，前面都是比height高的（已经早被弹出了），0...i-1都是可以构成底的宽度
                    length = i #以height为高度的区间
                ret = max(ret, height * length)
            mono_stack.append(i)
        return ret
```

和84相似：

 [42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/) 

相比#84需要额外比较左右两个边界柱子的高度，取较小值。

```python
# 单调栈：按层叠加
class Solution:
    def trap(self, height: List[int]) -> int:
        d = deque([]) #存储i，对应height[i]严格递减
        total = 0
        for i, h in enumerate(height):
            if not d or height[d[-1]] > h: #更小直接加
                d.append(i)
            else:
                while d and height[d[-1]] < h:
                    h0 = height[d.pop()] #base height
                    # 对于每一个h0,找最大的length即找最左和最右的端点（高度大于h0的柱子）
                    # 最左：d[-1]+1
                    # 最右：i-1
                    if d: #如果d为空说明左边没有承接的柱子了，不会增加，直接跳过
                        l = i-1 - d[-1]
                        h1 = min(height[d[-1]], height[i]) #取左右两条边中更短的
                        total += (h1 - h0) * l
                
                # 现在d中都比h[i]大
                d.append(i)
                
        return total
```



## 参考

 [Algorithms for Interview 2: Monoztonic Stack | by Yang Zhou | TechToFreedom | Medium](https://medium.com/techtofreedom/algorithms-for-interview-2-monotonic-stack-462251689da8) 
