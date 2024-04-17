'''
https://leetcode.com/problems/subtree-of-another-tree
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # pylint: disable-next=invalid-name
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> int:
            if p is None or q is None:
                return p is None and q is None
            if p.val != q.val:
                return False
            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
        if root is None:
            return subRoot is None
        if is_same_tree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
