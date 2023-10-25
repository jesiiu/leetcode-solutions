# 12. Integer to Roman
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = [
            ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
            ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
            ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
        ]

        roman = ""
        for symbol, value in roman_numerals:
            while num >= value:
                roman += symbol
                num -= value

        return roman


sol = Solution()
print(sol.intToRoman(1994))
