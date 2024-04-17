'''
https://leetcode.com/problems/count-good-nodes-in-binary-tree
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # pylint: disable-next=invalid-name
    def goodNodes(self, root: TreeNode) -> int:
        def good_nodes_helper(root: TreeNode | None, max_v: int) -> int:
            if not root:
                return 0
            delta = 1 if root.val >= max_v else 0
            max_v = max(max_v, root.val)
            lgn = good_nodes_helper(root.left, max_v)
            rgn = good_nodes_helper(root.right, max_v)
            return lgn + rgn + delta
        return good_nodes_helper(root, -1e10)
