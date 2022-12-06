from typing import Iterable
from aocfw import SolutionBase, IParser, StringParser
from collections import deque
from p1 import Solution as P1Solution


class Solution(P1Solution):
    offset = 13


if __name__ == '__main__':
    Solution.run(source='input.txt')
