package weeklyContest308;

public class Q2 {
    public String removeStars(String s) {
        int n = s.length(), i = n, cnt = 0;
        StringBuilder sb = new StringBuilder();
        while (--i >= 0) {
            if (s.charAt(i) != '*') {
                if (cnt > 0) {
                    cnt--;
                    continue;
                }
                sb.append(s.charAt(i));
                continue;
            }
            while (s.charAt(--i) == '*') {
                cnt++;
            }
        }
        return sb.reverse().toString();
    }
}
