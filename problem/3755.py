from typing import List


class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        s = xor = res = 0
        pos = {(0, 0): -1}
        for i, x in enumerate(nums):
            xor ^= x
            s += 1 if x % 2 == 1 else -1
            t = (xor, s)
            if t in pos:
                res = max(res, i - pos[t])
            else:
                pos[t] = i
        return res
