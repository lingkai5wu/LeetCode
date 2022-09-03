package weeklyContest302;

public class Q1 {
    public int[] numberOfPairs(int[] nums) {
        int[] map = new int[101];
        for (int num : nums) {
            map[num]++;
        }
        int[] res = new int[2];
        for (int i : map) {
            res[0] += i / 2;
            res[1] += i % 2;
        }
        return res;
    }
}
