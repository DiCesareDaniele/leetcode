'''
https://leetcode.com/problems/diameter-of-binary-tree
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # pylint: disable-next=invalid-name
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        def diameter_helper(root: TreeNode | None) -> tuple[int, int]:
            if not root:
                return (0, 0)
            ldiameter, ldepth = diameter_helper(root.left)
            rdiameter, rdepth = diameter_helper(root.right)

            return (max(ldiameter, rdiameter, ldepth + rdepth), max(ldepth, rdepth) + 1)
        return diameter_helper(root)[0]
