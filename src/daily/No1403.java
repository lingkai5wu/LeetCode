package daily;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class No1403 {
    public List<Integer> minSubsequence(int[] nums) {
        Arrays.sort(nums);
        int sum = Arrays.stream(nums).sum();
        int cur = 0, index = nums.length - 1;
        List<Integer> list = new ArrayList<>();
        while (cur <= sum) {
            cur += nums[index];
            sum -= nums[index];
            list.add(nums[index--]);
        }
        return list;
    }
}
