#231. Power of Two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        
        m = n & (n - 1)
        if m == 0:
            return True
        return False