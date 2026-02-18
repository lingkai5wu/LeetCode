from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        s = res = 0
        pos = {0: -1}
        for i, x in enumerate(nums):
            s += 1 if x == 1 else -1
            if s in pos:
                res = max(res, i - pos[s])
            else:
                pos[s] = i
        return res
