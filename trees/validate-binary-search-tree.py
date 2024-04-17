'''
https://leetcode.com/problems/validate-binary-search-tree
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # pylint: disable-next=invalid-name
    def isValidBST(self, root: TreeNode | None) -> bool:
        def is_valid_bst(root: TreeNode | None, lower_bound: int, upper_bound: int) -> bool:
            if not root:
                return True
            bounded = lower_bound < root.val and root.val < upper_bound
            if not bounded:
                return False
            if not is_valid_bst(root.left, lower_bound, root.val):
                return False
            if not is_valid_bst(root.right, root.val, upper_bound):
                return False
            return True
        if not root:
            return True
        return is_valid_bst(root, -1e10, 1e10)
