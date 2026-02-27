import math


def ans1(n: int) -> bool:
    s = 0
    for c in str(n):
        s += math.factorial(int(c))
    return ''.join(sorted(str(s))) == ''.join(sorted(str(n)))


def ans2(n: int) -> bool:
    s = 0
    cnt = [0] * 10
    while n > 0:
        n, d = divmod(n, 10)
        s += math.factorial(d)
        cnt[d] += 1
    while s > 0:
        s, d = divmod(s, 10)
        cnt[d] -= 1
    return not any(cnt)


class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        return ans2(n)
