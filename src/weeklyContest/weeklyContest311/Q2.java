package weeklyContest.weeklyContest311;

public class Q2 {
    public int longestContinuousSubstring(String s) {
        int max = 1, i = 0;
        int n = s.length();
        char[] cs = s.toCharArray();
        char pre = cs[0];
        for (int j = 1; j < n; j++) {
            if (cs[j] - pre != 1) {
                i = j;
            }
            pre = cs[j];
            max = Math.max(j - i + 1, max);
        }
        return max;
    }

    public static void main(String[] args) {
        System.out.println(new Q2().longestContinuousSubstring("abacaba"));
    }
}
