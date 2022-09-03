package daily;

import java.util.ArrayDeque;
import java.util.Deque;

public class No1417 {
    public String reformat(String s) {
        StringBuilder sb = new StringBuilder();
        int n = s.length();
        Deque<Character> deque = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                // sb 中先存放数字
                sb.append(c);
            } else {
                // 字母放在队列里
                deque.add(c);
            }
        }
        // 两者长度差大于1则无法构造
        if (Math.abs(sb.length() - deque.size()) > 1) {
            return "";
        }
        // 将字母间隔插入到数字串中，若数字的数量大于字母，则开头为数字，字母从下标1开始插入
        for (int i = sb.length() > deque.size() ? 1 : 0; i < n; i += 2) {
            sb.insert(i, deque.poll());
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        String s = "abc1234";
        System.out.println(new No1417().reformat(s));
    }
}
