## Senior Algo Class 1
- [x] [find-peak-element ii](https://www.lintcode.com/problem/find-peak-element-ii/description)
- [x] [connected-component-in-undirected-graph](https://www.lintcode.com/problem/connected-component-in-undirected-graph/description)
![f0a72245.png](:storage\4c828536-a3d0-4f7e-a16a-06f21ba5a4ea\f0a72245.png)
- [x] [find-the-weak-connected-component-in-the-directed-graph](https://www.lintcode.com/problem/find-the-weak-connected-component-in-the-directed-graph/description)

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
---
二刷：
如何统计unionfind以后，同一parent下点的数量：
- [x] [connecting ](https://www.lintcode.com/problem/connecting-graph-ii/description) 
- [x] [connecting-graph-iii](https://www.lintcode.com/problem/connecting-graph-iii/description)
- [x] [bricks-falling-when-hit](https://www.lintcode.com/problem/bricks-falling-when-hit/)

可以用bfs+路径，也可以并查集记录两点间的值。
- [x] [evaluate-division](https://www.lintcode.com/problem/evaluate-division/)


