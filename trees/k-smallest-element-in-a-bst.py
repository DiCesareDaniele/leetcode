'''
https://leetcode.com/problems/kth-smallest-element-in-a-bst
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # pylint: disable-next=invalid-name
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        if not root:
            return -1
        stack = []
        t = root
        while stack or t:
            while t:
                stack.append(t)
                t = t.left
            t = stack.pop()
            k -= 1
            if k == 0:
                return t.val
            t = t.right
        return -1
