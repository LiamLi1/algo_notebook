## Nine Chapter Class 4

### Dynamic Programming I

#### 1. Triangle

动态规划就是解决了重复计算的搜索。方式有：
1. 记忆化搜索
2. 循环


[Triangle](https://www.lintcode.com/problem/triangle/description) 五种解法 :carrot:
- [x] DFS
- [x] D&C
- [x] 记忆化搜索
- [x] 自底向上
- [x] 自顶向下

直接用DFS或者分治法，复杂度是 O($2^{n}$)。 
用动归优化以后，复杂度就只有O($n^{2}$)。 

#### 2. 面试经验
- 怎么想到用动归 (两个特点)
1. One of the following three
	a. Maximum\Minimum （最大\最小\最长...）
	b. Yes\No （能不能找到）
	c. Count(*) （一共有多少总走法）
2. Can not sort \ swap （不能排序\交换顺序）
- [ ] [Longest-consecutive-sequence](https://www.lintcode.com/problem/longest-consecutive-sequence/description)

#### 3. 动归四要素
1. 状态 State
灵感，创造力，存储小规模问题的结果
（走到某个地方的时候是什么值）
2. 方程 Function
状态之间的联系，怎么通过小的状态，来算大的状态
（小状态：离起点近，初始化时候得到的状态，不用计算直接得出的）
（大状态：最后求的目标）
3. 初始化 Intialization
最极限的小状态是什么, 起点
4. 答案 Answer
最大的那个状态是什么，终点

---
#### 四类题型

1. Matrix DP (15%)
2. Sequence (40%)
3. Two Sequences DP (40%)
4. Others (5%)

#### 1. Matrix DP
state: f[x][y] 表示我从起点走到坐标x,y……
function: 研究走到x,y这个点之前的一步
intialize: 起点
answer: 终点
1. path 类
- [x] [Minimum Path Sum](https://www.lintcode.com/problem/minimum-path-sum/description)
二维数组动态规划：初始化第一行和第一列
- [x] [Unique Paths](https://www.lintcode.com/problem/unique-paths)
- [x] [Unique Paths ii](https://www.lintcode.com/problem/unique-paths-ii)
- [ ] [Unique Paths iv](https://www.lintcode.com/problem/unique-path-iv/description)
取模放溢出时。对任何两个数相加可能溢出的情况，都需要取模。

2. square/rectangle 求最大面积。求最大frame等。记录每个点左边/上面有多少连续的1. 
- [ ] [maximal-square](https://www.lintcode.com/problem/maximal-square/description) 


#### 2. Sequence Dp
state: f[i]表示“前i”个位置/数字/字母,(以第i个为)...
function: f[i] = f[j] … j 是i之前的一个位置
intialize: f[0]..
answer: f[n-1]..

类型1：爬楼梯
- [x] [Climbing Stairs](https://www.lintcode.com/problem/climbing-stairs)
- [ ] [house-robber](https://www.lintcode.com/problem/house-robber/description)
只用一个dp数组就可以。其实是local和global化简得来的。

* 还是爬楼梯，但是是循环数组的类型
- [ ] [house-robber-ii](https://www.lintcode.com/problem/house-robber-ii/description)
从(0,n-1) ,(1-n)两个里面选。 


类型2：对下一个f[n], 需要遍历前面的f[n - 1]。
- [x] [Jump Game](https://www.lintcode.com/problem/jump-game) (可以用贪心做Greedy)
- [x] [Jump Game ii](https://www.lintcode.com/problem/jump-game-ii) (也可以用贪心做Greedy) 求最小值，但是有些情况没有解。求最小用无穷大。或者自定义一个数据结构来定义。
- [ ] [Palindrome Partitioning ii](https://www.lintcode.com/problem/palindrome-partitioning-ii/description) 用两次sequence dp
- [ ] [Word Break](https://www.lintcode.com/problem/word-break)