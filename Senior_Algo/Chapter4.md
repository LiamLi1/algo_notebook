## Senior Algo Class 4
### Hash Heap
```
要点：
1.用黑科技来代替HashHeap，实现update/delete/add
2.hashheap的hash和heap分别应该存什么
```
交换的时候，hash表里面指向的也要交换。
接口：插入/删除/ sit-up/ sit-dowm/


```java
class HashHeap {
    ArrayList<Integer> heap;
    String mode;
    int size_t;
    HashMap<Integer, Node> hash;

    class Node {
      public Integer id;
      public Integer num;
// heap 用来存数。
// Node 包含两个变量。一个id是在heap中的位置。一个num是数量。
// 有Node以后就可以存重复元素了

//heap删除元素的时候，只剩一个/正好删最后一个的情况拿出来. 删除要走一遍sift_up & sift_down
// parent = (pos - 1) // 2

```
*可以用TreeSet 来代替Hash Heap. 方法是在比较的时候加入unique的变量，这样就可以处理重复元素了*


- [x] [the-skyline-problem](https://www.leetcode.com/problems/the-skyline-problem/description)
```
用hashheap黑科技搞定
https://leetcode.com/problems/the-skyline-problem/discuss/593234/Python-3-Heap
```

- [x] [sliding-window-median](https://www.leetcode.com/problems/sliding-window-median)
固定滑动窗口问题： 1. 增加元素 2. 删除元素

- [x] [stock-price-fluctuation/](https://leetcode.com/problems/stock-price-fluctuation/)
1.增加元素 2.删除元素 3.更新元素
---

### Deque
- [x] [sliding-window-maximum](https://www.leetcode.com/problems/sliding-window-maximum/description)
$O(n)$ 时间复杂度，只有栈和队列
可以维护一个递减栈，但是还要有一个front_peek和front_pop操作，所以用deque。


### Stack
找左边/右边 第一个比它大/小的元素
- [x] [max-tree](https://www.lintcode.com/problem/max-tree/description)
- [x] [histogram](https://www.leetcode.com/problems/largest-rectangle-in-histogram/)
- [ ] [sum-of-subarray-ranges](https://leetcode.com/problems/sum-of-subarray-ranges/)

表达式树
1. 二叉树
2. 非叶子节点都是运算符
3. 叶子节点都是数字
4. 子树 = 表达式


中缀表达式
 -  [x] [expression-tree-build](https://www.lintcode.com/problem/expression-tree-build/)

后续遍历 = 后续表达式
前序遍历 = 前缀表达式

表达式求值

后缀表达式求值：遇到数字就存起来，遇到符号就运算。
- [x] [evaluate-reverse-polish-notation](https://www.leetcode.com/problems/evaluate-reverse-polish-notation/)


##### 两根指针
一个数组， 对撞
一个数组，同向
两个数组

1. 对撞形：
- [x] [two-sum-ii](https://www.lintcode.com/problem/two-sum-greater-than-target/description)
- [x] [triangle-count](https://www.lintcode.com/problem/triangle-count/)

灌水类：
- [x] [trapping-rain-water/](https://www.leetcode.com/problems/trapping-rain-water/)
- [x] [container with most water](https://www.leetcode.com/problems/container-with-most-water/) 
一样的也是小的那头移动

还有partition类。具体见初算9.7

---

Stack:
- [x] [flatten-nested-list-iterator](https://www.leetcode.com/problems/flatten-nested-list-iterator/description)


