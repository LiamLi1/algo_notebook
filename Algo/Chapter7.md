## Nine Chapter Class 7

Graph & Search
![d197ae23.png](:storage\f8f56076-8b9c-4d70-81dd-e5c4356c2ba5\e4cb0fb8.png)
##### 1. Clone Graph
 - [x] [clone-graph](https://www.lintcode.com/problem/clone-graph/description)
 
 克隆点和克隆边分开
 遍历图：用BFS比DFS好。
 - [x] [copy-list-with-random-pointer](https://www.lintcode.com/problem/copy-list-with-random-pointer/) 

##### 2. 拓扑排序 
入度/出度 有多少边可以入/出
- [x] [topological-sorting](https://www.lintcode.com/problem/topological-sorting/description)

- [ ] 拓扑dfs/bfs。需要带条件看需不需要进入

-  [ ] [minimum-height-trees](https://www.lintcode.com/problem/minimum-height-trees/description?_from=ladder&&fromId=18)
也是拓扑排序的题。

##### 3. Search
- [x] [permutations](https://www.lintcode.com/problem/permutations/description)一般这种问题都用深度优先搜索。深度优先搜索树$O(N!)$
![0ac105ee.png](:storage\f8f56076-8b9c-4d70-81dd-e5c4356c2ba5\459d7229.png)
- [x] [subsets](https://www.lintcode.com/problem/subsets/description)时间复杂度是$O(2^{n})$
- [x] [N-Queens](https://www.lintcode.com/problem/n-queens/description) 减枝
![280105ce.png](:storage\f8f56076-8b9c-4d70-81dd-e5c4356c2ba5\a2b82981.png)
![02d71ec8.png](:storage\f8f56076-8b9c-4d70-81dd-e5c4356c2ba5\4dfe7193.png)

- [x] [subsets-ii](https://www.lintcode.com/problem/subsets-ii/description)
- [x] [palindrome-partitioning](https://www.lintcode.com/problem/palindrome-partitioning/description)![7068bda6.png](:storage\f8f56076-8b9c-4d70-81dd-e5c4356c2ba5\32336bb6.png)
- [x] [combination sum](https://www.lintcode.com/problem/combination-sum/description)
- [x] :rabbit:
- [x] [combination sum ii](https://www.lintcode.com/problem/combination-sum-ii/description)
- [x] :rabbit: 比较如何对待重复的情况。

- [x] [word ladder](https://www.lintcode.com/problem/word-ladder/description) 
- [x] :rabbit:

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


- [x] [word ladder-ii](https://www.lintcode.com/problem/word-ladder-ii/description)
- [x] :carrot:

BFS to search the shortest routes and record the distance of each node to the start.
DFS to traverse routes, it is only a valid next node if the distance of node is decreasing. Record all possible nodes for the same distance to destination.

##### 5. 最小支撑树
UnionFind + PriorityQueue来做。
- [x](https://www.lintcode.com/problem/minimum-risk-path/description)
https://blog.csdn.net/luoshixian099/article/details/51908175

##### 6. 两点间最短距离（有权图）

- [x] [network-delay-time](https://leetcode.com/problems/network-delay-time/)



Dijkstra
求一个顶点到所有定点的最短路径
(1) 初始时，S只包含起点s；U包含除s外的其他顶点，且U中顶点的距离为"起点s到该顶点的距离"[例如，U中顶点v的距离为(s,v)的长度，然后s和v不相邻，则v的距离为∞]。

(2) 从U中选出"距离最短的顶点k"，并将顶点k加入到S中；同时，从U中移除顶点k。

(3) 更新U中各个顶点到起点s的距离。之所以更新U中顶点的距离，是由于上一步中确定了k是求出最短路径的顶点，从而可以利用k来更新其它顶点的距离；例如，(s,v)的距离可能大于(s,k)+(k,v)的距离。

(4) 重复步骤(2)和(3)，直到遍历完所有顶点。

可以用PriorityQueue优化
找最短距离的时间复杂度为O(|V|*|V|)(共循环V次，每次V个点)，考虑到Q每次递减1，实际复杂度为O(|V|^2/2)；

由于图共有E条边，每条边最多被更新2次（1条边2个端点），因此更新距离的时间复杂度为O(2*|E|)。

　因此，总时间复杂度=O(2*|E|+|V|^2/2)
   采用优先队列之后，总时间复杂度=O(2*|E|+|V|*log|V|)
   
   Floyd
   求所有顶点到所有定点的最短路径
   
   [sum-of-distances-in-tree](https://leetcode.com/problems/sum-of-distances-in-tree/submissions/) 可以用来联系。但是真的用Floyd要超时。
   
 Floyd-Warshall算法的时间复杂度為 ${ O(N^{3})}$，空间复杂度为 ${ O(N^{2})}$。 
 ```java
 记住顺序是k,j,j, dist[i][j] = dist[i][k] + dist[k][j];
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
- [x] [coin-change-2](https://www.lintcode.com/problem/coin-change-2/description)
- [x] [evaluate-division](https://www.lintcode.com/problem/evaluate-division/description) 

ii. dfs求所有情况。经典的permutation/combination
iii. 二维数组的dfs
- [x] [number-of-distinct-islands](https://www.lintcode.com/problem/number-of-distinct-islands/)
- [x] [number-of-big-islands](https://www.lintcode.com/problem/number-of-big-islands/description)
比起用union find， 应该优先考虑dfs+visited，更好写。

bfs: 
一般是求最短路径/最短距离等。利用bfs每次步数加一的性质，设置sentinel记录步数。
可以双向bfs节省空间复杂度/ 可以多源bfs，找到中心点等。

- [x] [minesweeper](https://www.lintcode.com/problem/minesweeper/description)



带条件的dfs/bfs
比如拓扑排序用dfs看是否可以进入。
还有bfs看是否需要进入queue。
- [x] [shortest-path-visiting-all-nodes](https://www.lintcode.com/problem/shortest-path-visiting-all-nodes/description)
