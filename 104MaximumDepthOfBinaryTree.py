from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # method1 - recursive dfs
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    # method2 - iterative bfs
    def iterativeBfs(self, root):
        if not root:
            return 0

        level = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level


    # method3 - iterative dfs
    def iterativeDfs(self, root):
        stack = [[root, 1]]
        result = 0

        while stack:
            node, depth = stack.pop()
            if node:
                result = max(result, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return result

if __name__ == "__main__":
    s = Solution()
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    node9 = TreeNode(9)
    node20 = TreeNode(20, node15, node7)
    node3 = TreeNode(3, node9, node20)
    


