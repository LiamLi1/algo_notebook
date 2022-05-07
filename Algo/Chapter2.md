## Nine Chapter Class 2  
### 模板
### 1. Binary Search
```java
public int BinarySearch(int A[], int target){
	int start = 0;
	int end = A.size() - 1;
	int mid;
	
	while (start + 1 < end) {
		mid = start + (end - start) / 2;
		if (A[mid] == target) {
			start = mid;
		} else if (A[mid] < target) {
			start = mid;
		} else if (A[mid] > target) {
			end = mid;
		}
	}
	
	if (A[start] == target) {
		return start;
	}
	if (A[end] == target){
		return end;
	}
	
	return -1;
}
```

---
### Problems
- [xx] [search insert position](https://leetcode.com/problems/search-insert-position/)
- [ ] [search a 2d Matrix](https://www.leetcode.com/problems/search-a-2d-matrix/)
- [xx] [search a 2d Matrix ii](https://www.leetcode.com/problems/search-a-2d-matrix-ii/description)(递增矩阵, 不能用二分） 
- [ ] ~~[first bad version](https://www.leetcode.com/problems/first-bad-version/)~~
- [x] [find peak element](https://www.leetcode.com/problems/find-peak-element/) O(n) -> O(logn)  80% binary search


- [xx] [search-in-rotated-sorted-array](https://www.leetcode.com/problems/search-in-rotated-sorted-array/description) :memo: i.mid是否大于start ii.二分
- [ ] [search-in-rotated-sorted-array-ii](https://www.lintcode.com/problem/search-in-rotated-sorted-array-ii/description) (prove can only be in O(n))
- [x] [find minimum in rotated sorted array](https://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array/description)
- [x] [merge sorted array](https://www.lintcode.com/problem/merge-sorted-array/description)
- [x] merge sorted array ii
- [¿¿] [median of two sorted arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) :memo:
---


## 二刷
复杂的二分法：

- [ ] [copy-books](https://www.lintcode.com/problem/copy-books/description) 可以用区间类dp。也可以写一个check，然后对总时间二分。另外一道算距离就不好写check函数，所以不容易二分。