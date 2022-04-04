## Nine Chapter Class 6

### Linked List
mitbbs /careercup /glassdoor

- [x] [remove-duplicates-from-sorted-list](http://www.leetcode.com/problems/remove-duplicates-from-sorted-list)

##### 1. 查找
	1. head != null / head.next != null
	2. while(head.next != null) 

##### 2. 删除
 	pre/ cur/ next
 	pre.next = next; (pre.next.next)

- [x] [remove-duplicates-from-sorted-list-ii](http://www.leetcode.com/problems/remove-duplicates-from-sorted-list-ii)

##### 3. 头节点要改变，就要建立 dummy node
	dummy node -> head
	然后把 dummy node 看成 head

- [x] [reverse-linked-list](http://www.leetcode.com/problems/reverse-linked-list)
 
##### 4. swap(a, b) 和翻转
	// swap
	temp = b
	b = a
	a = temp
	// 翻转 (上左变下右/ 上右变下左)
	temp = head.next
	head.next = pre
	pre = head
	head = temp
- [xx] [reverse-linked-list-ii](http://www.leetcode.com/problems/reverse-linked-list-ii)

 - [x] [merge-two-sorted-lists](https://www.leetcode.com/problems/merge-two-sorted-lists/description)
 - [x] [partition-list](https://www.leetcode.com/problems/partition-list/description)

##### 5. sort
	merge sort
	主函数：
	1. 找中点
	2. 拆分
	3. 排序（递归）
	4. 合并 
递归的时间复杂度： 每一层的复杂度 $\times$ 有多少层
- [x] [sort-list](https://www.leetcode.com/problems/sort-list/description)

##### 6. 基本操作的组合
	1. 找中间节点
	2. 插入/删除
	3. 翻转
	4. 合并
- [x] [reorder-list](https://www.leetcode.com/problems/reorder-list/description)
分别用merge sort 和 quick sort

##### 7. 快慢指针

 - [x] [remove nth node from the end of list](https://www.leetcode.com/problems/remove-nth-node-from-end-of-list/description)
- [x] [middle of linked list](https://www.lintcode.com/problem/middle-of-linked-list/description)
- [x] [linked list cycle](https://www.leetcode.com/problems/linked-list-cycle/description)
- [x] [linked list cycle ii](https://www.leetcode.com/problems/linked-list-cycle-ii/description)
```
假设环的长度为l，环上入口距离链表头距离为a，两指针第一次相遇处距离环入口为b，则另一段环的长度为c=l-b，由于快指针走过的距离是慢指针的两倍，则有a+l+b=2*(a+b),又有l=b+c，可得a=c，故当判断有环时(slow==fast)时，从头移动慢指针，同时移动快指针，两指针相遇处即为环的入口。
```

##### 8. heap
- [x] [merge-k-sorted-lists](https://www.leetcode.com/problems/merge-k-sorted-lists/description)
- [x] merge and heap 


- [x] [copy-list-with-random-pointer](https://www.leetcode.com/problems/copy-list-with-random-pointer/)
- [ ] O(1)做一遍

- [x] [convert-sorted-list-to-binary-search-tree](https://www.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description) 用分治，n(logN)。用奇怪的递归，得到O(n)。
