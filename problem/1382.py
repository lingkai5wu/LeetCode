from typing import Optional

from util.tree import TreeNode, deserialize


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums = []

        def inorder_traversal(node):
            if node is None:
                return
            inorder_traversal(node.left)
            nums.append(node.val)
            inorder_traversal(node.right)

        inorder_traversal(root)

        def dfs(l):
            if not l:
                return None
            n = len(l) // 2
            node = TreeNode(l[n])
            node.left = dfs(l[:n])
            node.right = dfs(l[n + 1:])
            return node

        return dfs(nums)


if __name__ == '__main__':
    root = [1, None, 2, None, 3, None, 4, None, None]
    root = deserialize(root)
    print(Solution().balanceBST(root))
