package weeklyContest301;

public class Q3 {
    public static void main(String[] args) {
        String start = "_R", target = "R_";
        System.out.println(new Q3().canChange(start, target));
    }

    public boolean canChange(String start, String target) {
        String str = start.replace("_", "");
        if (!str.equals(target.replace("_", ""))) {
            return false;
        }
        int n = start.length();
        int arr[][] = new int[2][];
        arr[0] = getIndexArr(start, str.length());
        arr[1] = getIndexArr(target, str.length());
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == 'L') {
                if (arr[1][i] > arr[0][i]) {
                    return false;
                }
            } else {
                if (arr[0][i] > arr[1][i]) {
                    return false;
                }
            }
        }
        return true;
    }

    private int[] getIndexArr(String origin, int len) {
        int[] arr = new int[len];
        int index = 0;
        for (int i = 0; i < origin.length(); i++) {
            if (origin.charAt(i) != '_') {
                arr[index++] = i;
            }
        }
        return arr;
    }
}
