from typing import Set, Dict, Iterable
from vector import Vector, LEFT, RIGHT, DOWN


class Cave:

    def __init__(self, width: int, height: int = 0) -> None:
        self._blocks: Set[Vector] = set()
        self._width = width
        self._height = height

    @property
    def height(self) -> int:
        return self._height

    def __contains__(self, block: Vector) -> bool:
        if block in self._blocks: return True
        elif not 0 <= block.x < self._width: return True
        else: return block.y >= 0

    def add_blocks(self, blocks: Iterable[Vector]) -> None:
        for block in blocks:
            self._height = min(block.y, self._height)
            self._blocks.add(block)

        ret = []
        for y in range(self._height, self._height + 100):
            line = []
            for x in range(7):
                if Vector(x, y) in self._blocks:
                    line.append("#")
                else:
                    line.append(".")
            ret.append("".join(line))
        return "\n".join(ret)


    def prune(self):
        # I don't trust this.
        _blocks = set()
        for block in self._blocks:
            if not block.y > self.height + 100:
                _blocks.add(block)
        self._blocks = _blocks

    def render(self):
        if not self._blocks:
            return ""
        min_y = min(map(lambda b: b.y, self._blocks))
        max_y = max(map(lambda b: b.y, self._blocks))
        repr = []
        for y in range(min_y, max_y + 1):
            line = ['|']
            for x in range(0, self._width):
                if Vector(x, y) in self._blocks:
                    line.append("#")
                else:
                    line.append(".")
            line.append("|")
            repr.append("".join(line))
        return "\n" + "\n".join(repr) + "\n+-------+"

