### 1.https://www.1point3acres.com/bbs/thread-791344-1-1.html
```
¿¿正方形组成题
类似后面的能拼成多少个正方形。看完回来一起想。
```
- [x] [minimum-knight-moves](https://leetcode.com/problems/minimum-knight-moves/)
```
可以用dfs/bfs。dfs的方法需要用马的走法来转换一下。感觉还dfs的方法还可以套dp。
解法容易理解，但是复杂度要想一下。因为用了memo，所以最坏的情况是走遍棋盘，并不是指数型增长。
```
- [x] [minimum-cost-to-connect-sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks/)
```
扩展题 区间dp 看完回来做
- [ ] [minimum-cost-to-merge-stones](https://leetcode.com/problems/minimum-cost-to-merge-stones/) 
```
- [x] [count-square-submatrices-with-all-ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)

- [x] [construct-binary-tree-from-inorder-and-postorder-traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

- [x] [construct-binary-tree-from-preorder-and-inorder-traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

### 2.https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=833146
- [x] [maximum-number-of-points-with-cost](https://leetcode.com/problems/maximum-number-of-points-with-cost/)
```
DP,max + for循环，可以只算一遍存下来化简。同stock/max subarray。
- [x] 用dfs+memo再来一遍：不行，一样是O(n^3)的复杂度。
```
- [x] [step-by-step-directions-from-a-binary-tree-node-to-another](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/)

### 3.https://www.1point3acres.com/bbs/thread-860809-1-1.html
```
round2
- part1: 让写一个Tree, 可以return a random node (O(1))
 - part2: 让写一个Tree, 可以return a random leaf (O(1)) insert-delete-getrandom-o1. 第二题可以用和最后一位交换删除的方法。

round4
part 1: shuffle("anyString" + anyChar) => newString,  判断 if we can obtain newString from `shuffle("anyString" + anyChar)`

“ABC” + anyChar => "BACD" (True)  因为加了一个D 然后Shuffle
“ABC” + anyChar => "BADD" (False)  

part 2: [oldString....] [newString....], return counter of pairs that statisfies part1 ((m*n)^2

(Strings only has 26 Chars, "A", "B"..."Z")
a = ["A", "B", ""]
b = ["AB", "AB", ""]

用counter来化简。可以再接一个count pair计数。空间开销比较高。
```
- [x] [stock-price-fluctuation/](https://leetcode.com/problems/stock-price-fluctuation/)


### 4.https://www.1point3acres.com/bbs/thread-857960-1-1.html
```

```
- [x] [race-car](https://leetcode.com/problems/race-car/)

### 5.https://www.1point3acres.com/bbs/thread-856992-1-1.html
```
#5-5 -> 同#3-1
用python sortedcontainers SortedList写一遍.
SortedList[index], 添加 删除 bisect_left 都是O(1).
感觉也可以用BST，但是很复杂（要找前后2，添加，删除node，还要想办法平衡）
```
- [x] [stream_delete_nums](./codes/stream_close_delete.py)
- [x] [shortest-path-in-a-grid-with-obstacles-elimination/](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/)

- [x] python sorted list (balanced binary tree)
- [x] python unit test

### 6.https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=838943 (股票题)
- [x] [stock-price-fluctuation/](https://leetcode.com/problems/stock-price-fluctuation/)

```
https://leetcode.com/problems/stock-price-fluctuation/discuss/1513293/Python-Clean-2-Heaps-Commented-Code
2 heap 解法。用了two heap模拟删除的思路。
```

### 7.https://www.1point3acres.com/bbs/thread-832915-1-1.html
```
1.餐厅排队系统：用hash + double linked list

2.每次pop medium，返回一个sorted array：每次medium一定是前后添加。用deque搞定。

3.cord tree

4.list of queues，pop()操作很expensive，尽量少用，让你找最短的queue，follow up找最小sum的queue
   # 用一个heap来存当前sum最小的是哪个queue，谁小就pop谁，直到有一个queue空掉

```
- [x] [cord tree string](./cord_segment_tree.py)

### 8.https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=831560&ctid=232507

```
字符串 第一轮 之前别人发过的，字符转换，定义F(str)是str permutation 再加上一个字母，比如ABC -> CBEA，给定俩字符串判断B=F(A) 是true还是false。同3-4
```
- [x] [maximum-swap/](https://leetcode.com/problems/maximum-swap/)

- [ ] [tiling-a-rectangle-with-the-fewest-squares/](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/)

- [ ] 实现 grep?


### 9.https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=831346&ctid=232507 1道没看懂，1道dfs
```
1.给你一个一个数组，其中的每一个元素代表一个player。举例：[1,2,3,4] ,  有4个player，player 1先和player 2比，player 3和player 4比，赢的人再互相比。直到剩下最后一个人为止。然后再给你一个概率的matrix 比如matrix[1][2] = 0.7 就代表了player1和player2比，player1赢得概率是0.7。求最终最有可能获胜的选手。
dfs 递归


```
- [ ] [strings-differ-by-one-character/](https://leetcode.com/problems/strings-differ-by-one-character/)
```
Trie树变形? 不可行。依然要搜索所有点，复杂度更高。
还是存wild card到dict比较好用
很可能要想到hash才行
另外一道类似的题/permutation string match 就可以用trie。用这个题的方法。
可以用Trie树来练习permutation string match。
```
- [ ][skyline]

### 10.https://www.1point3acres.com/bbs/thread-831180-2-1.html

### 11.https://www.1point3acres.com/bbs/thread-826273-1-1.html
```
字符串 permutation 比较题
https://leetcode.com/problems/strings-differ-by-one-character/
```

### 12.https://www.1point3acres.com/bbs/thread-805786-1-1.html
### 13.https://www.1point3acres.com/bbs/thread-558122-1-1.html

### 14.https://www.1point3acres.com/bbs/thread-355550-1-1.html
```
矩形填充
https://github.com/grandyang/leetcode/issues/1240
```
- [ ] [tiling-a-rectangle-with-the-fewest-squares/](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/)


### 15.https://www.1point3acres.com/bbs/thread-879616-1-1.html
猜词题
- [x] [guess-the-word/](https://leetcode.com/problems/guess-the-word/)
```
概率计算的方法
```
- [ ] [rectangle-area-ii/](https://leetcode.com/problems/rectangle-area-ii/)扫描线 动态维护区间长度
- [x] [word-search-ii/](https://leetcode.com/problems/word-search-ii/)
- [x] [interval-list-intersections/](https://leetcode.com/problems/interval-list-intersections/) 两个指针/扫描线
- [x] [palindrome-partitioning-ii/](https://leetcode.com/problems/palindrome-partitioning-ii/)
- [x] [stamping-the-grid/](https://leetcode.com/problems/stamping-the-grid/)




### 16.https://www.1point3acres.com/bbs/thread-468115-1-1.html 
```
¿¿很复杂的计算正方形个数
https://www.1point3acres.com/bbs/thread-870576-1-1.html

```

### 17.https://www.1point3acres.com/bbs/thread-873383-1-1.html

```
这个比较简单。Binary chain node/race car/string cipher/https://leetcode.com/problems/evaluate-reverse-polish-notation/
```

### 18.https://www.1point3acres.com/bbs/thread-870974-1-1.html
```
第二题可以考虑treemap+merge interval。自己写一遍
```
- [ ] [interleaving-string/](https://leetcode.com/problems/interleaving-string/)

- [ ] [binary-tree-coloring-game/](https://leetcode.com/problems/binary-tree-coloring-game/)

### 19.https://www.1point3acres.com/bbs/thread-886633-1-1.html

- [ ] [logger-rate-limiter](https://leetcode.com/problems/logger-rate-limiter/)
- [ ] [minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix](https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)

### 20.https://www.1point3acres.com/bbs/thread-888104-1-1.html
- [x] [combinations/](https://leetcode.com/problems/combinations/)

### 21.https://www.1point3acres.com/bbs/thread-887516-1-1.html
- [ ] [stock-price-fluctuation/](https://leetcode.com/problems/stock-price-fluctuation/)

- [ ] [meeting-rooms-ii/]https://leetcode.com/problems/meeting-rooms-ii/

### 22.https://www.1point3acres.com/bbs/thread-886985-1-1.html
- [x] [reverse-bits/](https://leetcode.com/problems/reverse-bits/)

- [x] [race-car/](https://leetcode.com/problems/race-car/)
```
线段-》矩形面积 换算， 类似于#16的那道题
```

### 23.https://www.1point3acres.com/bbs/thread-886985-1-1.html
```
https://leetcode.com/discuss/interview-question/1320700/Determine-if-a-string-can-be-shrunk-to-1-character-after-a-series-of-deletions
```
- [x] [longest-string-chain/](https://leetcode.com/problems/longest-string-chain/)
- [x] [exclusive-time-of-functions/](https://leetcode.com/problems/exclusive-time-of-functions/)

### 24
```python
# find right sibling in binary tree with parent pointer
https://www.geeksforgeeks.org/find-right-sibling-binary-tree-parent-pointers/
```

### 25 https://www.1point3acres.com/bbs/thread-892931-1-1.html
```
1.完美二叉树构造
```
- [x] [number-of-islands-ii/](https://leetcode.com/problems/number-of-islands-ii/) 
```
i. number of water -> reversily do it
follow up: minimal remove to get 1.
```

### 26 https://www.1point3acres.com/bbs/thread-852833-1-1.html
```
https://leetcode.com/discuss/interview-question/1920662/Google-or-Phone-or-Calculate-Total-Wait-Time

```
- [x] [total wait time](./codes/wait_time.py)
