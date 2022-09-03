package weeklyContest307;

import util.TreeNode;

import java.util.*;

public class Q3 {
    Map<Integer, List<Integer>> graph;

    public int amountOfTime(TreeNode root, int start) {
        if (root.left == null && root.right == null) {
            return 0;
        }
        graph = new HashMap<>();
        dfs(root);
        int res = -1;
        Deque<Integer> deque = new ArrayDeque<>();
        deque.add(start);
        while (!deque.isEmpty()) {
            int size = deque.size();
            for (int i = 0; i < size; i++) {
                int cur = deque.poll();
                for (int child : graph.get(cur)) {
                    if (graph.containsKey(child)) {
                        deque.add(child);
                    }
                }
                graph.remove(cur);
            }
            res++;
        }
        return res;
    }

    private void dfs(TreeNode root) {
        if (root == null) {
            return;
        }
        addEdge(root, root.left);
        addEdge(root, root.right);
        dfs(root.left);
        dfs(root.right);
    }

    private void addEdge(TreeNode root, TreeNode child) {
        if (child == null) {
            return;
        }
        graph.putIfAbsent(root.val, new ArrayList<>(3));
        graph.putIfAbsent(child.val, new ArrayList<>(3));
        graph.get(root.val).add(child.val);
        graph.get(child.val).add(root.val);
    }
}
