from typing import Iterable
from aocfw import SolutionBase
from p1 import Solution as P1Solution


class Solution(P1Solution):

    def compute_points(self, a, b):
        return super().compute_points(a, (a+b)%3+1)


if __name__ == '__main__':
    Solution.run(source='input.txt')
