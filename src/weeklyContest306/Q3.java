package weeklyContest306;

public class Q3 {
    public String smallestNumber(String pattern) {
        int n = pattern.length();
        char[] cs = pattern.toCharArray();
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < n + 2; i++) {
            sb.append(i);
        }

        for (int i = 0; i < n; i++) {
            char pre = cs[i];
            boolean flag = pre == 'D';
            int j = i;
            while (j < n && pre == cs[j]) {
                j++;
            }
            if (flag) {
                StringBuilder sub = new StringBuilder(sb.substring(i, j + 1));
                sub.reverse();
                sb.replace(i, j + 1, sub.toString());
            }
            i = j - 1;
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        String pattern = "IIIDIDDD";
        System.out.println(new Q3().smallestNumber(pattern));
    }
}
