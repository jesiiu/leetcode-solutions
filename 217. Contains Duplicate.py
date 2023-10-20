#217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memo = set()
        for i in range(len(nums)):
            if nums[i] in memo:
                return True
            memo.add(nums[i])
        return False