’‘’
一个class，一开始为空，有三个method，setManager(M, E), 
M是E的direct manager，setPeers(E1, E2), 
E1和E2是peers，E1的direct manager不是E2的，
queryManager(MM, E)，问MM是否是E的manager，
可以是很多层的manager。这三个method被call的顺序是随机的
‘’‘
class Solution:
    def __init__(self):
        self.peerMap = dict()
        self.managerMap = dict()
        self.peer_id = 0

    def setPeer(self, e1, e2):
        if e1 in self.peerMap:
            p = self.peerMap[e1]
        elif e2 in self.peerMap:
            p = self.peerMap[e2]
        else:
            p = 'p' + str(self.peer_id)
            self.peer_id += 1
        self.peerMap[e1] = p
        self.peerMap[e2] = p

    def setManager(self, m, e):
        if e in self.peerMap:
            pe = self.peerMap[e]
        else:
            pe = 'p' + str(self.peer_id)
            self.peerMap[e] = pe
            self.peer_id += 1

        if m in self.peerMap:
            pm = self.peerMap[m]
        else:
            pm = 'p' + str(self.peer_id)
            self.peerMap[m] = pm
            self.peer_id += 1

        self.managerMap[pe] = m

    def isManager(self, m, e):
        pm = self.peerMap[m]
        pe = self.peerMap[e]

        while pe != None and pe != pm:
            pe = self.managerMap.get(pe, None)
        if pe == pm:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    '''
    '''
    s.setPeer('a', 'b')
    s.setManager('c', 'a')
    s.setManager('b', 'e')

    print(s.isManager('c', 'a'))
    print(s.isManager('c', 'e'))
    print(s.isManager('e', 'a'))

