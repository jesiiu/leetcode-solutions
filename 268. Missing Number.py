#268. Missing Number

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        expec = (n * (n + 1)) // 2
        actual = sum(nums)
        return int(expec - actual)        
sol = Solution()
sol.missingNumber([1])
print("")