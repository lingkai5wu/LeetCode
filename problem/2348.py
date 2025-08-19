from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        l = -1
        for r, x, in enumerate(nums):
            if x:
                l = r
            else:
                res += r - l
        return res


if __name__ == '__main__':
    nums = [1, 3, 0, 0, 2, 0, 0, 4]
    print(Solution().zeroFilledSubarray(nums))
