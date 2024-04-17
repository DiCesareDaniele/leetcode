'''
https://leetcode.com/problems/invert-binary-tree
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # pylint: disable-next=invalid-name
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
