'''
https://leetcode.com/problems/balanced-binary-tree
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # pylint: disable-next=invalid-name
    def isBalanced(self, root: TreeNode | None) -> int:
        def is_balanced_helper(root: TreeNode | None) -> tuple[bool, int]:
            if not root:
                return (True, 0)
            lbalanced, ldepth = is_balanced_helper(root.left)
            rbalanced, rdepth = is_balanced_helper(root.right)
            return (lbalanced and rbalanced and abs(ldepth - rdepth) <= 1, max(ldepth, rdepth) + 1)
        return is_balanced_helper(root)[0]
