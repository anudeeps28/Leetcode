from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adjcencyList = {i: [] for i in range(n)}
        
        # it is an undirected graph
        for n1, n2 in edges:
            adjcencyList[n1].append(n2)
            adjcencyList[n2].append(n1)

        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)
            
            for j in adjcencyList[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
                
            return True
        
        return dfs(0,-1) and n == len(visited)


if __name__ == "__main__":
    s = Solution()
    n = 5 
    edges = [[0,1],[0,2],[0,3],[1,4]]
    s.validTree(n, edges)