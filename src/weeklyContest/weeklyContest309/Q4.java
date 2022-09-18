package weeklyContest.weeklyContest309;

import java.util.Arrays;
import java.util.Comparator;

public class Q4 {
    public int mostBooked(int n, int[][] meetings) {
        Arrays.sort(meetings, Comparator.comparingInt(a -> a[0]));
        int[] arr = new int[n], cnt = new int[n];
        int time = 0;
        for (int[] meeting : meetings) {
            if (meeting[0] > time) {
                time = meeting[0];
            }
            int need = meeting[1] - meeting[0];
            out:
            while (true) {
                int min = Integer.MAX_VALUE;
                for (int i = 0; i < n; i++) {
                    if (arr[i] <= time) {
                        arr[i] = time + need;
                        cnt[i]++;
                        break out;
                    }
                    min = Math.min(arr[i], min);
                }
                time = min;
            }
        }
        int max = cnt[0], maxi = 0;
        for (int i = 0; i < n; i++) {
            if (cnt[i] > max) {
                max = cnt[i];
                maxi = i;
            }
        }
        return maxi;
    }

    public static void main(String[] args) {
        int[][] arr = {{0, 10}, {1, 9}, {2, 8}, {3, 7}, {4, 6}};
        System.out.println(new Q4().mostBooked(3, arr));
    }
}
