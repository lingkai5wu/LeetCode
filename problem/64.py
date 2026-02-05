import math
from heapq import heappop, heappush
from typing import List


def ans1(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    g = [[] for _ in range(m * n)]
    for i in range(m):
        for j in range(n):
            u = i * n + j
            if i + 1 < m:
                g[u].append(((i + 1) * n + j, grid[i + 1][j]))
            if j + 1 < n:
                g[u].append((u + 1, grid[i][j + 1]))

    dis = [math.inf] * m * n
    dis[0] = grid[0][0]
    h = [(grid[0][0], 0)]
    while h:
        u_dis, u = heappop(h)
        if u_dis > dis[u]:
            continue
        for v, w in g[u]:
            v_dis = u_dis + w
            if v_dis < dis[v]:
                dis[v] = v_dis
                heappush(h, (v_dis, v))
    return dis[m * n - 1]


def ans2(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    f = [[math.inf] * (n + 1) for _ in range(m + 1)]
    f[0][1] = f[1][0] = 0
    for i in range(m):
        for j in range(n):
            f[i + 1][j + 1] = min(f[i + 1][j], f[i][j + 1]) + grid[i][j]
    return f[m][n]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return ans2(grid)
