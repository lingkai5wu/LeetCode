from math import gcd
from typing import List


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            while nums[i] >= 10:
                nums[i] //= 10
            for j in range(i + 1, n):
                if gcd(nums[i], nums[j] % 10) == 1:
                    res += 1
        return res

    def countBeautifulPairs2(self, nums: List[int]) -> int:
        count_arr = [0] * 9
        res = 0
        for x in nums:
            for j, count in enumerate(count_arr):
                if gcd(x % 10, j + 1) == 1:
                    res += count
            while x >= 10:
                x //= 10
            count_arr[x - 1] += 1
        return res


if __name__ == '__main__':
    nums = [11, 21, 12]
    res = Solution().countBeautifulPairs2(nums)
    print(res)
