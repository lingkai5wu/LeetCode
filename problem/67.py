def ans1(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]


def ans2(a: str, b: str) -> str:
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    res = ''
    while i >= 0 or j >= 0 or carry:
        s = carry
        s += int(a[i]) if i >= 0 else 0
        s += int(b[j]) if j >= 0 else 0
        carry, s = divmod(s, 2)
        res += str(s)
        i -= 1
        j -= 1
    return res[::-1]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return ans2(a, b)
