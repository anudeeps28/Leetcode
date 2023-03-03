class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i,n in enumerate(nums):
            difference = target - n
            if difference in hashmap:
                return [hashmap[difference], i]
            hashmap[n] = i
            

if __name__ == "__main__":
    s = Solution();
    numbers = [1,2,3,4]
    target = 3

    answer = s.twoSum(numbers, target)

    for i in answer:
        print(i)

