from typing import Optional

from util.tree import TreeNode, deserialize


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None or q is None:
                return p is q

            if p.val != q.val:
                return False

            return dfs(p.left, q.right) and dfs(p.right, q.left)

        return dfs(root.left, root.right)


if __name__ == '__main__':
    serialized_list = [1, 2, 2, 3, 4, 4, 3]
    root_node = deserialize(serialized_list)
    result = Solution().isSymmetric(root_node)
    print(result)
