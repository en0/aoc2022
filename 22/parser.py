import re
from typing import IO, Iterable
from aocfw import IParser

RE_MOVES = re.compile(r"(\d*)?([R,L]?)")

class Parser(IParser):
    def parse(self, data: IO) -> Iterable[str]:
        tiles = []
        for y, line in enumerate(map(lambda x: str(x).rstrip('\n'), data), start=1):
            if not line:
                break
            for x, char in enumerate(line, start=1):
                tiles.append((x, y, char))
        yield tiles

        moves = []
        for m in RE_MOVES.finditer(next(data)):
            for _m in m.groups():
                if _m in {"R", "L"}:
                    moves.append(("turn", _m))
                elif _m:
                    moves.append(("travel", int(_m)))
        yield moves

