package weeklyContest301;

import java.util.HashSet;
import java.util.Set;

public class Q2 {
    class SmallestInfiniteSet {
        Set<Integer> set;

        public SmallestInfiniteSet() {
            set = new HashSet<>();
        }

        public int popSmallest() {
            for (int i = 1; i < Integer.MAX_VALUE; i++) {
                if (!set.contains(i)) {
                    set.add(i);
                    return i;
                }
            }
            return -1;
        }

        public void addBack(int num) {
            if (set.contains(num)) {
                set.remove(num);
            }
        }
    }
}
