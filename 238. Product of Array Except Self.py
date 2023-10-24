#238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums):
        # res = []
        # left = 1
        # right = 1
        # for i in range(len(nums)):
        #     for l in range(i - 1, -1, -1):
        #         left *= nums[l]
        #     for r in range(i + 1, len(nums), 1):
        #         right *= nums[r]
        #     res.append(left * right)
        #     left = 1
        #     right = 1
        # return res
        n = len(nums)
        left = [1] * n
        right = [1] * n
        result = [1] * n
        
        left_sum = 1
        right_sum = 1
        
        for i in range(n):
            left[i] = left_sum
            left_sum *= nums[i]
        for i in range(n -1, -1, -1):
            right[i] = right_sum
            right_sum *= nums[i]
        for i in range(n):
            result[i] = left[i] * right[i]
        return result
        
sol = Solution()
sol.productExceptSelf([-1,1,0,-3,3])
print()