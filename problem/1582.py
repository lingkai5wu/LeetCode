from typing import List


def ans1(mat: list[list[int]]) -> int:
    row_1 = [sum(row) == 1 for row in mat]
    col_1 = [sum(col) == 1 for col in zip(*mat)]
    res = 0
    for i, row in enumerate(mat):
        for j, x in enumerate(row):
            if x == 1 and row_1[i] and col_1[j]:
                res += 1
    return res


def ans2(mat: list[list[int]]) -> int:
    res = 0
    for i, row in enumerate(mat):
        if sum(row) != 1:
            continue
        j = row.index(1)
        if sum(row[j] for row in mat) == 1:
            res += 1
    return res


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        return ans1(mat)
