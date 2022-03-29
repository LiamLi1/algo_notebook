## Senior Algo Class 5

##### 2.向前型指针:
##### (1)窗口类指针
一个left/一个right，统计left 和 right之间的状态。
比如longest substring without repeating characters.
用一个count来统计有没有repeat。
```java
while (i < n-1){   
  while(j < n-1){     
    if(满足条件)         
       j++;          
      更新状态     
    else(不满足条件)         
    break;   
    }   
  i++;   
  更新状态 
  }

```
- [x] [minimum-size-subarray-sum](https://www.leetcode.com/problems/minimum-size-subarray-sum/)
 - [x] [longest-substring-without-repeating-characters](https://www.leetcode.com/problems/longest-substring-without-repeating-characters/)
 HashMap 中输入字符可以直接计算其ascii值
 
- [x] [minimum-window-substring](https://www.leetcode.com/problems/minimum-window-substring/)
 ##### (2)快慢指针
##### 3.两个数组 两个指针

- [x] [the-smallest-difference](https://www.lintcode.com/problem/the-smallest-difference/description) 贪心


 ##### 动态规划
 
 1. 常规动态规划 + 空间优化
 不好想的时候，考虑用记忆化搜索。

 - [x]  [house robber](https://www.leetcode.com/problems/house-robber/)
 滚动数组的长度由最长滞后项的滞后数决定。
 - [X] [maximal square](https://www.leetcode.com/problems/maximal-square/description)
 dp[i][j], (i,j) 最大正方形。
 dp[i][j] = dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]

2. 记忆化搜索：
状态转移麻烦，不是顺序的 / 初始化都不好找的时候

- [x] [longest-continuous-increasing-subsequence-ii](https://www.lintcode.com/problem/longest-continuous-increasing-subsequence-ii/description)
dfs 向四面走也没关系。只要定义好记忆化搜索和返回条件。

