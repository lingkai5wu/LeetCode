from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = 0
        pre_min = nums[0]
        for n in nums[1:]:
            res = max(res, n - pre_min)
            pre_min = min(pre_min, n)
        return res or -1
