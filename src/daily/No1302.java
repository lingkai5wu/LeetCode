package daily;

import util.TreeNode;

import java.util.ArrayDeque;
import java.util.Deque;

public class No1302 {
    public int deepestLeavesSum(TreeNode root) {
        Deque<TreeNode> deque = new ArrayDeque<>();
        deque.add(root);
        int sum = 0;
        while (!deque.isEmpty()) {
            sum = 0;
            int size = deque.size();
            for (int i = 0; i < size; i++) {
                TreeNode cur = deque.poll();
                assert cur != null;
                sum += cur.val;
                if (cur.left != null) {
                    deque.add(cur.left);
                }
                if (cur.right != null) {
                    deque.add(cur.right);
                }
            }
        }
        return sum;
    }
}
