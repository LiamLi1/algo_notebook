### Python Syntax

### 常用函数

### String
```python
# count
message = "abcdeb"
message.count("b") # return 2

# index 如果找不到回报错。不如用find，找不到返回-1.
"abdcef".index("b") # 1
"abdcefb".index("b", 2) #6
"abdcefb".rindex("b") #6

# find
"S2sdf".find("sdf", 3) #-1
"S2sdf".find("sdf", 10) #-1
"S2sdf".rfind("sdf", 2) # 2
# isnumeric
txt.isnumeric("22") # true. 非负整数才行
# sorted 转换字符串成list
string = "BCBA"
"".join(sorted(string)) # "ABBC"

```

### 整除
```python
有负数的情况
int(num2 * 1.0 / num1)

没有负数
num1 // num2
```

### List

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

# sort 多个key
for l,r,h in buildings:
    points.append([l, h, 'start'])
    points.append([r, -h, 'end'])
points.sort(key=lambda x:( x[0], -x[1]))

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

*|list.index(obj) 从列表中找出某个值第一个匹配项的索引位置|*

list.insert(index, obj) 将对象插入列表
list.pop(index=-1) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj) 移除列表中某个值的第一个匹配项
list.reverse() 反向列表中元素
list.sort(cmp=None, key=None, reverse=False) 对原列表进行排序

list.pop() # 删除最后一个元素并返回
```

## dict
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
collections.defaultlist(list)
对没有定义key的，直接返回一个空list
```
>>> def zero():
...     return 0
...
>>> dd = defaultdict(zero)
dict1 = defaultdict(int)
dict2 = defaultdict(set)
dict3 = defaultdict(str)
dict4 = defaultdict(list)
```

hash 需要定义__hash__和__eq__
```
class MemDev(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def __hash__(self):
        return hash(self.name + str(self.age))
 
    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        return False
``` 

remove
```
my_dict.pop('key', None) # return None if not found
```

OrderedDict
```python
self.cache = OrderedDict()
if len(self.cache) == self.capacity:
    ## last = True时pop规则为FILO, last = False时pop规则为FIFO
    self.cache.popitem(last = False)
```

## stack
```
python的内置数据结构list可以用来实现栈，用append()向栈顶添加元素, pop() 可以以后进先出的顺序删除元素

但是列表本身有一些缺点，主要问题就是当列表不断扩大的时候会遇到速度瓶颈．列表是动态数组，因此往其中添加新元素而没有空间保存新的元素时，它会自动重新分配内存块，并将原来的内存中的值复制到新的内存块中．这就导致了一些append()操作会消耗更多的时间

有效率要求直接用deque
```
```python
from collections import deque     
# Declaring deque
queue = deque(['name','age','DOB']) 

append():- This function is used to insert the value in its argument to the right end of the deque.

appendleft():- This function is used to insert the value in its argument to the left end of the deque.

pop():- This function is used to delete an argument from the right end of the deque.

popleft():- This function is used to delete an argument from the left end of the deque. 

extend(iterable):- This function is used to add multiple values at the right end of the deque. The argument passed is iterable.
```



## queue
### deque 优先
可以用双向队列deque
```
append/appendleft/extend/extendleft/pop/popleft/count(x)

len
```

Queue 线程安全，所以速度满
queue.Queue
queue.PriorityQueue
queue.LifoQueue
```
import queue

#向队列中添加元素
Queue.put(item[, block[, timeout]])
#从队列中获取元素
Queue.get([block[, timeout]])
#队列判空
Queue.empty()
#队列大小
Queue.qsize()
```

## heap
heapq
```python
heapq.heappush(heap, item) 

heapq.heappop(heap) # 弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出 IndexError 。使用 heap[0] ，可以只访问最小的元素而不弹出它。

heapq.pushpop(heap, item) # 将 item 放入堆中，然后弹出并返回 heap 的最小元素。该组合操作比先调用  heappush() 再调用 heappop() 运行起来更有效率。

heapq.replace(heap, item) # 可能弹出的item比输入的小

heapq.heapify(x) # 将list x 转换成堆，原地，线性时间内。
```

对tuple，自动根据第一个数来排序
```
>>> h = []
>>> heappush(h, (5, 'write code'))
>>> heappush(h, (7, 'release product'))
>>> heappush(h, (1, 'write spec'))
>>> heappush(h, (3, 'create tests'))
>>> heappop(h)
(1, 'write spec')
```



只支持最小值堆。最大值堆需要把数值取负。
```
```

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

### 其他
```
for i,x in enumerate(equations):
    # i: 0~len(equation)
    # x: equation
```

### SortedList

### LFU
