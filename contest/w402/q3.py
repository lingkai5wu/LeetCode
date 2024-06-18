import bisect
from collections import Counter
from functools import cache
from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power_cnt_map = Counter(power)
        m = len(power_cnt_map)
        power = sorted(power_cnt_map.keys())

        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            x = power[i]
            j = bisect.bisect_left(power, x - 2)
            return max(dfs(i - 1), dfs(j - 1) + x * power_cnt_map[x])

        return dfs(m - 1)


if __name__ == '__main__':
    power = [7, 1, 6, 3]
    res = Solution().maximumTotalDamage(power)
    print(res)
