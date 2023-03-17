class Solution:
    def romanToInt(self, s: str) -> int:
        myMap = {}

        myMap["I"] = 1
        myMap["V"] = 5
        myMap["X"] = 10
        myMap["L"] = 50
        myMap["C"] = 100
        myMap["D"] = 500
        myMap["M"] = 1000

        result = 0

        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")

        for char in s:
            result += myMap[char]
        return result
    
        # another way
        # if "IV" in s:
        #     total -= 2
        # if "IX" in s:
        #     total -= 2
        # if "XL" in s:
        #     total -= 20
        # if "XC" in s:
        #     total -= 20
        # if "CD" in s:
        #     total -= 200
        # if "CM" in s:
        #     total -= 200

if __name__ == "__main__":
    s = Solution()
    myString = "IV"

    print(s.romanToInt(myString))