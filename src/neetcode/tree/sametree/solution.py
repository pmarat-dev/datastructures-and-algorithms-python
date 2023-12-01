class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    else:
        return False


def build_tree1():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)
    return tree


def build_tree2():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(9)
    return tree


if __name__ == "__main__":
    print(is_same_tree(build_tree1(), build_tree2()))
