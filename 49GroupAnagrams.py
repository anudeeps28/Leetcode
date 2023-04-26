class Solution(object):
    def groupAnagrams(self, strs):
        myMap = defaultdict(list) # dictionary of type list

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1
                
            myMap[tuple(count)].append(word)

        return myMap

        
if __name__ == "__main__":
    s = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    s.groupAnagrams(strs)

