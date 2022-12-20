from typing import NamedTuple


class Vector(NamedTuple):

    x: int
    y: int

    def __add__(self, other: "Vector") -> "Vector":
        _x, _y = other
        return Vector(
            x=self.x + _x,
            y=self.y + _y,
        )

    def __repr__(self):
        if self == Vector(-1, 0):
            return "<LEFT>"
        if self == Vector(1, 0):
            return "<RIGHT>"
        if self == Vector(0, 1):
            return "<DOWN>"
        return f"<{self.x}, {self.y}>"

LEFT = Vector(-1, 0)
RIGHT = Vector(1, 0)
DOWN = Vector(0, 1)

