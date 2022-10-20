# 链表
https://leetcode-cn.com/leetbook/read/linked-list/x6ybqh/ 

215 169 274 275 229 74 29 141 142 160 

19 206 203 328 234 21 138  61 430 707



## 结构

单链表

双链表



## 例题

##### 反转链表

迭代

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            tmp = cur.next #存储下一步
            cur.next = prev #反转
            prev, cur = cur, tmp #下一步
        return prev
```



头插法

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0, head)
        g,p = dummy, head 
            
        while p.next:
            #remove after p
            removed = p.next
            p.next = p.next.next

            #insert after g
            g.next, removed.next = removed, g.next
        
        return dummy.next
```



递归

因为反转有换头操作，所以调用时：

head = f(head)





```python
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode newHead = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return newHead;
    }
}
```



##### 打印两个有序链表的公共部分

双指针：

谁小谁移动，相等打印后共同移动，有一个出界则停止

##### 判断回文链表

 [github code](https://github.com/Aaron-TangCode/zuoshen/blob/master/src/com/tanghainlin/basic_class_03/Code_11_IsPalindromeList.java) 

方法1：

不要求空间复杂度：放到栈里，依次从尾弹出和头比

方法2：

快慢指针找中点，只放后半段到栈里，从头再遍历一遍和栈里比对。

方法3：**要求额外空间复杂度O(1)**

反转后半部分链表，从两端向中间逐个比对。

重要技巧：

1. 额外数据记录结构（哈希表等）

2. **快慢指针**

- 注意边界条件
  1. 奇偶数长度的中点，尤其是偶数在左中点/右中点的情况）
  2. 长度为0,1,2的情况
  3. 如何提前停止（中点前一个节点）

##### 链表排序partition

对于小于，等于，大于部分，分别维护头、尾指针。遍历过程中分到属于的区域：

- 如果头尾为null，直接作为头尾

- 如果头尾不为null，尾.next指向新的节点，更新尾为新节点

SH, ST, EH, ET, BH, BT

最后ST->EH,ET->BH

- 讨论清除边界：空指针

##### 随机指针拷贝

[github code](https://github.com/Aaron-TangCode/zuoshen/blob/master/src/com/tanghainlin/basic_class_03/Code_13_CopyListWithRandom.java) 

方法1：哈希表辅助，额外空间O(N)

维护哈希表`老节点:新节点`

遍历两次老链表：

第一遍遍历新建节点，放在哈希表中

第二遍遍历替换为新节点->新节点(用老结点的random和next指针指向的老结点去查对应的)



方法2：不用额外空间 

第一遍：在每个老结点后插入新节点：老结点.next=新节点，新节点.next=下一个老结点

第二遍：遍历**每一对**节点，新节点.random=老结点.random.next

##### 

##### 判断有环（返回第一个入环节点）

方法1：哈希表

方法2：快慢指针

- 如果快指针走到空节点：没有环

- 快慢指针相遇：有环

  - 两个指针一个从开头一个从相遇处，同时开始一次走一步，相遇点为第一个入环点  

     [证明](https://leetcode.cn/problems/c32eOV/solution/lian-biao-zhong-huan-de-ru-kou-jie-dian-vvofe/) 

##### 链表相交节点

1. 两个链表分别判断是否有环，返回第一个入环点

2. 对于无环链表：分别遍历链表，记录长度

   - 如果end1!=end2: 一定不相交

   - 如果end1=end2:

     长链表先走差值步，然后长短链表一起一次走一步，第一次相遇节点即相交节点

3. 对于有环链表：

   - (case 2)如果loop1=loop2: 

     一定相交，把入环节点当做共用的终点，按照无环链表求

   - (case 1 or case 3) 如果loop1 != loop2:

     让loop1继续前进，如果转圈过程中遇到loop2则相交节点是loop1或者loop2（根据从那个链表算，都算第一个），如果回到了自己则不相交。

##### 排序链表

 [148. 排序链表 - 力扣（LeetCode）](https://leetcode.cn/problems/sort-list/) 