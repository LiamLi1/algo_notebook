## Senior Algo Class 6
 ##### DP continue
 3. 博弈类
 - [ ] [coins-in-a-line](https://www.lintcode.com/problem/coins-in-a-line/)
 - [ ] [coins-in-a-line-ii](https://www.lintcode.com/problem/coins-in-a-line-ii/description)

4. 循环引用解决复杂dp
用local和global来优化
- [ ] [maximum-subarray](https://www.lintcode.com/problem/maximum-subarray/)
也可以用subsum, minsum来解决。
这里用local/global dp:
local[i+1] = max(num[i+1], local[i] + num[i+1])
global[i + 1] = max(local[i + 1], global[i])

- [ ] [best-time-to-buy-and-sell-stock-iv](https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-iv/)
- [ ] [maximum-product-subarray](https://www.lintcode.com/problem/maximum-product-subarray/)
要记录localmin 和 localmax

5. 区间动态规划
都是怎么把一个数组分成k段的问题。
每次更新dp[i][j], 需要遍历整个区间的情况。
有些情况可以用二分法（复杂版）。比如第一个，直接把$O(n^3)$ 优化成$O(nlogn)$

- [ ] [copy-books](https://www.lintcode.com/problem/copy-books/)
 dp[i][nk] 前i本书，nk个人去抄写的最小花费。
 dp[i][nk] = max{dp[j][nk - 1], w[j+1][i]}
 
 
 - [ ] [post-office-problem](https://www.lintcode.com/problem/post-office-problem/description)
 dp[i][nk] 前i个房子，用nk个邮局的最小花费。把i按顺序排列。
 dp[i][nk] = min{dp[j][nk - 1] + dis[j+1][i]}
 前j个房子，都走向nk-1个邮局。从第j+1开始到i，都走向第i个邮局。这样来算最小花费。
 
 6. 不从头开始，而是从长度为0的区间开始。把大数组拆分成小区间。小区间合并成大数组。
 
 - [ ] [longest-palindromic-subsequence](https://www.lintcode.com/problem/longest-palindromic-subsequence/description)
单sequence，但是
关键在于dp[i][j] 不再是前i项/j次，而是字符串从i到j的情况。
初始化为dp[i][i] == 1; dp[i][i+1]=1or2;
然后从dp[i][i + k]， k>=3开始算。

- [ ] [burst-balloons](https://www.lintcode.com/problem/burst-balloons/description) dp的状态表示。dp[i][j] 表示只剩下dp[i][j]的时候，能得到的最大值。

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