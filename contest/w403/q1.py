from math import inf
from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        res = inf
        nums.sort()
        m = len(nums)
        for i in range(m // 2):
            res = min(nums[i] + nums[m - 1 - i], res)
        return res / 2
