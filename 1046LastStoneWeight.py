from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # making max heap
        stones = [-s for s in stones]
        heapq.heapify(stones) # O(n)

        while len(stones) > 1:
            first = heapq.heappop(stones) # this gives the largest
            second = heapq.heappop(stones) 

            if second > first: # remember they are -ve
                heapq.heappush(stones, first - second)
        
        stones.append(0) # if the list was empty, we are appending that so that we can return that
        return abs(stones[0])



            

if __name__ == "__main__":
    s = Solution()
    stones = [2,7,4,1,8,1]
    s.lastStoneWeight(stones)