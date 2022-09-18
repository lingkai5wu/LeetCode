package weeklyContest.weeklyContest311;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Q4 {
    public int[] sumPrefixScores(String[] words) {
        Map<String, Integer> map = new HashMap<>();
        for (String word : words) {
            int len = word.length();
            for (int i = 0; i < len; i++) {
                String s = word.substring(0, i + 1);
                map.put(s, map.getOrDefault(s, 0) + 1);
            }
        }

        String[] key = map.keySet().toArray(new String[0]);
        Arrays.sort(key, (a, b) -> {
            if (a.length() != b.length()) {
                return a.length() - b.length();
            }
            return a.compareTo(b);
        });
        int keyCnt = key.length;
        Map<String, Integer> preSum = new HashMap<>();
        for (int i = 0; i < keyCnt; i++) {
            if (key[i].length() < 2) {
                preSum.put(key[i], map.get(key[i]));
            } else {
                String s = key[i].substring(0, key[i].length() - 1);
                preSum.put(key[i], preSum.get(s) + map.get(key[i]));
            }
        }

        int n = words.length;
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            res[i] = preSum.get(words[i]);
        }
        return res;
    }

    public static void main(String[] args) {
        String[] strings = new String[]{"abc", "ab", "bc", "b"};
        System.out.println(new Q4().sumPrefixScores(strings));
    }
}
