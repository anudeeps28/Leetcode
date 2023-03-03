class Solution(object):
    def containsDuplicate(self, nums) -> bool:
        myList = set()

        for i in nums:
            if i in myList:
                return True
            myList.add(i)
        return False

if __name__ == "__main__":
    s = Solution()
    numbers = [1,2,3,1]
    print(s.containsDuplicate(numbers))