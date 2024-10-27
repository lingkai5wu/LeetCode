from typing import Optional

from util.tree import TreeNode, deserialize


class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        subtree_size_list = []

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            if node.left is None and node.right is None:
                subtree_size_list.append(1)
                return 1
            left = dfs(node.left)
            right = dfs(node.right)
            if left < 0 or left != right:
                return -1
            subtree_size_list.append(left * 2 + 1)
            return left * 2 + 1

        dfs(root)
        subtree_size_list.sort(reverse=True)
        if k > len(subtree_size_list):
            return -1
        return subtree_size_list[k - 1]


if __name__ == '__main__':
    serialized_list = [5, 3, 6, 5, 2, 5, 7, 1, 8, None, None, 6, 8]
    root = deserialize(serialized_list)
    k = 2
    print(Solution().kthLargestPerfectSubtree(root, k))
