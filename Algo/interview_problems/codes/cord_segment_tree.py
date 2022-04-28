class Solution:
    def __init__(self, string, max_leaf_length = 5):
        self.max_leaf_length = max_leaf_length
        self.root = self.build(string, 0, len(string) - 1)

    def build(self, string, left, right):
        if right - left + 1 <= self.max_leaf_length:
            node = TreeNode(right - left + 1, True, string[left:right + 1])
        else:
            mid = (right + left) // 2 # (0 + 4) // 2 = 2, (0, 2), (3, 4) | (0 + 5) // 2 = 2, (0, 2), (3, 5)
            node = TreeNode(right - left + 1)
            node.left = self.build(string, left, mid)
            node.right = self.build(string, mid + 1, right)
        print("node:{}".format(node))
        return node

    def get_index(self, index):
        return self.get_index_helper(index, self.root)

    def get_index_helper(self, index, node):
        if node.isLeaf:
            return node.word[index]

        if node.left.length > index:
            return self.get_index_helper(index, node.left)
        else:
            index -= node.left.length
            return self.get_index_helper(index, node.right)

    def remove_substr(self, start, end):
        return self.remove_substr_helper(start, end, self.root)

    def remove_substr_helper(self, start, end, node):
        if node.isLeaf:
            node.word = node.word[:start] + node.word[end + 1:]
            node.length = len(node.word)
            return node
        if node.left.length <= end:
            node.right = self.remove_substr_helper(max(0, start - node.left.length), end - node.left.length, node.right)
        if node.left.length > start:
            node.left = self.remove_substr_helper(start, end, node.left)
        node.length = node.left.length + node.right.length
        return node

class TreeNode:
    def __init__(self, length=0, isLeaf=False, word=""):
        self.left, self.right = None, None
        self.length = length
        self.isLeaf = isLeaf
        self.word = word

    def __repr__(self):
        return "length:{}, word:{}".format(self.length, self.word)

if __name__ == "__main__":

    string = "my_name_is_lian_i_am_coding_now_lololol"
    solution = Solution(string)
    for index in range(len(string)):
        print("index:{}, char:{}".format(index, solution.get_index(index)))

    solution.remove_substr(3, 7)

    for index in range(len(string) - 5):
        print("index:{}, char:{}".format(index, solution.get_index(index)))



