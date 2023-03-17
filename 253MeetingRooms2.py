from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        time = []
        for start, end in intervals:
            time.append((start, 1))
            time.append((end, -1))

        time.sort(key=lambda x: (x[0], x[1]))

        count = 0
        maxCount = 0
        for t in time:
            count += t[1]
            maxCount = max(maxCount, count)
        return maxCount
    

# alternate solution
# def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         rooms = 0
#         if not intervals:
#             return 0
        
#         endp = 0
#         starts = sorted([i[0] for i in intervals])
#         ends = sorted([i[1] for i in intervals])
        
#         for i in range(len(starts)):
#             if starts[i]>=ends[endp]:
#                 endp+=1
#             else:
#                 rooms+=1
        
#         return rooms            

if __name__ == "__main__":
    s = Solution()
    intervals = [[0,30],[5,10],[15,20]]
