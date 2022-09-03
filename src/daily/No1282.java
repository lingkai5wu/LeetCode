package daily;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class No1282 {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        Map<Integer, List<Integer>> map = new HashMap<>();
        List<List<Integer>> res = new ArrayList<>();
        int n = groupSizes.length;
        for (int i = 0; i < n; i++) {
            int curSize = groupSizes[i];
            map.putIfAbsent(curSize, new ArrayList<>());
            map.get(curSize).add(i);
            if (map.get(curSize).size() == curSize) {
                res.add(new ArrayList<>(map.get(curSize)));
                map.get(curSize).clear();
            }
        }
        return res;
    }
}
