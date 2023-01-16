class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        roman = {"I":1, "V":5, "X":10, "L": 50, "C":100, "D":500, "M": 1000}
        for i in s:
            total += roman[i]
        if "IV" in s:
            total -= 2
        if "IX" in s:
            total -= 2
        if "XL" in s:
            total -= 20
        if "XC" in s:
            total -= 20
        if "CD" in s:
            total -= 200
        if "CM" in s:
            total -= 200
        return total