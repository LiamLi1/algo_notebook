## Senior Algo Class 7
1. Kth

(1)
- [ ] [kth-smallest-element-in-a-sorted-matrix](https://www.lintcode.com/problem/kth-smallest-element-in-a-sorted-matrix/)
有点像d算法求最短路径。 不用更新距离，所以可以用堆优化。还有一种二分法。感觉没有这个好用。
- [x] 求两数组，每组选一个的元素对和（积）的第k小。可以先弄成上面的矩阵，再来求第k小。

(2)
- [ ] 求n个排序数组的第k大。用两个那种方法效果不好也难写。就直接顺序扫，用一个堆来存。
- [ ] 多线程的情况。还有k的大小。
i. 两两分组，找到前k大。重复。然后合并来找。总复杂度是O(klogn)， 这个O(k)是并行的。
ii. 如果k非常大， 可以用二分+count。先找到每个数组的min_i和max_i 。再找到总的max/min/ mid = (min + max) / 2. 然后用二分看mid在每个数组中的大小a_i。 如果(a1+a2+a3+a4) < k, 则max = mid. 不然取min = mid。 然后二分继续。O(log(max - min)*log(len)) 这个log(len)是并行的。这个就与k没有关系了。
- [ ] bad version
找到第一次变bad的地方。单机直接二分。
多机：$log_k(n)$

---

2. 扫描线

新建一个数据结构 Point， 然后存进list，再sort。可以把comparator写在Point Class里面。
```java
class Point{
    int time;
    int flag;

    Point(int t, int s) {
        this.time = t;
        this.flag = s;
    }
    public static Comparator<Point> PointComparator = new Comparator<Point>() {
        public int compare(Point p1, Point p2) {
            if(p1.time == p2.time) 
                return p1.flag - p2.flag;
            else 
                return p1.time - p2.time;
      }
    };
}
```

- [x] [number-of-airplanes-in-the-sky](https://www.lintcode.com/problem/number-of-airplanes-in-the-sky/description)

hard: building outline
- [x] [the-skyline-problem](https://www.lintcode.com/problem/the-skyline-problem/description) 求轮廓和轮廓高度。用一个堆来记录当前高度。

可以用TreeSet来解决这道题。因为每个进来的点在原始数组中的index是unique的。把这个信息放入TreeSet 的comparator就导入多个高度相同的点了。


---
3. Subarray Sum (用map来记录中间状态)

（1）subarray sum
- [x] [submatrix-sum](https://www.lintcode.com/problem/submatrix-sum/)
直接暴力解是$O(n^4)$
首先subarray sum 是O(n). 
用途sum(i)转换为列数组可以转换为array sum. 枚举需要$O(n^3)$

- [x] [subarray-sum-closest](https://www.lintcode.com/problem/subarray-sum-closest/)
先排序。然后遍历subsum， 求相邻的差。找到最小的。
- [ ] [subarray-sum-ii](https://www.lintcode.com/problem/subarray-sum-ii/description) 先和上题一样排序。
start<= sum[i] - sum[j] <= end
sum[j] + start<= sum[i] <=sum[j] + end
把sum[i] 放进线段树。相当于求[sum[j] + start, sum[j] + end] 这个范围内有多少点。这个就是一个区间count型的线段树。

（2） maximum subarray
[maximum-subarray](https://www.lintcode.com/problem/maximum-subarray/)

- [ ] [continuous-subarray-sum-ii](https://www.lintcode.com/problem/continuous-subarray-sum-ii/) 循环的数组。技巧在于转换。求minimum-subarray，得到跨界取正的情况。求maxSum, 得到不跨界的情况。然后比较。

同样类型的还有House Robber534/ 这道题可以分类来做。不偷最后一间/ 不偷第一间。比较哪个大。

---
Trie 树 见初级班第八章