from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        return ans1(height)


def ans1(height: List[int]) -> int:
    n = len(height)
    pre_max = [0] * n
    suf_max = [0] * n
    res = 0
    for i in range(1, n):
        pre_max[i] = max(pre_max[i - 1], height[i - 1])
        suf_max[n - 1 - i] = max(suf_max[n - i], height[n - i])
    for i in range(n):
        current = min(pre_max[i], suf_max[i]) - height[i]
        if current > 0:
            res += current
    return res
