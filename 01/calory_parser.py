from typing import Iterable, List
from aocfw import StringParser


class CaloryParser(StringParser):

    def parse(self, data) -> Iterable[int]:
        val = 0
        for d in super().parse(data):
            if d:
                val += int(d)
            else:
                yield val
                val = 0
        yield val
