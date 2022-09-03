package weeklyContest306;

public class Q2 {
    public int edgeScore(int[] edges) {
        int n = edges.length;
        int[] arr = new int[n];
        int max = 0, res = 0;
        for (int i = 0; i < n; i++) {
            arr[edges[i]] += i;
            if (arr[edges[i]] > max) {
                res = edges[i];
                max = arr[edges[i]];
            } else if (arr[edges[i]] == max && res > edges[i]) {
                res = edges[i];
            }
        }
        return res;
    }
}