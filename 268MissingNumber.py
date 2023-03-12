class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        sortedNums = sorted(nums)

        for i in range(len(sortedNums)-1):
            if sortedNums[i] != sortedNums[i+1]-1:
                return sortedNums[i] + 1
        if sortedNums[0] != 0:
            return sortedNums[0] - 1
        return sortedNums[-1]+1




if __name__ == "__main__":
    s = Solution()
    numbers = [1]
    print(s.missingNumber(numbers))