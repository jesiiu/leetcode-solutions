#349. Intersection of Two Arrays

class Solution:
    def intersection(self, nums1, nums2):
        memo = {}
        res = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                memo.update({nums1[i]: i})
        return list(memo.keys())
    
sol = Solution()
res = sol.intersection([4,9,5], [9,4,9,8,4])
print(res)