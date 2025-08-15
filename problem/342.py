import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and math.log(n, 4).is_integer()

    def isPowerOfFour2(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n & 0x55555555 > 0


if __name__ == '__main__':
    n = 1
    print(Solution().isPowerOfFour2(n))
