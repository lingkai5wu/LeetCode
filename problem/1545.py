class Solution:
    # TODO 非模拟写法
    def findKthBit(self, n: int, k: int) -> str:
        arr = [False]
        for i in range(n - 1):
            invert_arr = [not x for x in arr]
            invert_arr.reverse()
            arr += [1] + invert_arr
        return '1' if arr[k - 1] else '0'


if __name__ == '__main__':
    n = 4
    k = 11
    print(Solution().findKthBit(n, k))
