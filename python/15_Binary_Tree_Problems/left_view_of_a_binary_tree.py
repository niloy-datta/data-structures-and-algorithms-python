# Problem link: https://www.codingninjas.com/studio/problems/left-view-of-a-binary-tree_920519
from collections import deque

def getLeftView(root):
    ans = []
    fre = [False] * 3005
    q = deque()
    if root:
        q.append((root, 1))
    while len(q) > 0:
        parent = q.popleft()
        node = parent[0]
        level = parent[1]

        if fre[level] == False:
            ans.append(node.data)
            fre[level] = True

        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))

    return ans
