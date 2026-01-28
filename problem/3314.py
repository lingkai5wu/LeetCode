from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            if n & 1 == 0:
                res.append(-1)
                continue
            for i in range(n.bit_length()):
                if n & (1 << i) and not n & (1 << (i + 1)):
                    res.append(n - (n & (1 << i)))
                    break
        return res
