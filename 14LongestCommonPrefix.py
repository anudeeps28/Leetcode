from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs[0]:    
            return strs
        
        strs.sort()

        str1 = strs[0]
        str2 = strs[-1]

        result = ""
        i = 0

        while i < len(strs):
            if str1[i] == str2[i]:
                result += str1[i]
                i += 1
            else:
                break
                
        return result
            


if __name__ == "__main__":
    s = Solution()
    # strs = ["flower","flow","flight"]
    strs = [""]
    print(s.longestCommonPrefix(strs))
