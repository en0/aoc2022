from typing import Iterable
from aocfw import SolutionBase
from functools import cmp_to_key
from p1 import Solution as P1Solution


class Solution(P1Solution):
    def solve(self, data: Iterable[int]) -> int:
        packets = [[[2]], [[6]]]
        for a, b in data:
            packets.append(a)
            packets.append(b)
        packets = sorted(packets, key=cmp_to_key(self.compare))
        return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


if __name__ == '__main__':
    Solution.run(source='input.txt')
