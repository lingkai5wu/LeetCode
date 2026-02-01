from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        arr = sorted(nums[1:])
        return sum([nums[0]] + arr[:2])
