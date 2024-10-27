import collections
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        for i in range(len(nums) - k + 1):
            counter = collections.Counter(nums[i:i + k])
            count_list = list(counter.items())
            count_list.sort(key=lambda x: (x[1], x[0]), reverse=True)
            total = 0
            for j in range(min(x, len(count_list))):
                total += count_list[j][0] * count_list[j][1]
            ans.append(total)
        return ans


if __name__ == '__main__':
    nums = [9, 2, 2]
    k = 3
    x = 3
    print(Solution().findXSum(nums, k, x))
