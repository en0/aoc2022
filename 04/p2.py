from aocfw import SolutionBase, IParser
from parser import SetParser


class Solution(SolutionBase):

    bindings = {IParser: SetParser}

    def solve(self, data) -> int:
        return sum([1 if len(a & b) > 0 else 0 for a, b in data])

if __name__ == '__main__':
    Solution.run(source='input.txt')
