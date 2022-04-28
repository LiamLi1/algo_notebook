
import collections

# Tree Node
class newNode:
    def __init__(self, item, parent):
        self.data = item
        self.left = self.right = None
        self.parent = parent

    def __repr__(self):
        return "node:{}".format(self.data)

#              1
#             / \
#            2   3
#           /  \  \
#          4    6  5
#         /      \  \
#        7        9  8
#        /         \
#       10         12
# Input : Given above tree with parent pointer and node 10
# Output : 12

'''
parent right/ 
parent right -> left most + same depth.

go parent, if parent -> right == cur or None , continue
i. find a parent, where its right != node, != none.
ii. parent-right
'''
def findRightSibling(node):
    height = 0
    cur = node
    parent = node.parent

    while parent:
        if (parent.right == None or parent.right == cur):
            pass
        else:
            cur_node = parent.right
            node = findNode(cur_node, height)
            if node:
                return node
        # continue moving up
        height += 1
        cur = parent
        parent = parent.parent
    return None


def findNode(node, height):
    # bfs to find the node with same depth.
    step = 0
    queue = collections.deque()
    queue.append(node)
    while queue and step <= height:
        leng = len(queue)
        for _ in range(leng):
            out_node = queue.popleft()
            if out_node and step == height:
                return out_node
            # add childrens
            if out_node.left:
                queue.append(out_node.left)
            if out_node.right:
                queue.append(out_node.right)
        step += 1
    return None



if __name__ == '__main__':
    #               1
    #             /   \
    #            2      3
    #           /  \     \
    #          4    6     5
    #         /      \    / \
    #        7        9  13   8
    #        /         \     /
    #       10         12   14

    root = newNode(1, None)
    root.left = newNode(2, root)
    root.left.left = newNode(4, root.left)
    root.left.left.left = newNode(7, root.left.left)
    root.left.left.left.left = newNode(10, root.left.left.left)
    root.left.right = newNode(6, root.left)
    root.left.right.right = newNode(9, root.left.right)
    root.left.right.right.right = newNode(12, root.left.right.right)
    root.right = newNode(3, root)
    root.right.right = newNode(5, root.right)
    root.right.right.left = newNode(13, root.right.right)
    root.right.right.right = newNode(8, root.right.right)
    root.right.right.right.left = newNode(14, root.right.right.right)


    # passing 10
    print("passing 10, return:{}".format(findRightSibling(root.left.left.left.left)))
    # passing 9
    print("passing 9, return:{}".format(findRightSibling(root.left.right.right)))
    # passing 12
    print("passing 12, return:{}".format(findRightSibling(root.left.right.right.right)))
    # passing 7
    print("passing 7, return:{}".format(findRightSibling(root.left.left.left)))
    # passing 14
    print("passing 14, return:{}".format(findRightSibling(root.right.right.right.left)))