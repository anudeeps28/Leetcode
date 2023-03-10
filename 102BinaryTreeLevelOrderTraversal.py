from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution: # basically bfs
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        q = deque()
        result = []
        q.appendleft(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.pop()
                if node:
                    level.append(node.val)
                    q.appendleft(node.left)
                    q.appendleft(node.right)
            if level:
                result.append(level)
            
        return result

if __name__ == "__main__":
    s = Solution()

    node9 = TreeNode(9)
    node15 = TreeNode(15)
    node7 = TreeNode(7)

    node20 = TreeNode(20, node15, node7)
    node3 = TreeNode(3, node9, node20)

    s.levelOrder(node3)
    
    