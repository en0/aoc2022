from typing import IO, Iterable
from aocfw import IParser


class Parser(IParser):
    def parse(self, data: IO) -> Iterable[str]:
        return map(lambda x: str(x).rstrip('\n'), data)