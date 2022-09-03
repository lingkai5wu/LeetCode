package weeklyContest304;

public class Q2 {
    public int maximumGroups(int[] grades) {
        int n = grades.length;
        int res = 0;
        while (n >= 0) {
            res++;
            n -= res;
        }
        return --res;
    }
}
