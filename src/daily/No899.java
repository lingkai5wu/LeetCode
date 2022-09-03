package daily;

import java.util.Arrays;

public class No899 {
    public String orderlyQueue(String s, int k) {
        char[] cs = s.toCharArray();
        if (k > 1) {
            Arrays.sort(cs);
            return new String(cs);
        }
        StringBuilder sb = new StringBuilder(s);
        int n = s.length();
        String res = s;
        for (int i = 0; i < n; i++) {
            sb.deleteCharAt(0);
            sb.append(cs[i]);
            if (res.compareTo(sb.toString()) > 0) {
                res = sb.toString();
            }
        }
        return res;
    }

    public static void main(String[] args) {
        String s = "nhtq";
        int k = 1;
        System.out.println(new No899().orderlyQueue(s, k));
    }
}
