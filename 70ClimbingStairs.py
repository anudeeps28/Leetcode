class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one

if __name__ == '__main__':
    s = Solution()
    n = 2

    print(s.climbStairs(n))