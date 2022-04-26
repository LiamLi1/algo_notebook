## Senior Algo Class 1
- [x] [find-peak-element ii](https://www.lintcode.com/problem/find-peak-element-ii/description) / 贪心或者二分/ 二分解更优(4向递归)
- [x] [connected-component-in-undirected-graph](https://www.lintcode.com/problem/connected-component-in-undirected-graph/description) 普通dfs/ 也可以用union find
- [x] [find-the-weak-connected-component-in-the-directed-graph](https://www.lintcode.com/problem/find-the-weak-connected-component-in-the-directed-graph/description) 可以用union find

如果有向图的边变成无向图时，如果是联通的，就叫弱联通块
如果有向图就是相互联通的，那是强联通快。

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
二刷：
如何统计unionfind以后，同一parent下点的数量：
- [x] [connecting-graph-ii](https://www.lintcode.com/problem/connecting-graph-ii/description) 
- [x] [connecting-graph-iii](https://www.lintcode.com/problem/connecting-graph-iii/description)
- [x] [bricks-falling-when-hit](https://www.leetcode.com/problems/bricks-falling-when-hit/)

可以用bfs+路径/dfs，也可以并查集，单开一个dict记录key到parent的factor。
路径压缩的时候要处理factor
- [x¿¿] [evaluate-division](https://www.leetcode.com/problems/evaluate-division/) 

- [x] [possible-bipartition/](https://leetcode.com/problems/possible-bipartition/)
```
用union find的时候，如果两个点的find一样则两个点在统一个group里面。
```
