def ans1(s: str, t: str) -> str:
    t_cnt_1 = sum(c == '1' for c in t)
    t_cnt_0 = sum(c == '0' for c in t)
    res = ''
    for i, c in enumerate(s):
        if c == '0' and t_cnt_1 > 0:
            res += '1'
            t_cnt_1 -= 1
            continue
        if c == '1' and t_cnt_0 > 0:
            res += '1'
            t_cnt_0 -= 1
            continue
        res += '0'
    return res


def ans2(s: str, t: str) -> str:
    cnt_0 = t.count('0')
    cnt = [cnt_0, len(t) - cnt_0]
    res = list(s)
    for i, c in enumerate(s):
        x = int(c)
        if cnt[x ^ 1] > 0:
            res[i] = '1'
            cnt[x ^ 1] -= 1
        else:
            res[i] = '0'
            cnt[x] -= 1
    return ''.join(res)


class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        return ans2(s, t)


if __name__ == '__main__':
    s = "101"
    t = "011"
    print(Solution().maximumXor(s, t))
