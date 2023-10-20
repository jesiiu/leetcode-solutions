#119. Pascal's Triangle II

class Solution:
    # def getRow(self, rowIndex: int) -> List[int]:
    #     if rowIndex <= 0:
    #         return [1]
    #     triangle = []

    #     for i in range(rowIndex):
    #         row = [1] * (i + 1)
    #         for j in range(1, i):
    #             row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    #         triangle.append(row)
    #     return triangle[rowIndex- 1]
    def getRow(self, rowIndex: int):
        row = []
        row.append(1)
        if rowIndex == 0:
            return row
        prev = self.getRow(rowIndex - 1)
        for i in range(1, len(prev)):
            current = prev[i - 1] + prev[i]
            row.append(current)
        row.append(1)
        return row
    
sol = Solution()
result = print(sol.getRow(3))
print("")