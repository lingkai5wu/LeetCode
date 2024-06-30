from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = len(numbers)
        l, r = 0, m - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:
                return [l + 1, r + 1]
