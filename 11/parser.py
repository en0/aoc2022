from aocfw import IParser, StringParser
from monkey import Monkey, MonkeyOperation, MonkeyThrowTest


class MonkeyParser(StringParser):
    def parse(self, data):
        spec = []
        for line in super().parse(data):
            if line == "":
                yield self._to_monkey(spec)
                spec = []
                continue
            spec.append(line.strip(" "))
        yield self._to_monkey(spec)

    def _to_monkey(self, spec):
        operation = MonkeyOperation(*spec[2][len('Operation: new = '):].split(' '))
        throw_test = MonkeyThrowTest(int(spec[3][len('Test: divisible by '):]))
        return Monkey(
            name=spec[0][:-1],
            starting_items=[int(x) for x in spec[1][len('Starting items: '):].split(',')],
            operation=operation,
            throw_test=throw_test,
            targets=(
                int(spec[4][len("If true: throw to monkey "):]),
                int(spec[5][len("If false: throw to monkey "):])
            )
        )
