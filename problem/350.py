from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return ans2(nums1, nums2)


def ans1(nums1, nums2):
    res = []
    nums1.sort()
    nums2.sort()
    m, n = len(nums1), len(nums2)
    i = j = 0
    while True:
        if i >= m or j >= n:
            break
        if nums1[i] == nums2[j]:
            res.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return res


def ans2(nums1, nums2):
    count = Counter(nums1)
    res = []
    for x in nums2:
        if count[x] > 0:
            res.append(x)
            count[x] -= 1
    return res


if __name__ == '__main__':
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(Solution().intersect(nums1, nums2))
