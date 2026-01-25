# Problem link: https://www.codingninjas.com/studio/problems/node-level_920383
from collections import deque

def nodeLevel(root, searchedValue: int) -> int:
    q = deque()
    if root:
        q.append((root, 1))
    while len(q) > 0:
        parent = q.popleft()
        node = parent[0]
        level = parent[1]

        if node.val == searchedValue:
            return level

        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))

    return 0
