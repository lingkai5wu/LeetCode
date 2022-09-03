package weeklyContest308;

import java.util.Arrays;

public class Q1 {
    public int[] answerQueries(int[] nums, int[] queries) {
        Arrays.sort(nums);
        int n = nums.length, m = queries.length;
        int[] res = new int[m];
        out:
        for (int i = 0; i < m; i++) {
            int sum = 0;
            for (int j = 0; j < n; j++) {
                sum += nums[j];
                if (sum > queries[i]) {
                    res[i] = j;
                    continue out;
                }
            }
            res[i] = n;
        }
        return res;
    }
}
