from typing import Iterable, NamedTuple
from functools import reduce
from aocfw import SolutionBase, IParser, StringParser


class Vector(NamedTuple):

    x: int
    y: int

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(other.x + self.x, other.y + self.y)


class Solution(SolutionBase):

    bindings = {IParser: StringParser}

    def __init__(self):
        self.trees = None

    def solve(self, data: Iterable[str]) -> int:
        ans = 0
        self.load_trees(data)
        for y, row in enumerate(self.trees):
            for x, tree in enumerate(row):
                pos = Vector(y, x)
                ans = max(self.compute_view_score(pos), ans)
        return ans

    def compute_view_score(self, pos: Vector) -> int:
        vals = [
            self.view_from(pos, Vector(0, -1)),
            self.view_from(pos, Vector(-1, 0)),
            self.view_from(pos, Vector(1, 0)),
            self.view_from(pos, Vector(0, 1)),
        ]
        return reduce(lambda a, b: a*b, vals, 1)

    def view_from(self, pos: Vector, vec: Vector) -> int:
        count = 0
        val_at = lambda v: self.trees[v.y][v.x]
        val = val_at(pos)
        while True:
            pos += vec
            if pos.x < 0 or pos.y < 0:
                break
            try:
                other_val = val_at(pos)
            except IndexError:
                break
            count += 1
            if other_val >= val:
                break
        return count

    def load_trees(self, data: Iterable[str]):
        self.trees = []
        for line in data:
            row = []
            for tree in line:
                row.append(int(tree))
            self.trees.append(row)


if __name__ == '__main__':
    Solution.run(source='input.txt')
