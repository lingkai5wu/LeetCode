class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10 ** 9 + 7
        f = [1] + [0] * high
        for i in range(1, high + 1):
            f[i] = sum(f[i - x] for x in (zero, one) if i - x >= 0) % mod
        return sum(f[low:]) % mod
