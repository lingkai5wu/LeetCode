class Solution:
    def numSteps(self, s: str) -> int:
        x = int(s, 2)
        res = 0
        while x > 1:
            if x & 1 == 1:
                x += 1
                res += 1
            x >>= 1
            res += 1
        return res
