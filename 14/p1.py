from typing import Iterable
from aocfw import SolutionBase, IParser
from parser import LineParser
from space import Space


class Solution(SolutionBase):

    bindings = {IParser: LineParser}

    def __init__(self):
        self.space = Space()
        self._origin = (500, 0)

    def solve(self, data: Iterable[int]) -> int:
        for datum in data:
            self.space.add_lines(datum)

        i = 0
        while not self.space.overflow:
            i += 1
            self.space.drop_sand(self._origin)
        self.space.show()
        return i - 1


if __name__ == '__main__':
    Solution.run(source='input.txt')
