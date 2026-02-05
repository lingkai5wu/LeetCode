def ans1(n: int) -> int:
    res = 0
    for i in range(n + 1):
        if i.bit_length() == i.bit_count():
            res += 1
    return res


def ans2(n: int) -> int:
    return (n + 1).bit_length()


class Solution:
    def countMonobit(self, n: int) -> int:
        return ans1(n)
