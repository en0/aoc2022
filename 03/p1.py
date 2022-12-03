from typing import Iterable
from aocfw import SolutionBase, IParser, StringParser


class Solution(SolutionBase):

    bindings = {IParser: StringParser}

    def solve(self, data: Iterable[str]) -> int:
        value = 0
        for items in data:
            c1 = set(items[:len(items) // 2])
            c2 = set(items[len(items) // 2:])
            value += sum([self.value_of(p) for p in c1.intersection(c2)])
        return value

    def value_of(self, c):
        v = ord(c) - ord("a")
        if v < 0:
            v += 58
        return v + 1


if __name__ == '__main__':
    Solution.run(source='input.txt')
