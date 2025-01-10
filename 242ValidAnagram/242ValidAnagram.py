def isAnagram(letter1, letter2):
    hashmap = {}
    for letter1 in s:
        if letter1 in hashmap:
            hashmap[letter1] += 1
        else:
            hashmap[letter1] = 1
    
    for letter2 in t:
        if letter2 in hashmap:
            hashmap[letter2] -= 1
        else:
            hashmap[letter2] = -1

    for letter, frequency in hashmap.items():
        if frequency != 0:
            return False
    return True

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s,t))