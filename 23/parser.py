from typing import IO, Iterable
from aocfw import IParser


class Parser(IParser):
    def parse(self, data: IO) -> Iterable[str]:
        data = map(lambda x: str(x).rstrip('\n'), data)
        for y, line in enumerate(data):
            for x, c in enumerate(line):
                yield x, y, c
