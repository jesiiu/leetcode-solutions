# 350. Intersection of Two Arrays II

class Solution:
    def intersect(self, nums1, nums2):
        res = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.append(nums1[i])
                nums2.remove(nums1[i])
        return res
    
sol = Solution()
res = sol.intersect([1,2,2,1], [2,2])
print(res)