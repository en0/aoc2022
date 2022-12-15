from typing import List, Tuple, Iterable


Point = Tuple[int, int]


def point_range(a: Point, b: Point) -> Iterable[Point]:
    (x1, y1), (x2, y2) = a, b
    for y in range(min(y1, y2), max(y1, y2) + 1):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            yield x, y
