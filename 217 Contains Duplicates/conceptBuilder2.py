def if_duplicate(nums):
    # declaring hashmap
    hashmap = {}

    # putting numbers in hashmap with their frequency
    for num in nums:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1
    
    # printing numbers if their frequency > 1
    for number, frequency in hashmap.items():
        if frequency > 1:
            print(number)

if __name__ == "__main__":
    arr = [4, 5, 6, 4, 7, 5]
    if_duplicate(arr)