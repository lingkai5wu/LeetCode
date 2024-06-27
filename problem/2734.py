class Solution:
    def smallestString(self, s: str) -> str:
        arr = list(s)
        found = False
        for i, c in enumerate(arr):
            if c == 'a':
                if not found:
                    found = True
                    continue
                else:
                    break
            arr[i] = chr(ord(c) - 1)
        if not found:
            arr[-1] = 'z'
        return ''.join(arr)
