from typing import Iterable, Set, Tuple, Dict
from aocfw import SolutionBase, IParser
from parser import Parser


Point = Tuple[int, int, int]


class Solution(SolutionBase):

    bindings = { IParser: Parser }

    def __init__(self):
        self.points: Set[Point] = set()
        self.faces: Dict[Point] = dict()

    def solve(self, data: Iterable[int]) -> int:
        for point in data:
            self.points.add(point)
            self.add_faces(point)
            if point in self.faces:
                del self.faces[point]
        return sum(self.faces.values())

    def add_faces(self, point: Point) -> None:
        for face in self.faces_from_point(point):
            if face not in self.points:
                self.faces.setdefault(face, 0)
                self.faces[face] += 1

    def faces_from_point(self, point: Point) -> Iterable[Point]:
        x, y, z = point
        yield (x+1, y, z)
        yield (x-1, y, z)
        yield (x, y+1, z)
        yield (x, y-1, z)
        yield (x, y, z+1)
        yield (x, y, z-1)


if __name__ == '__main__':
    Solution.run(source='input.txt')
