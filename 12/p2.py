from typing import Iterable
from aocfw import SolutionBase
from p1 import Solution as P1Solution


class Solution(P1Solution):
    def solve(self, data: Iterable[int]) -> int:
        self._grid = next(data)
        _ = next(data)
        end = next(data)
        steps = []
        for start in [p for p, v in self._grid.items() if v == ord('a')]:
            count = self.find_path(start, end)
            if count is not None:
                steps.append(count)
        return min(steps)


if __name__ == '__main__':
    Solution.run(source='input.txt')
