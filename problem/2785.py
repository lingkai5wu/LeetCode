from collections import Counter

VOWELS = 'AEIOUaeiou'


def ans1(s):
    index_list = []
    vowels_list = []
    for i, c in enumerate(s):
        if c in VOWELS:
            index_list.append(i)
            vowels_list.append(c)
    vowels_list.sort()
    s_list = list(s)
    for i, c in enumerate(vowels_list):
        s_list[index_list[i]] = c
    return ''.join(s_list)


def ans2(s):
    cnt = Counter(c for c in s if c in VOWELS)
    cur = VOWELS[0]
    s_list = list(s)
    for i, c in enumerate(s):
        if c in VOWELS:
            if cnt[cur] == 0:
                cur = [c for c in VOWELS if cnt[c]][0]
            s_list[i] = cur
            cnt[cur] -= 1
    return ''.join(s_list)


class Solution:
    def sortVowels(self, s: str) -> str:
        return ans2(s)


if __name__ == '__main__':
    s = "lEetcOde"
    print(ans2(s))
