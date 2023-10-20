# 219. Contains Duplicate II
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_indexes = ()
        for i, num in enumerate(nums):
            if num in num_indexes and abs(i - num_indexes[num]) <= k:
                return True
            num_indexes[num] = i
        return False
