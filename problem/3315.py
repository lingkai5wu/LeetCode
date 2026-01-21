from typing import List


def ans1(nums: list[int]) -> list[int]:
    for i, n in enumerate(nums):
        if n == 2:
            nums[i] = -1
        else:
            t = ~n
            lowbit = t & -t
            nums[i] ^= lowbit >> 1
    return nums


def ans2(nums: list[int]) -> list[int]:
    for i, n in enumerate(nums):
        if n == 2:
            nums[i] = -1
        else:
            t = n + 1
            nums[i] -= (t & -n) >> 1
    return nums


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        return ans2(nums)


if __name__ == '__main__':
    nums = [2, 3, 5, 7]
    print(Solution().minBitwiseArray(nums))
