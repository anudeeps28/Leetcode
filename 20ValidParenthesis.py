class Solution(object):
    def isValid(self, s):
        stk = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stk.append(s[i])
            elif s[i] == ")" and (not stk or stk.pop() != "("):
                return False
            elif s[i] == "}" and (not stk or stk.pop() != "{"):
                return False
            elif s[i] == "]" and (not stk or stk.pop() != "["):
                return False
        return not stk


if __name__ == "__main__":
    S = Solution()
    s = "()"
    print(S.isValid(s))

