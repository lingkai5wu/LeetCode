from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        res = []
        count = 0
        while n > 0:
            mod = n % 10
            if mod != 0:
                res.append(mod * 10 ** count)
            n = n // 10
            count += 1
        res.reverse()
        return res
