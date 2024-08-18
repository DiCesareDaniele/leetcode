'''
https://leetcode.com/problems/detect-squares
'''

class DetectSquares:
    points: dict[tuple[int, int], int]

    def __init__(self):
        self.points = {}

    def add(self, point: list[int]) -> None:
        p = tuple(point)
        self.points[p] = self.points.get(p, 0) + 1

    def count(self, point: list[int]) -> int:
        x, y = point
        res = 0
        for (xp, yp), n in self.points.items():
            x_dist = abs(x - xp)
            y_dist = abs(y - yp)
            if x_dist == y_dist and x_dist > 0:
                x_corner = (x, yp)
                y_corner = (xp, y)
                res += n * self.points.get(x_corner, 0) * self.points.get(y_corner, 0)
        return res
