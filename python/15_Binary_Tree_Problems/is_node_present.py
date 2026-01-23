# Problem link: https://www.codingninjas.com/studio/problems/code-find-a-node_5682

def isNodePresent(root, x: int) -> bool:
    if root is None:
        return False
    if root.data == x:
        return True
    l = isNodePresent(root.left, x)
    r = isNodePresent(root.right, x)
    return (l or r)
