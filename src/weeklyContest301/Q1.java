package weeklyContest301;

import java.util.Arrays;

public class Q1 {
    public static void main(String[] args) {
        int[] arr = new int[]{5, 4, 4};
        System.out.println(new Q1().fillCups(arr));
    }

    public int fillCups(int[] amount) {
        int res = 0;
        Arrays.sort(amount);
        while (amount[2] > 0) {
            if (amount[1] > 0) {
                amount[1]--;
            }
            amount[2]--;
            res++;
            Arrays.sort(amount);
        }
        return res;
    }
}
