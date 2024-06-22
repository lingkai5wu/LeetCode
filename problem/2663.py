class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        a = ord('a')
        k += a
        s = list(map(ord, s))
        n = len(s)
        i = n - 1
        s[i] += 1
        while i < n:
            if s[i] == k:
                if i == 0:
                    return ''
                s[i] = a
                i -= 1
                s[i] += 1
            elif i > 0 and s[i] == s[i - 1] or i > 1 and s[i] == s[i - 2]:
                s[i] += 1
            else:
                i += 1
        return ''.join(map(chr, s))


if __name__ == '__main__':
    s = "abcz"
    k = 26
    res = Solution().smallestBeautifulString(s, k)
    print(res)
