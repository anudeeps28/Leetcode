from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        result = []

        while k > 0:
            dist,x,y = heapq.heappop(minHeap)
            result.append([x,y])
            k-=1
        
        return result
        

if __name__ == "__main__":
    s = Solution()
    points = [[1,3],[-2,2]]
    k = 1
    s.kClosest(points, k)