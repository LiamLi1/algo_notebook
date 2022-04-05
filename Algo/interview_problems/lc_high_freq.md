### Google & Microsoft highfreq(2022-03)
https://leetcode.com/problemset/all/?sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&companySlugs=google%2Cmicrosoft&page=1

- [r] [minimum-window-subsequence](https://leetcode.com/problems/minimum-window-subsequence/)
```
滚动数组复用时，需要重新初始化
```
- [x] [shortest-path-in-a-grid-with-obstacles-elimination](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/)
```
记忆化搜索不行。因为记忆会受路径影响（visited). 用BFS更好做。
```
- [r] [remove-comments](https://leetcode.com/problems/remove-comments/)
```
字符串处理
```
- [x] [https://leetcode.com/problems/number-of-islands/submissions/](number-of-islands)
```
bfs 进队的时候就要标记。不然会重复。
```
- [x] [serialize-and-deserialize-n-ary-tree/](https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/)
```
用preorder dfs容易做。也可用bfs，serialize 可读性强，但是写出来比较复杂。
```

- [x] [validate-stack-sequences](https://leetcode.com/problems/validate-stack-sequences/)
```
贪心
```
- [x] [encode-string-with-shortest-length/](https://leetcode.com/problems/encode-string-with-shortest-length/submissions/)
```
1.区间动态规划
2.找最小重复字符串的方法：
index = (tmp + tmp).find(tmp, 1)
size = len(tmp)
if index < len(tmp):
    replace = "{}[{}]".format(size // index, dp[i][i + index - 1])
```

- [ ] [sum-of-subarray-ranges](https://leetcode.com/problems/sum-of-subarray-ranges) 
```
单调栈 有点难
```

- [x] [remove-duplicate-letters/](https://leetcode.com/problems/remove-duplicate-letters/)
```
dfs会超时。用贪心+栈。考虑什么时候入栈。
```

- [x] [count-of-range-sum/](https://leetcode.com/problems/count-of-range-sum/) 
```
非二叉树的Divide and Conquer. （Merge & Sort）
¿¿¿ segment tree 的用法。离散化。一边插入一边搜索。
```


---
https://leetcode.com/company/google/

google high freq
- [ ] [https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/](https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/)||[ans](https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/discuss/1669895/C%2B%2B-solution-determine-to-flip-by-the-1st-row-and-1st-column-with-explanation)

### bitmask
```
bitmask 原意指用一个bit来修改数字
例如：
Mask:   10000000b
Value:  00000101b
---- OR ---------
Result: 10000101b

这里主要是把数字扁平化来存状态。然后再用这个状态来进行bfs/dfs memo

```
- [x] [minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/](https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)

