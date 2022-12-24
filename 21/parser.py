from typing import IO, Iterable, Callable, Tuple
from aocfw import IParser


class Parser(IParser):
    def parse(self, data: IO) -> Iterable[str]:
        return map(lambda x: str(x).rstrip('\n').split(": "), data)

