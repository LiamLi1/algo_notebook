## Nine Chapter Class 9

High frequency question

1. single number I, II, III
2. Majority Number I, II, III
3. Best Time to Buy and Sale Stock I, II, III
4. subarray sum I, II, III, IV
5. 2-sum, 3-sum, 4-sum, k-sum, 3-sum closet
6. quick questions
7. partition array
---

##### 1. Single Number
 - [x]  [single-number](https://www.lintcode.com/problem/single-number/) 所有的都异或起来就行。
 用 xor 异或 ^  口诀：不进位加法
 相同为0，不同为1
 
 
 ```
 => a ^ a = 0
 => a ^ 0 = a
 a ^ b = c => b ^ c = a, b ^ a = c
 满足结合律/交换律
 ```
 - [x]  [single-number-ii](https://www.lintcode.com/problem/single-number-ii/) 三进制下的异或。也可以用口诀算。
 - [x]  [single-number-iii](https://www.lintcode.com/problem/single-number-iii/) int lastBit = xor - (xor & (xor - 1));
 - [x]  [single-number-iv](https://www.lintcode.com/problem/single-number-iv/)

##### 2. Majority Number
- [x] [majority element](https://www.lintcode.com/problem/majority-element/description) 发现不一样的就扔掉
- [x] [majority element ii](https://www.lintcode.com/problem/majority-element-ii/description)
- [x] [majority element iii](https://www.lintcode.com/problem/majority-element-iii/description)
- [ ] :carrot: 还要再多统计比一遍。以及怎么删除map中的元素。

用Iterator<Map.Entry<Integer, Integer>> 来遍历才能删除。
对第二、三题，找到可能的候选数字以后，要重新计数一次才行。

#### 3.4 Subarray 类型：注意累加的应用
- [x] [contiguous-array](https://www.lintcode.com/problem/contiguous-array/description)

##### 3. Best Time buy or sell stock
- [x] [best-time-to-buy-and-sell-stock](https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock/)
- [x] [best-time-to-buy-and-sell-stock-ii](https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-ii/)
- [x] [best-time-to-buy-and-sell-stock-iii](https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-iii/) 左右分别算
- [x] [best-time-to-buy-and-sell-stock-iv](https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-iv/) 动归
- [ ] :carrot: 动归的思想。用一个mustsell 和一个globalmax一起动归。原因？ global的最大值当然由mustsell来更新。因为不论如何都有一个最佳卖出的时机。但是mustsell的最大值不仅仅由mustsell决定。还和globalmax有关。

##### 4. Maximum Subarray
- [x] [Maximum Subarray](https://www.lintcode.com/problem/maximum-subarray/)
- [x] [Maximum Subarray ii](https://www.lintcode.com/problem/maximum-subarray-ii/)
- [ ] :carrot: 怎么确定初始状态
- [x] [Maximum Subarray iii](https://www.lintcode.com/problem/maximum-subarray-iii/)
- [ ] :carrot: 动归中的global与local
- [x] [Maximum Subarray iv](https://www.lintcode.com/problem/maximum-subarray-iv/)
- [x] [maximum subarray difference](https://www.lintcode.com/problem/maximum-subarray-difference/)
- [x] [subarray-sum-closest](https://www.lintcode.com/problem/subarray-sum-closest/)


- [x] [subarray-sum-ii](https://www.lintcode.com/problem/subarray-sum-ii/description) 二分查找。或者两个指针。

##### 5. n sum
- [x] [two sum](https://www.lintcode.com/problem/two-sum/description)
- [x] [3sum](https://www.lintcode.com/problem/3sum/description)
- [ ] [2Sum-closet](https://www.lintcode.com/problem/two-sum-closest-to-target/description)
- [x] [3sum-closest](https://www.lintcode.com/problem/3sum-closest/)
ksum: DP II

##### 6. Quick Questions
- [ ] [power](https://www.lintcode.com/problem/fast-power/)
[快速幂取模算法详解 - 72 73 76 89 82 84 89 81 - CSDN博客](https://blog.csdn.net/ltyqljhwcm/article/details/53043646)
```
模运算与基本四则运算有些相似，但是除法例外。其规则如下：
(a + b) % p = (a % p + b % p) % p （1）
(a - b) % p = (a % p - b % p) % p （2）
(a * b) % p = (a % p * b % p) % p （3）
a ^ b % p = ((a % p)^b) % p （4）
结合律：
((a+b) % p + c) % p = (a + (b+c) % p) % p （5）
((a*b) % p * c)% p = (a * (b*c) % p) % p （6）
交换律：
(a + b) % p = (b+a) % p （7）
(a * b) % p = (b * a) % p （8）
分配律：
((a +b)% p * c) % p = ((a * c) % p + (b * c) % p) % p （9）
```

- [ ] [dyeing-problem](https://www.lintcode.com/problem/dyeing-problem/description) 运算完了以后，还要再取一次模
- [x] [sqrt](https://www.lintcode.com/problem/sqrtx/description)
- [x] [Trailing Zeros](https://www.lintcode.com/problem/trailing-zeros/description)
- [x] [o1-check-power-of-2](https://www.lintcode.com/problem/o1-check-power-of-2/description) (x - 1) & x ==0
- [ ] [string-to-integer-atoi](https://www.lintcode.com/problem/string-to-integer-atoi/)
- [ ] [roman-to-integer](https://www.lintcode.com/problem/roman-to-integer/)

##### 7. Partition array
```java
/**
*Quick Select 和 Quick Sort
(1) 与pivot，全部都不加等号
(2) left 与 right，全部都要加等号。
这样才能保证：每次都会有变化。且
如果不是全部都加，可能会有死循环。

Partition时，要根据题目来：
比如 求交换后，比k大的第一个的坐标。
(1) 与pivot，必须有一边有等号。
(2) 因为pivot有一边取等号，所以在查找过程中，
不可能出现left == right。但是交换以后，
有可能出现。
所以外层while要加。
内层也必须为left == right准备变化。
*/

public int partitionArray(int[] nums, int k) {
	if (nums.length == 0 || nums == null){
		return 0;
	}
	int left = 0;
	int right = nums.length - 1;
	while (left <= right) {
		while (left <= right && nums[left] < k) {
			left++;
		}
		while (left <= right && nums[right] >= k) {
			right--;
		}
		if (left < right){
			int temp = nums[left];
			nums[left] = nums[right];
			nums[right] = temp;
			left ++;
			right --;
		}
	}
	return left;
}
```

- [x] [Partition Array](https://www.lintcode.com/problem/partition-array/description)
- [x] [sort-letters-by-case](https://www.lintcode.com/problem/sort-letters-by-case/description)
- [x] [sort-colors](https://www.lintcode.com/problem/sort-colors/description)
用两次partition可以解决。但是更好的解法是搞三个指针，一个指针从头走到尾，如果等于0和头换，等于2和尾换。换了以后指针要移动。
- [x] [interleaving-positive-and-negative-numbers](https://www.lintcode.com/problem/interleaving-positive-and-negative-numbers/)

##### 8. Top K 问题
 - [x] [kth-smallest-numbers-in-unsorted-array](https://www.lintcode.com/problem/kth-smallest-numbers-in-unsorted-array/description)
1. 用heap有两种解法。maxHeap/minHeap, 看K和N的大小来决定用哪种。
2. 用quick select来递归
```java
// Partition 模板
注意与pivot比较的时候都不能带等号。放宽交换条件，这样的结果是：
left和它右边都 >= pivot
right和它左边都 <= pivot
right = left - 1
保证至少能让left/right移动一次，否则有可能死循环。
中间有可能空出来一个数。quick select 要考虑这种情况。

private void quickSort(int[] A, int start, int end) {
        
        if (start >= end) {
            return;
        }
        
        int left = start;
        int right = end;
        // System.out.println(right);
        int pivot = A[(start + end) / 2];
        while (left <= right) {
            while (left <= right && A[left] < pivot) {
                left++;
            }
            while (left <= right && A[right] > pivot) {
                right--;
            }
            if (left <= right) {
                int temp = A[left];
                A[left] = A[right];
                A[right] = temp;
                left++;
                right--;
            }
        }

        quickSort(A, left, end);
        quickSort(A, start, right);
    }

```
##### 9. Window 问题
- [x] [sliding-window-maximum](https://www.lintcode.com/problem/sliding-window-maximum/description)
$O(n)$ 时间复杂度，只有栈和队列
可以维护一个递减栈，但是还要有一个front_peek和front_pop操作，所以用deque。
找中间用heap


##### 10. Ugly Number
 - [x] [Ugly-number](https://www.lintcode.com/problem/ugly-number/description)
 - [x] [ugly-number-ii](https://www.lintcode.com/problem/ugly-number-ii/)
 
 可以用Heap+Hash来解决，时间复杂度O(nlogn)。空间复杂度O(n)。从1开始，每次用最小的数乘以所有prime，出重以后加入heap。
 数据大的时候很可能溢出，所以要用Long来转换。
 
 也可以用排队的办法。复杂度O(n)。
 
 ```java
 for (int i = 1; i < n; i++) {
            int lastNumber = uglys.get(i - 1);
            while (uglys.get(p2) * 2 <= lastNumber) p2++;
            while (uglys.get(p3) * 3 <= lastNumber) p3++;
            while (uglys.get(p5) * 5 <= lastNumber) p5++;
            //每个prime都派出候选人。
			//这个候选人必须比lastNumber 大。
			//否则就选下一个。
			
            uglys.add(Math.min(
                Math.min(uglys.get(p2) * 2, uglys.get(p3) * 3),
                uglys.get(p5) * 5
            ));
        }
 ```
 
 ##### 11. 博弈类
 - 想办法统一状态，然后记忆化搜索：
 - [x] [the-game-of-take-numbers](https://www.lintcode.com/problem/the-game-of-take-numbers/description)
 - 和上一题类似。只是下一步的选择太多。可以用Map<String, boolean> 来记忆化优化。复杂度$O(n^{n})$ 优化为$O(2^{n})$
-  [ ] [flip-game-ii](https://www.lintcode.com/problem/flip-game-ii/)

##### 12. 排序
partition/ merge/ 插入/ 选择/ 冒泡/ 桶排序
- 最好情况： 冒泡和插入可以是O(n), 冒泡要用一个flag来看是否有交换。
选择排序则都是O(n^2)
- [x] [multi-keyword-sort](https://www.lintcode.com/problem/multi-keyword-sort/)
- [x] [sort-list](https://www.lintcode.com/problem/sort-list/description)


##### 13 Interval
- [x] [merge-intervals](https://www.lintcode.com/problem/merge-intervals/)
- [ ] 面经/银行与交易

##### 14 扫描线
在一个list里面排好序，然后扫一遍，计算同时进行的最大会议数。（扫描线算法）
- [x] [meeting-rooms-ii](https://www.lintcode.com/problem/meeting-rooms-ii/description)
- [ ] [skyline](https://www.lintcode.com/problem/the-skyline-problem/description)


##### 15 zigzag/ spiral/ 矩阵旋转

##### 16 map reduce
https://www.lintcode.com/problem/?tag=map-reduce
