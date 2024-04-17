'''
https://leetcode.com/problems/serialize-and-deserialize-binary-tree
'''

from collections import deque

class Codec:
    def serialize_pre(self, root, seq):
        if root is None:
            seq.append("#")
        else:
            seq.append(str(root.val))
            self.serialize_pre(root.left, seq)
            self.serialize_pre(root.right, seq)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        nodes = []
        self.serialize_pre(root, nodes)
        return "[" + ",".join(nodes) + "]"

    def deserialize_pre(self, seq):
        if not seq:
            return None

        v = seq.popleft()
        if v == "#":
            return None
        # pylint: disable-next=undefined-variable
        t = TreeNode(int(v)) # type: ignore
        t.left = self.deserialize_pre(seq)
        t.right = self.deserialize_pre(seq)
        return t

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        l = data.strip('][').split(',')
        q = deque(l)
        return self.deserialize_pre(q)
