MOD = 10 ** 9 + 7


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        return ans1(delay, forget, n)


def ans1(delay, forget, n):
    res = 1
    delay_list = [0] * delay + [1]
    forget_list = [0] * forget + [1]
    for i in range(0, n):
        # 忘记秘密
        res -= forget_list[i % (forget + 1)]
        forget_list[i % (forget + 1)] = 0

        # 分享秘密
        delay_list[i % (delay + 1)] = 0
        can_share = res - sum(delay_list)
        delay_list[(i - 1) % (delay + 1)] += can_share
        forget_list[(i - 1) % (forget + 1)] += can_share
        res += can_share
        res %= MOD
    return res


def ans2(delay, forget, n):
    f = [0] * (n + 1)
    f[1] = 1
    for i in range(1, n + 1):
        f[i] %= MOD
        for j in range(i + delay, min(i + forget, n + 1)):
            f[j] += f[i]
    return sum(f[- forget:]) % MOD


if __name__ == '__main__':
    n = 4
    delay = 1
    forget = 4
    # n = 425
    # delay = 81
    # forget = 118
    print(Solution().peopleAwareOfSecret(n, delay, forget))
