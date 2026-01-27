import math
from heapq import heappop, heappush
from typing import List


def ans1(edges: list[list[int]], n: int) -> int:
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, w * 2))
    dis = [math.inf] * n
    dis[0] = 0
    h = [(0, 0)]
    while h:
        u_dis, u = heappop(h)
        if u_dis > dis[u]:
            continue
        for v, w in g[u]:
            v_dis = u_dis + w
            if v_dis < dis[v]:
                dis[v] = v_dis
                heappush(h, (v_dis, v))
    res = dis[n - 1]
    return res if res < math.inf else -1


# 朴素 Dijkstra（适用于稠密图），超时了
# 稠密图：边的数量级和 n^2 相当的图。
def ans2(edges: list[list[int]], n: int) -> int:
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, w * 2))
    dis = [math.inf] * n
    dis[0] = 0
    flag = [False] * n
    while True:
        # 找到当前最小 dis 节点
        u = -1
        for i, ok in enumerate(flag):
            if not ok and (u < 0 or dis[i] < dis[u]):
                u = i
        # 找不到
        if u < 0:
            return -1
        # 到最后一个节点
        if u == n - 1:
            return dis[u] if dis[u] < math.inf else -1
        # 维护状态
        flag[u] = True
        for v, w in g[u]:
            v_dis = dis[u] + w
            if v_dis < dis[v]:
                dis[v] = v_dis


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        return ans2(edges, n)


if __name__ == '__main__':
    n = 4
    edges = [[0, 1, 3], [3, 1, 1], [2, 3, 4], [0, 2, 2]]
    print(Solution().minCost(n, edges))
