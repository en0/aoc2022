class Sensor:

    def __init__(self, sensor, beacon):
        self._loc = sensor
        self._dist = self._distance_between(sensor, beacon)
        self._border = None

    def _distance_between(self, a, b):
        (x1, y1), (x2, y2) = a, b
        return abs(x1 - x2) + abs(y1 - y2)

    def __repr__(self):
        return f"{self._loc}"

    def __contains__(self, val):
        delta = self._distance_between(self._loc, val)
        return delta <= self._dist

    @property
    def x(self):
        return self._loc[0]

    @property
    def max(self):
        x, y = self._loc
        return (x + self._dist, y + self._dist)

    @property
    def min(self):
        x, y = self._loc
        return (x - self._dist, y - self._dist)

    ## Added for part 2

    def get_boarder(self):
        if self._border is None:
            self._border = list(self._compute_border())
        return self._border

    def _compute_border(self):
        x, y = self._loc
        b1y = y - self._dist - 1
        b2y = y + self._dist + 1
        b1x, b2x = x, x
        yield x, b1y
        yield x, b2y
        while y != b1y:
            b1y += 1
            b2y -= 1
            b1x += 1
            b2x -= 1
            yield b1x, b1y
            yield b2x, b1y
            if b1y != b2y:
                yield b1x, b2y
                yield b2x, b2y
