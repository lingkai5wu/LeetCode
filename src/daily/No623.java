package daily;

import util.TreeNode;

import java.util.ArrayDeque;
import java.util.Deque;

public class No623 {
    public TreeNode addOneRow1(TreeNode root, int val, int depth) {
        if (depth == 1) {
            return new TreeNode(val, root, null);
        }
        Deque<TreeNode> deque = new ArrayDeque<>();
        deque.add(root);
        while (!deque.isEmpty()) {
            int size = deque.size();
            if (depth == 2) {
                for (int i = 0; i < size; i++) {
                    TreeNode cur = deque.poll();
                    TreeNode leftNode = new TreeNode(val), rightNode = new TreeNode(val);
                    assert cur != null;
                    leftNode.left = cur.left;
                    rightNode.right = cur.right;
                    cur.left = leftNode;
                    cur.right = rightNode;
                }
                return root;
            }
            for (int i = 0; i < size; i++) {
                TreeNode cur = deque.poll();
                assert cur != null;
                if (cur.left != null) {
                    deque.add(cur.left);
                }
                if (cur.right != null) {
                    deque.add(cur.right);
                }
            }
            depth--;
        }
        return root;
    }

    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        if (root == null) {
            return null;
        }
        if (depth == 1) {
            return new TreeNode(val, root, null);
        }
        if (depth == 2) {
            root.left = new TreeNode(val, root.left, null);
            root.right = new TreeNode(val, null, root.right);
        } else {
            root.left = addOneRow(root.left, val, depth - 1);
            root.right = addOneRow(root.right, val, depth - 1);
        }
        return root;
    }
}
