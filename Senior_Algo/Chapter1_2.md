## Senior Algo Class 1

- [xk] [number-of-connected-components-in-an-undirected-graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/)

- [k] [redundant-connection-ii](https://leetcode.com/problems/redundant-connection-ii/)
暴力union find可以做
O(N)的办法是：分情况讨论 环或者定点有两个parent。
```
如果有两个parent，得到candidate1/candidate2
case1 移除candidate2且union find找下来没有环，那么返回two parent顶点的第二条边
如果union find找下来有环：
	case 2 返回candidate1
	case 3 返回最后成环的那一条边。	
图解 https://leetcode.com/problems/redundant-connection-ii/solutions/108058/one-pass-disjoint-set-solution-with-expl-45lf/
```

Union Find:
```java
class UnionFind{
	int[] parent; // Map<Integer, Integer> parent
	public int find(int x){
	}
	public void union (int x, int y){
	}
}
```

应用： 关于集合合并/ 查找两个元素是否在一个集合中。

1. 查找 Find
非递归比较好。 

```java
HashMap<Integer, Integer> father = new HashMap<Integer, Integer>();
int find(int x) {
	int parent = father.get(x);
	while (parent != father.get(parent)) {
		parent = father.get(parent);
	}
	return parent;
}
```

路径压缩：
```python
def find(self, label):
	orig = label
	while self.parents[label] != label:
		label = self.parents[label]
	parent = label
	label = orig
	while self.parents[label] != label:
		temp = self.parents[label]
		self.parents[label] = parent
		label = temp
	return parent
```
2. 合并Union (老大哥合并)

```java
void union(int x, int y) {
	int fa_x = find(x);
	int fa_y = find(y);
	if (fa_x != fa_y) {
		father.put(fa_x, fa_y)
	}
}
```

3. 带size的union find
```python
class UnionFindSet:
    def __init__(self, max_size):
        self.father = list(range(max_size))
        self.size = [1] * max_size
    def find(self, x):
        if x == self.father[x]:
            return x
        else:
            self.father[x] = self.find(self.father[x])
            return self.father[x]
    def merge(self, a, b):
        fa = self.find(a)
        fb = self.find(b)
        if fa != fb:
            self.size[fa] += self.size[fb]
            self.father[fb] = fa
    def getSize(self, x):
        return self.size[self.find(x)]
```
---

- [x] [bricks-falling-when-hit](https://www.leetcode.com/problems/bricks-falling-when-hit/)
bv
可以用bfs+路径/dfs，也可以并查集，单开一个dict记录key到parent的factor。
路径压缩的时候要处理factor
- [x¿¿] [evaluate-division](https://www.leetcode.com/problems/evaluate-division/) 

- [x] [possible-bipartition/](https://leetcode.com/problems/possible-bipartition/)
