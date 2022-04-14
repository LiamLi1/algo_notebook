## Senior Algo Class 6
 ##### DP continue
 3. 博弈类
 - [x] [coins-in-a-line](https://www.lintcode.com/problem/coins-in-a-line/)
 - [x] [coins-in-a-line-ii](https://www.lintcode.com/problem/coins-in-a-line-ii/description)

4. 循环引用解决复杂dp
用local和global来优化
- [x] [maximum-product-subarray](https://www.leetcode.com/problems/maximum-product-subarray/)

下面的都可以从$O(N^{3})$ -> $O(N^{2})$
- [¿¿] [maximum-subarray-iii](https://www.lintcode.com/problem/maximum-subarray-iii/)
```
最后两层的for loop，要同方向。不然不好化简。
```
- [¿¿] [best-time-to-buy-and-sell-stock-iv](https://www.leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)
要记录localmin 和 localmax
- [x] [maximum-number-of-points-with-cost](https://leetcode.com/problems/maximum-number-of-points-with-cost/) 狗家面经

5. 区间动态规划
都是怎么把一个数组分成k段的问题。
每次更新dp[i][j], 需要遍历整个区间的情况。
有些情况可以用二分法（复杂版）。比如第一个，直接把$O(n^3)$ 优化成$O(nlogn)$

- [x] [copy-books](https://www.lintcode.com/problem/copy-books/)
 
 ```
 贪心+二分也可以做。验证时间时用贪心。
 
 dp：
 dp[i][nk] 前i本书，nk个人去抄写的最小花费。
 dp[i][nk] = max{dp[j][nk - 1], w[j+1][i]}
 ```
 - [ ] [post-office-problem](https://www.lintcode.com/problem/build-post-office-problem/description)
 dp[i][nk] 前i个房子，用nk个邮局的最小花费。把i按顺序排列。
 dp[i][nk] = min{dp[j][nk - 1] + dis[j+1][i]}
 前j个房子，都走向nk-1个邮局。从第j+1开始到i，都走向第i个邮局。这样来算最小花费。
 
 6. 不从头开始，而是从长度为0的区间开始。把大数组拆分成小区间。小区间合并成大数组。
 
 - [x] [longest-palindromic-subsequence](https://www.leetcode.com/problems/longest-palindromic-subsequence/description)
单sequence，但是
关键在于dp[i][j] 不再是前i项/j次，而是字符串从i到j的情况。
初始化为dp[i][i] == 1; dp[i][i+1]=1or2;
然后从dp[i][i + k]， k>=3开始算。

```
区间dp的循环方式也可以是
for i in range(size - 1,-1,-1):
    for j in range(i + 1,size):
```

- [x] [burst-balloons](https://www.leetcode.com/problems/burst-balloons/description) dp的状态表示。dp[i][j] 表示只剩下dp[i][j]的时候，能得到的最大值。
```
同样区间循环，三层，用上面的方法写。
```

7.“贡献度” DP:
- [ ] [count-unique-characters-of-all-substrings-of-a-given-string/](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/)
```
求所有subarry的某个特征的时候，可以考虑用这个方法。
暴力接发是在创建subarray的时候同步update关键feature。
```

 ---

 
 
 ##### Follow Up Questions
 ##### 1. Partition 思想
 [nuts-bolts-problem](https://www.lintcode.com/problem/nuts-bolts-problem/)
 [Kth-largest-element-in-an-array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
 [Medianth 题解](https://www.jiuzhang.com/solution/median/)
 
 ##### 2. Median follow up
 [sliding-window-median](https://www.lintcode.com/problem/sliding-window-median/description)

  [median](https://www.lintcode.com/problem/median/description)

  [median-of-two-sorted-arrays/description](https://www.lintcode.com/problem/median-of-two-sorted-arrays/description)
  
  [data-stream-median](https://www.lintcode.com/problem/data-stream-median/description)