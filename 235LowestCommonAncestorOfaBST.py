class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root.val > p.val and root.val < q.val) or (root.val < p.val and root.val > q.val):
            return root
        else:
            if root.val == p.val or root.val == q.val:
                return root
            if root.val < p.val and root.val < q.val:
                return self.lowestCommonAncestor(root.right, p, q)
            if root.val > p.val and root.val > q.val:
                return self.lowestCommonAncestor(root.left, p, q)
            

if __name__ == "__main__":
    s = Solution()

    node0 = TreeNode(0)
    node3 = TreeNode(3)
    node5 = TreeNode(5)
    node7 = TreeNode(7)
    node9 = TreeNode(9)

    node4 = TreeNode(4)
    node4.left = node3
    node4.right = node5

    node2 = TreeNode(2)
    node2.left = node0
    node2.right= node4

    node8 = TreeNode(8)
    node8.left = node7
    node8.right = node9

    node6 = TreeNode(6)
    node6.left = node2
    node6.right = node8

    print(s.lowestCommonAncestor(node6 ,node2, node8))

