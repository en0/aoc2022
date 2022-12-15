from aocfw import StringParser
from typing import Iterable, IO
from common import Point


class LineParser(StringParser):

    def parse(self, data: IO) -> Iterable[Point]:
        for line in super().parse(data):
            yield [tuple(map(int, p.split(','))) for p in line.split(' -> ')]

