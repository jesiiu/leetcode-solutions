#205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        memo = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in memo:
                if t[i] not in memo.values():
                    memo.update({s[i]: t[i]})
                else:
                    return False
            if s[i] in memo:
                curr = memo.get(s[i])
                if t[i] != curr:
                    return False
        return True
    
sol = Solution()
sol.isIsomorphic("badc", "baba")
print("")