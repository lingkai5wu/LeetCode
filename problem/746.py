from itertools import pairwise
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        for i in range(2, n):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return cost[n - 1]

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        f0 = f1 = 0
        for c0, c1 in pairwise(cost):
            f0, f1 = f1, min(f0 + c0, f1 + c1)
        return f1
