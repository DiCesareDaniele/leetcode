'''
https://leetcode.com/problems/binary-tree-maximum-path-sum
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # pylint: disable-next=invalid-name
    def maxPathSum(self, root: TreeNode | None) -> int:
        def max_path_helper(root: TreeNode | None) -> tuple[int, int]:
            if not root:
                return [-1e10, 0]
            lhs_max, lhs_root_max = max_path_helper(root.left)
            rhs_max, rhs_root_max = max_path_helper(root.right)
            curr_root_max = root.val + max(lhs_root_max, rhs_root_max, 0)
            curr_max = max(lhs_max, rhs_max, root.val + max(lhs_root_max, 0) + max(rhs_root_max, 0))
            return (curr_max, curr_root_max)
        return max_path_helper(root)[0]
