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
- [x] [search insert position](https://www.lintcode.com/problem/search-insert-position/description)
- [x] [search a 2d Matrix](https://www.lintcode.com/problem/search-a-2d-matrix/)
- [x] [search a 2d Matrix ii](https://www.lintcode.com/problem/search-a-2d-matrix-ii/description)(递增矩阵） 
- [x] [first bad version](https://www.lintcode.com/problem/first-bad-version/)
- [x] [find peak element](https://www.lintcode.com/problem/find-peak-element/) O(n) -> O(logn)  80% binary search


- [x] [search-in-rotated-sorted-array](https://www.lintcode.com/problem/search-in-rotated-sorted-array/description) :memo: 通过mid是否大于start，再进一步二分。
- [x] [search-in-rotated-sorted-array-ii](https://www.lintcode.com/problem/search-in-rotated-sorted-array-ii/description) (prove can only be in O(n))
- [x] [find minimum in rotated sorted array](https://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array/description)
- [x] [merge sorted array](https://www.lintcode.com/problem/merge-sorted-array/description)
- [x] merge sorted array ii
- [x] [median of two sorted arrays](https://www.lintcode.com/problem/median-of-two-sorted-arrays/) :memo:
---


## 二刷
复杂的二分法：

- [ ] [copy-books](https://www.lintcode.com/problem/copy-books/description) 可以用区间类dp。也可以写一个check，然后对总时间二分。另外一道算距离就不好写check函数，所以不容易二分。