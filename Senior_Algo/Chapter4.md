## Senior Algo Class 4
##### Hash Heap



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
// 有Node以后就可以存重复元素了。
```
*可以用TreeSet 来代替Hash Heap. 方法是在比较的时候加入unique的变量，这样就可以处理重复元素了*


- [ ] [the-skyline-problem](https://www.lintcode.com/problem/the-skyline-problem/description)

- [x] [sliding-window-median](https://www.lintcode.com/problem/sliding-window-median)
固定滑动窗口问题： 1. 增加元素 2. 删除元素
---
##### Deque
- [x] [sliding-window-maximum](https://www.lintcode.com/problem/sliding-window-maximum/description)
$O(n)$ 时间复杂度，只有栈和队列
可以维护一个递减栈，但是还要有一个front_peek和front_pop操作，所以用deque。


##### Stack
找左边/右边 第一个比它大/小的元素
- [x] [max-tree](https://www.lintcode.com/problem/max-tree/description)
- [x] [histogram](https://www.lintcode.com/problem/largest-rectangle-in-histogram/)

表达式树
1. 二叉树
2. 非叶子节点都是运算符
3. 叶子节点都是数字
4. 子树 = 表达式


中缀表达式
![26b008a3.png](:storage\278fae5f-0a52-4d46-a9fc-bfa3096d31bc\71721465.png)
按照优先级，建立最小值树，可以得到中缀表达式树。
![87db0620.png](:storage\278fae5f-0a52-4d46-a9fc-bfa3096d31bc\87db0620.png)

 -  [ ] [expression-tree-build](https://www.lintcode.com/problem/expression-tree-build/)

后续遍历 = 后续表达式
前序遍历 = 前缀表达式

表达式求值

后缀表达式求值：遇到数字就存起来，遇到符号就运算。
- [x] [evaluate-reverse-polish-notation](https://www.lintcode.com/problem/evaluate-reverse-polish-notation/)

- [x] [expression-evaluation/](https://www.lintcode.com/problem/expression-evaluation/)


##### 两根指针
一个数组， 对撞
一个数组，同向
两个数组

1. 对撞形：
- [x] [two-sum-ii](https://www.lintcode.com/problem/two-sum-greater-than-target/description)
- [x] [triangle-count](https://www.lintcode.com/problem/triangle-count/)
灌水类：
- [x] [trapping-rain-water/](https://www.lintcode.com/problem/trapping-rain-water/)
- [x] [container with most water](https://www.lintcode.com/problem/container-with-most-water/) 
一样的也是小的那头移动

还有partition类。具体见初算9.7

---

Stack:
- [ ] [flatten-nested-list-iterator](https://www.lintcode.com/problem/flatten-nested-list-iterator/description)


