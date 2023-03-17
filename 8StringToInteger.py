class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 0
        # read and ignore any whitespace
        newS = s.lstrip()
        # check if the next character is + or -
        if newS[0] == "-":
            sign = -1
        else:
            sign = 1
        # read all digit characters
        digits = " "
        for num in newS:
            if num.isdigit():
                digits += num
        # convert the string to an int. If no digits, int is 0
        if not digits:
            return 0
        result = int(digits)*sign
        # clamp the integers
        
        return result

if __name__ == "__main__":
    s = Solution()
    myString = "42"
    print(s.myAtoi(myString))
    