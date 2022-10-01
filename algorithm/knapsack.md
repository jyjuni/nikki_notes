# 背包问题(knapsack) 

[动态规划精讲（二） - LeetBook ](https://leetcode.cn/leetbook/read/dynamic-programming-2-plus/5253i5/) 

## 简介

### 01背包

n个物品，体积限制为V。物品j的体积为v_j，价值为w_i。每种物品只有一个，只有选或者不选，没有选几个的问题。

#### 状态设计

```python
dp[i][j] := 考虑了 [0..i]  里的物品，占用了 j 空间，所能取得的最大价值。
```

#### 转移方式

转移方式有两种，一种是放入，一种是不放入。如果放，则区间 [0...i-1] 只能占 j - v[i] 空间，如果不放，则区间 [0...i-1] 的物品还是占了 j 空间。

```python
dp[i][j] = max(dp[i - 1][j], # 当前物品不选
          		 dp[i - 1][j - v[i]] + w[i]) # 当前物品选，j - v[i] 要大于等于 0
```

#### 初始值

初始化时将所有状态置为 0 即可。这就是 01 背包问题。一共 N×V 种状态, 状态的转移 O(1) 可以完成，因此时间复杂度，空间复杂度都是 O(NV)。

#### 空间优化

因为每次第i个只考虑上一行第i-1行的信息，所以可以使用滚动数组对空间占用进行优化，由存N行降低到存1行：

```
dp[j] = max(dp[j], dp[j - v[i]] + w[i]) // j 从大往小推
```

假设状态只有一行，即 `dp[j] := 占用了 j 空间的情况下可以取到的最大价值`, 在推第 i 行的时候，需要同时访问上一行j和j以前的信息，这里要用到第 i - 1 行的 dp[j - v[i]]，但是如果按照正常的 j 从 0 到 V 推的话，计算 dp[j] 的时候，dp[j - v[i]] 保存的已经是第 i 行信息了。因此j从大往小推，推到 dp[j] 时，dp[j+1], dp[j+2],...,dp[V] 都已经是第 i 行的信息了，但是它们对 dp[j] 的计算没有影响，有影响的 dp[j-v[i]] 此时还是第 i - 1 行的信息。因此当空间这一维的状态从大往小推的时候，i 这一维状态可以优化到一维。

#### 衍生问题：要求放满

在01背包的基础上更改：

1. dp 初始化是要初始化为 $-1$，$-1$ 表示方案不可取。同时 $dp[0][0] = 0$
2. 状态转移时，$dp[i - 1][j - v[i]] + w[i]$ 要更新进 $dp[i][j]$ 前，先要判断 $dp[i - 1][j - v[i]]$ 是否为 $-1$，不为 $-1$，则 $dp[i - 1][j - v[i]]$ 代表的物品组才能放出来

### 完全背包

#### 朴素想法

但是由于有体积限制，因此实际取的数量也是有限制的。每个物品其实最多只能取 V / v[i] 个。

一个朴素的思路是将完全背包强行变成 01 背包：对每个物品 i，都可以求出一个 V / v[i] ，然后就 将物品展开 ，即视为有 V / v[i]个同样的物品，每个物品有选和不选两种选择。再套用 01 背包的解法可以解决完全背包。

但是这种办法复杂度太高了，需要优化。优化的方法非常巧妙，现在我们不把每个物品展开来考虑这个问题。

#### 状态设计

与01背包相同：

```
dp[i][j] := 考虑了区间 [0..i]  里的物品，占用了 j 空间，所能取得的最大价值。
```

#### 转移方式

考虑的状态转移，对于当前物品 i ，也是有两种情况：选和不选。

如果选，在 01 背包中 物品区间 [0...i-1] 个只能占 j - v[i] 空间，而在完全背包中因为 i 有无限多个，因此选了 i 之后是 前 i 个物品只能占 j - v[i] 空间。
如果不选，则 物品区间 [0...i-1] 还是占了 j 空间，这与 01 背包一样。状态转移方程如下，注意唯一的区别就是第 2 行的 dp[i - 1] 变成了 dp[i]。

```
dp[i][j] = dp[i - 1][j] 当前物品不选
           dp[i][j - v[i]] + w[i] 当前物品选，j - v[i] 要大于等于 0
```

#### 空间优化

可以使用和01背包相似的滚动数组方式将存储空间压缩到1行，唯一不同的是，现在第i行需要访问的是第i行j往前和第i-1行j位置的信息。可以发现，如果j改为从小到大访问，那么dp[0], dp[1], dp[2],...,dp[j-1]已经被覆盖，当前dp[j]还没有被覆盖，因此j从小往大推的时候，就可以同时访问到所需信息。

```
dp[j] = max(dp[j], dp[j - v[i]] + w[i]) 
```

### 多重背包

重背包问题是这样描述的：

有 $n$ 种物品，物品 $j$ 的体积为 $v_j$, 价值为$w_j$, 有体积限制$V$。每种物品限制个数$c_i$。

**思路 1 ：将物品展开，全拆成 01**

[优化](https://leetcode.cn/leetbook/read/dynamic-programming-2-plus/5253i5/)

**思路 2 ：2 进制分解**

有这样一个事实：任意一个数 n，它一定可以用 1,2,4,8,... $2^k$，以及$2^k$到$2^{k+1}$之间的某个数表示。例如13以内的所有数都可以用1,2,4,6表示。

所以对于物品 i, 数量限制是c_{i}*c**i* , 可以将其分成若干物品，它们的价值和体积为：

$(w_i, v_i), (2*w_i, 2*v_i)$

然后对这些物品做 01 背包。这样 01 背包的物品数就比思路 1 少很多了。这可以理解为类似于倍增法的思想。倍增法超出了力扣的范围，感兴趣的话可以找相关的资料学习。

## 例题

 [购物单 - 华为笔试](https://www.nowcoder.com/practice/f9c6f980eeec43ef85be20755ddbeaf4?tpId=37&tqId=21239&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=) 

可以看做01背包，物品就是主件物品，对于每个物品i考虑其配件的所有组合(每个主件有0-2个附件，所以最多只有4种组合，~O(k))，每个组合算一次最大dp即可。

```python
import sys
from collections import defaultdict, deque
items = {}
accessories = defaultdict(list)
i = 0
N, m = 0, 0
for line in sys.stdin:
    a = line.split()
    if len(a)==2: # first line
        N, m = [int(ai) for ai in a]
    else:
        i+=1
        v,p,q = [int(ai) for ai in a]
        if q == 0:
            items[i] = (v//10, p)
        else:
            accessories[q].append((v//10, p))

# print(items, accessories)
# dp[i][j]: 考虑前i个物品[1...i], 钱在j*10以下
dp = [[0] * (N//10+1) for _ in range(m+1)]
for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        dp[i][j] = max(dp[i-1][j], dp[i][j]) #可以不取
        if i in items and items[i][0] <= j: #可以包含主件i
            dp[i][j] = max(dp[i-1][j], dp[i][j])
            v, p = items[i]
            # candidate combinations of accessories
            pool = deque([(v, v*p)]) #value, satisfaction
            if accessories[i]:
                for v1, p1 in accessories[i]:
                    for _ in range(len(pool)):
                        v0, p0 = pool.popleft()
                        pool.append((v0+v1, p0+p1*v1))
                        pool.append((v0, p0))
                # print(pool)
            for v1, p1 in pool:
                if v1 <= j:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-v1] + p1)
# print(dp)
print(dp[-1][-1]*10) 
```

