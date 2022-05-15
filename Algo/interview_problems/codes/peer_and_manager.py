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

        if m not in self.peerMap:
            pm = 'p' + str(self.peer_id)
            self.peerMap[m] = pm
            self.peer_id += 1

        self.managerMap[pe] = m

    def isManager(self, m, e):

        pe = self.peerMap[e]
        me = self.managerMap.get(pe, None)

        while me != None and me != m:
            pm = self.peerMap[me]
            me = self.managerMap.get(pm, None)
        if me == m:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    '''
    p2 <- [e]    peerMap:{e:p2}
    p1 <- [c]    peerMap:{c:p1}
    p0 <- [a, b] peerMap:{a:p0, b:p0}
    '''
    s.setPeer('a', 'b')
    s.setManager('c', 'a')
    s.setManager('b', 'e')

    print(s.managerMap)
    print(s.peerMap)

    print(s.isManager('c', 'a'))
    print(s.isManager('c', 'e'))
    print(s.isManager('e', 'a'))

