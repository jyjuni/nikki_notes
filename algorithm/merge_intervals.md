# 合并区间问题

**区间重叠条件：**

```python
start, end = current_inverval
for l,r in intervals:
	if interval[0] <= end and interval[1] >= start: #overlapping
    ...
```

