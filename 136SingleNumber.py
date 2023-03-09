class Solution:
    def singleNumber(self, nums: int) -> int:
        map = {}

        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]] += 1
            else:
                map[nums[i]] = 1
        
        for key, value in map.items():
            if value == 1:
                return key

if __name__ == "__main__":
    s = Solution()
    numbers = [2,1,2]
    print(s.singleNumber(numbers))