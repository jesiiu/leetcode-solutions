#171. Excel Sheet Column Number
class Solution(object):
    def titleToNumber(self, columnTitle):
        result = 0
        for l in range(len(columnTitle)):
            result *= 26
            result += ord(columnTitle[l]) - ord('A') + 1
            
        return result
        