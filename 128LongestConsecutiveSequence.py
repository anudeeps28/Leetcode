class Solution(object):
    # custon alphanumeric function
    def alphanum(self, c):
        return(
            ord("A") <= ord(c) <= ord("Z") 
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )
    
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            while l<r and not self.alphanum(s[l]):
                l += 1
            while l<r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


        
if __name__ == "__main__":
    s = Solution()
    string = "0P"
    print(s.isPalindrome(string))
