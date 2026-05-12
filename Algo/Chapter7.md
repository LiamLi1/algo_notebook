## Nine Chapter Class 7

Graph & Search
##### 1. Clone Graph
 - [xk] [clone-graph](https://www.leetcode.com/problems/clone-graph/description)
 
 克隆点和克隆边分开
 遍历图：用BFS比DFS好。
 - [xk] [copy-list-with-random-pointer](https://www.leetcode.com/problems/copy-list-with-random-pointer/) 

##### 2. 拓扑排序 
入度/出度 有多少边可以入/出
- [xk] [course-schedule-ii](https://leetcode.com/problems/course-schedule-ii/description/)
- [xk] 拓扑dfs/bfs。需要带条件看需不需要进入

-  [xxk] [$minimum-height-trees](https://www.leetcode.com/problems/minimum-height-trees/)
也是拓扑排序的题/从叶子结点往上BFS来找，可以找到最短树


##### 3. Search （回溯backtracking + 剪枝)
dfs笔记：

dp中的memo search：更像是利用recursion的思想。
dp与memo search 主要考虑的是状态的转变。主要是考虑当前状态与下一个状态之间的联系（自顶向下 memo search - 自底向上 bp）


搜索的dfs和backtracking：同样依靠递归来模拟stack。但是思想不是递归。

搜索的DFS需要通过标记和visited数组来判定是否已经访问过节点。
backtrack则不止是剪枝，还要状态回溯。公式化理解：回溯法 = DFS + 剪枝 + 状态重置。


dfs算法一般递归写。eg：纯遍历用栈来写dfs。用递归写。
```python
class Node{
       def __init__(self, val):
              self.val = val
              self.neighbors = []
}

def dfs(node):
       # 递归
    visited = set()
    for neighbor in node.neighbors:
       if neighbor not in visited:
            visited.add(neighbor)
            dfs(neighbor)

def dfs(node):
       # stack
    visited = set()
    visited.add(node)
    stack = [node]
    while stack:
        curr = stack.pop()
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
```
回溯的算法
```
function dfs(array,index, ...) {
    if(some_condition){
        return;
    }
    for(i=index;i<array.size();++i){
        obj = array[i];
        choose();
        dfs(array,i, ...);
        //backtracking
        unchoose();
    }
}
```

- [xk] [permutations](https://www.leetcode.com/problems/permutations/description)一般这种问题都用深度优先搜索。深度优先搜索树$O(N!)$
- [xk] [subsets](https://www.leetcode.com/problems/subsets/description)时间复杂度是$O(2^{n})$
传统做法 Backtracking 
- [ ] [find-the-k-sum-of-an-array](https://leetcode.com/problems/find-the-k-sum-of-an-array/)
树状图 图解backtracking - 可以做到按顺序输出

DFS
- [xk] [N-Queens](https://www.leetcode.com/problems/n-queens/description) 减枝

- [xk] [subsets-ii](https://www.leetcode.com/problems/subsets-ii/description)
- [xk] [palindrome-partitioning](https://www.leetcode.com/problems/palindrome-partitioning/description)
- [xk] [combination sum](https://www.leetcode.com/problems/combination-sum/description)
- [xk] [combination sum ii](https://www.leetcode.com/problems/combination-sum-ii/description)
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
3. 双向BFS， 从target和start分别bfs。效果是可以让复杂度减少。$2 \times O(b^{d/2})$, 显著小于$O(b^{d})$。同样是用于求解两点间最短路径的长度问题。
4. 多源bfs。可以用BitSet来追踪当前状态。


- [xk] [word ladder-ii](https://www.leetcode.com/problems/word-ladder-ii/description)


BFS to search the shortest routes and record the distance of each node to the start.
DFS to traverse routes, it is only a valid next node if the distance of node is decreasing. Record all possible nodes for the same distance to destination.
最短路径+回溯


##### 5. 最小支撑树

```
 * 连通图： 在无向图中，若任意两个顶点 Vi与Vj都有路径相通，则称该无向图为连通图。
强连通图： 在有向图中，若任意两个顶点Vi与Vj都有路径相通，则该有向图为强连通图。

* 连通网： 在连通图中，若图的边具有一定的意义，每一条边都对应一个数，称为权；权代表着连接两个顶点的代价，称这种连通图叫做连通网。

* 生成树： 一个连通图的生成树是指一个连通子图，它含有图中全部n 
 个顶点，但只有足以构成一棵树的 n-1条边。一颗有n个顶点的生成树有且仅有 n-1条边，如果生成树中再添加一条边，则必定成环。

* 最小生成树： 在连通网的所有生成树中，所有边的代价和最小的生成树，称为最小生成树。
```

Kruskal 算法 ： UnionFind + PriorityQueue来做。


Prim 算法(不用union find，其实更好写）：
```python
import heapq

def prim(graph, start_node=0):
    """
    :param graph: 邻接表表示的图 {u: [(v, weight), ...]}
    :param start_node: 起始顶点
    :return: 最小生成树的总权重

    for h1, h2, cost in edges:
            graph[h1].append((h2, cost))
            graph[h2].append((h1, cost))
    
    用队列可以不用处理parallel edge的情况

    """
    n = len(graph)
    visited = [False] * n
    # 优先队列存储格式: (权重, 目标节点)
    min_heap = [(0, start_node)]
    total_weight = 0
    nodes_in_mst = 0

    while min_heap and nodes_in_mst < n:
        weight, u = heapq.heappop(min_heap)
        
        # 如果该点已在生成树中，则跳过
        if visited[u]:
            continue
            
        # 将点加入生成树
        visited[u] = True
        total_weight += weight
        nodes_in_mst += 1
        
        # 遍历邻居，将潜在的“桥梁”边加入堆
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
                
    return total_weight

```

- [k] [connecting-cities-with-minimum-cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/)

- [k] [optimize-water-distribution-in-a-village](https://leetcode.com/problems/optimize-water-distribution-in-a-village)

- [x] [minimum-risk-path](https://www.lintcode.com/problem/minimum-risk-path/description)

- [r] [find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree) must union find + kruskal

```
这个题更像是bfs的题，dijkstra变种
```
https://blog.csdn.net/luoshixian099/article/details/51908175

##### 6. 两点间最短距离（有权图）

- [xk] [network-delay-time](https://leetcode.com/problems/network-delay-time/)

- [k] [path-with-maximum-probability/](https://leetcode.com/problems/path-with-maximum-probability/)

``` python
Dijkstra
求一个顶点到所有定点的最短路径
1.用一个hashmap记录起始点到其他点的距离。不存在就是无穷
2.用heap存（距离，点），并用来BFS。先存起始点（0，x0)。
从优先队列里面弹出点，标记为走过的。每次弹出一个最近的点，然后把它相邻的点的距离在hash里更新，并进队没有走过的/距离比现在的更短的。如果走过或者距离长就不用再走了。
3.这里存的距离是指定点到下一个点的距离。

# --- Dijkstra 算法 (最短路径) ---
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # (累计距离, 当前节点)

    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > distances[u]: continue #这一步把visited取代了
        
        for v, weight in graph[u]:
            # 【核心区别】：Dijkstra 压入的是从源点到该点的“累积”距离
            new_dist = curr_dist + weight
            if new_dist < distances[v]:
                distances[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    return distances
```

7.求所有顶点到所有定点的最短路径
Floyd

- [x] [sum-of-distances-in-tree](https://leetcode.com/problems/sum-of-distances-in-tree/submissions/) 可以用来练习。但是真的用Floyd要超时。
这里要把图看成树，手动设一个根节点，方便求解。
   
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
- [xk] [coin-change-2](https://www.leetcode.com/problems/coin-change-2/description)
- [xk] [evaluate-division](https://www.leetcode.com/problems/evaluate-division/description) 
dfs：有visited的情况 不能加memory。无状态才能加memory。
- [k] union find 用uf做，必须用路径压缩。不然 factor[i] * i = father[i]. 虽然 uf.find(a) == uf.find(b), 但是father[a] 不一定 = father[b]

ii. dfs求所有情况。经典的permutation/combination. backtracking
iii. 二维数组的dfs
- [xk] [number-of-distinct-islands](https://www.leetcode.com/problems/number-of-distinct-islands/)
- [xk] [number-of-big-islands](https://www.lintcode.com/problem/number-of-big-islands/description)
比起用union find， 应该优先考虑dfs+visited，更好写。

bfs: 
一般是求最短路径/最短距离等。利用bfs每次步数加一的性质，设置sentinel记录步数。
还有MST Prim 和 Djikstra 用heap做bfs
可以双向bfs节省空间复杂度/ 可以多源bfs，找到中心点等。

- [x] [minesweeper](https://www.leetcode.com/problems/minesweeper/description)
带条件的dfs/bfs
比如拓扑排序用dfs看是否可以进入。
还有bfs看是否需要进入queue。

- [x] [shortest-path-visiting-all-nodes](https://www.leetcode.com/problems/shortest-path-visiting-all-nodes/description)
状态压缩 + bfs求最短路径 + /path记录/

##### 8. 图里找环（树是无环图）
- [ ] [redundant-connection/](https://leetcode.com/problems/redundant-connection/)
内部找退出条件 不如放一个global变量来存 