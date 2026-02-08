class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = cnt = s.count('a')
        for c in s:
            cnt += 1 if c == 'b' else -1
            if res > cnt:
                res = cnt
        return res


if __name__ == '__main__':
    s = "aababbab"
    print(Solution().minimumDeletions(s))
