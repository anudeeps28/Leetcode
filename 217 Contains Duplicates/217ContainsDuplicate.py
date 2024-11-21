class Solution(object):
    def containsDuplicate(self, nums) -> bool:
        myList = set()

        for num in nums:
            if num in myList:
                return True
            myList.add(num)
        return False

if __name__ == "__main__":
    s = Solution()
    numbers = [1,2,3,1]
    print(s.containsDuplicate(numbers))
