## Senior Algo Class 3
   
线段树：
- [x] [Count of smaller number](https://www.lintcode.com/problem/count-of-smaller-number/)
- [x] [Count of smaller number-before-itself](https://www.lintcode.com/problem/count-of-smaller-number-before-itself/)
由于data value 限制在0-10000， 所以用计数型复杂度更低。每次查询，查找(0,A[i] - 1) 的计数。查找以后，A[i]这个点计数加一。写modify/query两个函数即可。

- [ ] [construction-queue](https://www.lintcode.com/problem/construction-queue/description) 要调用内联class的静态方法，则内联class也要弄成static的。
线段树的高级应用。:cow:

count形。查询count个数的位置。
初始化线段树，从1到n，每个点都是1. 从最大的数开始查询count。因为每个数都比它小，所以查到count的点就是它的位置。然后查第二小的数。刚刚最大数占的位置的数比它大了，所以那个点的值更新为0. 
这样query函数要兼顾查询和修改的功能。





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
