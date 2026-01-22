from typing import List


class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums_set = set(nums)
        nums_set_list = sorted(nums_set, reverse=True)
        return nums_set_list[:k]
