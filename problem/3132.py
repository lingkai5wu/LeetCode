from typing import List


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        n = len(nums2)
        for i in range(2, 0, -1):
            x = nums2[0] - nums1[i]
            j = 0
            for v in nums1:
                if v + x == nums2[j]:
                    j += 1
                    if j == n:
                        return x
        return nums2[0] - nums1[0]


if __name__ == '__main__':
    nums1 = [4, 20, 16, 12, 8]
    nums2 = [14, 18, 10]
    res = Solution().minimumAddedInteger(nums1, nums2)
    print(res)
