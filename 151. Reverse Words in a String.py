#151. Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        filtered = [word for word in temp if word != '']
        reversed = " ".join(filtered[::-1])
        return reversed
        
sol = Solution()
print(sol.reverseWords("  hello world  "))