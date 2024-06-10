from typing import Optional

from util.tree import TreeNode, deserialize


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is q

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    serialized_list_p = [1, 2, 3]
    serialized_list_q = [1, 2, 3]
    p_node = deserialize(serialized_list_p)
    q_node = deserialize(serialized_list_q)
    result = Solution().isSameTree(p_node, q_node)
    print(result)
