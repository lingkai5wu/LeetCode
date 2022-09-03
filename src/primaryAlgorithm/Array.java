package primaryAlgorithm;

public class Array {
    public int removeDuplicates(int[] nums) {
        int i = 1, n = nums.length;
        for (int j = 1; j < n; j++) {
            if (nums[j] != nums[j - 1]) {
                nums[i++] = nums[j];
            }
        }
        return i;
    }

    public int removeDuplicates2(int[] nums) {
        int i = 0, n = nums.length;
        for (int j = 1; j < n; j++) {
            if (nums[i] != nums[j]) {
                nums[++i] = nums[j];
            }
        }
        return ++i;
    }

    public int maxProfit(int[] prices) {
        int res = 0, n = prices.length;
        for (int i = 1; i < n; i++) {
            if (prices[i] > prices[i - 1]) {
                res += prices[i] - prices[i - 1];
            }
        }
        return res;
    }
}
