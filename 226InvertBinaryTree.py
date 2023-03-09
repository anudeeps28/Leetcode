class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # swap the children 
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # recursively do this
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

if __name__ == "__main__":
    s = Solution()
    # setting up the tree
    node1 = TreeNode(1)
    node3 = TreeNode(2)
    node2 = TreeNode(2, node1, node3)

    node6 = TreeNode(6)
    node9 = TreeNode(9)
    node7 = TreeNode(7, node6, node9)

    node4 = TreeNode(4, node2, node7)

    s.invertTree(node4)
