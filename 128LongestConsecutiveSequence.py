class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n-1) not in numSet:
                length = 1
                while(n+length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

if __name__ == "__main__":
    s = Solution()
    numbers = [100,4,200,1,3,2]
    print(s.longestConsecutive(numbers))
