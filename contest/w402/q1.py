from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        res = 0
        for i in range(len(hours)):
            for j in range(i + 1, len(hours)):
                m, n = divmod(hours[i] + hours[j], 24)
                if m > 0 and n == 0:
                    res += 1
        return res


if __name__ == '__main__':
    hours = [12, 12, 30, 24, 24]
    res = Solution().countCompleteDayPairs(hours)
    print(res)
