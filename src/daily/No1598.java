package daily;

public class No1598 {
    public int minOperations(String[] logs) {
        int depth = 0;
        for (String log : logs) {
            if (log.startsWith("..")) {
                if (depth > 0) {
                    depth--;
                }
            } else if (!log.startsWith(".")) {
                depth++;
            }
        }
        return depth;
    }
}
