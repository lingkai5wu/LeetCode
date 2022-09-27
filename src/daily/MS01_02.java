package daily;

public class MS01_02 {
    public boolean CheckPermutation(String s1, String s2) {
        int n = s1.length();
        if (n != s2.length()) {
            return false;
        }
        int[] map = new int[26];
        for (int i = 0; i < n; i++) {
            map[s1.charAt(i) - 'a']++;
            map[s2.charAt(i) - 'a']--;
        }
        for (int i = 0; i < 26; i++) {
            if (map[i] != 0) {
                return false;
            }
        }
        return true;
    }
}
