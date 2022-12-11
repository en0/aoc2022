from aocfw import StringParser


class MovementParser(StringParser):
    def parse(self, data):
        for line in super().parse(data):
            d, v = line.split(' ', 2)
            yield d, int(v)
