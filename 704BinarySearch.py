class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left+right)//2 # or ()left + (right - left)//2) in case of memory overflow
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

if __name__ == "__main__":
    s = Solution()
    array = [1,2,3,5,6,7,9]
    target = 7
    print(s.search(array,target))