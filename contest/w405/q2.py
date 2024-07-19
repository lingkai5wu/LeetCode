from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        return ans2(n)


def ans1(n: int) -> List[str]:
    if n == 1:
        return ['0', '1']
    last_s = ans1(n - 1)
    res = set()
    for i in range(len(last_s)):
        s = last_s[i]
        res.add('1' + s)
        if s[0] == '1':
            res.add('0' + s)
        res.add(s + '1')
        if s[-1] == '1':
            res.add(s + '0')
    return list(res)


def ans2(n: int) -> List[str]:
    res = []
    mask = (1 << n) - 1
    for i in range(1 << n):
        x = mask ^ i
        if x & (x >> 1) == 0:
            res.append(f'{i:0{n}b}')
    return res


if __name__ == '__main__':
    print(Solution().validStrings(3))
