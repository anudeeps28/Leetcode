from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() # this will sort the interval based on first the start, and then the end value (if there is a tie)

        result = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                result += 1
                prevEnd = min(end, prevEnd)

        return result

if __name__ == "__main__":
    s = Solution()
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    s.eraseOverlapIntervals(intervals)


