from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n & 1 == 0:
                ans.append(-1)
                continue
            for i in range(n.bit_length()):
                if n & (1 << i) and not n & (1 << (i + 1)):
                    ans.append(n - (n & (1 << i)))
                    break
        return ans