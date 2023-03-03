class Solution(object):
    def groupAnagrams(self, strs):
        myMap = {}

        for i in strs:
            myMap[sorted(i)] = i

        
if __name__ == "__main__":
    s = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    s.groupAnagrams(strs)

