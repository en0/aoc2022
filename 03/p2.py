from typing import Iterable
from aocfw import SolutionBase, IParser, StringParser


class Solution(SolutionBase):

    bindings = {IParser: StringParser}

    def solve(self, data: Iterable[str]) -> int:
        groups = {}
        for i, items in enumerate(data):
            g = i // 3
            c1 = set(items)
            groups.setdefault(g, c1)
            groups[g] &= set(items)

        value = 0
        for badges in groups.values():
            for badge in badges:
                value += self.value_of(badge)
        return value

    def value_of(self, c):
        v = ord(c) - ord("a")
        if v < 0:
            v += 58
        return v + 1


if __name__ == '__main__':
    Solution.run(source='input.txt')
