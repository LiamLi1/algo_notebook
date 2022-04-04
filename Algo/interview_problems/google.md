### 1.https://www.1point3acres.com/bbs/thread-791344-1-1.html
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

### 4.https://www.1point3acres.com/bbs/thread-857960-1-1.html
- [x] [race-car](https://leetcode.com/problems/race-car/)

### 5.https://www.1point3acres.com/bbs/thread-856992-1-1.html
- [ ] [shortest-path-in-a-grid-with-obstacles-elimination/](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/)

- [ ] python sorted list (balanced binary tree)

- [ ] python unit test

### 6.https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=838943 (股票题)
- [x] [stock-price-fluctuation/](https://leetcode.com/problems/stock-price-fluctuation/)

```
https://leetcode.com/problems/stock-price-fluctuation/discuss/1513293/Python-Clean-2-Heaps-Commented-Code
2 heap 解法。用了two heap模拟删除的思路。
```

### 7.https://www.1point3acres.com/bbs/thread-832915-1-1.html
- [x] [cord tree string](./cord_segment_tree.py)

### 8.https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=831560&ctid=232507

```
字符串 permutation 比较题
```
- [ ] [strings-differ-by-one-character/](https://leetcode.com/problems/strings-differ-by-one-character/)
- [x] [maximum-swap/](https://leetcode.com/problems/maximum-swap/)

- [ ] [tiling-a-rectangle-with-the-fewest-squares/](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/)

- [ ] 实现 grep


### 9.https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=831346&ctid=232507 1道没看懂，1道dfs
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