# 167. Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers, target: int):
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left += 1
            else:
                right -= 1
        return []


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
print()
