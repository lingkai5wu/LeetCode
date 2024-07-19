from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        return ans2(grid)


def ans1(grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    x_sum_arr = [[0] * (n + 1) for _ in range(m + 1)]
    y_sum_arr = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            x_sum_arr[i][j] = (x_sum_arr[i][j - 1] + x_sum_arr[i - 1][j] - x_sum_arr[i - 1][j - 1]
                               + (1 if grid[i - 1][j - 1] == 'X' else 0))
            y_sum_arr[i][j] = (y_sum_arr[i][j - 1] + y_sum_arr[i - 1][j] - y_sum_arr[i - 1][j - 1]
                               + (1 if grid[i - 1][j - 1] == 'Y' else 0))
    res = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x_sum_arr[i][j] == y_sum_arr[i][j] != 0:
                res += 1
    return res


def ans2(grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    res = 0
    col_sum_arr = [[0, 0] for _ in range(n)]
    for i in range(m):
        cur_x = cur_y = 0
        for j in range(n):
            if grid[i][j] == 'X':
                col_sum_arr[j][0] += 1
            elif grid[i][j] == 'Y':
                col_sum_arr[j][1] += 1
            cur_x += col_sum_arr[j][0]
            cur_y += col_sum_arr[j][1]
            if cur_x and cur_x == cur_y:
                res += 1
    return res


if __name__ == '__main__':
    grid = [["X", "Y", "."], ["Y", ".", "."]]
    print(Solution().numberOfSubmatrices(grid))
