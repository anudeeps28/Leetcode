from typing import List
import heapq

# method -1 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sort
        nums.sort()
        # get the kth largest element = kth element from the back
        return nums[len(nums)-k]
    
# method - 2: using a max heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums: # creating a max heap
            heapq.heappush(heap, -1 * num)
        
        # pop k times
        while k > 0:
            val = heapq.heappop(heap)
            k -= 1

        return -1 * val
        
            


if __name__ == "__main__":
    s = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    print(s.findKthLargest(nums, k))
    