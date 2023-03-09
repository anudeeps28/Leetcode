class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        
    
            
            

if __name__ == "__main__":
    s = Solution()

    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1 = TreeNode(1, node2, node3)

    node5 = TreeNode(2)
    node6 = TreeNode(3)
    node4 = TreeNode(1, node5, node6)

    print(s.isSameTree(node1, node4))