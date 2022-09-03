package weeklyContest308;

public class Q3 {
    public int garbageCollection(String[] garbage, int[] travel) {
        int n = garbage.length;
        int[] garbageSum = new int[3], needMax = new int[3];
        for (int i = 0; i < n; i++) {
            int m = garbage[i].length();
            for (int j = 0; j < m; j++) {
                switch (garbage[i].charAt(j)) {
                    case 'M':
                        garbageSum[0]++;
                        needMax[0] = i;
                        break;
                    case 'P':
                        garbageSum[1]++;
                        needMax[1] = i;
                        break;
                    case 'G':
                        garbageSum[2]++;
                        needMax[2] = i;
                        break;
                }
            }
        }

        int[] preSum = new int[n];
        for (int i = 1; i < n; i++) {
            preSum[i] = preSum[i - 1] + travel[i - 1];
        }

        int res = 0;
        for (int i = 0; i < 3; i++) {
            res += garbageSum[i] + preSum[needMax[i]];
        }
        return res;
    }
}
