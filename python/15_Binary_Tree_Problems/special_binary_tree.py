# Problem link: https://www.codingninjas.com/studio/problems/special-binary-tree_920502

def isSpecialBinaryTree(root) -> bool:
    if root is None:
        return True
    if (root.left is not None and root.right is None) or (root.left is None and root.right is not None):
        return False
    l = isSpecialBinaryTree(root.left)
    r = isSpecialBinaryTree(root.right)
    return l and r
