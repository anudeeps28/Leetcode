def isAnagram(letter1, letter2):
    hashmap = {}
    for letter in s:
        if letter in hashmap:
            hashmap[letter] += 1
        else:
            hashmap[letter] = 1
    
    for letter in t:
        if letter in hashmap:
            hashmap[letter] -= 1
        else:
            hashmap[letter] = -1

    for letter, frequency in hashmap.items():
        if frequency != 0:
            return False
    return True

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s,t))