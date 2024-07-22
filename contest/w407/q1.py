class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if (n & k) != k:
            return -1
        return (n - k).bit_count()


if __name__ == '__main__':
    print(Solution().minChanges(n=13, k=4))
