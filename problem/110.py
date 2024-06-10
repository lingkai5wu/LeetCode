from typing import Optional

from util.tree import TreeNode, deserialize


class Solution:
    def dfs(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        left_depth = self.dfs(node.left)
        if left_depth == -1:
            return -1
        right_depth = self.dfs(node.right)
        if right_depth == -1 or abs(left_depth - right_depth) > 1:
            return -1
        return max(left_depth, right_depth) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) != -1


if __name__ == '__main__':
    serialized_list = [3, 9, 20, None, None, 15, 7]
    root_node = deserialize(serialized_list)
    result = Solution().isBalanced(root_node)
    print(result)
