#15. 3Sum

class Solution:
    def threeSum(self, nums):
        nums.sort()  # Sortujemy tablicę, co ułatwi nam pracę z dwoma wskaźnikami
        res = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Pomijamy duplikaty
            
            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1 
                    
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  
                    
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return res
            
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))