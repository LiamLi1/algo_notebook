## Nine Chapter Class 8

##### 1. Queue

##### 2. Stack
非递归的二叉树遍历
Push O(1)
Pop O(1)
Top O(1) //都是average
 - [x] [min-stack](https://www.leetcode.com/problems/min-stack/description)建两个栈。一个放最小值。保持两个栈大小一致。
 - [x] [implement-queue-by-two-stacks](https://www.lintcode.com/problem/implement-queue-by-two-stacks/description)

 单调栈：当一个数被pop出来的时候，左边/右边比他大/小的第一个数就知道了
 - [x] [largest-rectangle-in-histogram](https://www.leetcode.com/problems/largest-rectangle-in-histogram/description) 找左/右边比它小/大的第一个数，用栈来做
 
 ```
 两道拓展题，利用height转换，第二道不是单调栈的题
 ```
 - [ ] [maximal-rectangle/](https://leetcode.com/problems/maximal-rectangle/)
 - [ ] [largest-submatrix-with-rearrangements/](https://leetcode.com/problems/largest-submatrix-with-rearrangements/)
 

 ```
 ```

 - [x] [max-tree](https://www.lintcode.com/problem/max-tree/description) 用上一题的方法。找每个数的父节点。

- [x] [remove-k-digits/](https://www.leetcode.com/problems/remove-k-digits/description) 另类单调栈！

##### 3. Hash
Collision:
Open hashing(LinkedList)
Closed hashing(Array) 缺点:不支持删除

```
模运算与基本四则运算有些相似，
加/减/乘/幂 都可以拿进去。
但是除法例外。
其规则如下：
(a + b) % p = (a % p + b % p) % p （1）
(a - b) % p = (a % p - b % p) % p （2）
(a * b) % p = (a % p * b % p) % p （3）
a ^ b % p = ((a % p)^b) % p （4）

```
- [x] [hash-function](https://www.lintcode.com/problem/hash-function/description)

java: 先用long来存，最后再转成int

python: 
```
>>> ord('a')
97
>>> chr(97)
'a'
>>> chr(ord('a') + 3)
'd'

```

Rehasing:
- [x] [Rehashing](https://www.lintcode.com/problem/rehashing/description)

Difference of HashTable/ HashSet/ HashMap (Thread safe? only hashTable. )

- [x] [LRU cache](https://www.leetcode.com/problems/lru-cache/description)
思路： 用链表+hash
Doubly Linked List 好理解。单链表也可以。

- [x] [LFU cache](https://www.leetcode.com/problems/lfu-cache/description)
用heap来做。是O(n(logn))
用bucket的链表来做。是O(n)
- [ ] *代码量太大，二刷再重新做*
```
https://leetcode.com/problems/lfu-cache/discuss/166683/Python-only-use-OrderedDict-get-O(1)-put-O(1)-Simple-and-Brief-Explained!!!!!!
利用数据结构速度搞定
```

```
def linkFreqNode(self, listNode, freqNode):
# link Freq的同时也处理listNode的位置
def unlinkFreqNode(self, listNode, freqNode)
# unlinkFreq的同时也unlink listNode
```

- [x] [longest-consecutive-sequence](https://www.leetcode.com/problems/longest-consecutive-sequence/)  看每个元素近来几次/出去几次，来计算时间复杂度
- [x] [subarray-sum](https://www.lintcode.com/problem/subarray-sum/description)
- [x] [anagrams](https://www.lintcode.com/problem/anagrams/description)

##### 4. Heap
最优二叉树/ 最大堆，父节点大于儿子/ 最小堆同.
父节点： (j - 1)/2
左子节点/右子节点： j * 2 + 1/ j * 2 + 2
- [x] [heapfily](https://www.lintcode.com/problem/heapify/description) 操作：sift down 建堆， sift up/down 添加/删除元素。 建堆复杂度是O(N)
```java
private void siftdown(int[] A, int k) {
        while (k * 2 + 1 < A.length) {
            int son = k * 2 + 1;
            if (k * 2 + 2 < A.length && A[son] > A[k * 2 + 2])
                son = k * 2 + 2;
            if (A[son] >= A[k])
                break;
            
            int temp = A[son];
            A[son] = A[k];
            A[k] = temp;
            k = son;
        }
    }
    
```

 [堆排序之堆的概念—插入、删除、建堆 - 陈云佳的专栏 - CSDN博客](https://blog.csdn.net/BillCYJ/article/details/78482468)
- [x] [find median from data stream](https://www.leetcode.com/problems/find-median-from-data-stream/description) keep Set1 || Median || Set2, 保证两边数字相等或set1 = set2 - 1. 所以set1/set2分别是最大值/最小值堆，然后进来新的数就调整。
- [x] [find median in silding window](https://leetcode.com/problems/sliding-window-median/)
*黑科技/ 两个heap来实现可以删除元素的heap。删除的效率为O(1).

java 优先队列可以直接实现堆。除了最小值堆，都要实现Comparator接口。
```java
PriorityQueue<Integer> maxHeap;
maxHeap = new PriorityQueue<Integer>(cnt, revCmp);
```
可以直接在数据类型里实现接口，也可以在new里传入一个comparactor的引用。

```java

//Comparator 接口定义如下：
public  interface  Comparable<T>{
        public  int compareTo(T  o);
}

//不允许创建接口的实例(实例化),但允许定义接口类型的引用变量,
//该引用变量引用实现了这个接口的类的实例.例子如下：

Comparator<Integer> revCmp = new Comparator<Integer>() {
	@Override
	public int compare(Integer left, Integer right) {
		return right.compareTo(left);
	}
	
```

- [x] [merge-k-sorted-lists](https://www.leetcode.com/problems/merge-k-sorted-lists/description)

##### 5. Trie
- [x] [word-search-ii](https://www.leetcode.com/problems/word-search-ii/)
- [ ] 注意定义清楚dfs的状态。初始调用的时候是什么样子。

前缀树
prefix search: 前缀查询 可以根据首字符来查是否有。
插入和查询的效率很高，都为O(m)，其中 m 是待插入/查询的字符串的长度。
作用：
1. 统计词频（用int count 代替 String word)
2. 字符排序（用数组代替map。数组从a-z排列。然后做一个先序遍历）
3. 字符串检索（如本题）

```java
class TrieNode {
    String word; // 表示到该节点为止，是否是一个关键字。也可以用boolean来代替。
    HashMap<Character, TrieNode> children;
    public TrieNode() {
        word = null;
        children = new HashMap<Character, TrieNode>();
    }
};


class TrieTree{
    TrieNode root;
    
    public TrieTree(TrieNode TrieNode) {
        root = TrieNode;
    }
    
    public void insert(String word) {
        TrieNode node = root;
        for (int i = 0; i < word.length(); i++) {
            if (!node.children.containsKey(word.charAt(i))) {
                node.children.put(word.charAt(i), new TrieNode());
            }
            node = node.children.get(word.charAt(i));
        }
        node.word = word;
    }
};

```

#### TreeDict
```python
from sortedcollections import SortedList
from sortedcollections import SortedDict
from sortedcollections import SortedSet

python只能找插入位置。bisect_left/ bisect_right 表示插在最左边/最右边。floor和ceil要另外写，利用插入位置找到index，
再根据
i.key是否在dict里面
ii.index是否为首尾
来判断

ind_floor = d.bisect_left(key)
if key not in keys:
    ind_floor -= -1
    
        
ind_ceil = d.bisect_right(key)
if ind_ceil == len(keys):
    ind_ceil = -1

```
