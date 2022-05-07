'''
给一个stream，每次进来一个新的floating point num存到池子里，如果池子里有三个number两两之间的差小于d就把这三个数从池子里删掉并返回。

1,5,7,3
[1,5,7] -> [7]
'''
from sortedcontainers import SortedList

def streamUpdate(stream, target):
    sl = SortedList()

    for num in stream:
        # insert num
        sl.add(num)
        index = sl.index(num)
        # Three conditions that need to remove nums
        # (index - 2, index - 1, index) (index - 1, index, index + 1), (index, index + 1, index + 2)
        flag = False
        if index - 2 >= 0:
            num1 = sl[index -  2]
            num2 = sl[index - 1]
            num3 = sl[index]
            if num2 - num1 <= target and num3 - num2 <= target:
                flag = True
        elif flag == False and index - 1 >= 0 and index + 1 < len(sl):
            num1 = sl[index - 1]
            num2 = sl[index]
            num3 = sl[index + 1]
            if num2 - num1 <= target and num3 - num2 <= target:
                flag = True
        elif flag == False and index + 2 < len(sl):
            num1 = sl[index]
            num2 = sl[index + 1]
            num3 = sl[index + 2]
            if num2 - num1 <= target and num3 - num2 <= target:
                flag = True

        if flag:
            sl.remove(num1)
            sl.remove(num2)
            sl.remove(num3)

        print(sl)

if __name__ == '__main__':
    streamUpdate([1,5,7,3,8,9,11,30,40], 2)