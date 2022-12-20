import vector
from aocfw import StringParser


class Parser(StringParser):
    def parse(self, data):
        line = next(super().parse(data))
        for c in line:
            if c == '<':
                yield vector.LEFT
            elif c == '>':
                yield vector.RIGHT
            else:
                raise Exception(f"Unexpected input: {c}")
