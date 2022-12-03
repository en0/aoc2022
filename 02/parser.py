from typing import Tuple, Iterable, IO
from aocfw import StringParser


class RPCParser(StringParser):

    def parse(self, data: IO) -> Iterable[Tuple[str, str]]:
        return map(self.decode, super().parse(data))

    def decode(self, datum: str) -> Tuple[str, str]:
        return tuple(map(self.value_of, datum.split(" ", 2)))

    def value_of(self, move) -> int:
        return {
            "A": 1, "B": 2, "C": 3,
            "X": 1, "Y": 2, "Z": 3,
        }[move]

