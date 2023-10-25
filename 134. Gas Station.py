class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        current_gas = 0
        total_gas = 0
        start = 0
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                start = i + 1
                current_gas = 0
        return start if total_gas >= 0 else -1
sol = Solution()

print(sol.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]))
            
            
            