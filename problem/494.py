from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2

        @cache
        def dfs(i, c):
            if i < 0:
                return c == 0
            return dfs(i - 1, c) + dfs(i - 1, c - nums[i])

        return dfs(len(nums) - 1, target)


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    target = 3
    res = Solution().findTargetSumWays(nums, target)
    print(res)
