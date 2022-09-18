package weeklyContest.weeklyContest309;

public class Q1 {
    public boolean checkDistances(String s, int[] distance) {
        int n = s.length();
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (distance[c - 'a'] != -1) {
                if (i + distance[c - 'a'] + 1 >= n || s.charAt(i + distance[c - 'a'] + 1) != c) {
                    return false;
                }
                distance[c - 'a'] = -1;
            }
        }
        return true;
    }
}
