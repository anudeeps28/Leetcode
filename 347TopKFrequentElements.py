import heapq #in-built heap implementation in python

class Solution(object):
    def topKFrequent(self, nums, k):
        freqMap = {}
        ans = []
        
        for num in nums:
            if not num in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] += 1

        # heappush and heappushpop are just meathods of pushing and popping which will maintain the heap
        # maintaining the heap = will keep just the most frequent elements in the ans array, deleting the less frequent items
        for key, value in freqMap.items():
            if len(ans) < k:
                heapq.heappush(ans, [value, key])
            else:
                heapq.heappushpop(ans, [value, key])
            # (1,2) is considered smaller than (2,3)
        
        return [key for value, key in ans]

if __name__ == "__main__":
    s =  Solution()
    numbers = [1,1,1,2,2,3]
    s.topKFrequent(numbers)

