from typing import Iterable
from aocfw import SolutionBase, IParser
from parser import Parser
from math import ceil, floor
from itertools import count


class Solution(SolutionBase):

    bindings = {IParser: Parser}

    def solve(self, data: Iterable[int]) -> int:
        return self.to_snafu(sum(map(self.to_int, data)))

    def to_int(self, val: str) -> int:
        cols = []
        for i, sym in enumerate(reversed(val)):
            cols.append(5**i * {
                "2": 2,
                "1": 1,
                "0": 0,
                "-": -1,
                "=": -2,
            }[sym])
        return sum(cols)

    def to_snafu(self, val: int) -> str:
        for i in count():
            if val < 5 ** i:
                break

        oper = ceil
        snafu = []
        _v, v, m = val, val, 0

        while v != 0:

            i -= 1
            m = oper(v / 5**i)

            if m < -2 or m > 2:
                v = _v
                snafu = snafu[:-1]
                oper = floor
                i += 2
                continue

            _v = v
            v -= m * 5 ** i
            snafu.append(m)
            oper = ceil

        snafu += ['0'] * i
        return "".join([{
            2:'2',
            1:'1',
            0:'0',
            -1:'-',
            -2:'='
        }[a] for a in snafu])


if __name__ == '__main__':
    Solution.run(source='input.txt')
