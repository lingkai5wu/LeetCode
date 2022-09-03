package daily;

public class No1455 {
    public int isPrefixOfWord(String sentence, String searchWord) {
        String[] words = sentence.split(" ");
        int n = words.length, len = searchWord.length();
        out:
        for (int i = 0; i < n; i++) {
            String cur = words[i];
            if (cur.length() < len) {
                continue;
            }
            for (int j = 0; j < len; j++) {
                if (cur.charAt(j) != searchWord.charAt(j)) {
                    continue out;
                }
            }
            return i + 1;
        }
        return -1;
    }
}
