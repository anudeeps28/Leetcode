class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        if n%2 != 0:
            return False
        if n == 2:
            return True
        n = n//2

        return self.isPowerOfTwo(n)
        
if __name__ == "__main__":
    s = Solution()
    n = 16
    print(s.isPowerOfTwo(n))
