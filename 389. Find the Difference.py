#389. Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # letters_fist = {}
        # for x in s:
        #     if x not in letters_fist:
        #         letters_fist.update = {x, s.count(x)}
        return [x for x in t if t.count(x) > s.count(x)][0]