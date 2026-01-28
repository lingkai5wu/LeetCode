import math
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
        dis = [math.inf] * n
        dis[0] = 0
        h = [(0, 0)]
        while h:
            u_dis, u = heappop(h)
            if u_dis > dis[u]:
                continue
            for v, w in g[u]:
                v_dis = u_dis + w
                if v_dis < dis[v] and v_dis < disappear[v]:
                    dis[v] = v_dis
                    heappush(h, (v_dis, v))
        return [x if x < math.inf else -1 for x in dis]
