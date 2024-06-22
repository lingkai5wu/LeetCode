from itertools import pairwise
from typing import List


class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        res = same = 0
        for (a1, b1), (a2, b2) in pairwise(zip(temperatureA, temperatureB)):
            if (a1 > a2) - (a1 < a2) == (b1 > b2) - (b1 < b2):
                same += 1
                res = max(res, same)
            else:
                same = 0
        return res


if __name__ == '__main__':
    temperatureA = [21, 18, 18, 18, 31]
    temperatureB = [34, 32, 16, 16, 17]
    res = Solution().temperatureTrend(temperatureA, temperatureB)
    print(res)
