#55. Jump Game

class Solution:
    def canJump(self, nums):
        jump = 0
        for i in range(len(nums)):
            if i > jump:
                return False
            jump = max(jump, i + nums[i])
            if jump >= len(nums) - 1:
                return True
        return False
        