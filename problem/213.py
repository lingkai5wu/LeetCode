from functools import cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        @cache
        def dfs(n: int, start=0) -> int:
            if n < start:
                return 0

            return max(dfs(n - 1, start), dfs(n - 2, start) + nums[n])

        return max(dfs(len(nums) - 2), dfs(len(nums) - 1, 1))


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(Solution().rob(nums))
