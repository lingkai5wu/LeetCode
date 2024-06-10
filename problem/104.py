from typing import Optional

from util.tree import TreeNode, deserialize


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == '__main__':
    serialized_list = [3, 9, 20, None, None, 15, 7]
    root_node = deserialize(serialized_list)
    result = Solution().maxDepth(root_node)
    print(result)
