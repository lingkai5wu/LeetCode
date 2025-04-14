from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        return ans2(arr, a, b, c)


def ans1(arr: List[int], a: int, b: int, c: int) -> int:
    res = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    res += 1
    return res


def ans2(arr: List[int], a: int, b: int, c: int) -> int:
    res = 0
    max_a = max(arr)
    s = [0] * (max_a + 2)
    for j, y in enumerate(arr):
        for z in arr[j + 1:]:
            if abs(y - z) > b:
                continue
            l = max(y - a, z - c, 0)
            r = min(y + a, z + c, max_a)
            res += max(s[r + 1] - s[l], 0)
        for i in range(y + 1, len(s)):
            s[i] += 1
    return res
