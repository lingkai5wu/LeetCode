from itertools import pairwise


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        for p, q in pairwise(s):
            if int(p) < int(q):
                return False
        return True
