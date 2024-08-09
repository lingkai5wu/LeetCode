class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i = 0
        n = len(s)
        for c in t:
            if s[i] == c:
                i += 1
                if i == n:
                    return True
        return False
