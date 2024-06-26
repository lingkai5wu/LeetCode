from functools import cache
from math import inf
from typing import List


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        m = len(nums)

        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            x = -inf
            if i > 0:
                x = dfs(i - 2) + nums[i - 1] - nums[i]
            return max(dfs(i - 1) + nums[i], x)

        return dfs(m - 1)


if __name__ == '__main__':
    nums = [-937]
    res = Solution().maximumTotalCost(nums)
    print(res)
