## Nine Chapter Class 8

##### 1. Queue

##### 2. Stack
非递归的二叉树遍历
Push O(1)
Pop O(1)
Top O(1) //都是average
 - [x] [min-stack](https://www.lintcode.com/problem/min-stack/description)建两个栈。一个放最小值。保持两个栈大小一致。
 - [x] [implement-queue-by-two-stacks](https://www.lintcode.com/problem/implement-queue-by-two-stacks/description)
 - [x] [largest-rectangle-in-histogram](https://www.lintcode.com/problem/largest-rectangle-in-histogram/description) 找左/右边比它小/大的第一个数，用栈来做
 - [x] [max-tree](https://www.lintcode.com/problem/max-tree/description) 用上一题的方法。找每个数的父节点。

- [ ] [remove-k-digits/](https://www.lintcode.com/problem/remove-k-digits/description) 另类单调栈！

##### 3. Hash
Collision:
Open hashing(LinkedList)
Closed hashing(Array) 缺点:不支持删除

Hash funciton:
![d3588a87.png](:storage\50a5b1a5-828c-4d13-82ad-21ff858aaa40\d3588a87.png)

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
先用long来存，最后再转成int

Rehasing:
- [x] [Rehashing](https://www.lintcode.com/problem/rehashing/description)


Difference of HashTable/ HashSet/ HashMap (Thread safe? only hashTable. )


- [x] [LRU cache](https://www.lintcode.com/problem/lru-cache/description)
思路： 用链表+hash
Doubly Linked List 好理解。单链表也可以。


- [ ] [LFU cache](https://www.lintcode.com/problem/lfu-cache/description)
用heap来做。是O(n(logn))
用bucket的链表来做。是O(n)
- [x] [longest-consecutive-sequence](https://www.lintcode.com/problem/longest-consecutive-sequence/)  看每个元素近来几次/出去几次，来计算时间复杂度
- [x] [subarray-sum](https://www.lintcode.com/problem/subarray-sum/description)
- [x] [anagrams](https://www.lintcode.com/problem/anagrams/description)

##### 4. Heap
最优二叉树/ 最大堆，父节点大于儿子/ 最小堆同.
父节点： (j - 1)/2
左子节点/右子节点： j * 2 + 1/ j * 2 + 2
- [x] [heapfily](https://www.lintcode.com/problem/heapify/description) 操作：sift down 建堆， sift up/down 删除元素。 建堆复杂度是O(N)
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
![e28668b7.png](:storage\50a5b1a5-828c-4d13-82ad-21ff858aaa40\e28668b7.png))
- [x] [find median from data stream](https://www.lintcode.com/problem/find-median-from-data-stream/description) keep Set1 || Median || Set2, 保证两边数字相等或set1 = set2 - 1. 所以set1/set2分别是最大值/最小值堆，然后进来新的数就调整。

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

- [x] [merge-k-sorted-lists](https://www.lintcode.com/problem/merge-k-sorted-lists/description)
[堆排序](https://blog.csdn.net/MoreWindows/article/details/6709644)
##### 5. Trie
- [x] [word-search-ii](https://www.lintcode.com/problem/word-search-ii/)
- [ ] :carrot: 注意定义清楚dfs的返回状态。
前缀树。
![3ee6c24b.png](:storage\50a5b1a5-828c-4d13-82ad-21ff858aaa40\3ee6c24b.png)
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
