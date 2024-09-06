'''
https://leetcode.com/problems/cheapest-flights-within-k-stops
'''

from collections import deque

class Solution:
    # pylint: disable-next=invalid-name, too-many-arguments
    def findCheapestPrice(
            self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))
        distances = [1e10] * n
        distances[src] = 0
        queue = deque()
        queue.append((src, 0))
        count = 1
        while len(queue) > 0 and k >= 0:
            u, dist = queue.popleft()

            for v, w in graph[u]:
                if dist + w < distances[v]:
                    distances[v] = dist + w
                    queue.append((v, dist + w))

            count -= 1
            if count == 0:
                count = len(queue)
                k -= 1
        d = distances[dst]
        return -1 if d == 1e10 else d
