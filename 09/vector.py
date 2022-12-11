from typing import NamedTuple, Tuple, List


class Vector(NamedTuple):

    x: int
    y: int

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def get_nearby_positions(self) -> List["Vector"]:
        return [
            self + Vector.from_direction("U"),
            self + Vector.from_direction("D"),
            self + Vector.from_direction("L"),
            self + Vector.from_direction("R"),
            self + Vector.from_direction("UL"),
            self + Vector.from_direction("UR"),
            self + Vector.from_direction("DL"),
            self + Vector.from_direction("DR"),
        ]

    @staticmethod
    def from_tuple(self, vec: Tuple[int, int]) -> "Vector":
        return Vector(*vec)

    @staticmethod
    def from_direction(direction: str) -> "Vector":
        return {
            "U": Vector(0, -1),
            "D": Vector(0, 1),
            "L": Vector(-1, 0),
            "R": Vector(1, 0),
            "UL": Vector(-1, -1),
            "UR": Vector(1, -1),
            "DL": Vector(-1, 1),
            "DR": Vector(1, 1),
        }[direction]

