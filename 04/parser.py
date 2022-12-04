from aocfw import StringParser


class SetParser(StringParser):

    def parse(self, data):
        for dat in super().parse(data):
            yield tuple(map(self.to_set, dat.split(",")))

    def to_set(self, dat):
        a, b = map(int, dat.split('-'))
        return set(range(a, b + 1))
