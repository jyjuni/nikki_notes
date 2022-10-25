# 哈希表



性能：增删改查$O(1)$

哈希表内部基础类型按照值传递， 非基础类型按照引用（指针地址）传递

# 有序表

哈希表是无序组织key，有序表是有序组织key

性能：

增删改查$O(logN)$

### python有序表

`OrderedList`

`OrderedDict`

### 比较器

**cmp函数：满足a<b，函数返回负数；a==b，函数返回0；a>b，函数返回正数**

python3 取消了`cmp` 参数，可以用`functools.cmp_to_key` 代替

`sort(...,key=cmp_to_key(...))`

```python
import functools

nums=[3,30,34,5,9]
strs=[str(num) for num in nums]
strs.sort(key=functools.cmp_to_key(lambda x,y:int(x+y)-int(y+x)))

print(''.join(strs))
```

