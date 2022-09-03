package weeklyContest306;

public class Q1 {
    int[] d = {-1, 0, 1};

    public int[][] largestLocal(int[][] grid) {
        int n = grid.length;
        int[][] res = new int[n - 2][n - 2];
        for (int i = 1; i < n - 1; i++) {
            for (int j = 1; j < n - 1; j++) {
                int max = Integer.MIN_VALUE;
                for (int dx : d) {
                    for (int dy : d) {
                        max = Math.max(grid[i + dx][j + dy], max);
                    }
                }
                res[i-1][j-1] = max;
            }
        }
        return res;
    }
}
