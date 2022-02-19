## Nine Chapter Class 7

Graph & Search
##### 1. Clone Graph
 - [x] [clone-graph](https://www.leetcode.com/problems/clone-graph/description)
 
 克隆点和克隆边分开
 遍历图：用BFS比DFS好。
 - [x] [copy-list-with-random-pointer](https://www.leetcode.com/problems/copy-list-with-random-pointer/) 

##### 2. 拓扑排序 
入度/出度 有多少边可以入/出
- [x] [topological-sorting](https://www.lintcode.com/problem/topological-sorting/description)

- [x] 拓扑dfs/bfs。需要带条件看需不需要进入

-  [x] [$minimum-height-trees](https://www.leetcode.com/problems/minimum-height-trees/)
也是拓扑排序的题/从叶子结点往上BFS来找，可以找到最短树
- [ ] retry 


##### 3. Search
- [x] [permutations](https://www.leetcode.com/problems/permutations/description)一般这种问题都用深度优先搜索。深度优先搜索树$O(N!)$
- [x] [subsets](https://www.leetcode.com/problems/subsets/description)时间复杂度是$O(2^{n})$
- [x] [N-Queens](https://www.leetcode.com/problems/n-queens/description) 减枝


- [x] [subsets-ii](https://www.leetcode.com/problems/subsets-ii/description)
- [x] [palindrome-partitioning](https://www.leetcode.com/problems/palindrome-partitioning/description)
- [x] [combination sum](https://www.leetcode.com/problems/combination-sum/description)
- [x] [combination sum ii](https://www.leetcode.com/problems/combination-sum-ii/description)
- [x] [word ladder](https://www.leetcode.com/problems/word-ladder/description) 最短路径用BFS！


思路：简单图找最短路径，要用BFS。如果用DFS的复杂度是O($2^n$)， 而用BFS复杂度是O(N)
之前用的搜索（permutation/combination) 都是DFS。利用visited和for循环的方式得到结果。
求最短的话就不要用把所有的情况列出来比较了。直接BFS就可以。

1. 看是否与dict中的单词能转换: 
两种方法:
第一是遍历字典中的单词。复杂度(len * k)
第二种是对每个字符做替换，然后看字典里有没有。复杂度(26 * len)
这里应该都用第二种，假设字典比较大。
2. 确定长度：可以用记录queue长度， 一次性全部出队的方法。也可以用一个Map同时担当visited 和计数的作用。通用的方法是用哨兵。每一批次入队以后加一个变量sentinel， 遇到sentinel就总步数加一，然后队列再入一个sentinel
3. 双向BFS， 从target和start分别bfs。效果是可以让复杂度减少。$2 \times O(b^{d/2})$, 显著小于$O(b^{d})$
4. 多源bfs。可以用BitSet来追踪当前状态。


- [x] [word ladder-ii](https://www.leetcode.com/problems/word-ladder-ii/description)
- [ ] retry

BFS to search the shortest routes and record the distance of each node to the start.
DFS to traverse routes, it is only a valid next node if the distance of node is decreasing. Record all possible nodes for the same distance to destination.
最短路径+回溯


##### 5. 最小支撑树
UnionFind + PriorityQueue来做。

- [x] [minimum-risk-path](https://www.lintcode.com/problem/minimum-risk-path/description)
https://blog.csdn.net/luoshixian099/article/details/51908175

##### 6. 两点间最短距离（有权图）

- [x] [network-delay-time](https://leetcode.com/problems/network-delay-time/)



Dijkstra
求一个顶点到所有定点的最短路径
从起始点开始，用一个优先队列存相邻的点的距离。每次弹出一个最近的点，然后把它相邻的点的距离更新，并把没有走过的做BFS。如果走过或者距离长就不用再走了。

7.求所有顶点到所有定点的最短路径
Floyd

- [x] [sum-of-distances-in-tree](https://leetcode.com/problems/sum-of-distances-in-tree/submissions/) 可以用来练习。但是真的用Floyd要超时。
这里是树（树是一幅无环连通图）。可以用两次dfs来求解。
   
 Floyd-Warshall算法的时间复杂度為 ${ O(N^{3})}$，空间复杂度为 ${ O(N^{2})}$。 
 
 ```java
 记住顺序是k,i,j, dist[i][j] = dist[i][k] + dist[k][j];
 这段代码的基本思想就是：最开始只允许经过 1 号顶点进行中转，
 接下来只允许经过 1 和 2 号顶点进行中转……
 允许经过 1~n 号所有顶点进行中转，求任意两点之间的最短路程。
 其实是动态规划的思想。
 1 let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
2 for each vertex v
3    dist[v][v] ← 0
       path[v][k] = k; 
4 for each edge (u,v)
5    dist[u][v] ← w(u,v)  // the weight of the edge (u,v)
6 for k from 1 to |V|
7    for i from 1 to |V|
8       for j from 1 to |V|
9          if dist[i][j] > dist[i][k] + dist[k][j] 
10             dist[i][j] ← dist[i][k] + dist[k][j];
                  path[i][j] = path[i][k];//顺序打印
                  path[i][j] = k;//倒序打印
                  //如果用dij, 则只能倒序打印。因为不知道path[k][j]. 
11         end if


 ```

##### 7. 最短路径path

用一个数组，存放到这个节点前序的节点。floyd/dijkstra/bfs都可以用这个方法来存。


---
####二刷总结：

dfs:
i. dfs + 记忆化搜索。经常和dp一起。
eg:
[Represent N Cents 美分的组成](https://www.cnblogs.com/grandyang/p/4840713.html)
```
用dp的方式可以解。如果要求路径，则需要用dfs(combination sum)。
这里dfs的时候，可以记忆化来减少复杂度。记忆化的方式是int 
meme[leftAmount][index]. 如果要求路径（212，221算两种），
则需要把List cur转为key来记录memo。
```
- [x] [coin-change-2](https://www.leetcode.com/problems/coin-change-2/description)
- [x] [evaluate-division](https://www.leetcode.com/problems/evaluate-division/description) 
- [] union find

ii. dfs求所有情况。经典的permutation/combination
iii. 二维数组的dfs
- [x] [number-of-distinct-islands](https://www.leetcode.com/problems/number-of-distinct-islands/)
- [x] [number-of-big-islands](https://www.lintcode.com/problem/number-of-big-islands/description)
比起用union find， 应该优先考虑dfs+visited，更好写。

bfs: 
一般是求最短路径/最短距离等。利用bfs每次步数加一的性质，设置sentinel记录步数。
可以双向bfs节省空间复杂度/ 可以多源bfs，找到中心点等。

- [x] [minesweeper](https://www.leetcode.com/problems/minesweeper/description)
带条件的dfs/bfs
比如拓扑排序用dfs看是否可以进入。
还有bfs看是否需要进入queue。

- [x] [shortest-path-visiting-all-nodes](https://www.leetcode.com/problems/shortest-path-visiting-all-nodes/description)
状态压缩 + bfs求最短路径 + /path记录/
