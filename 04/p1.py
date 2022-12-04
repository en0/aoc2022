from aocfw import SolutionBase, IParser
from parser import SetParser


class Solution(SolutionBase):

    bindings = {IParser: SetParser}

    def solve(self, data) -> int:
        return sum([1 if a & b == a or a & b == b else 0 for a, b in data])

if __name__ == '__main__':
    Solution.run(source='input.txt')
