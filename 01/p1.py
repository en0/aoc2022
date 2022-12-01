from typing import Iterable
from aocfw import SolutionBase, IParser
from calory_parser import CaloryParser

class Solution(SolutionBase):

    bindings = {IParser: CaloryParser}

    def solve(self, data: Iterable[str]) -> int:
        return max(data)


if __name__ == '__main__':
    Solution.run(source='input.txt')
