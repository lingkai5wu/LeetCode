package daily;

public class No871 {
    public long minRefuelStops(int target, int startFuel, int[][] stations) {
        int n = stations.length;
        long[] dp = new long[n + 1];
        dp[0] = startFuel;
        for (int i = 0; i < n; i++) {
            long max = 0;
            for (int j = i; j < n; j++) {
                if (dp[i] < stations[j][0]) {
                    break;
                }
                max = Math.max(stations[j][1], max);
            }
            long res = dp[i] + max;
            if (res >= target) {
                return res;
            }
            dp[i + 1] = res;
        }
        return -1;
    }
}
