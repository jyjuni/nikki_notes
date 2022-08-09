# trie树

### 实现

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



----

[Lfool's note on Trie Tree](https://lfool.github.io/LFool-Notes/algorithm/%E8%AF%A6%E8%A7%A3%E5%89%8D%E7%BC%80%E6%A0%91TrieTree.html)

## 例题

[729. 我的日程安排表 I](https://leetcode.cn/problems/my-calendar-i/)

[731. 我的日程安排表 II](https://leetcode.cn/problems/my-calendar-ii/)

[732. 我的日程安排表 III](https://leetcode.cn/problems/my-calendar-iii/)

[715. Range 模块](https://leetcode.cn/problems/range-module/)

[307. 区域和检索 - 数组可修改](https://leetcode.cn/problems/range-sum-query-mutable/)

[933. 最近的请求次数](https://leetcode.cn/problems/number-of-recent-calls/)

[699. 掉落的方块](https://leetcode.cn/problems/falling-squares/)

