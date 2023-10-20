# 228. Summary Ranges
class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        start, next, end = nums[0], nums[0], None
        res = []
        for i in nums[1:]:
            next += 1
            if i == next:
                end = i
            else:
                if not end:
                    res.append(str(start))
                else:
                    res.append(str(start)+"->"+str(end))
                start = i
                next = i
                end = None
        if not end:
            res.append(str(start))
        else:
            res.append(str(start)+"->"+str(end))
        return res


sol = Solution()
res = sol.summaryRanges([0, 2, 3, 4, 6, 8, 9])
print(res)
