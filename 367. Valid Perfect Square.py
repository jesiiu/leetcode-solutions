#367. Valid Perfect Square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        check = num ** 0.5
        if check.is_integer():
            return True
        return False
    
sol = Solution()
res = sol.isPerfectSquare(4)
print(res)