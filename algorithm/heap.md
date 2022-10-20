# 堆 heap
912 23 215

## 原理

[heapq API](https://docs.python.org/3/library/heapq.html)

## 堆使用

```python
# initialize
minHeap = []
# push new value
heappush(minHeap, i)
# pop min
heappop(minHeap)
# get(peek) min
min = minHeap[0]
```

[code: tests.ipynb](../code/tests.ipynb) 

- heap[0]始终最小
- heap相当于是在list结构上原地修改，例：
    - `heappush`和`heappop`之后list的数据类型不变，在list原地in place修改数值，使minHeap[0]为最小值。
    - `heapify()`: takes populated list, change in-place

#### maxHeap

存`-value`

#### 自定义排序key

1) 存tuples: (priority, task)，用正负指定升降序
2) 自定义类，覆盖__lt__(self, other) 

## 堆实现

 [3.详解桶排序以及排序内容大总结](https://www.bilibili.com/video/BV1kQ4y1h7ok?p=4&vd_source=3ee85a74f53c722d5c1f8a852c0c7504)   

 [code](https://github.com/Aaron-TangCode/zuoshen/blob/master/src/com/tanghainlin/basic_class_01/Code_03_HeapSort.java) 



```python
def heap_sort
def heapify

def heapinsert
```

**扩容代价：**加n个数平均$O(logN)$

**手写和库（黑盒）的区别：**库不支持改变某一个位置的值，只从这个位置向下的heapify/只从这个位置向上insert（可以实现但只能遍历，不像手写这么高效率）



### 比较器

规则：

返回负数时，第一个参数排在前面

返回正数时，第二个参数排在前面

返回0的时候，谁在前面无所谓

python比较器: `key=cmp_to_key(f)`

```python
>>> def lessthan(x, y):
...     return x[0] - y[0] #负数：x在y前
... 
>>> data = [(4, None), (3, None), (2, None), (1, None)]
>>> from functools import cmp_to_key
>>> sorted(data, key=cmp_to_key(lessthan))
[(1, None), (2, None), (3, None), (4, None)]
```





## 堆排序

堆排序实现

**<u>方法1：</u>**遍历heapinsert($N*O(logN)$) + 从顶向下swap-heapify($N*O(logN)$)

**<u>方法2：</u>**从底向上heapify(可推导得：$全部元素O(N)$) + 从顶向下swap-heapify($N*O(logN)$)

**例题：**近乎有序数组

> 已知一个几乎有序的数组，几乎有序是指如果把数组排好顺序的话，每个元素移动的距离可以不超过k，并且k相对于数组来说比较小。选择一个合适的排序算法针对这个数据进行排序。

思路：维护一个长度为k+1的小根堆，则前k+1个数里必存在数组最小值（对于最小值来说，移动距离也不超过k）。当堆长度满k+1之后，每次把最小值取出放在下一个对应位置（从位置0开始），就可以得到顺序递增数列了。

时间复杂度：$O(NlogK)$

**例题：**最小的k个数（剑指offer 40)

时间复杂度：$O(NlogK)$

## 例题

### 数据流的中位数

维护一个大根堆（放小的一半）和一个小根堆（放大的一半）。对于每一个新数据：

1. 和中间值（`maxHeap[0]`）进行比较：

   - 如果<=中间值进大根堆
   - 否则进小根堆

2. 加完后如果两个堆size相差$\geq 2$，弹出`maxHeap[0]`放入`minHeap`

3. 根据两个堆size求中位数：

   - size相等则取两个堆顶平均

   - size不等，直接取size大的堆顶

时间复杂度：每添加一个元素，O(logN)

### 优化Dijkstra

