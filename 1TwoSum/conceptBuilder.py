def hasPairWithSum(nums, target):
    hashmap = {} # this is essentially a dictionary
    for index, number in enumerate(nums):
        difference = target - number
        if difference in hashmap:
            return [index, hashmap[difference]]
        hashmap[number] = index

if __name__ == "__main__":
    arr = [1,2,4,4]
    target = 8
    answer = hasPairWithSum(arr,target)
    for i in answer:
        print(i)
