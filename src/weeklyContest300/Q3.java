package weeklyContest300;

import java.util.ArrayDeque;
import java.util.Queue;

public class Q3 {
    public static void main(String[] args) {
        int n = 684, delay = 18, forget = 496;
        System.out.println(new Q3().peopleAwareOfSecret(n, delay, forget));
    }

    public int peopleAwareOfSecret(int n, int delay, int forget) {
        Queue<long[]> shareQueue = new ArrayDeque<>();
        Queue<long[]> forgetQueue = new ArrayDeque<>();
        int day = 1, share = 0, num = 1;
        shareQueue.add(new long[]{day + delay, 1});
        forgetQueue.add(new long[]{day + forget, 1});
        while (day++ < n) {
            if (!forgetQueue.isEmpty() && forgetQueue.peek()[0] <= day) {
                long curNum = forgetQueue.poll()[1];
                num -= curNum;
                share -= curNum;
            }
            if (!shareQueue.isEmpty() && shareQueue.peek()[0] <= day) {
                share += shareQueue.poll()[1];
            }
            if (share > 0) {
                num += share;
                num %= 1000000007;
                shareQueue.add(new long[]{day + delay, share});
                forgetQueue.add(new long[]{day + forget, share});
            }
        }
        return Math.toIntExact(num);
    }
}
