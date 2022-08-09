# 线段树 
## Template

[reference](https://lfool.github.io/LFool-Notes/algorithm/%E7%BA%BF%E6%AE%B5%E6%A0%91%E8%AF%A6%E8%A7%A3.html)

### **lazy propagation+动态开点**

```python
class Node:
    def __init__(self, val=0):
        self.left = None
        self.right = None
        self.val = val
        self.add = 0
    
class SegmentTreeDynamic: #直接用指定class覆盖

    def __init__(self):
        self.N = 0
        self.root = Node(0)
       
   	# def XXX(self, start, end):
    #     if self.query(self.root, 0, self.N, (start, end-1)) >= 2:
    #         return False
    #     self.update(self.root, 0, self.N, (start, end-1), 1)
    #     return True
    
    ## *******************TEMPLATE START*******************
    def update(self, node, start, end, update_range, val):
        
        # [start, end] included completely in update range
        # so stop and update lazily
        if update_range[0]<= start and end <= update_range[1]:
            # CHECK1: update method
            node.val += (end-start+1) * val
            node.add += val
            return

        mid = (start+end)//2
        # left: [start, mid]
        # right: [mid+1, end]
        leftNum = mid-start+1
        rightNum = end-mid
        print(start, end, leftNum, rightNum)
        
        # lazy propagation
        self.propagate(node, leftNum, rightNum)
        
        # update left child recursively
        if update_range[0] <= mid: #[start,mid] and [update_l, update_r] overlaps    
           self.update(node.left, start, mid, update_range, val)
        
        # update right child recursively
        if update_range[1] >= mid+1:
           self.update(node.right, mid+1, end, update_range, val)
        
        ## CHECK2: aggregate method
        node.val = node.left.val + node.right.val
        
    def query(self, node, start, end, query_range):
        
        # [start, end] included completely in query range
        if query_range[0] <= start and end <= query_range[1]:
            return node.val
        
        ans = 0
        mid = (start + end)//2
        # left: [start, mid]
        # right: [mid+1, end]
        leftNum = mid-start+1
        rightNum = end-mid
        
        self.propagate(node, leftNum, rightNum)
        
        # query left child recursively
        if query_range[0] <= mid: #[start,mid] and [update_l, update_r] overlaps  
            ## CHECK3: aggregate method
            ans += self.query(node.left, start, mid, query_range)
        
        # query right child recursively
        if query_range[1] >= mid+1:
  
            ## CHECK4: aggregate method
            ans += self.query(node.right, mid+1, end, query_range)
        
        return ans
        
    
    def propagate(self, node, leftNum, rightNum):
        if not node.left:
            node.left = Node()
        
        if not node.right:
            node.right = Node()
        
        # nothing to propagate
        if not node.add:
            return
        
        ## CHECK5: aggregate method决定是否*左右子节点数(加减要*，max不*)
        node.left.val += leftNum * node.add
        node.right.val += rightNum * node.add
        
        ## CHECK6: update method决定累加(减)/覆盖
        node.left.add += node.add
        node.right.add += node.add

        # clear lazy add
        node.add = 0
        
    ## *******************TEMPLATE END*******************

```



## 例题

### 我的日程安排表I~III

[729. 我的日程安排表 I](https://leetcode.cn/problems/my-calendar-i/)

[731. 我的日程安排表 II](https://leetcode.cn/problems/my-calendar-ii/)

[732. 我的日程安排表 III](https://leetcode.cn/problems/my-calendar-iii/)

### 区域和检索（数组不可变、数组可变、二维可变）

[303. 区域和检索 - 数组不可变](https://leetcode.cn/problems/range-sum-query-immutable/) 

[307. 区域和检索 - 数组可修改](https://leetcode.cn/problems/range-sum-query-mutable/)

[308. 二维区域和检索 - 可变](https://leetcode.cn/problems/range-sum-query-2d-mutable/) 

### 其他

[715. Range 模块](https://leetcode.cn/problems/range-module/)

[933. 最近的请求次数](https://leetcode.cn/problems/number-of-recent-calls/)

[699. 掉落的方块](https://leetcode.cn/problems/falling-squares/)