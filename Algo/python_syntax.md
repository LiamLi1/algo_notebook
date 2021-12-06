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

#### heap
heapq
```python
heapq.heappush(heap, item) 

heapq.heapop(heap) # 弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出 IndexError 。使用 heap[0] ，可以只访问最小的元素而不弹出它。

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
