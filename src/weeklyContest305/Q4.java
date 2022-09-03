package weeklyContest305;

import java.util.Arrays;

public class Q4 {
    public int longestIdealString(String s, int k) {
        int n = s.length();
        int[] dp = new int[n];
        char[] cs = s.toCharArray();
        int max = 0;
        Arrays.fill(dp, 1);
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (cs[i] == cs[j]) {
                    dp[i] = dp[j] + 1;
                } else if (Math.abs(cs[i] - cs[j]) <= k) {
                    dp[i] = Math.max(dp[j] + 1, dp[i]);
                }
            }
            max = Math.max(dp[i], max);
        }
        return max;
    }
}
