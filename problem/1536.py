from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        tail_1_pos = [-1] * n
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    tail_1_pos[i] = j
                    break
        res = 0
        for i in range(n - 1):
            for j in range(i, n):
                if tail_1_pos[j] <= i:
                    res += j - i
                    tail_1_pos[i + 1:j + 1] = tail_1_pos[i:j]
                    break
            else:
                return -1
        return res


if __name__ == '__main__':
    grid = [[0, 0], [0, 1]]
    print(Solution().minSwaps(grid))
