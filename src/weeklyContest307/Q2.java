package weeklyContest307;

public class Q2 {
    public String largestPalindromic(String num) {
        int[] map = new int[10];
        int n = num.length();
        for (int i = 0; i < n; i++) {
            map[num.charAt(i) - '0']++;
        }

        int maxSingle = -1;
        for (int i = 0; i < 10; i++) {
            if (map[i] % 2 == 1) {
                maxSingle = i;
                map[i]--;
            }
            map[i] /= 2;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 9; i > 0; i--) {
            while (map[i] > 0) {
                sb.append(i);
                map[i]--;
            }
        }
        if (map[0] > 0 && maxSingle == -1) {
            maxSingle = 0;
        }
        if (sb.length() > 0) {
            while (map[0] > 0) {
                sb.append(0);
                map[0]--;
            }
        }
        StringBuilder rsb = new StringBuilder(sb).reverse();
        if (maxSingle != -1) {
            sb.append(maxSingle);
        }
        sb.append(rsb);
        return sb.toString();
    }

    public static void main(String[] args) {
        String num = "0000";
        System.out.println(new Q2().largestPalindromic(num));
    }
}
