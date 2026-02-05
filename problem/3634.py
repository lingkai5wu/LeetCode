from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        max_size = 0
        for j in range(n):
            while nums[i] * k < nums[j]:
                i += 1
            max_size = max(max_size, j - i + 1)
        return len(nums) - max_size
