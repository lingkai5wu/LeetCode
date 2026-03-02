import math


class Solution:
    def minCost(self, n: int) -> int:
        return math.comb(n, 2)
