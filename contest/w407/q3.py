class Solution:
    def maxOperations(self, s: str) -> int:
        return ans2(s)


def ans1(s: str) -> int:
    res = 0
    count = 0
    n = len(s)
    for i in range(n - 1, -1, -1):
        if (i + 1 >= n or s[i + 1] == '1') and s[i] == '0':
            count += 1
        if s[i] == '1':
            res += count
    return res


def ans2(s: str) -> int:
    res = cnt1 = 0
    for i, c in enumerate(s):
        if c == '1':
            cnt1 += 1
        elif i and s[i - 1] == '1':
            res += cnt1
    return res


if __name__ == '__main__':
    print(Solution().maxOperations('101'))
