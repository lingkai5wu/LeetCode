from functools import cache
from typing import List


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        @cache
        def gcd(a: int, b: int) -> int:
            r = a % b
            if r == 0:
                return b
            return gcd(b, r)

        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if gcd(int(str(nums[i])[0]), int(str(nums[j])[-1])) == 1:
                    count += 1
        return count


if __name__ == '__main__':
    nums = [11, 21, 12]
    res = Solution().countBeautifulPairs(nums)
    print(res)
