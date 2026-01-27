import math
from heapq import heappop, heappush
from typing import List


def ans1(k, n, times):
    g = [[] for _ in range(n)]
    for u, v, w in times:
        g[u - 1].append((v - 1, w))
    dis = [math.inf] * n
    res = dis[k - 1] = 0
    flag = [False] * n
    while True:
        u = -1
        for i, is_done in enumerate(flag):
            if not is_done and (u < 0 or dis[i] < dis[u]):
                u = i
        if u < 0:
            return res
        if dis[u] == math.inf:
            return -1
        res = dis[u]
        flag[u] = True
        for v, w in g[u]:
            dis[v] = min(dis[v], dis[u] + w)


def ans2(k, n, times):
    g = [[] for _ in range(n)]
    for u, v, w in times:
        g[u - 1].append((v - 1, w))
    dis = [math.inf] * n
    dis[k - 1] = 0
    h = [(0, k - 1)]
    while h:
        u_dis, u = heappop(h)
        if u_dis > dis[u]:
            continue
        for v, w in g[u]:
            v_dis = u_dis + w
            if v_dis < dis[v]:
                dis[v] = v_dis
                heappush(h, (v_dis, v))
    res = max(dis)
    return res if res < math.inf else -1


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        return ans1(k, n, times)


if __name__ == '__main__':
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    print(Solution().networkDelayTime(times, n, k))
