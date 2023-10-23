# 122. Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        sell = 0
        sum = 0
        for i in range(1, len(prices)):
            sell = prices[i]
            if sell - buy < 0:
                buy = prices[i]
            elif sell - buy >= 0:
                sum += (sell - buy)
                buy = prices[i]
        return sum


sol = Solution()
res = sol.maxProfit([7,1,5,3,6,4])
print(res)
