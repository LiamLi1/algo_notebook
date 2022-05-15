'''
[(1,3),(2,4),(2,5)] ==> 3
[(1,3),(3,6), (3,5), (5,6)] ==> 2
[(1,6), (3,4), (4,6), (5,6)] ==> 3

sweep line


            0/1
-> (time, isStart, index)
0:(1, 3) -> (1, 0, True), (3, 0, False)
...

heap[(1, 0, True), (3, 0, False) ... ]

lives = set()
lives.add(0)
len(lives)

[[1,2),[2,4),[2,5)] ==> 2
'''
import heapq

def maxProcess(array):
    heap = []
    for index, input_tuple in enumerate(array):
        startTime, endTime = input_tuple
        heapq.heappush(heap, (startTime, 1, index))
        heapq.heappush(heap, (endTime, 0, index))
    lives = set()
    res = 0

    while heap:
        # pop every tuple for the same time
        '''
        [[1,2),[2,4),[2,5)] 

        (1, 1, 0),                      lives(0)
        (2, 0, 0) (2, 1, 1) (2, 1, 2)   lives(1, 2)  -  len(lives) max
        (4, 0, 1),                      lives(2)
        (5, 0, 2)                       lives()
        space complexity O(N)
        time complexity O(NlogN)


        '''
        time, isStart, index = heapq.heappop(heap)
        if isStart:
            lives.add(index)
        else:
            lives.remove(index)
        while heap and heap[0][0] == time:
            time, isStart, index = heapq.heappop(heap)
            if isStart:
                lives.add(index)
            else:
                lives.remove(index)
        res = max(res, len(lives))
    return res

'''
[[1,2),[2,4),[2,5),[3,5],[5,6]] 

[2, 4]
-> [3, 5] / count(3)
[5, 6] count(1)
'''

test_array1 = [(1,3),(2,4),(2,5)] # 3
print(maxProcess(test_array1))

test_array2 = [(1,3),(3,6), (3,5), (5,6)] # 2
print(maxProcess(test_array2))

test_array3 = [(1,6), (3,4), (4,6), (5,6)] # 3
print(maxProcess(test_array3))


def maxProcess2(array):

    '''
    [(3, 1), (4, 2), (5, 2)]  -> 3
    [(4, 2), (5, 2)] -> 2

    [(1,3),(3,6), (3,5), (5,6)]

    (1, 3)   ->heap[(3, 1)]
    (3, 6)   ->heap((6, 3))

    (3, 5).  -> heap[(5, 3), (6, 3)]
    
    (5, 8)

    '''
    heap = []
    res = 0
    for index, input_tuple in enumerate(array):
        start, end = input_tuple
        new_tuple = (end, start)

        if heap and heap[0][0] <= start:
            heapq.heappop(heap)

        heapq.heappush(heap, new_tuple)
        res = max(res, len(heap))
    return res
    
test_array1 = [(1,3),(2,4),(2,5)] # 3
print(maxProcess2(test_array1))

test_array2 = [(1,3),(3,6), (3,5), (5,6)] # 2
print(maxProcess2(test_array2))

test_array3 = [(1,6), (3,4), (4,6), (5,6)] # 3
print(maxProcess2(test_array3))
