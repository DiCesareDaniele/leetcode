'''
https://leetcode.com/problems/binary-tree-right-side-view
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # pylint: disable-next=invalid-name
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        def dfs(root: TreeNode | None, depth: int, output: list[int]):
            if not root:
                return
            if depth >= len(output):
                output.append(root.val)
            dfs(root.right, depth + 1, output)
            dfs(root.left, depth + 1, output)
        output = []
        dfs(root, 0, output)
        return output
