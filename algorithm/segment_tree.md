# 线段树 
## Template

[reference](https://lfool.github.io/LFool-Notes/algorithm/%E7%BA%BF%E6%AE%B5%E6%A0%91%E8%AF%A6%E8%A7%A3.html)

```python
class SegmentTree:
	def __init__(self, l):
		self.l = l
		N = len(l)
		self.sum = [0] * (N<<2)
		self.lazy = [0] * (N<<2)
		self.update = [-float('inf')] * (N<<2)

	def pushUp(self, rt):
		self.sum[rt] = self.sum[rt<<1] + self.sum[rt<<1|1]

	def pushDown(self, rt, ln, rn):
		sub_l, sub_r = rt<<1, rt<<1|1
		if self.update[rt] > -float('inf'): #父节点下发update到左右子树
			# update重置
			self.update[sub_l] = self.update[rt]
			self.update[sub_r] = self.update[rt]
			# lazy重置
			self.lazy[sub_l] = 0
			self.lazy[sub_r] = 0
			# sum重置
			self.sum[sub_l] = ln * self.update[rt]
			self.sum[sub_r] = ln * self.update[rt]
			# 父节点解放了
			self.update[rt] = -float('inf')

		if self.lazy[rt]: #父节点下发lazy任务到左右子树
			# lazy叠加
			self.lazy[sub_l] += self.lazy[rt]	
			self.lazy[sub_r] += self.lazy[rt]	
			# sum叠加
			self.sum[sub_l] += ln * self.lazy[rt]	
			self.sum[sub_r] += rn * self.lazy[rt]	
			# 父节点解放了
			self.lazy[rt] = 0

	def add(self, l, r, rt, task_l, task_r, val):
		# 覆盖本节点全部范围，更新lazy和sum
		if task_l <= l and task_r >= r: #cover completely
			self.lazy[rt] += val
			self.sum[rt] += val * (r - l + 1)
		else: #不覆盖，先懒传播再下放
		mid = (l + r) >> 1
		# [l, mid], [mid+1, r]
		# lazy propagate 
		self.pushDown(t, mid-l+1, r-mid)	
		# 下放左右节点
		if task_l <= mid:
			self.add(l, mid, rt<<1, task_l, task_r, val)

		if task_r > mid:
			self.add(mid+1, r, rt<<1|1, task_l, task_r, val)
		
		# 回收
		self.pushUp(rt)
		
		pass

	def update(self, l, r, rt, task_l, task_r, val):
		# 完全覆盖本节点全部范围
		if task_l <= l and task_r >= r:
			self.update[rt] = val
			self.sum[rt] = (r-l+1) * val
			self.lazy[rt] = 0
		else:
			# propagate 
			self.pushDown(t, mid-l+1, r-mid)	
				
			# 下放左右节点
			if task_l <= mid:
				self.update(l, mid, rt<<1, task_l, task_r, val)

			if task_r > mid:
				self.update(mid+1, r, rt<<1|1, task_l, task_r, val)
			
			# 回收
			self.pushUp(rt)
		pass

	def query(self, l, r, rt, task_l, task_r):
		# 覆盖本节点全部范围
		if task_l <= l and task_r >= r:
			return self.sum[rt]
		else:
			# propagate 
			self.pushDown(t, mid-l+1, r-mid)	

			res = 0
			# 下放左右节点
			if task_l <= mid:
				res += self.query(l, mid, rt<<1, task_l, task_r)

			if task_r > mid:
				res += self.query(mid+1, r, rt<<1|1, task_l, task_r)

			return res
```



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



update:

完全覆盖

lazy: lazy清空

sum直接变为新的值

不完全覆盖

- 之前的懒任务下发
- 更新任务如果和左边有关就发给左边
- 更新任务如果和右边有关就发给右边

分发：

父节点先发update，再发lazy（按照任务顺序：未被清空的lazy一定是在update后的任务）；最后汇总sum

更新：

如果父范围有更新，子范围的lazy清空，更新被覆盖，sum累加；最后重置父范围的更新。

lazy：

如果大范围有lazy，子范围

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
