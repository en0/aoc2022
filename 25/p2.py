from typing import Iterable
from aocfw import SolutionBase, IParser
from parser import Parser


class Solution(SolutionBase):

    bindings = {IParser: Parser}

    def solve(self, data: Iterable[int]) -> int:
        raise NotImplementedError()


if __name__ == '__main__':
    Solution.run(source='input.txt')
