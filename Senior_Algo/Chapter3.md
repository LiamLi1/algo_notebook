## Senior Algo Class 3
   
线段树：
```python
class Solution:
    class SegmentTreeNode:
        def __init__(self, start, end, count):
            self.start, self.end, self.count = start, end, count
            self.left, self.right = None, None
        
    """
    @param A: A list of integer
    @return: The number of element in the array that 
             are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        
        # build segmeng tree
        root = self.build(0, 10000)
        result = []
        
        # modify count value for each
        for num in A:
            self.modify(root, num, 1)
        
        for i in queries:
            count = 0
            if i > 0:
                count = self.query(root, 0, i - 1)
            result.append(count)
        
        return result
    
    def build(self, start, end):
        if start >= end:
            return SegmentTreeNode(start, end, 0)
        root = SegmentTreeNode(start, end, 0)
        mid = start + (end - start) / 2
        root.left = self.build(start, mid)
        root.right = self.build(mid + 1, end)
        return root
    
    def modify(self, root, index, value):
        if root.start == index and root.end == index:
            root.count += value
            return
        # query
        mid = root.start + (root.end - root.start) / 2
        if index <= mid:
            self.modify(root.left, index, value)
        
        if mid < index:
            self.modify(root.right, index, value)
        root.count = root.left.count + root.right.count
    
    def query(self, root, start, end):
        if start == root.start and end == root.end:
            return root.count
        
        mid = root.start + (root.end - root.start) / 2
        if end <= mid:
            return self.query(root.left, start, end)
        
        if start > mid:
            return self.query(root.right, start, end)
            
        return self.query(root.left, start, mid) + \
            self.query(root.right, mid + 1, end)
```
- [x] [Count of smaller number](https://www.lintcode.com/problem/count-of-smaller-number/)
- [x] [Count of smaller number-after-itself](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
由于data value 限制在0-10000， 所以用计数型复杂度更低。每次查询，查找(0,A[i] - 1) 的计数。查找以后，A[i]这个点计数加一。写modify/query两个函数即可。

- [ ] [construction-queue](https://www.lintcode.com/problem/construction-queue/description) 要调用内联class的静态方法，则内联class也要弄成static的。
线段树的高级应用。:cow:

count形。查询count个数的位置。
初始化线段树，从1到n，每个点都是1. 从最大的数开始查询count。因为每个数都比它小，所以查到count的点就是它的位置。然后查第二小的数。刚刚最大数占的位置的数比它大了，所以那个点的值更新为0. 
这样query函数要兼顾查询和修改的功能。

- [xx] [count-of-range-sum/](https://leetcode.com/problems/count-of-range-sum/)

```
1.也可以用递归，难想好写
2.需要保留前后顺序的时候，可以从最后一个开始往前增加元素
3.用（2）的思路，也可以用二分查找来做。但是添加元素的操作会是O(n)，最后还是O(N^2).

离散化线断树的思路：
用sorted array valSet一一对应。TreeNode用min/max代替start/end。其中min=valSet[start], max=valSet[end]
build的时候还是用start，end。
query/update的时候就可以直接用min/max
```

树状数组：binary indexed tree 见Onenote
要注意的是，序号从1开始。线段树可以直接查区间，可以最大/最小/求和/计数（计数就是求和的一种），树状数组只能从开始到某一点，只能求和。
```java

class IndexedTree{
	private int[] c; 
	// 只需要维护c[i], 用a[]和add来build, c[i]来求和
	// 要注意c[i]只能从1开始计数。
	
	private int lowbit(int i) {
		return i & (-i);
	}

	public int sum(int x) {
		int s = 0;
		for (int i = x; i >= 0; i -= lowbit(i)) {
			s += c[i];
		}
		return s;
	}

	public int add(int x, int delta) {
		for (int i = x; i <= n; i += lowbit(i)) {
			c[i] += delta;
		}
	}

}
```

Heap
- [x] [trapping-rain-water/](https://www.leetcode.com/problems/trapping-rain-water/)

不用stack也可以，两个指针

- [ ] [trapping-rain-water-ii/](https://www.leetcode.com/problems/trapping-rain-water-ii/)

要用堆来灌水。最小值堆来定义外围。然后从外向内灌水

Cord Tree 谷歌面经(https://www.1point3acres.com/bbs/thread-856992-1-1.html)
```
```

递归
- [x] [convert-sorted-list-to-binary-search-tree/](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)

- [ ] [count-of-range-sum/](https://leetcode.com/problems/count-of-range-sum/)
