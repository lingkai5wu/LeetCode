package weeklyContest307;

import java.util.Arrays;

public class Q1 {
    public int minNumberOfHours(int initialEnergy, int initialExperience, int[] energy, int[] experience) {
        int n = energy.length;
        initialEnergy -= Arrays.stream(energy).sum();
        int sumNeedExp = 0;
        for (int i = 0; i < n; i++) {
            if (initialExperience <= experience[i]) {
                int needExp = experience[i] - initialExperience + 1;
                initialExperience += needExp;
                sumNeedExp += needExp;
            }
            initialExperience += experience[i];
        }
        return initialEnergy > 0 ? 0 : 1 - initialEnergy + Math.max(sumNeedExp, 0);
    }

    public static void main(String[] args) {
        int initialEnergy = 1, initialExperience = 1;
        int[] energy = {1, 1, 1, 1}, experience = {1, 1, 1, 50};
        System.out.println(new Q1().minNumberOfHours(initialEnergy, initialExperience, energy, experience));
    }
}
