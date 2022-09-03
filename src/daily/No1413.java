package daily;

public class No1413 {
    public int minStartValue(int[] nums) {
        int sum = 0, min = 0;
        for (int num : nums) {
            sum += num;
            min = Math.min(sum, min);
        }
        return 1 - min;
    }
}
