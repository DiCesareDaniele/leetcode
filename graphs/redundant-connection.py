'''
https://leetcode.com/problems/redundant-connection
'''

class Solution:
    # pylint: disable-next=invalid-name
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [1] * (n + 1)
        def find(i: int) -> int:
            while parent[i] != i:
                i = parent[i]
            return i
        def union(i: int, j: int) -> bool:
            pi = find(i)
            pj = find(j)
            if pi == pj:
                return False
            if rank[pi] > rank[pj]:
                parent[pj] = pi
                rank[pi] += rank[pj]
            else:
                parent[pi] = pj
                rank[pj] += rank[pi]
            return True
        for i, j in edges:
            if not union(i, j):
                return [i, j]
        return [-1, -1]
