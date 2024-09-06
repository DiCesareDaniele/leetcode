'''
https://leetcode.com/problems/reconstruct-itinerary
'''

from collections import defaultdict

START: str = "JFK"

class Solution:
    # pylint: disable-next=invalid-name
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adj = defaultdict(list)
        for u, v in tickets:
            adj[u].append(v)
        for u in adj:
            adj[u].sort(reverse=True)
        tour = []
        def dfs(u: str):
            while len(adj[u]) > 0:
                v = adj[u].pop()
                dfs(v)
            tour.append(u)
        dfs(START)
        return tour[::-1]
