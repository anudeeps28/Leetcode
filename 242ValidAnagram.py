class Solution(object):
    def isAnagram(self, s, t):
        myMap = {}
        
        for i in s:
            if i not in myMap:
                myMap[i] = 0
            myMap[i] += 1
        
        for i in t:
            if i not in myMap:
                myMap[i] = 0
            myMap[i] -= 1

        for val in myMap.values():
            if val != 0:
                return False
        return True

        

if __name__ == "__main__":
    S = Solution()
    s = "anagram"
    t = "nagaram"
    print(S.isAnagram(s,t))
