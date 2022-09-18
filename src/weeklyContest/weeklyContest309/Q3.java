package weeklyContest.weeklyContest309;

public class Q3 {
    public int longestNiceSubarray(int[] nums) {
        int n = nums.length, i = 0, j = 1, max = 1;
        while (j < n) {
            boolean flag = true;
            for (int k = i; k < j; k++) {
                if ((nums[k] & nums[j]) != 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                max = Math.max(j - i + 1, max);
            } else {
                i++;
                j--;
            }
            j++;
        }
        return max;
    }
}
