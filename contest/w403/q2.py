from math import inf
from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        left = top = inf
        right = button = -inf
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    left = min(left, j)
                    right = max(right, j)
                    top = min(top, i)
                    button = i
        return (button - top + 1) * (right - left + 1)


if __name__ == '__main__':
    grid = [[0, 1, 0], [1, 0, 1]]
    res = Solution().minimumArea(grid)
    print(res)
