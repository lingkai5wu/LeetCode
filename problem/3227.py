import random
import string

from util.timer import timer


@timer
def ans1(s):
    return sum(s.count(c) for c in 'aeiou') != 0


@timer
def ans2(s):
    return any(c in 'aeiou' for c in s)


@timer
def ans3(s):
    return any(c in s for c in 'aeiou')


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return ans1(s)


if __name__ == '__main__':
    random_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(100000000))
    for _ in range(10):
        ans1(random_str)
        ans2(random_str)
        ans3(random_str)
