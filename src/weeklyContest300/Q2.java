package weeklyContest300;

import util.ListNode;

import java.util.Arrays;

public class Q2 {
    int[][] dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    public int[][] spiralMatrix(int m, int n, ListNode head) {
        int[][] res = new int[m][n];
        for (int i = 0; i < m; i++) {
            Arrays.fill(res[i], -1);
        }
        int i = 0, j = 0, d = 0;
        while (true) {
            res[i][j] = head.val;
            head = head.next;
            if (head == null) {
                break;
            }
            while (true) {
                int ni = i + dir[d][0], nj = j + dir[d][1];
                if (ni < 0 || nj < 0 || ni >= m || nj >= n || res[ni][nj] != -1) {
                    d = (d + 1) % 4;
                } else {
                    // 走到下一个格子
                    i = ni;
                    j = nj;
                    break;
                }
            }
        }
        return res;
    }
}
