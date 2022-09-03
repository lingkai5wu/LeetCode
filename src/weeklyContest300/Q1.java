package weeklyContest300;

import java.util.HashMap;
import java.util.Map;

public class Q1 {
    public String decodeMessage(String key, String message) {
        Map<Character, Character> map = new HashMap<>(26);
        char cur = 'a';
        for (char c : key.toCharArray()) {
            if (c != ' ' && !map.containsKey(c)) {
                map.put(c, cur++);
            }
        }
        StringBuffer sb = new StringBuffer();
        for (char c : message.toCharArray()) {
            if (c == ' ') {
                sb.append(c);
            } else {
                sb.append(map.get(c));
            }
        }
        return sb.toString();
    }
}
