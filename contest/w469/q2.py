from math import inf
from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        res = inf
        f1 = [False] * (len(nums) - 1)
        f1[0] = True
        f2 = [False] * (len(nums) - 1)
        f2[len(nums) - 2] = True
        for i in range(1, len(nums) - 1):
            if f1[i - 1] and nums[i - 1] < nums[i]:
                f1[i] = True
        for i in range(len(nums) - 2, 0, -1):
            if f2[i] and nums[i] > nums[i + 1]:
                f2[i - 1] = True
        for i in range(0, len(nums) - 1):
            if f1[i] and f2[i]:
                res = min(res, abs(sum(nums[:i + 1]) - sum(nums[i + 1:])))
        return -1 if res == inf else res


if __name__ == '__main__':
    nums = [1, 2, 4, 3]
    print(Solution().splitArray(nums))
