package weeklyContest302;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Q2 {
    public int maximumSum(int[] nums) {
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int num : nums) {
            int sum = 0;
            int cur = num;
            while (cur > 0) {
                sum += cur % 10;
                cur /= 10;
            }
            if (!map.containsKey(sum)) {
                map.put(sum, new ArrayList<>());
            }
            map.get(sum).add(num);
        }
        int res = -1;
        for (Map.Entry<Integer, List<Integer>> entry : map.entrySet()) {
            Integer num = entry.getKey();
            List<Integer> list = entry.getValue();
            if (list.size() < 2) {
                continue;
            }
            list.sort((a, b) -> b - a);
            res = Math.max(list.get(0) + list.get(1), res);
        }
        return res;
    }
}
