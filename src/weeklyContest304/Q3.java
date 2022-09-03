package weeklyContest304;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class Q3 {
    int n;
    int[] edges;

    public int closestMeetingNode(int[] edges, int node1, int node2) {
        n = edges.length;
        this.edges = edges;
        int[][] visiteds = new int[2][n];
        visiteds[0] = bfs(node1);
        visiteds[1] = bfs(node2);
        int res = -1, min = n;
        for (int i = 0; i < n; i++) {
            if (visiteds[0][i] != -1 && visiteds[1][i] != -1) {
                int max = Math.max(visiteds[0][i], visiteds[1][i]);
                if (max < min) {
                    min = max;
                    res = i;
                }
            }
        }
        return res;
    }

    private int[] bfs(int node) {
        Deque<Integer> deque = new ArrayDeque<>();
        int[] visited = new int[n];
        Arrays.fill(visited, -1);
        deque.add(node);
        int depth = 0;
        while (!deque.isEmpty()) {
            int size = deque.size();
            for (int i = 0; i < size; i++) {
                int cur = deque.poll();
                if (visited[cur] == -1) {
                    visited[cur] = depth;
                    if (edges[cur] != -1) {
                        deque.add(edges[cur]);
                    }
                }
            }
            depth++;
        }
        return visited;
    }

    public static void main(String[] args) {
        int[] edges = {4, 3, 0, 5, 3, -1};
        int node1 = 4, node2 = 0;
        System.out.println(new Q3().closestMeetingNode(edges, node1, node2));
    }
}
