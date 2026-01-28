import math
from itertools import pairwise
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        min_diff = math.inf
        for x, y in pairwise(arr):
            diff = y - x
            if diff < min_diff:
                min_diff = diff
                res = [[x, y]]
            elif diff == min_diff:
                res.append([x, y])
        return res
