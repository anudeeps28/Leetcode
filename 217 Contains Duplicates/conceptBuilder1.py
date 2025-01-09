def frequency_counter(nums):
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    for num, freq in frequency.items(): # items is used with frequency to iterate
        print(num, freq)

if __name__ == "__main__":
    arr = [1,2,3,1]
    frequency_counter(arr)

