package daily;

import util.TreeNode;

import java.util.ArrayDeque;
import java.util.Deque;

public class No513 {
    public int findBottomLeftValue(TreeNode root) {
        Deque<TreeNode> deque = new ArrayDeque<>();
        deque.add(root);
        int res = root.val;
        while (!deque.isEmpty()) {
            int n = deque.size();
            for (int i = 0; i < n; i++) {
                TreeNode cur = deque.poll();
                if (i == 0) {
                    res = cur.val;
                }
                if (cur.left != null) {
                    deque.add(cur.left);
                }
                if (cur.right != null) {
                    deque.add(cur.right);
                }
            }
        }
        return res;
    }
}
