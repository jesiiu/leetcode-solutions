#45. Jump Game II

class Solution:
    def jump(self, nums) -> int:
        if len(nums) <= 1:
            return 0
        max_jump = nums[0]
        steps = 1
        current_max_jump = nums[0]
        for i in range(1, len(nums)):
            if i > current_max_jump:
                steps += 1
                current_max_jump = max_jump
            max_jump = max(max_jump, i + nums[i])
        return steps
            
    
sol = Solution()
sol.jump([2,3,1,1,4])
print()