from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix
            


if __name__ == "__main__":
    s = Solution()
    # strs = ["flower","flow","flight"]
    strs = [""]
    print(s.longestCommonPrefix(strs))
