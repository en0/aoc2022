from typing import Iterable
from aocfw import SolutionBase, IParser
from parser import PacketParser


class Solution(SolutionBase):

    bindings = {IParser: PacketParser}

    def solve(self, data: Iterable[int]) -> int:
        ans = []
        for i, (a, b) in enumerate(data, start=1):
            self.log.debug("== Pair %s ==", i)
            if self.compare(a, b) == -1:
                ans.append(i)
        return sum(ans)

    def compare(self, left, right, nest = 1) -> int:

        self.log.debug("%s- COMPARE %s vs %s", ' '*nest, left, right)

        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                self.log.debug("%s - Left side is smaller, so inputs are in the right order", ' '*nest)
                return -1
            elif left > right:
                self.log.debug("%s - Right side is smaller, so inputs are not in the right order", ' '*nest)
                return 1
            else:
                return 0

        elif isinstance(left, list) and isinstance(right, list):
            for _left, _right in zip(left, right):
                comp = self.compare(_left, _right, nest+1)
                if comp != 0:
                    return comp
            if len(left) < len(right):
                self.log.debug("%s - left side ran out of items, so inputs are in the right order", ' '*nest)
                return -1
            elif len(left) > len(right):
                self.log.debug("%s - right side ran out of items, so inputs are not in the right order", ' '*nest)
                return 1
            else:
                return 0

        elif  isinstance(left, int):
            return self.compare([left], right, nest+1)

        elif isinstance(right, int):
            return self.compare(left, [right], nest+1)


if __name__ == '__main__':
    Solution.run(source='input.txt')
