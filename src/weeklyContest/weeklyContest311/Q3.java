package weeklyContest.weeklyContest311;

import util.TreeNode;

import java.util.ArrayDeque;
import java.util.Deque;

public class Q3 {
    public TreeNode reverseOddLevels(TreeNode root) {
        if (root.left == null) {
            return root;
        }
        Deque<TreeNode> deque = new ArrayDeque<>();
        deque.add(root.left);
        deque.add(root.right);
        boolean flag = true;
        while (flag) {
            int size = deque.size();
            if (deque.peek().left==null || deque.peek().left.left == null) {
                flag = false;
            }
            Deque<TreeNode> needReversal = new ArrayDeque<>();
            for (int i = 0; i < size; i++) {
                TreeNode cur = deque.pop();
                needReversal.add(cur);
                if (flag) {
                    deque.add(cur.left.left);
                    deque.add(cur.left.right);
                    deque.add(cur.right.left);
                    deque.add(cur.right.right);
                }
            }
            while (needReversal.size() > 0) {
                int temp = needReversal.peek().val;
                needReversal.poll().val = needReversal.peekLast().val;
                needReversal.pollLast().val = temp;
            }
        }
        return root;
    }
}
