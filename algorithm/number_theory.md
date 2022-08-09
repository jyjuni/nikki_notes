# 数论

## 专题

### 最大公约数 

[592. 分数加减运算](https://leetcode.cn/problems/fraction-addition-and-subtraction/) 

```python
# 辗转相除法求最大公约数
a,b = max(d,n), min(d,n) #a>b
while a%b:
  r = a%b
  a,b = b,r
# now a%b==0, b is gcd

# a > b
# 24 15
# 24 / 15 = 1 ... 9
# 15 / 9  = 1 ... 6
# 9  / 6  = 1 ... 3
# 6  / 3  = 2 ... 0
# 3 is gcd
```

### 快速乘

[29. 两数相除](https://leetcode.cn/problems/divide-two-integers/) 

```python
# 5*4 = (2^2+2^0)*4 = 4*2*2 + 4
def mul(x, a):
    ans = 0
    while x>0: 
      if x&1: #ith digit is 1
      		ans += a #ans+=a0 * a^i
       x = x>>1
       a += a # a = a0 * 2^i
    return ans
```

### 快速幂

```python
# 4^5 = 4^(2^2+2^0) = 
def power(x, a):  
    ans = 0
    while x>0: 
      if x&1: #ith digit is 1
      		ans *= a #ans *= a0 * a^i
       x = x>>1
       a *= a # a = a0 * 2^i
    return ans
```

