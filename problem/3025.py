from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        res = 0
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                if x1 > x2 or y2 > y1:
                    continue
                for x3, y3 in points:
                    if x1 == x3 and y1 == y3:
                        continue
                    if x2 == x3 and y2 == y3:
                        continue
                    if x1 <= x3 <= x2 and y1 >= y3 >= y2:
                        break
                else:
                    res += 1
        return res


if __name__ == '__main__':
    points = [[0, 0], [0, 3]]
    print(Solution().numberOfPairs(points))
