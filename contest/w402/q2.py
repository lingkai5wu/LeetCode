from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = [0] * 24
        res = 0
        for h in hours:
            res += cnt[(24 - h % 24) % 24]
            cnt[h % 24] += 1
        return res


if __name__ == '__main__':
    hours = [12, 12, 30, 24, 24]
    res = Solution().countCompleteDayPairs(hours)
    print(res)
