from typing import Iterable, Tuple, Dict
from collections import deque
from logging import getLogger


Point = Tuple[int, int]


class Elf:

    def __init__(self, pos: Point):
        self._pos = pos
        self._prop = None
        self._dir = deque(["N", "S", "W", "E"])
        self._log = getLogger(self.__class__.__name__)

    def __repr__(self) -> str:
        return f"Elf(pos={self._pos})"

    def get_pos(self) -> Point:
        return self._pos

    def propose(self, elves: Dict[Point, "Elv"]) -> Point:
        targets = []
        for target_dir in self._dir:
            a, b, c = self._compute_adjacent_points(target_dir)
            if not any([p in elves for p in [a, b, c]]):
                targets.append(b)
        if 0 < len(targets) < 4:
            self._prop = targets[0]
        else:
            self._prop = None
        self._rotate_dir()
        return self._prop

    def move(self) -> None:
        if self._prop:
            self._log.debug("Moving from %s to %s", self._pos, self._prop)
            self._pos = self._prop

    def _compute_adjacent_points(self, target_dir: str):
        x, y = self._pos
        return {
            "N": [(x-1, y-1), (x, y-1), (x+1, y-1)],
            "S": [(x-1, y+1), (x, y+1), (x+1, y+1)],
            "W": [(x-1, y+1), (x-1, y), (x-1, y-1)],
            "E": [(x+1, y-1), (x+1, y), (x+1, y+1)],
        }[target_dir]

    def _rotate_dir(self):
        self._dir.rotate(-1)

