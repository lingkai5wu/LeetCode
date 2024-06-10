class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deserialize(serialized_list, index=0):
    if index >= len(serialized_list) or serialized_list[index] is None:
        return None

    root = TreeNode(serialized_list[index])
    root.left = deserialize(serialized_list, 2 * index + 1)
    root.right = deserialize(serialized_list, 2 * index + 2)
    return root
