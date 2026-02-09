class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deserialize(lst):
    it = iter(lst)

    def build():
        try:
            val = next(it)
        except StopIteration:
            return None
        if val is None:
            return None
        node = TreeNode(val)
        node.left = build()
        node.right = build()
        return node

    return build()
