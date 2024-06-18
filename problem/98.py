from math import inf
from typing import Optional

from util.tree import TreeNode, deserialize


class Solution:
    per = -inf

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        if not self.isValidBST(root.left):
            return False
        if not self.per < root.val:
            return False

        self.per = root.val
        return self.isValidBST(root.right)

    def isValidBST2(self, root: Optional[TreeNode], left=-inf, right=inf) -> bool:
        if root is None:
            return True

        if not left < root.val < right:
            return False

        return self.isValidBST2(root.left, left, root.val) and self.isValidBST2(root.right, root.val, right)


if __name__ == '__main__':
    serialized_list = [5, 1, 4, None, None, 3, 6]
    root_node = deserialize(serialized_list)
    result = Solution().isValidBST2(root_node)
    print(result)
