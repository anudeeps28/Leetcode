from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        finalArr = []
        
        for num in nums:
            if num not in finalArr:
                finalArr.append(num)
        
        return len(finalArr)


if __name__ == "__main__":
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]

    print(s.removeDuplicates(nums))