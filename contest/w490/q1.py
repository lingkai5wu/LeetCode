from typing import List


def ans1(nums: list[int]) -> int:
    is_a = True
    res = 0
    for i, x in enumerate(nums):
        if x % 2 == 1:
            is_a = not is_a
        if (i + 1) % 6 == 0:
            is_a = not is_a
        res += x if is_a else -x
    return res


def ans2(nums: list[int]) -> int:
    res = cur = 0
    for i, x in enumerate(nums):
        cur ^= x & 1
        if i % 6 == 5:
            cur ^= 1
        res -= x if cur else -x
    return res


class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        return ans2(nums)
