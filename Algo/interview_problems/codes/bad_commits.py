'''
找出所有的bad commit。给一个commit number 
n代表有0到n个commit,再给一个boolean isWorse(int c1,int c2)
方法,返回true代表c2比c1 bad。

commits. [0,1,1,2,2,2,2,3,3,3,3]
	    0,1,2,3,4,5,6,7,8,9,10
isWorse(1, 2) = False: 1 and 2 are same level, 2 is not bad.
isWorse(2, 3) = True: then 3 must be a bad commits.

Solution 1: O(N) -> go throught the array.
Solution 2: Binary Search:

left = 0, right = n - 1
if isWorse(left, right) == TRUE: means there is bad commit between then. Need to do search. Else: no bad version, can return.
'''
import unittest

class Solution:
	def findBadVersion(self, commits):
		'''
		return: boolean[]
		'''
		res = []
		self.search(0, len(commits) - 1, commits, res)
		return res

	def isWorse(self, i, j, commits):
		return commits[i] < commits[j]

	def search(self, left, right, commits, res):
		'''
		[0,1,1,2,2,2,3,3,3]
		 0,1,2,3,4,5,6,7,8

		search(0,8)
		mid = 4
		search(0,4) (4,8)
		'''
		if left == right:
			return
		if left == right - 1:
			if self.isWorse(left, right, commits):
				res.append(right)
			return
		mid = (left + right) // 2
		if self.isWorse(left, mid, commits):
			self.search(left, mid, commits, res)
		if self.isWorse(mid, right, commits):
			self.search(mid, right, commits, res)

class TestBadCommits(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.solution = Solution()

	def testGoodCase(self):
		commits = [0,1,1,2,2,2,3,3,3]
		res = self.solution.findBadVersion(commits)
		self.assertEqual(res, [1,3,6], 'Good case pass')

if __name__ == '__main__':
	unittest.main()