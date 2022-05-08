'''
example:
a-(b+c+b) = a-2b-c
3a(4b-3a) = 12ab-9aa
'''
import collections

def stringHelper(string):
    '''
    stack: map{a:2, ab:-3, ...}
    op_stack:['-','+', ...]

    when '(', add empty map {} in stack to save result in ()
    when ')', do one extra calculation

    Current version supports 2a(a+b)
    doesn't support (a+b)(c+d)
    doesn't support space ' ' very well
    
    '''

    stack = collections.deque()
    op_stack = collections.deque()
    op_stack.append('+')
    stack.append({})

    index = 0
    curStr = []
    curNum = -1
    while index < len(string):
        char = string[index]
        if ord('a') <= ord(char) <= ord('z'):
            if curNum == -1:
                curNum = 1
            curStr.append(char)
        elif ord('0') <= ord(char) <= ord('9'):
            if curNum == -1:
                curNum = 0
            curNum *= 10
            curNum += int(char)
        else:
            # now need to calculate tmp result.
            key = ''.join(sorted(curStr))
            curMap = {key: curNum}
            flag = doCalculation(curMap, op_stack, stack)
            curStr = []
            curNum = -1

            if char in '+-':
                op_stack.append(char)
            if char == '*':
                op_stack.append('*')
            if char == '(':
                if flag:
                    op_stack.append('*')
                op_stack.append('+')
                stack.append({})

            if char == ')':
                curMap = stack.pop()
                doCalculation(curMap, op_stack, stack)
        # print("index:{}, stack:{}".format(index, stack))
        index += 1

    res = stack.pop()
    # print(res)
    return res

def doCalculation(curMap, op_stack, stack):
    if curMap == {'': -1}:
        return False
    operator = op_stack.pop()
    if operator == '+':
        prevMap = stack.pop()
        stack.append(mapAddMap(prevMap, curMap))

    elif operator == '-':
        prevMap = stack.pop()
        stack.append(mapMinusMap(prevMap, curMap))

    elif operator == '*':
        stack.append(mapMutipleMap(stack.pop(), curMap))
    return True

def mapMinusMap(map1, map2):
    for k2, v2 in map2.items():
        if k2 in map1:
            map1[k2] -= v2
        else:
            map1[k2] = -v2
    return map1

def mapAddMap(map1, map2):
    for k1, v1 in map1.items():
        if v1 == 0:
            v1 = 1
        if k1 in map2:
            map2[k1] += v1
        else:
            map2[k1] = v1
    return map2

def mapMutipleMap(map1, map2):
    res = dict()
    for k1, v1 in map1.items():
        for k2, v2 in map2.items():
            newKey = ''.join(sorted(k1 + k2))
            if newKey not in res:
                res[newKey] = 0
            res[newKey] += v1 * v2
    return res


if __name__ == '__main__':
    print(stringHelper('a-(b+c+b)'))
    print(stringHelper('3a(4b-3a)'))
    print(stringHelper('3a(4b-3a(3c-2a))'))
    print(stringHelper('(a+b)*(a+b)*(a+b)'))

    '''
    print 
    {'a': 1, 'b': -2, 'c': -1}
    {'ab': 12, 'aa': -9}
    {'abc': 36, 'aab': -24, 'aac': -27, 'aaa': 18}
    {'bbb': 1, 'abb': 3, 'aab': 3, 'aaa': 1}
    '''