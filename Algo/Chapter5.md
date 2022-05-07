## Nine Chapter Class 5

### Dynamic Programming II
subarray的题在senior7中有单独讨论。一般不是dp，有可能是线段树或者map/subsum等记录中间状态。比如下面这道题，就是用min_subsum 和 subsum来做成O(n)。
- [x] [Maximum Subarray](http://www.leetcode.com/problems/maximum-subarray)


#### 3. Two Sequences DP
state: f[i][j]代表了第一个sequence的前i个数字
/字符 配上第二个sequence的前j个...
function: f[i][j] = 研究第i个和第j个的匹配关系
intialize: f[i][0] 和 f[0][i]
answer: f[s1.length()][s2.length()]

- [x] [Longest Common Subsequence](http://www.leetcode.com/problems/longest-common-subsequence) (Array (Substring)是连续的。Sequence则不是)
- [x] [Longest Common Substring](http://www.lintcode.com/problem/longest-common-substring) 
- [xx] [Edit Distance](http://www.leetcode.com/problems/edit-distance) f[i][j]表示第一个字符串的前i个字符，配上第二个字符串的前j个字符的edit distance最小是多少。
EditDistance(A,B) = MAXLEN(A,B) - LCS(A,B)
- [xx] [Distinct Subsequences](http://www.leetcode.com/problems/distinct-subsequences) 

滚动数组，二维情况也可以像一维一样用。但是如果和当前行有关，则必须每次开始前都初始化。

NO 不能用记忆化搜索。和reg expression 不一样，不是之和后面的一步有关。

- [xx] [interleaving-string](http://www.leetcode.com/problems/interleaving-string) 
- [x] 记忆化搜索/ dp 都做一次


- [x] [Wildcard Matching](http://www.leetcode.com/problems/wildcard-matching) 
- [x] :carrot: 记忆化搜索/ dp 都做一次
- [xx] [regular-expression-matching](https://www.leetcode.com/problems/regular-expression-matching/description) 
用dfs + 记忆华搜索解决更容易。因为不确定*的情况要往回走几步。注意在dfs里只能往前，不能回头。

总结：
1. 如果只和后面一步有关，可以用记忆化搜索。如果只和前面的一步有关，可以动归。
2. 记忆化搜索不用初始化。其实就是dfs递归，把结束条件写在前面，避免数组超出范围。
 
#### 4. Backpack
state: f[i][j]“前i“个数，取出一些能否组成和为j
function: f[i][j] = f[i-1][j - a[i]] or f[i-1][j]
initialize: f[x][0] = true; f[0][1...m] = false
answer: 能够使得f[n][X]最大的X （0 <= X <= m)


- [x] [*Backpack](http://www.lintcode.com/problem/backpack) 考虑如何省空间（取模做成滚动数组）
- [x] [*Backpack II](http://www.lintcode.com/problem/backpack-ii) 
- [x] 背包求具体方案（回溯）
- [x] [k-sum](http://www.lintcode.com/problem/k-sum/)
- [x] [Minimum Adjustment Cost](http://www.lintcode.com/problem/minimum-adjustment-cost/) 

#### Conclusion

- Recursive VS DP:
递归是一种程序的实现方式，即函数的自我调用
动归是一种方法：大规模问题的结果由小规模结果计算而来。主要是用来优化，减少搜索的次数。动归可以由递归来实现（Memorization Search）


#### 补充题：
minmax 博弈类
- [x] [the game of take numbers](https://leetcode.com/problems/predict-the-winner/) i 表示长度， j表示start point, f[i][j] 表示A最大能取得的优势
- [ ] 把空间优化到一维

---
## 刷题
senior 中还有6种题型的总结


- [ ] [scramble-string](https://www.lintcode.com/problem/scramble-string/description)
除了dp，还可以用记忆化搜索/dfs等方法来做。
所搜的难点在于判定scramble的方式。怎么记忆。
简单粗暴的方法，直接存一个Map<String, boolean>

dp的难点是想状态。
f[i][j][k], s1的i开始，s2的j开始，长度为k。


- [ ] [burst-balloons](https://www.lintcode.com/problem/burst-balloons/description)
dp的状态表示。dp[i][j] 表示只剩下i,j, i + 1 ~ j - 1都爆掉的时候，能得到的最大值。
所以dp[i][i] = 0. dp[i][i + 1] = 0. 只有三个以上的情况才有值。在原数组前后都加一个1， 然后再来dp。不太好想到这一层。

dp[i][j]的这个状态，和上题一样，既可以当作dp的状态，又可以当作dfs的memo。本质上两个是一样的。dfs是从大到小，dp则是从小（不会再往回的状态）到大。

- [ ] [largest-sum-of-averages](https://www.lintcode.com/problem/largest-sum-of-averages/description)
```java
//区间划分形的模板

// dp中，用实际次数/实际前i项作为下标
// 次数放最外层， 从2开始。
//i表示前i项，所以要从k开始。
//j表示前j项，所以要从k - 1 开始，并小于i。
// 用dp[k - 1][j] 来更新dp[k][i]即可

class Solution {
    public double largestSumOfAverages(int[] A, int K) {
        int n = A.length;
        double[][] dp = new double[K + 1][n + 1];
        double[] sum = new double[n + 1];
        for (int i = 1; i <= n; i++) {
            sum[i] = sum[i - 1] + A[i - 1];
            dp[1][i] = sum[i] / i;
        }
        
        for (int k = 2; k <= K; k++) {
            for (int i = k; i <= n; i++) {
                for (int j = k - 1; j < i; j++) {
                    dp[k][i] = Math.max(dp[k][i], dp[k - 1][j] + (sum[i] - sum[j]) / (i - j));
                }
            }
        }
        return dp[K][n];
    }
}

```


- [ ] [dyeing-problem](https://www.lintcode.com/problem/dyeing-problem/description) 1. cycle数组。2.乘法容易越界。本身是到非常规dp，考数学。

- [ ] [Longest Increasing Subsequence](https://www.lintcode.com/problem/longest-increasing-subsequence) 从中间往两边扩展

- [ ] [maximum-product-subarray](https://www.lintcode.com/problem/maximum-product-subarray/description)


- [ ] [valid-palindrome-iii/](https://leetcode.com/problems/valid-palindrome-iii/) 
```
用dfs更直观。也可以看成有条件的edit distance。
```


