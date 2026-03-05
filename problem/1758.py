def ans1(s: str) -> int:
    arr = [[0, 0], [0, 0]]
    for i, c in enumerate(s):
        arr[i & 1][int(c)] += 1
    return min(arr[0][1] + arr[1][0], arr[0][0] + arr[1][1])


def ans2(s: str) -> int:
    diff = 0
    for i, c in enumerate(s):
        if int(c) == i & 1:
            diff += 1
    return min(diff, len(s) - diff)


class Solution:
    def minOperations(self, s: str) -> int:
        return ans2(s)
