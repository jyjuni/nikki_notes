# 数据结构

## String
str:
isnumeric > isdigit > isdecimal
isdigit: numbers, superscript
isdecimal: numbers
isnumeric: numbers, superscript, fractions

https://stackoverflow.com/questions/22789392/str-isdecimal-and-str-isdigit-difference-example 


## list
reverse a list in python:
1. l.reverse()
     inplace and do not cost extra mem
2. list(reversed(l))
     not inplace
3. l[::-1]
     use slicing and create a shallow copy, is faster, less readable

## list comprehension

> all elements

```[1 if condition else 0 for x in sequence)]```

> with elements that satisfy if conditions only

```[f(x) for x in sequence if condition]```


## dict
[#508. 出现次数最多的子树元素和](https://leetcode.cn/problems/most-frequent-subtree-sum/)

### sort dictionary by value:
> sort dictionary, return [(k,v)] list, descending

```python
d = sorted(d.items(), key=lambda x:x[1], reverse=True)
```

> sort by value, return list of keys

```python
d = sorted(d, key=d.get, reverse=True) 
```

> OrderedDict

```python
collections.OrderedDict: preserve insertion key ordering
```
> SortedDict

```python
sortedcontainers.SortedDict: preserve key ordering
```

## Counter
> Sort by descending first. Elements with equal counts are ordered in the order first encountered
```python
from collections import Counter
# count
>>> Counter({3: 3, 2: 2, 4: 2})
[2,2,3,3,3,4,4]

# top n most common pairs
>>> Counter({3: 3, 2: 2, 4: 2}).most_common(1)
[('3', 3)]`

```
