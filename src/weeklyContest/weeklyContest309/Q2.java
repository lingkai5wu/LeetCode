package weeklyContest.weeklyContest309;

public class Q2 {
    public int numberOfWays(int startPos, int endPos, int k) {
        int m = Math.abs(Math.abs(endPos) - Math.abs(startPos));
        if (m > k || (k - m) % 2 == 1) {
            return 0;
        }
        m *= 1.5;
        if (m == k) {
            return 1;
        }
        return (int) ((f(k) / f(m) / f(k - m)) % (1e9 + 1));
    }

    public static long f(long n) {
        if (n <= 1)
            return 1;
        else
            return n * f(n - 1);
    }
}
