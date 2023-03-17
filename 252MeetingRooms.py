from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda i: i[0])

        for i in range(1, len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]

            if i1[1] > i2[0]:
                return False
        return True
            

if __name__ == "__main__":
    s = Solution()
    intervals = [[0,30],[5,10],[15,20]]

