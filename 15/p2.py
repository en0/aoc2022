from typing import Iterable, List, Tuple, Set
from aocfw import SolutionBase, IParser
from sensor import Sensor
from parser import Parser


class Solution(SolutionBase):

    bindings = {IParser: Parser}

    def __init__(self):
        self._sensors: List[Sensor] = []

    def solve(self, data: Iterable[int]) -> int:
        for sensor, beacon in data:
            p = Sensor(sensor, beacon)
            self._sensors.append(p)

        limit = 4000000
        if self._sensors[0].x == 2:
            # This is a sample run
            self.log.info("This is a test run. setting limit to 20")
            limit = 20

        c = dict()
        for s in self._sensors:
            for b in s.get_boarder():
                x, y = b
                if 0 <= x <= limit and 0 <= y <= limit:
                    c.setdefault(b, 0)
                    c[b] += 1

        self.log.debug("I have %s candidates. Check each against all sensors...", len(c))

        for p, _ in sorted(c.items(), key=lambda v: v[1], reverse=True):
            candidate = True
            for s in self._sensors:
                if p in s:
                    self.log.debug("Rejecting candidate! %s", p)
                    candidate = False
                    break
            if candidate:
                x, y = p
                return x * 4000000 + y

if __name__ == '__main__':
    Solution.run(source='input.txt')
