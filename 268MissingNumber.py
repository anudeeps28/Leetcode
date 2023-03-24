class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        sortedNums = sorted(nums)

        for i in range(len(sortedNums)-1):
            if sortedNums[i] != sortedNums[i+1]-1:
                return sortedNums[i] + 1
        if sortedNums[0] != 0:
            return sortedNums[0] - 1
        return sortedNums[-1]+1

    # O(1) memory using bitwise XOR
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)
        
        for i in range(len(nums)):
            res += (i - nums[i])
        return res
    
    # O(1) memory using bitwise sum
    # sum of [0-3] - sum of original = 2




if __name__ == "__main__":
    s = Solution()
    numbers = [1]
    print(s.missingNumber(numbers))