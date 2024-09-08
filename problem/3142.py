from typing import List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if i and x != grid[i - 1][j]:
                    return False
                if j and x == row[j - 1]:
                    return False
        return True
