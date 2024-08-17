'''
https://leetcode.com/problems/clone-graph
'''

class Node:
    def __init__(self, val: int = 0, neighbors: list['Node'] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # pylint: disable-next=invalid-name
    def cloneGraph(self, node: Node | None) -> Node | None:
        if node is None:
            return None
        clones = {}
        def dfs(node: Node) -> Node:
            if node.val in clones:
                return clones[node.val]
            clone = Node(node.val)
            clones[node.val] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone
        return dfs(node)
