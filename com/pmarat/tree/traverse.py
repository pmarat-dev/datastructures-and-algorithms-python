class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val, end=" "),
        print_inorder(root.right)


def print_preorder(root):
    if root:
        print(root.val, end=" "),
        print_preorder(root.left)
        print_preorder(root.right)


def print_postorder(root):
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.val, end=" "),


if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)

    print("\nInorder traversal of binary tree is: ")
    print_inorder(tree)

    print("\nPreorder traversal of binary tree is: ")
    print_preorder(tree)

    print("\nPostorder traversal of binary tree is: ")
    print_postorder(tree)
