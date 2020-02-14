## Nine Chapter Class 6

### Linked List
mitbbs /careercup /glassdoor

- [x] [remove-duplicates-from-sorted-list](http://www.lintcode.com/problem/remove-duplicates-from-sorted-list)

##### 1. 查找
	1. head != null / head.next != null
	2. while(head.next != null) 

##### 2. 删除
 	pre/ cur/ next
 	pre.next = next; (pre.next.next)

- [x] [remove-duplicates-from-sorted-list-ii](http://www.lintcode.com/problem/remove-duplicates-from-sorted-list-ii)

##### 3. 头节点要改变，就要建立 dummy node
	dummy node -> head
	然后把 dummy node 看成 head

- [x] [reverse-linked-list](http://www.lintcode.com/problem/reverse-linked-list)
![12348ba4.png](:storage\7dcdc590-9c4d-44b9-88e0-6198c9105623\8c4d4865.png)
 
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
- [x] [reverse-linked-list-ii](http://www.lintcode.com/problem/reverse-linked-list-ii)
- [x] :carrot:

 - [x] [merge-two-sorted-lists](https://www.lintcode.com/problem/merge-two-sorted-lists/description)
 - [x] [partition-list](https://www.lintcode.com/problem/partition-list/description)

##### 5. sort
	merge sort
	主函数：
	1. 找中点
	2. 拆分
	3. 排序（递归）
	4. 合并 
递归的时间复杂度： 每一层的复杂度 $\times$ 有多少层
- [x] [sort-list](https://www.lintcode.com/problem/sort-list/description)
- [x] :carrot: 快排/归并 各做一次
##### 6. 基本操作的组合
	1. 找中间节点
	2. 插入/删除
	3. 翻转
	4. 合并
- [x] [reorder-list](https://www.lintcode.com/problem/reorder-list/description)
分别用merge sort 和 quick sort

##### 7. 快慢指针

 - [x] [remove nth node from the end of list](https://www.lintcode.com/problem/remove-nth-node-from-end-of-list/description)
- [x] [middle of linked list](https://www.lintcode.com/problem/middle-of-linked-list/description)
- [x] [linked list cycle](https://www.lintcode.com/problem/linked-list-cycle/description)
- [x] [linked list cycle ii](https://www.lintcode.com/problem/linked-list-cycle-ii/description):notebook:
快指针从head.next 开始走。 交点过后看slow.next == head

##### 8. heap
- [x] [merge-k-sorted-lists](https://www.lintcode.com/problem/merge-k-sorted-lists/description)(heap)


- [x] [copy-list-with-random-pointer](https://www.lintcode.com/problem/copy-list-with-random-pointer/)
- [x] [convert-sorted-list-to-binary-search-tree](https://www.lintcode.com/problem/convert-sorted-list-to-binary-search-tree/description) 用分治，n(logN)。用奇怪的递归，得到O(n)。:notebook:
- [x] :carrot:
