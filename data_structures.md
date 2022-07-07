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
#508

### sort dictionary by value:
> sort dictionary, return [(k,v)] list, descending

```python
d = sorted(d.items(), key=lambda x:x[1], reverse=True)
```

> sort by value, return list of keys

```d = sorted(d, key=d.get, reverse=True) ```

> OrderedDict

```collections.OrderedDict: preserve insertion key ordering```
> SortedDict

```sortedcontainers.SortedDict: preserve key ordering```
