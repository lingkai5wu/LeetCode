from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != 'X':
                    continue
                if i > 0 and board[i - 1][j] == 'X':
                    continue
                if j > 0 and board[i][j - 1] == 'X':
                    continue
                count += 1
        return count


if __name__ == '__main__':
    board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
    result = Solution().countBattleships(board)
    print(result)
