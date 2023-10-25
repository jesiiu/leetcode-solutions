#11. Container With Most Water

class Solution:
    def maxArea(self, height) -> int:
        i, j = 0, len(height) - 1
        res = []
        while True:
            cap = min(height[i], height[j]) * (j - i)
            res.append(cap)
            if height[i] <= height[j]:
                i += 1
            elif height[i] >= height[j]:
                j -= 1
            if i > j:
                break
        return max(res)
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))