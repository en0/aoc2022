from typing import List
from common import Point, point_range


AIR = 0
ROCK = 1
SAND = 2


class Space:

    def __init__(self):
        self._grid = {}
        self._y_of_no_return = 0
        self.overflow = False

    def add_lines(self, points: List[Point]):
        for i, b in enumerate(points[1:], start=1):
            a = points[i - 1]
            for point in point_range(a, b):
                self._y_of_no_return = max(self._y_of_no_return, point[1])
                self._grid[point] = ROCK

    def drop_sand(self, point: Point):
        if self.get_val(point) != AIR:
            raise Exception("That shouldn't happen: %s", point)
        x, y = point
        while self.get_val((x, y+1)) == AIR:
            if y > self._y_of_no_return:
                self.overflow = True
                return
            y += 1
        if self.get_val((x-1, y+1)) == AIR:
            self.drop_sand((x-1, y+1))
        elif self.get_val((x+1, y+1)) == AIR:
            self.drop_sand((x+1, y+1))
        else:
            self._grid[(x, y)] = SAND

    def get_val(self, point: Point) -> int:
        return self._grid.get(point, AIR)

    def show(self):

        to_char = lambda v: {AIR: '.', ROCK: '#', SAND: 'o'}[v]
        x1 = min([x for x, _ in self._grid.keys()])
        x2 = max([x for x, _ in self._grid.keys()])
        y1 = min([y for _, y in self._grid.keys()])
        y2 = max([y for _, y in self._grid.keys()])

        for y in range(y1, y2 + 1):
            line = []
            for x in range(x1, x2 + 1):
                v = self.get_val((x, y))
                c = to_char(v)
                line.append(c)
            print("".join(line))

    ## Added for part 2 ##

    def get_val_p2(self, point: Point) -> int:
        if point[1] == self._y_of_no_return + 2:
            return ROCK
        return self._grid.get(point, AIR)

    def drop_sand_p2(self, point: Point):
        if self.get_val_p2(point) != AIR:
            self.overflow = True
            return
        x, y = point
        while self.get_val_p2((x, y+1)) == AIR:
            y += 1
        if self.get_val_p2((x-1, y+1)) == AIR:
            self.drop_sand_p2((x-1, y+1))
        elif self.get_val_p2((x+1, y+1)) == AIR:
            self.drop_sand_p2((x+1, y+1))
        else:
            self._grid[(x, y)] = SAND


