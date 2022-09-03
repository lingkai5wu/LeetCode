package weeklyContest302;

import java.util.Arrays;
import java.util.Comparator;

public class Q3 {
    public static void main(String[] args) {
        String[] nums = {"102", "473", "251", "814"};
        int[][] queries = {{1, 1}, {2, 3}, {4, 2}, {1, 2}};
        System.out.println(new Q3().smallestTrimmedNumbers(nums, queries));
    }

    public int[] smallestTrimmedNumbers(String[] nums, int[][] queries) {
        int qn = queries.length;
        int n = nums.length;
        int sn = nums[0].length();
        int[] res = new int[qn];
        int[][] resi = new int[sn + 1][];
        for (int i = 0; i < qn; i++) {
            int k = queries[i][0];
            int trim = queries[i][1];
            if (resi[trim] == null) {
                class Str {
                    int i;
                    String s;

                    public Str(int i, String s) {
                        this.i = i;
                        this.s = s;
                    }
                }
                Str[] ss = new Str[n];
                for (int j = 0; j < n; j++) {
                    ss[j] = new Str(j, nums[j].substring(sn - trim));
                }
                Arrays.sort(ss, Comparator.comparing(a -> a.s));
                int[] indexs = new int[n];
                for (int j = 0; j < n; j++) {
                    indexs[j] = ss[j].i;
                }
                resi[trim] = indexs;
            }
            res[i] = resi[trim][k - 1];
        }
        return res;
    }
}
