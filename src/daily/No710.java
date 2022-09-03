package daily;

import java.util.HashSet;
import java.util.Random;
import java.util.Set;

public class No710 {
    class Solution {
        Set<Integer> set = new HashSet<>();
        int n;
        Random random;

        public Solution(int n, int[] blacklist) {
            this.n = n;
            random = new Random();
            for (int i : blacklist) {
                set.add(i);
            }
        }

        public int pick() {
            int res = random.nextInt(n);
            while (set.contains(res)) {
                res = random.nextInt(n);
            }
            return res;
        }
    }
}
