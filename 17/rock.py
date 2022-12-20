from typing import Set, Dict, Iterable
from vector import Vector, LEFT, RIGHT, DOWN
from cave import Cave


class Rock:

    _blocks: Set[Vector]

    def __init__(self, blocks: Iterable[Vector], name: str = None):
        self._blocks = set(blocks)
        self._name = name

    def copy(self) -> "Rock":
        return Rock(self._blocks, self._name)

    @property
    def name(self) -> str:
        return self._name

    def __iter__(self) -> Iterable[Vector]:
        return iter(self._blocks)

    def translate(self, vector: Vector, cave: Cave = None) -> bool:
        cave = cave if cave else set()
        blocks = set()
        for block in map(lambda v: v + vector, self._blocks):
            if block in cave:
                return False
            else:
                blocks.add(block)
        self._blocks = blocks
        return True

    def __repr__(self):
        min_x = min(map(lambda b: b.x, self._blocks))
        max_x = max(map(lambda b: b.x, self._blocks))
        min_y = min(map(lambda b: b.y, self._blocks))
        max_y = max(map(lambda b: b.y, self._blocks))

        repr = []
        for y in range(min_y, max_y + 1):
            line = []
            for x in range(min_x, max_x + 1):
                if Vector(x, y) in self._blocks:
                    line.append("@")
                else:
                    line.append(" ")
            repr.append("".join(line))
        return "\n" + "\n".join(repr)

    def render(self):
        if not self._blocks:
            return ""
        min_y = min(map(lambda b: b.y, self._blocks))
        max_y = max(map(lambda b: b.y, self._blocks))
        repr = []
        for y in range(min_y, max_y + 1):
            line = ['|']
            for x in range(0, 7):
                if Vector(x, y) in self._blocks:
                    line.append("#")
                else:
                    line.append(".")
            line.append("|")
            repr.append("".join(line))
        return "\n" + "\n".join(repr)


H_LINE = Rock([
    Vector(0, 0),
    Vector(1, 0),
    Vector(2, 0),
    Vector(3, 0),
], "H_LINE")

V_LINE = Rock([
    Vector(0, -3),
    Vector(0, -2),
    Vector(0, -1),
    Vector(0, 0),
], "V_LINE")

BOX = Rock([
    Vector(0, -1),
    Vector(1, -1),
    Vector(0, 0),
    Vector(1, 0),
], "BOX")

PLUS = Rock([
    Vector(1, -2),
    Vector(0, -1),
    Vector(1, -1),
    Vector(2, -1),
    Vector(1, 0),
], "PLUS")

ANGLE = Rock([
    Vector(2, -2),
    Vector(2, -1),
    Vector(0, 0),
    Vector(1, 0),
    Vector(2, 0),
], "ANGLE")

