import math
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        res = math.inf
        nums.sort()
        for i in range(len(nums) - k + 1):
            res = min(res, nums[i + k - 1] - nums[i])
        return res
