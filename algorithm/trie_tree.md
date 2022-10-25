# trie树（前缀树、字典树）

## 结构

### 存储

边存储：每个字母

节点存储：pass,end

- 表达路：每个节点存next，数组或者哈希表、有序表

- pass：经过这个节点的次数

- end：在这个节点结束的次数

> 可以理解为节点代表它上面的边组成的前缀
>
> eg: 根节点的p值含义 -- 有多少个字符串以空串为前缀==共有多少字符串

### 查询

怎么加入的就怎么查

> pass - 有多少是以...为前缀的
>
> end - 有没有这个字符串

查询之前加入过几个：

- 如果能查到底：返回`end`
- 如果查到一半路径不存在，返回`0`

查询以...为前缀：

- 如果查到一半路径不存在，返回`0`
- 如果能查到底：返回`pass`

### 删除

1. 先search，确定存在再删

2. 如果存在：沿途`pass--`，最后一个节点`end--`。遇到`pass`更新后变为`0`，整体释放(`=null`)。 

```python
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
    
    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None

```







## 实现

[leetcode notes](https://leetcode.cn/problems/replace-words/solution/by-ac_oier-jecf/)

I. 二维数组实现

```
class Solution {
    static int N = 100000, M = 26;
    static int[][] tr = new int[N][M];
    static boolean[] isEnd = new boolean[N * M];
    static int idx;
    void add(String s) {
        int p = 0;
        for (int i = 0; i < s.length(); i++) {
            int u = s.charAt(i) - 'a';
            if (tr[p][u] == 0) tr[p][u] = ++idx;
            p = tr[p][u];
        }
        isEnd[p] = true;
    }
    String query(String s) {
        for (int i = 0, p = 0; i < s.length(); i++) {
            int u = s.charAt(i) - 'a';
            if (tr[p][u] == 0) break;
            if (isEnd[tr[p][u]]) return s.substring(0, i + 1);
            p = tr[p][u];
        }
        return s;
    }
    public String replaceWords(List<String> ds, String s) {
        for (int i = 0; i <= idx; i++) {
            Arrays.fill(tr[i], 0);
            isEnd[i] = false;
        }
        for (String d : ds) add(d);
        StringBuilder sb = new StringBuilder();
        for (String str : s.split(" ")) sb.append(query(str)).append(" ");
        return sb.substring(0, sb.length() - 1);
    }
}
```

II. Node链表实现

```
class Solution {
    class Node {
        boolean isEnd;
        Node[] tns = new Node[26];
    }
    Node root = new Node();
    void add(String s) {
        Node p = root;
        for (int i = 0; i < s.length(); i++) {
            int u = s.charAt(i) - 'a';
            if (p.tns[u] == null) p.tns[u] = new Node();
            p = p.tns[u];
        }
        p.isEnd = true;
    }
    String query(String s) {
        Node p = root;
        for (int i = 0; i < s.length(); i++) {
            int u = s.charAt(i) - 'a';
            if (p.tns[u] == null) break;
            if (p.tns[u].isEnd) return s.substring(0, i + 1);
            p = p.tns[u];
        }
        return s;
    }
    public String replaceWords(List<String> ds, String s) {
        for (String str : ds) add(str);
        StringBuilder sb = new StringBuilder();
        for (String str : s.split(" ")) sb.append(query(str)).append(" ");
        return sb.substring(0, sb.length() - 1);
    }
}
```

## 复杂度分析

时间复杂度：令 n = \sum_{i = 0}^{ds.length - 1} ds[i].length, m 为 s 长度，复杂度为 O(n + m)

空间复杂度：O(n×C)，其中C=26为字符集大小

## 例题

[729. 我的日程安排表 I](https://leetcode.cn/problems/my-calendar-i/)

[731. 我的日程安排表 II](https://leetcode.cn/problems/my-calendar-ii/)

[732. 我的日程安排表 III](https://leetcode.cn/problems/my-calendar-iii/)

[715. Range 模块](https://leetcode.cn/problems/range-module/)

[307. 区域和检索 - 数组可修改](https://leetcode.cn/problems/range-sum-query-mutable/)

[933. 最近的请求次数](https://leetcode.cn/problems/number-of-recent-calls/)

[699. 掉落的方块](https://leetcode.cn/problems/falling-squares/)



##### 参考：

- [Lfool's note on Trie Tree](https://lfool.github.io/LFool-Notes/algorithm/%E8%AF%A6%E8%A7%A3%E5%89%8D%E7%BC%80%E6%A0%91TrieTree.html)
-  [详解前缀树 - 左程云算法](https://www.bilibili.com/video/BV1kQ4y1h7ok?p=9&vd_source=3ee85a74f53c722d5c1f8a852c0c7504) 
