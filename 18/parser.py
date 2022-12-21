from aocfw import StringParser


class Parser(StringParser):

    def parse(self, data):
        for line in super().parse(data):
            yield tuple(map(int, line.split(',')))
