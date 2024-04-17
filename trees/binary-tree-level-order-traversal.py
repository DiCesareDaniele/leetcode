'''
https://leetcode.com/problems/binary-tree-level-order-traversal
'''

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # pylint: disable-next=invalid-name
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        level = []
        levels = []
        queue = deque()
        queue.append(root)
        count = 1
        while queue:
            u = queue.popleft()
            level.append(u.val)

            if u.left:
                queue.append(u.left)
            if u.right:
                queue.append(u.right)

            count -= 1
            if count == 0:
                count = len(queue)
                levels.append(level)
                level = []
        return levels
