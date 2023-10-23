# 283. Move Zeroes

class Solution:
    # def moveZeroes(self, nums) -> None:
    #     for i in range(len(nums)):
    #         for z in range(len(nums)):
    #             if nums[z] == 0:
    #                 nums += [nums.pop(z)]

    #     return nums
    def moveZeroes(self, nums) -> None:
        for i in nums:
            if i == 0:
                nums.remove(0)
                nums.insert(len(nums), 0)
        return nums


sol = Solution()
sol.moveZeroes([0,1,0,3,12])
print()
