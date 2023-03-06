class Solution(object):
    def mySqrt(self, x):
        counter = 0
        i = 1
        while x >= 0:
            x = x - i
            i += 2
            counter += 1

        return counter - 1

if __name__ == "__main__":
    s = Solution()
    number = 36
    print(s.mySqrt(number))
