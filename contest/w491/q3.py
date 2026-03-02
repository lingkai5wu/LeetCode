from typing import List


class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        max_len = max(map(max, grid)).bit_length()
        res = 0
        for i in range(max_len - 1, -1, -1):
            mask = res | ((1 << i) - 1)
            for row in grid:
                for x in row:
                    if (x | mask) == mask:
                        break
                else:
                    res |= 1 << i
                    break
        return res
