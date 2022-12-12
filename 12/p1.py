from typing import Iterable, Dict, Tuple, Set, List
from aocfw import SolutionBase, IParser
from parser import MapParser
from collections import deque


class Solution(SolutionBase):

    bindings = {IParser: MapParser}

    def __init__(self):
        self._grid: Dict[Tuple[int, int], int] = None
        self._visited: Set[Tuple[int, int]] = set()

    def solve(self, data: Iterable[int]) -> int:
        self._grid = next(data)
        start = next(data)
        end = next(data)
        return self.find_path(start, end)

    def find_path(self, start: Tuple[int, int], end: Tuple[int, int]) -> Tuple[int, Tuple[int, int]]:
        queue = deque([(0, start)])
        self._visited = set()
        while queue:
            steps, pos = queue.popleft()
            if pos in self._visited:
                continue
            if pos == end:
                return steps
            for _pos in self.options_from(pos):
                queue.append((steps+1, _pos))
            self._visited.add(pos)

    def options_from(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        x, y = pos
        for p in [(x, y-1),(x-1, y),(x+1, y),(x, y+1)]:
            if p not in self._grid:
                continue
            elif p in self._visited:
                continue
            elif self._grid[p] - self._grid[pos] < 2:
                yield p


if __name__ == '__main__':
    Solution.run(source='input.txt')
