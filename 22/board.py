from typing import Tuple
from collections import deque
from logging import getLogger


Direction = int
Point = Tuple[int, int]
Tile = str
Turn = str

EMPTY = " "
WALL = "#"
OPEN = "."

TURN_CW = 'R'
TURN_CCW = 'L'

EAST = 0
SOUTH = 1
WEST = 2
NORTH = 3


class Board:

    def __init__(self, tiles):
        self._points = dict(tiles)

    def get_tile(self, point: Point) -> Tile:
        return self._points.get(point, EMPTY)


class Player:

    def __init__(self) -> None:
        self._facing = deque([EAST, SOUTH, WEST, NORTH])
        self._position = (0, 0)
        self.log = getLogger(self.__class__.__name__)

    def __repr__(self) -> str:
        direction = {
            EAST:  "East ",
            SOUTH: "South",
            WEST:  "West ",
            NORTH: "North",
            }[self.get_direction()]
        return (
            f"Player(dir={direction}, "
            f"pos={self.get_position()}), "
            f"pos_forward={self.get_forward_position()}"
        )

    def turn(self, d: Turn) -> None:
        p = str(self)
        if d == TURN_CW:
            self._facing.rotate(-1)
        elif d == TURN_CCW:
            self._facing.rotate(1)
        self.log.debug(
            "Turning player (%s): %s : %s",
            {TURN_CCW: "CCW", TURN_CW: "CW "}[d],
            p, self)

    def get_forward_position(self) -> Point:
        x, y = self.get_position()
        return {
            EAST: (x+1, y),
            SOUTH: (x, y+1),
            WEST: (x-1, y),
            NORTH: (x, y-1),
        }[self.get_direction()]

    def get_backward_position(self, distance: int) -> Point:
        x, y = self.get_position()
        return {
            EAST: (x-distance, y),
            SOUTH: (x, y-distance),
            WEST: (x+distance, y),
            NORTH: (x, y+distance),
        }[self.get_direction()]

    def get_position(self) -> Point:
        return self._position

    def set_position(self, value: Point) -> None:
        self.log.debug("Set player position: %s : %s", self._position, value)
        self._position = value

    def get_direction(self) -> Direction:
        return self._facing[0]

    def get_password(self) -> int:
        x, y = self.get_position()
        r = self.get_direction()
        return sum([1000 * y, 4 * x, r])
