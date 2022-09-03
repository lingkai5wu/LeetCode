package weeklyContest304;

import java.util.*;

public class Q4 {
    int n;
    List<Integer>[] graphReverse;

    public int longestCycle(int[] edges) {
        n = edges.length;
        graphReverse = new List[n];
        for (int i = 0; i < n; i++) {
            graphReverse[i] = new ArrayList();
        }
        for (int i = 0; i < n; i++) {
            if (edges[i] != -1)
                graphReverse[edges[i]].add(i);
        }
        int res = -1;
        for (int i = 0; i < n; i++) {
            if (edges[i] == -1) {
                res = Math.max(bfs(i), res);
            }
        }
        return res;
    }

    private int bfs(int node) {
        Deque<Integer> deque = new ArrayDeque<>();
        int[] visited = new int[n];
        Arrays.fill(visited, -1);
        deque.add(node);
        int depth = 0;
        while (!deque.isEmpty()) {
            int size = deque.size();
            for (int i = 0; i < size; i++) {
                int cur = deque.poll();
                if (visited[cur] != -1) {
                    return depth - visited[cur];
                }
                visited[cur] = depth;
                for (int edge : graphReverse[cur]) {
                    deque.add(edge);
                }
            }
            depth++;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] edges = {3, 3, 4, 2, 3};
        System.out.println(new Q4().longestCycle(edges));
    }
}
