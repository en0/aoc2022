from typing import Iterable
from aocfw import SolutionBase, IParser
from parser import Parser
from p1 import Solution as P1Solution


class Solution(P1Solution):

    bindings = {IParser: Parser}

    def solve(self, data: Iterable[int]) -> int:
        zero_node = self.load_data(data)
        self.mix(10)
        return sum(self.get_coords(zero_node))

    def load_data(self, data):
        return super().load_data(map(lambda i:i*811589153, data))

if __name__ == '__main__':
    Solution.run(source='input.txt')
