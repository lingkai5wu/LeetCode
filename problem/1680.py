MOD = 10 ** 9 + 7


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = 0
        for i in range(1, n + 1):
            res <<= i.bit_length()
            res |= i
            res %= MOD
        return res


if __name__ == '__main__':
    n = 12
    print(Solution().concatenatedBinary(n))
