class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        res = 0
        sign = 1
        i = 0

        while i < n:
            if s[i] == ' ':
                i += 1
            else:
                break

        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        int_max = (1 << 31) - 1
        int_min = -(1 << 31)

        while i < n:
            digit = ord(s[i]) - ord('0')
            if not 0 <= digit <= 9:
                break
            if res > (int_max - digit) / 10:
                return int_max if sign == 1 else int_min
            res = res * 10 + digit
            i += 1
        return res * sign


if __name__ == '__main__':
    s = "42"
    print(Solution().myAtoi(s))
