# 数据结构

## String
### string functions

`s.count()`: return total count of instances found in String s



str:
isnumeric > isdigit > isdecimal
isdigit: numbers, superscript
isdecimal: numbers
isnumeric: numbers, superscript, fractions

https://stackoverflow.com/questions/22789392/str-isdecimal-and-str-isdigit-difference-example 

## Set

### functions

`set.add() `: add single element

`set.update()`: add another iterable

`set.union()`: union, not in-place

> ` s1 = s1.union(s2) `same as ` s1.update(s2)`



## List

### functions

`l.count()`: return total count of instances found in List l



### reverse a list

reverse a list in python:

1. l.reverse()
     inplace and do not cost extra mem
2. list(reversed(l))
     not inplace
3. l[::-1]
     use slicing and create a shallow copy, is faster, less readable

### list comprehension

#### if

> all elements

```[1 if condition else 0 for x in sequence)]```

> with elements that satisfy if conditions only

```[f(x) for x in sequence if condition]```

#### 双重循环

`[e for l in grid for e in l]`


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



## Itertools

> permutation：排列对（无放回）

```python
 permutations('ABCD', 2)
 >>> AB AC AD BA BC BD CA CB CD DA DB DC
```

> combinations：组合对（无放回） 
>
> [593. 有效的正方形](https://leetcode.cn/problems/valid-square/) 

```python
combinations('ABCD', 2)
>>> AB AC AD BC BD CD
```

> pairwise: 相邻的对（比如构建邻接表）
>
>  [444. 序列重建](https://leetcode.cn/problems/sequence-reconstruction/) 

```python
pairwise('ABCDEFG') 
>>> AB BC CD DE EF FG
```

> product: 笛卡尔积

```python
product('ABCD', 'xy') 
>>> Ax Ay Bx By Cx Cy Dx Dy

product('ABCD', repeat=2) # self X self
>>> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD

product(range(2), repeat=3) # self X self X self
>>> 000 001 010 011 100 101 110 111
```

