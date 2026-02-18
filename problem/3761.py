import math
from typing import List


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        d = {}
        res = math.inf
        for i, n in enumerate(nums):
            if n in d:
                res = min(res, i - d[n])
            d[int(str(n)[::-1])] = i
        return -1 if res == math.inf else res
