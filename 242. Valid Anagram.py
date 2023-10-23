#242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        for i in range(len(s)):
            count = 0
            sc = s.count(s[i])
            tc = t.count(s[i])
            if sc != tc:
                return False
            if sc == 0 and tc == 0:
                return False
        return True
    
sol = Solution()
sol.isAnagram("rat", "car")
print()