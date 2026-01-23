# Problem link: https://www.codingninjas.com/studio/problems/diameter-of-the-binary-tree_920552

mx = 0

def max_height(root):
    global mx
    if root is None:
        return 0
    l = max_height(root.left)
    r = max_height(root.right)
    d = l + r
    mx = max(mx, d)
    return max(l, r) + 1

def diameterOfBinaryTree(root):
    global mx
    mx = 0
    h = max_height(root)
    return mx
