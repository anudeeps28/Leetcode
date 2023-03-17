from collections import heapq
from collections import Counter 

class Solution:
    def reorganizeString(self, S: str) -> str:
        count = Counter(S) # hashmap, count each char
        maxheap = [(-cnt,char) for char,cnt in count.items()]
        heapq.heapify(maxheap) # O(n) -> this line will turn that into a heap
        
        prev = None
        res = ""

        while maxheap or prev:
            if prev and not maxheap:
                return ""

            # most frequent, except prev
            cnt, char = heapq.heappop(maxheap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxheap, prev)

            if cnt != 0:
                prev = [cnt, char]
        
        return res
