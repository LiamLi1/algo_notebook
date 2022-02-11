### Python Syntax

### 常用函数

#### List

1. sort（原数组上改）/sorted（返回一个copy）
   
```python
l = [list(range(i, i+4)) for i in range(10,1,-1)]
# [[10, 11, 12, 13],
#  [9, 10, 11, 12],
#  [8, 9, 10, 11],
#  [7, 8, 9, 10],
#  [6, 7, 8, 9],
#  [5, 6, 7, 8],
#  [4, 5, 6, 7],
#  [3, 4, 5, 6],
#  [2, 3, 4, 5]]

l.sort(key=sum, reverse=True)
# [[10, 11, 12, 13],
#  [9, 10, 11, 12],
#  [8, 9, 10, 11],
#  [7, 8, 9, 10],
#  [6, 7, 8, 9],
#  [5, 6, 7, 8],
#  [4, 5, 6, 7],
#  [3, 4, 5, 6],
#  [2, 3, 4, 5]]

l.sort(key=lambda x:x[0])
# [[2, 3, 4, 5],
#  [3, 4, 5, 6],
#  [4, 5, 6, 7],
#  [5, 6, 7, 8],
#  [6, 7, 8, 9],
#  [7, 8, 9, 10],
#  [8, 9, 10, 11],
#  [9, 10, 11, 12],
#  [10, 11, 12, 13]]

```
2. 添加元素

```
l1 = ["apple", "banana", "cherry"]
e1 = "orange"
e2 = "peach"
l2 = ["mango", "pineapple", "papaya"]

l1.insert(1, e1)
l1.append(e2)
l1.extend(l2)

l1.extend(l2)

3. 其他
list = [0] * 10 初始化数组（[0,0,0,0,0,0,0,0,0,0])
list = [[0]*3 for i in range(3)] (2纬开始不要用*)

list.append(obj) 在列表末尾添加新的对象
list.count(obj) 统计某个元素在列表中出现的次数
list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj) 从列表中找出某个值第一个匹配项的索引位置

list.insert(index, obj) 将对象插入列表
list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj) 移除列表中某个值的第一个匹配项
list.reverse() 反向列表中元素
list.sort(cmp=None, key=None, reverse=False) 对原列表进行排序


```

#### dict
python 记忆化搜索可以用dict代替list用作memo
eg：
```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle == None or triangle[0] == None:
            return 0
        self.memo = {}
        self.helper(triangle, 0, 0)
        return self.memo[(0, 0)]
        
    def helper(self, triangle, i, j):
        if i >= len(triangle):
            return 0
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        self.memo[(i, j)] = min(self.helper(triangle, i + 1, j), self.helper(triangle, i + 1, j + 1)) + triangle[i][j]
        return self.memo[(i, j)]
```

#### heap
heapq
```python
heapq.heappush(heap, item) 

heapq.heappop(heap) # 弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出 IndexError 。使用 heap[0] ，可以只访问最小的元素而不弹出它。

heapqpushpop(heap, item) # 将 item 放入堆中，然后弹出并返回 heap 的最小元素。该组合操作比先调用  heappush() 再调用 heappop() 运行起来更有效率。

heapqreplace(heap, item) # 可能弹出的item比输入的小

heapq.heapify(x) # 将list x 转换成堆，原地，线性时间内。
```

只支持最小值堆。最大值堆需要把数值取负。
heap自定义comparator通过给元素新增tuple，其中第一项是可以排序来实现。
或者自定义一个class 重写__lt__(self, other).


```
Define a class, in which override the __lt__() function. See example below (works in Python 3.7):

import heapq

class Node(object):
    def __init__(self, val: int):
        self.val = val

    def __repr__(self):
        return f'Node value: {self.val}'

    def __lt__(self, other):
        return self.val < other.val

heap = [Node(2), Node(0), Node(1), Node(4), Node(2)]
heapq.heapify(heap)
print(heap)  # output: [Node value: 0, Node value: 2, Node value: 1, Node value: 4, Node value: 2]

heapq.heappop(heap)
print(heap)  # output: [Node value: 1, Node value: 2, Node value: 2, Node value: 4]
```

