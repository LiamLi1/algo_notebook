## Data Structure

[LintCode BB Question List](https://www.lintcode.com/problem/?tag=bloomberg)


### 1 String

- String的基本操作
- 结合Trie的题，DP的题，recurison的题等。
- String Compression
```java
1. String与其他基本变量的转换：

String.valueOf(); //里面可以是 Integer， Double， int，等等。同样也可以String转其他变量。

2. substring
String substring(int beginIndex) //取从beginIndex位置开始到结束的子字符串。
String substring(int beginIndex, int endIndex) //取从beginIndex位置开始到endIndex位置前一位的子字符串。所以(3,4)(4,5) 都只有一个且不重复

3. indexOf/ lastIndexOf
双引号/单引号都可以
找不到时返回-1

4.s.toCharArray(); //扫字符串的时候很有用
String s = new String(charArray); 

5. StringBuilder
StringBuilder sb = new StringBuilder();
sb.append(); // 什么数据类型都可以
sb.toString();
sb.deleteCharAt(permutation.length() - 1); //删除
sb.delete(int start, int end);
sb.reverse(); //反方向
sb.replace(int start, int end, String str); //替换

StringBuilder/ String 直接相加，可以得到新的String

6. String[] stubs = path.split("/+"); // 用正则表达式拆分成字符串数组
如果第一个字符串是split，会得到第一个为"".
" is blue" -> ["", "is", "blue"]
如果末尾是，却没有影响。会全部删除。
"is blue " -> ["is", "blue"]
中间“多余”出来的分隔符，会产生空字符串
"is   blue" -> ["is", , , "blue"]
三个空格。一个用来分割，两个多余的产生了空串。

```
[LintCode Question List](https://www.lintcode.com/problem/?tag=string)
- [x] [String Compression
](https://www.lintcode.com/problem/string-compression/description):cat: :cat:
- [x] [word-abbreviation](https://www.lintcode.com/problem/word-abbreviation/) :cat::cat:




---
### 2 Binary Tree
- devide and conquer 最常用
- recursion的各种应用。比如返回list的情况，还有pre/in/post 建树等。
[LintCode Quesiton List](https://www.lintcode.com/problem/?tag=binary-tree)

- [x] [minimum-depth-of-binary-tree](https://www.lintcode.com/problem/minimum-depth-of-binary-tree/description) 可以BFS/ 也可以divide and conquer :cat: 
- [x] [invert-binary-tree](https://www.lintcode.com/problem/invert-binary-tree/description) :cat:
- [x] [same-tree](https://www.lintcode.com/problem/same-tree/description) :cat:
- [x] [lowest-common-ancestor-of-a-binary-tree](https://www.lintcode.com/problem/lowest-common-ancestor-of-a-binary-tree/description) :cat::cat:
- [x] [Kth-smallest-element-in-a-bst](https://www.lintcode.com/problem/kth-smallest-element-in-a-bst/) :carrot:
- [x] [house-robber-iii/](https://www.lintcode.com/problem/house-robber-iii/) :cat::cat:

树的递归：
下面两道是相似的递归题。
关键是怎么来找leftson和rightson的位置。有inorder比较简单，左右关系明确。preorder/postorde的情况稍微复杂，要根据post中pre的第二个点的位置来分别拆分pre和post。在想好递归方法以后再来写终止情况会比较容易。
- [x] [construct-binary-tree-from-preorder-and-inorder-traversal](https://www.lintcode.com/problem/construct-binary-tree-from-preorder-and-inorder-traversal/) :cat::cat: recursion.
- [x] :rabbit:
- [x] [construct-binary-tree-from-preorder-and-postorder-traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/) :cat::cat:
- [ ] :rabbit:

分治法返回list的情况:
- [x] [unique-binary-search-trees-ii](https://www.lintcode.com/problem/unique-binary-search-trees-ii/description)
- [ ] :carrot:
- [x] [binary-tree-paths](https://www.lintcode.com/problem/binary-tree-paths/description) 和上一题一样的模板。分治返回list。然后分别对为null和为叶子节点的情况单独列出来考虑。

- BST
BST的LCA可以直接用大于/小于来找到。
- [ ] [bst-node-distance](https://www.lintcode.com/problem/bst-node-distance/)




---
### 3 Graph
#### 两种思路： 搜索（p/c） 和 recursion
[dfs / recursion LeetCode List](https://www.lintcode.com/problem/?tag=depth-first-search)
1. 搜索（ p/c两个模板）的思想是穷路径的可能性。combination用位置避免了重复。permutation每次都遍历全部点，用map记录当前是否走过该点。
2. recursion是自顶向下把大问题拆成小问题，状态的定义最重要。
3. dp：后面的由前面的记录得出。然后继续向后推算。和recursion思路相反。自底向上。

#### 3.1 search(p/c) 
- p/c 和 图的dfs
相同：都是从一个方向走到头。所谓“深度”。都需要记录visited。
不同：p的visited只表示当前路径，所以要回溯。而图的dfs不回溯，只访问一次。
- [x] [generate-parentheses](https://www.lintcode.com/problem/generate-parentheses/description) 两个变量的dfs，因为String每次都相当于传值，所以不需要回溯。:cat::cat: 相当于两个值的permutation
- [x] :carrot: 也可以用recursion的思路来解题
- [x] [binary-tree-path-sum-ii](https://www.lintcode.com/problem/binary-tree-path-sum-iii/)
- [ ] [flip-game-ii](https://www.lintcode.com/problem/flip-game-ii/description) search解法：只返回true false，不记录path。需要回溯，因为要确定最后是否能过。可以记忆化搜索，因为给定字符串的结果时唯一的。

#### 3.2 Recursion 

- 记忆化搜索：
- [x] [the-game-of-take-numbers](https://www.lintcode.com/problem/the-game-of-take-numbers/description) :tiger:
- 两个变量的recursion分治：
- [x] [unique-binary-search-trees-ii](https://www.lintcode.com/problem/unique-binary-search-trees-ii/description) 也是递归的问题。用递归的思路来想。:cat::cat:

- [ ] [letter-combinations-of-a-phone-number](https://www.lintcode.com/problem/letter-combinations-of-a-phone-number/description)

#### 3.3 DFS / BFS
- 拓扑排序，遍历图。拓扑排序dfs也要掌握。
[bfs LeetCode List](https://www.lintcode.com/problem/?tag=breadth-first-search)

- 有条件的dfs
- [ ] [word ladder-ii](https://www.lintcode.com/problem/word-ladder-ii/description) :tiger:
- [x] [topological-sorting](https://www.lintcode.com/problem/topological-sorting/description):cat::cat:

---
### 4 DP 
自底向上的思想解题。recursion则是自顶向下。
- 但是有的题找不到初始状态只能recursion。
- [x] [regular-expression-matching](https://www.lintcode.com/problem/regular-expression-matching/description) 
- [ ] [4-way-unique-paths](https://www.lintcode.com/problem/4-way-unique-paths/description)


- 有的题又当前值不能由后面的值给出，只能dp。
- [x] [Distinct Subsequences](http://www.lintcode.com/problem/distinct-subsequences) 



- 矩阵里面移动
- [ ] [4-way-unique-paths](https://www.lintcode.com/problem/4-way-unique-paths/description) 这题不能记忆化搜索。这里如果定义f[i][j] 为当前点出发到最后的path数量，则变量之间是相互依赖的关系。“状态”固定不下来。如果不能回头，则状态时可以固定的。
- [ ] [longest-continuous-increasing-subsequence](https://www.lintcode.com/problem/longest-continuous-increasing-subsequence-ii/description) // 不用回溯，因为是求上升序列，所以不需要存是否访问过，如果当前是8，下一要访问的必须大于8，自然不可重复访问8。“状态"是可以固定的。
- [ ] [unique-paths-iii](https://www.lintcode.com/problem/unique-paths-iii/description) 直接dfs不能记忆化，会超时。记忆化搜索用状态是HashSet， 所以用map来做。要一维化坐标。


- 四大基本类型（矩阵，Array， 双Array， 背包）
 - [x] [house-robber-iii](https://www.lintcode.com/problem/house-robber-iii/description) 包括1/2，都是dp问题。这里一样使用dp的思路来后续扫树。对每个节点的值存成 偷这个点/不偷这个点 能得到的最大值。要理解dp的状态究竟是怎么来的。
 - [x] [maximum-vacation-days/](https://www.lintcode.com/problem/maximum-vacation-days/description) 题目长但其实不难。flights相当于是邻接矩阵。days是每个点在不同时间的值。dp[i][j]表示在第j周待在城市i可以修的最长假期。然后就可以自底向上的dp，或者自顶向下dfs。


- 矩阵/正方形求和
- [x] [sliding-window-matrix-maximum](https://www.lintcode.com/problem/sliding-window-matrix-maximum/)


---
### 5 Linked List
- 各种基本操作
- LRU/LFU

[linked-list](https://www.lintcode.com/problem/?tag=linked-list)
- [x] [intersection-of-two-linked-lists](https://www.lintcode.com/problem/intersection-of-two-linked-lists/description) 交叉走一遍。

- [x] [linked-list-cycle-ii](https://www.lintcode.com/problem/linked-list-cycle-ii/) 背模板：下面
```java 
// fast = head.next;
// slow = head; 
// 相等以后，head == slow.next的时候返回head。都只走一步。
    public ListNode detectCycle(ListNode head) {
        // write your code here
        if (head == null || head.next == null) {
            return null;
        }
        
        ListNode slow = head;
        ListNode fast = head.next;
        
        while (slow != fast) {
            if (fast == null || fast.next == null) {
                return null;
            }
            fast = fast.next.next;
            slow = slow.next;
        }
        
        while(head != slow.next) {
            head = head.next;
            slow = slow.next;
        }
        return head;
    }
```

---
### 6 Stack
- MaxTree、 rectangle等维护递增、递减栈
- 表达式求值。
- String相关
- 利用stack性质做iterator/queue/stackSet/minStack等

[LintCode Question List](https://www.lintcode.com/problem/?tag=stack)
[simplify-path](https://www.lintcode.com/problem/simplify-path/description)
[flatten-nested-list-iterator](https://www.lintcode.com/problem/flatten-nested-list-iterator/description) //用两个stack来展开NestedIterator
- [ ] :carrot:


---
### 7 Hash
- 线性探查Linear Probing、开散列open hashing、哈希函数
- LRU/LFU
- 用hash记录同向型两个指针的中间状态。比如subarray sum， longest consecutive sequence
```java
map.getOrDefault(ans[i], 0) // 不用写if了
```

LRU

LFU
```java
class Node {
        public int value;
        public int key;
        public int freq;
        public Node pre;
        public Node next;
        public FreqNode bucket; // 用来找到bucket，方便右移操作。
        public Node (int key, int value, int freq) {
            this.key = key;
            this.value = value;
            this.freq = freq;
            pre = next = null;
            bucket = null;
        }
    }
    
    class FreqNode { 
    //有Node head和Node tail方便添加元素。
    //pre/next则记录FreqNode， 方便找到下一个/删除自身。
        public int freq;
        public Node head;
        public Node tail;
        public FreqNode pre;
        public FreqNode next;
        public FreqNode(int freq) {
            this.freq = freq;
            pre = next = null;
            head = new Node(-1, 0, freq);
            tail = new Node(-1, 0, freq);
            head.next = tail;
            tail.pre = head;
        }
    }
```

求Array中的某个性质（最长的substring， 最长0,1个数相等）
i. 用Hash来记录累加，转换对应关系。类似于subarray Sum的题。
- [x] [contiguous-array](https://www.lintcode.com/problem/contiguous-array/description)
ii. 同样是Hash，记录两个指针间的状态。
- [x] [minimum-window-substring](https://www.lintcode.com/problem/minimum-window-substring/)
- [x] [longest-substring-without-repeating-characters](https://www.lintcode.com/problem/longest-substring-without-repeating-characters/description)

double 类型也可以用来做key
- [x] [max-points-on-a-line](https://www.lintcode.com/problem/max-points-on-a-line/description) 用斜率来确定是否共线。


---
### 8 Heap

- Heapify
- merge Kth sorted array (找到最小range)
- Kth 和 window的题。其中Kth的题最好的方法是quick sort。
- [x] [top-k-largest-numbers-ii](https://www.lintcode.com/problem/top-k-largest-numbers-ii/description) :cat::cat: 
java.util.Collections 中的sort, reverse等函数，都是直接改造传入的Collections，而不会返回。
把heap转为list的时候如果直接new ArrayList<>(heap);, 出来的顺序可能会不对。

---
### 9 Queue

---

### 10 Union Find
[LintCode Question List)](https://www.lintcode.com/problem/?tag=union-find)

[graph-valid-tree](https://www.lintcode.com/problem/graph-valid-tree/description) 可以用union find, 但是要注意判断是否有环。树的性质：边比node少一条。
[bricks-falling-when-hit](https://www.lintcode.com/problem/bricks-falling-when-hit/) UnionFind 如果是数字，就直接用数组来记录。比Map方便。

用size[] 数组可以记录连接到这个老大哥的点的总数。方法是在合并的时候，
id[rootB] = id[rootA];
size[rootA] += size[rootB];
这样一来，size[find(A)] == size[find(B)] == 这条路径上点的个数。 

虚拟一个结点和第一排所有点union， 则可以统计与第一排相连的点的总数


---

### 11 Trie
[LintCode Quesiton List](https://www.lintcode.com/problem/?tag=trie)
- [x] [palindrome-pairs](https://www.lintcode.com/problem/palindrome-pairs/)

### 12 Segment Tree

### 13 Indexed Tree
