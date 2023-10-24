# 274. H-Index

class Solution:
    def hIndex(self, citations) -> int:
        citations.sort(reverse=True)  # Sortuj cytowania malejąco

        h_index = 0
        for i, citation in enumerate(citations, start=1):
            if citation >= i:
                h_index = i
            else:
                break

        return h_index


sol = Solution()
res = sol.hIndex([3, 0, 6, 1, 5])
print(res)
