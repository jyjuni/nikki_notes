#!/usr/bin/python
# -*- coding:utf-8 -*-

"""SegmentTreeDynamic.py: 线段树代码template(动态开点)"""

__author__ = "Yijia Jin"
__copyright__ = "Copyright 2022, Yijia Jin"
__version__ = "1.0.0"
__email__ = "yj2682@columbia.edu"


class Node:
    def __init__(self, val=0):
        self.left = None
        self.right = None
        self.val = val
        self.add = 0
    
class SegmentTreeDynamic:

    def __init__(self):
        self.N = 0
        self.root = Node(0)
    
    
    # def someresultfunction(self, start, end):
    #     if self.query(self.root, 0, self.N, (start, end-1)) >= 2:
    #         return False
    #     self.update(self.root, 0, self.N, (start, end-1), 1)
    #     return True
    
    
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
    
# display the binary tree structure
def display(node):
    def display_aux(node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # None node
        if not node:
            return None
        
        # No child.
        if node.right is None and node.left is None:
            line = f'{node.val}'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = display_aux(node.left)
            s = '%s' % node.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = display_aux(node.right)
            s = '%s' % node.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display_aux(node.left)
        right, m, q, y = display_aux(node.right)
        s = '%s' % node.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q) 
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display_aux(node)
    for line in lines:
        print(line)

if __name__ == "__main__":
    
    ## FOR TESTING ONLY
    
    tree = SegmentTreeDynamic()

    start, end = 1,3
    N = 10
    
    # 先查询该区间是否已有值（参考732. 我的日程安排表I）
    if tree.query(tree.root, 0, N, (start, end)) != 0:
        print(f"range overlapped: {(start, end)}")
    else:
        tree.update(tree.root, 0, N, (start, end), 1)
        display(tree.root)
        print(f"query for range {(start, end)}: {tree.query(tree.root, 0, N, (start, end))}")


