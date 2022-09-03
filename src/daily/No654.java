package daily;

import util.TreeNode;

import java.util.Arrays;

public class No654 {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        if (nums.length == 0) {
            return null;
        }
        int max = -1, index = -1, n = nums.length;
        for (int i = 0; i < n; i++) {
            if (nums[i] > max) {
                max = nums[i];
                index = i;
            }
        }
        TreeNode root = new TreeNode(max);
        root.left = constructMaximumBinaryTree(Arrays.copyOf(nums, index));
        root.right = constructMaximumBinaryTree(Arrays.copyOfRange(nums, index + 1, n));
        return root;
    }

    public static void main(String[] args) {
        int[] nums = {3, 2, 1, 6, 0, 5};
        System.out.println(new No654().constructMaximumBinaryTree(nums));
    }
}
