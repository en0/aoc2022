from typing import IO, Iterable
from aocfw import IParser


class Parser(IParser):
    def parse(self, data: IO) -> Iterable[int]:
        return map(int, map(str, data))
