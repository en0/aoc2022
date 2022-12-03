from typing import Iterable, Tuple
from aocfw import SolutionBase, IParser
from parser import RPCParser


class Solution(SolutionBase):

    bindings = {IParser: RPCParser}

    def solve(self, data: Iterable[Tuple[str, str]]) -> int:
        return sum([self.compute_points(a, b) for a, b in data])

    def compute_points(self, a, b) -> int:
        return {b-1: 6+b, b%3: 3+b}.get(a%3, b)


if __name__ == '__main__':
    Solution.run(source='input.txt')
