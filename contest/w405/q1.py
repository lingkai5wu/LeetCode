class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        return ans2(s, k)


def ans1(s: str, k: int) -> str:
    res = ""
    for i in range(len(s)):
        res += s[(i + k) % len(s)]
    return res


def ans2(s: str, k: int) -> str:
    k %= len(s)
    return s[k:] + s[:k]
