class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        n = len(s)
        for i in range(n - 1, -1, -1):
            if s[i] not in 'aeiou':
                return s[:i + 1]
        return ''
