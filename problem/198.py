from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        f0, f1 = 0, 0
        for num in nums:
            f0, f1 = f1, max(f0 + num, f1)
        return f1


if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]
    print(Solution().rob(nums))
