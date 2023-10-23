#258. Add Digits
class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) < 2:
            return num
        cache = num
        ptr = 0
        sum = 0
        while len(str(cache)) >= 2:
            for i in range(len(str(cache))):
                sum += int(str(cache)[i])
            prt = sum
            sum = 0
            cache = prt
        return prt
    
    
sol = Solution()
sol.addDigits(39)
print("")