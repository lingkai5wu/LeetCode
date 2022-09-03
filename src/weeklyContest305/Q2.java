package weeklyContest305;

import java.util.*;

public class Q2 {
    public int reachableNodes(int n, int[][] edges, int[] restricted) {
        List<Integer>[] graph = new List[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }

        Set<Integer> set = new HashSet<>();
        for (int i : restricted) {
            set.add(i);
        }

        for (int[] edge : edges) {
            if (set.contains(edge[0]) || set.contains(edge[1])) {
                continue;
            }
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }

        int res = 0;
        boolean[] isVisit = new boolean[n];
        Deque<Integer> deque = new ArrayDeque<>();
        deque.add(0);
        while (!deque.isEmpty()) {
            int cur = deque.poll();
            res++;
            isVisit[cur] = true;
            for (int i : graph[cur]) {
                if (!isVisit[i]) {
                    deque.add(i);
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {
        int n = 7;
        int[][] edges = {{0, 1}, {1, 2}, {3, 1}, {4, 0}, {0, 5}, {5, 6}};
        int[] restricted = {4, 5};
        System.out.println(new Q2().reachableNodes(n, edges, restricted));
    }
}
