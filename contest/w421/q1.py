from math import lcm, gcd
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        score = lcm(*nums) * gcd(*nums)
        for i in range(len(nums)):
            cur_nums = nums[:i] + nums[i + 1:]
            score = max(score, lcm(*cur_nums) * gcd(*cur_nums))
        return score


if __name__ == '__main__':
    nums = [2, 29]
    print(Solution().maxScore(nums))
