import math
from collections import defaultdict
from fractions import Fraction
from functools import cache
from typing import List


def ans1(k: int, nums: list[int]) -> int:
    n = len(nums)
    f = [defaultdict(int) for _ in range(n + 1)]
    f[0][Fraction(1)] = 1
    for i, x in enumerate(nums):
        for val, cnt in f[i].items():
            f[i + 1][val] += cnt
            f[i + 1][val * x] += cnt
            f[i + 1][val / x] += cnt
    return f[-1][k]


def ans2(k: int, nums: list[int]) -> int:
    @cache
    def dfs(i, p, q) -> int:
        if i < 0:
            return 1 if p == k and q == 1 else 0
        x = nums[i]
        res1 = dfs(i - 1, p, q)
        g = math.gcd(p * x, q)
        res2 = dfs(i - 1, p * x // g, q // g)
        g = math.gcd(p, q * x)
        res3 = dfs(i - 1, p // g, q * x // g)
        return res1 + res2 + res3

    return dfs(len(nums) - 1, 1, 1)


class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        return ans2(k, nums)


if __name__ == '__main__':
    nums = [5, 3, 5]
    k = 3
    print(ans1(k, nums))
    print(ans2(k, nums))
