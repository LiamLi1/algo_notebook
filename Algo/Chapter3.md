## Nine Chapter Class 3

#### 二叉树（BST）+ 排序

BST 可以重复。定义上 左 < 父， 右 >= 父
### 模板
### 1. DFS/ Divide & Conquer /Morris
```java
Template 1: Traverse

public class Solution {
    public void traverse(TreeNode root) {
        if (root == null) {
            return;
        }
        // do something with root
        traverse(root.left);
        // do something with root
        traverse(root.right);
        // do something with root
    }
}


Tempate 2: Divide & Conquer

public class Solution {
    public ResultType traversal(TreeNode root) {
        // null or leaf
        if (root == null) {
            // do something and return;
        }
        
        // Divide
        ResultType left = traversal(root.left);
        ResultType right = traversal(root.right);
        
        // Conquer
        ResultType result = Merge from left and right.
        return result;
    }
}

Template 3: Morris

void morris_inOrder(BiTree T) {
    BNode *p = T, *temp;
    while(p != NULL) {
        if(p->left == NULL) {
            printf("%4c",p->ch);
            p = p->right;
        } else {
            temp = p->left;
            while(temp->right != NULL && temp->right != p) {
                temp = temp->right;
            }
            if(temp->right == NULL) {
                temp->right = p;
                // 前序 printf("%4c",p->ch);
				p = p->left;
            } else {
                temp->right = NULL;
				printf("%4c",p->ch);
                p = p->right;
            }
        }
        //中序 - 往右走 
        //前序 - 左为空 或者 往左走
    }
	
Template 4: While Loop (in/post order 比较难, preorder 直接可以写)
 public List<Integer> postorderTraversal(TreeNode root) {
        // write your code here
        List<Integer> result = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        
        if (root == null) {
            return result;
        }
        TreeNode node = root;
        // push all left nodes
        while (node != null) {
            stack.push(node);
            node = node.left;
        }
        while (!stack.empty()) {
            node = stack.peek();
            if (node.right != null) {
                node = node.right;
                stack.push(node);
                while (node.left != null) {
                    stack.push(node.left);
                    node = node.left;
                }
            } else {
                node = stack.pop();
                result.add(node.val); # post order
                while (!stack.empty() && stack.peek().right == node) {
                    node = stack.pop();
                    result.add(node.val); # post order
                }
            }
        }
        return result;
    }

                 1
                / \
                2 3
                \
                 4
                  \
                   5
                  /
                 6

post order: add to result when pop
    1: stack[1,2]
    2: stack[1,2,4]
    stack[1,2,4,5,6]
    stack[1,2,4,5], result[6]
    stack[1,], result[6,5,4,2]

in order: add to result when peek
result: [2,4,6,5,1,3]

pre-order? Stack. Push left, Push right.


```
[Morris Traversal遍历二叉树 ](https://www.jianshu.com/p/d2059062efac)

### 2. while 循环的 inorder, postorder traversal。
见Problem中 Binary Tree 的第二题。

### 2. BFS
while 队列循环 + for循环。见Problem 中 BFS，  Binary Tree Level Order Traversal


### 3. Quick Sort
```java


/*
* Quick Select/ 
* （1）至少需要一次交换（利用两边都==pivot的情况）来保证迭代的参数发生变化，避免死循环
* （2）全部都加等号。然后用一个if来判断是否交换。
*/
private void quickSort(int[] A, int start, int end) {
      if (start >= end) {
          return;
      }

      int left = start;
      int right = end;

      int pivot = A[(start + end) / 2];
      while(left <= right) {
          while(left <= right && A[left] < pivot) {
              left++;
          }
          while(left <= right && A[right] > pivot) {
              right--;
          }

          if (left <= right) {
              int temp = A[left];
              A[left] = A[right];
              A[right] = temp;
              left++;
              right--;
          }

      }
      quickSort(A, start, right);
      quickSort(A, left, end);
  }
```

### 4. Merge Sort
- [x] [Sort LinkedList](https://www.lintcode.com/problem/sort-integers-ii/description)
- [xk] [Merge Sort来写数组排序](https://leetcode.com/problems/sort-an-array/description/)
### 5. Heap Sort
- [xk] [Heap Sort写数组排序](https://leetcode.com/problems/sort-an-array/description/)
- [k] [Quick Sort写数组排序](https://leetcode.com/problems/sort-an-array/description/)
- [k] [Kth largest element quick sort -> 快排模版](https://leetcode.com/problems/kth-largest-element-in-an-array/description/) 

### 6. 排序总结
桶排序：先划分成若干个桶(比如用map，0-9/10-19/.../)， 桶内排序以后再合并。
稳定的排序: 
稳定性得好处：从一个键上排序，然后再从另一个键上排序，第一个键排序的结果可以为第二个键排序所用。

各排序算法的稳定性：

1、堆排序、快速排序、希尔排序、直接选择排序不是稳定的排序算法；

2、基数（桶）排序、冒泡排序、直接插入排序、折半插入排序、归并排序是稳定的排序算法。

冒泡：
```java
void bubbleSort(int[] A) {
	for (int i = 0; i < A.length; i++) {
		for(int j = A.length - 1; j >= i; j--) {
			if (A[j] < A[j - 1]) {
				swithch(A[j], A[j - 1]);
			}
		}
	}	
}

```

选择：
```java
void selectSort(int[] A) {
	for (int i = 0; i < A.length; i++) {
		for (int j = i; j < A.length; j++) {
			if (A[j] < A[i]) {
				swithch(A[j], A[i]);
			}
		}
	}
}

```

插入：
```java
void insertSort(int[] A) {
	for (int i = 1; i < A.length; i++) {
		int key = A[i];
		j = i - 1;
		while (j >= 0 && A[j] > key) {
			A[j + 1] = A[j];
			j--;
		}
		A[j + 1] = key;
	}
}
// 折半插入法，用二分来找最后一个插入点。
```

各路排序算法 O(nlogn)
```python
class Heap:
    def __init__(self, nums):
        self.heap = nums
        self.heapify()
        print("heap:{}".format(self.heap))

    def heapify(self):
        for i in range(len(self.heap) - 1, -1, -1):
            self.shiftDown(i)
        return
        
    def shiftDown(self, index):
        while len(self.heap) > index * 2 + 1:
            son = index * 2 + 1
            right_son = index * 2 + 2
            if right_son < len(self.heap) and self.heap[right_son] < self.heap[son]:
                son = right_son
            if self.heap[index] > self.heap[son]:
                temp = self.heap[son]
                self.heap[son] = self.heap[index]
                self.heap[index] = temp
            index = son
        # print("heap after shiftDown:{}".format(self.heap))
        return
    
    def pop(self):
        if self.size() <= 0:
            return None
        res = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.shiftDown(0)
        return res
    
    def size(self):
        return len(self.heap)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.heapSort(nums)
    
    def heapSort(self, nums):
        h = Heap(nums)
        res = []
        while(h.size() > 0):
            res.append(h.pop())
        return res 
    
    def mergeSort(self, nums, start, end):
        if end <= start + 1:
            return nums[start:end]
        
        mid = (start + end) // 2
        left = self.mergeSort(nums, start, mid)
        right = self.mergeSort(nums, mid, end)
        res = self.mergeArray(left, right)
        return res
        
        
    
    def mergeArray(self, nums1, nums2):
        res = []
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1
        
        if p1 < len(nums1):
            res.extend(nums1[p1:])
        if p2 < len(nums2):
            res.extend(nums2[p2:])
        # print(res)
        return res
        
    
    
    def quickSort(self, nums: List[int], start: int, end: int):
        # print("s:{}, e:{}".format(start, end))
        
        if not nums or end <= start:
            return
        pivot = nums[(start + end) // 2]
        
        left = start
        right = end
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right -= 1
        
        
        self.quickSort(nums, start, right)
        self.quickSort(nums, left, end)
        return
    
```         


---
### Problems 

- Binary Search Tree
- [xk] [Binary Tree Preorder Traversal (recursion/ divide & conquer/ no recursion)](https://www.leetcode.com/problems/binary-tree-preorder-traversal/description)
- [xk] :carrot: inorder by loop
- [xk] :carrot: postorder by loop
- [xk] :carrot: Morris inorder
- [xk] [Binary Tree Inorder/Preorder/Postorder Traversal (while loop)](https://www.leetcode.com/problems/binary-tree-inorder-traversal/description)
- divide & conquer （两种传值方式。这里主要是子节点传给父节点。而BST的第一题就用了父节点的传给子节点）
- [xk]  [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [xk]  [Balanced Binary Tree](https://www.leetcode.com/problems/balanced-binary-tree/)
- [xk] [$$$Binary Tree Maximum Path Sum$$$](https://www.leetcode.com/problems/binary-tree-maximum-path-sum/description) (对非法情况，求最大返回最小，求最小返回最大，求方案数返回0)
- [xk] [*Lowest Common Ancestor (包含parent指针 用List，或者不包含 用分治)](https://www.leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/)
```
返回值可以进一步简化：如果左边/右边有一边是lca就直接传上来。如果两边都是lca就返回root。如果root是p或者q就返回root。否则返回None。
```
- [k] [closest-binary-search-tree-value-ii/](https://leetcode.com/problems/closest-binary-search-tree-value-ii/)
```
搞懂为什么用stack可以遍历BST。实质上是吧前驱全部存进stack。
如果只是inorder traversal，可以不用peek，只pop。每次pop以后继续维护栈。

i. BST的特性 越深的节点 越接近target。 
推理：inorder traversl是桉顺序排列。all left son < node. all right son > node.
ii. 问题本质是：怎样从BST的一个点开始 traversal predecessor 和 successor
对predecessor：先往右，然后找到最左
对于successor：先往左，然后找到最右

```


### BFS
- [x] [Binary Tree Level Order Traversal](http://www.leetcode.com/problems/binary-tree-level-order-traversal/)
- Binary Search Tree
- [xk] [Validate Binary Search Tree](http://www.leetcode.com/problems/validate-binary-search-tree/) 
```
两种思路，分别对应前序/后序遍历。前序把父节点参数传给子节点。后序把子节点结果传回父节点。
这用前序遍历的思路，把父节点的参数传给子节点再来分治，写起来更简洁，可以当作另一种思路的模板。用divideConquer也可以做。类似LCA。
```
- [k] :carrot: 还有一个性质是，后序遍历时得到最小值排序。 

```java
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: True if the binary tree is BST, or false
     */
    public boolean isValidBST(TreeNode root) {
        // write your code here
        return divConq(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    
    private boolean divConq(TreeNode root, long min, long max){
        if (root == null){
            return true;
        }
        if (root.val <= min || root.val >= max){
            return false;
        }
        return divConq(root.left, min, Math.min(max, root.val)) && 
                divConq(root.right, Math.max(min, root.val), max);
    }
}
```
- [xk] [Insert Node in a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)
前序 + 返回root以改变bst的结构
```python
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
```

- [k] [Search Range in a Binary Search Tree]https://leetcode.com/problems/range-sum-of-bst/
- [xxk] :memo: [$$$Remove Node in Binary Search Tree$$$](https://leetcode.com/problems/delete-node-in-a-bst/description/)第一道hard难度的题。和 Insert 一样，通过分治返回TreeNode的方式来改变BST的结构。  而且也是前序的思路完成的分治。
- [xxk] [*Binary Search Tree Iterator](https://www.leetcode.com/problems/binary-search-tree-iterator/description) 


---

## 二刷

- [xx] [inorder-predecessor-in-bst](https://www.lintcode.com/problem/inorder-predecessor-in-bst/description)
```
一般的找前驱/后驱，用while+stack容易能看清楚访问的逻辑。
BST找，并且一定存在这个点，那么问题就转换成找最后一个比p.val小的点。可以直接递归搜索。

BST的前序搜索可以用while来模拟。因为每次只走一边，if以后的所搜某一边换成root = root.left/root.right 就可以了。

如果是遍历二叉树 需要用queue. 但是bst只走一遍，相当于queue size=1，直接while就行。
```

