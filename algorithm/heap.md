# 堆 heap
912 23 215

## 原理

[heapq API](https://docs.python.org/3/library/heapq.html)

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
    - `heappush`和``heappop`之后list的数据类型不变，在list in-place修改数值，使minHeap[0]为最小值。
    - `heapify()`: takes populated list, change in-place

#### maxHeap

存-value

#### 自定义排序key

1) 存tuples: (priority, task)，用正负指定升降序
2) 自定义类，覆盖__lt__(self, other) 
2) 

## 堆排序

