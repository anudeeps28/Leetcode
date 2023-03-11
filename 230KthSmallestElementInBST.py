from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = deque()        
        curr = root
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

    # Recursive approach
    def kthSmallest(self, root, k):
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)


if __name__ == "__main__":
    
    s = Solution()

    node2 = TreeNode(2)
    node1 = TreeNode(1)
    node4 = TreeNode(4)
    node3 = TreeNode(3)

    node1.right = node2
    node3.left = node1
    node3.right = node4

    s.kthSmallest(node3, 1)

