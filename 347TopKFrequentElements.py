import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        freqMap = {}
        ans = []
        
        for num in nums:
            if not num in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] += 1

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
