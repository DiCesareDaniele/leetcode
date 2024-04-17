'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # pylint: disable-next=invalid-name
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        lca = root
        while lca:
            if lca in (p, q):
                return lca
            if p.val < lca.val and lca.val < q.val:
                return lca
            if p.val < lca.val and q.val < lca.val:
                lca = lca.left
            elif lca.val < p.val and lca.val < q.val:
                lca = lca.right
        return lca
