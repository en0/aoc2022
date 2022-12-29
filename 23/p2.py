from typing import Iterable
from aocfw import SolutionBase, IParser
from parser import Parser
from p1 import Solution as P1Solution
from itertools import count


class Solution(P1Solution):

    bindings = {IParser: Parser}

    def solve(self, data: Iterable) -> int:
        self.load_data(data)
        for i in count():
            if self.move() == 0:
                return i + 1


if __name__ == '__main__':
    Solution.run(source='input.txt')
