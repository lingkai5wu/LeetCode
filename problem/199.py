from typing import Optional, List

from util.tree import TreeNode, deserialize


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result_list = []

        def bfs(node: Optional[TreeNode], deep: int) -> None:
            if node is None:
                return

            if deep >= len(result_list):
                result_list.append(node.val)

            bfs(node.right, deep + 1)
            bfs(node.left, deep + 1)

        bfs(root, 0)
        return result_list


if __name__ == '__main__':
    serialized_list = [1, 2, 3, None, 5, None, 4]
    root_node = deserialize(serialized_list)
    result = Solution().rightSideView(root_node)
    print(result)
