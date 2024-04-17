'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
'''

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # pylint: disable-next=invalid-name
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        val_to_idx = {v: i for i, v in enumerate(inorder)}
        def build_tree_helper(preorder: deque[int], inorder: list[int], i: int, j: int) -> \
            TreeNode | None:
            if not preorder:
                return None
            root_val = preorder[0]
            k = val_to_idx[root_val]
            if k >= j or k < i:
                return None
            preorder.popleft()
            lt = build_tree_helper(preorder, inorder, i, k)
            rt = build_tree_helper(preorder, inorder, k + 1, j)
            return TreeNode(root_val, lt, rt)
        return build_tree_helper(deque(preorder), inorder, 0, len(preorder))
