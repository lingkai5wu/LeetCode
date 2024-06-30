from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        prev = None
        res = []
        n = len(nums)
        for i in range(n - 2):
            if nums[i] == prev:
                continue
            prev = nums[i]
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    break
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return res
