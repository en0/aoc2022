from aocfw import SolutionBase
from collections import deque
from math import inf
from p1 import Solution as P1Solution, Point
from typing import Iterable, Set


class Solution(P1Solution):

    def __init__(self):
        super().__init__()
        self.exposed_faces: Set[Point] = set()
        self._min_x = inf
        self._max_x = -inf
        self._min_y = inf
        self._max_y = -inf
        self._min_z = inf
        self._max_z = -inf

    def solve(self, data: Iterable[int]) -> int:
        for point in data:
            self.points.add(point)
            self.add_faces(point)
            self.update_boundaries(point)
            if point in self.faces:
                del self.faces[point]

        # Make space around the cubes to allow for continuous trarsial
        self.update_boundaries((self._min_x - 1, self._min_y - 1, self._min_z - 1))
        self.update_boundaries((self._max_x + 1, self._max_y + 1, self._max_z + 1))
        self.search_for_external_faces()
        return sum([v for k, v in self.faces.items() if k in self.exposed_faces])

    def search_for_external_faces(self) -> None:
        visited = set()
        stack = deque([(self._min_x + 1, self._min_y + 1, self._min_z + 1)])
        while stack:
            point = stack.pop()
            if point in self.points:
                continue
            elif point in self.faces:
                self.exposed_faces.add(point)
            for face in self.faces_from_point(point):
                x, y, z = face
                # Keep it inbounds
                if x < self._min_x: continue
                elif x > self._max_x: continue
                elif y < self._min_y: continue
                elif y > self._max_y: continue
                elif z < self._min_z: continue
                elif z > self._max_z: continue
                elif face not in visited:
                    visited.add(point)
                    stack.append(face)

    def update_boundaries(self, point: Point) -> None:
        x, y, z = point
        self._min_x = min(self._min_x, x)
        self._max_x = max(self._max_x, x)
        self._min_y = min(self._min_y, y)
        self._max_y = max(self._max_y, y)
        self._min_z = min(self._min_z, z)
        self._max_z = max(self._max_z, z)


if __name__ == '__main__':
    Solution.run(source='input.txt')
