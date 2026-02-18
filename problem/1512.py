from collections import defaultdict
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = defaultdict(int)
        res = 0
        for x in nums:
            res += d[x]
            d[x] += 1
        return res
