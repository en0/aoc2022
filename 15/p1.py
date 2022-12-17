from typing import Iterable, List, Tuple, Set
from aocfw import SolutionBase, IParser
from sensor import Sensor
from parser import Parser


class Solution(SolutionBase):

    bindings = {IParser: Parser}

    def __init__(self):
        self._sensors: List[Sensor] = []
        self._beacons: Set[Tuple[int, int]] = set()
        self._min_x = None
        self._max_x = None
        self._y = 2000000

    def solve(self, data: Iterable[int]) -> int:
        for sensor, beacon in data:
            p = Sensor(sensor, beacon)
            self._sensors.append(p)
            self._beacons.add(beacon)

            min_x, _ = p.min
            max_x, _ = p.max

            if self._min_x == None:
                self._min_x = min_x

            if self._max_x == None:
                self._max_x = max_x

            self._min_x = min(min_x, self._min_x)
            self._max_x = max(max_x, self._max_x)

        if self._sensors[0].x == 2:
            # This is a sample run
            self.log.info("This is a test run. setting Y to 10")
            self._y = 10

        poi = set()
        # This is going to be slow
        for x in range(self._min_x, self._max_x):
            for sensor in self._sensors:
                if (x, self._y) in sensor and (x, self._y) not in self._beacons:
                    poi.add((x, self._y))
        return len(poi)


if __name__ == '__main__':
    Solution.run(source='input.txt')
