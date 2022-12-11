from typing import Iterable, List
from aocfw import SolutionBase, IParser
from parser import MonkeyParser
from pprint import pprint as pp
from monkey import Monkey, ModuloWRS


class Solution(SolutionBase):

    bindings = {IParser: MonkeyParser}

    def __init__(self):
        self.monkeys: List[Monkey] = []
        self.counts: List[int] = []

    def solve(self, data: Iterable[Monkey]) -> int:

        throw_test_product = 1

        for monkey in data:
            throw_test_product *= monkey.thow_test_divisor
            monkey.add_to_group(self.monkeys)
            self.counts.append(0)

        wrs = ModuloWRS(throw_test_product)

        for monkey in self.monkeys:
            monkey.set_wrs(wrs)

        for _ in range(10000):
            self.execute_round()
        a, b = sorted(self.counts, reverse=True)[:2]
        return a * b

    def execute_round(self):
        for i, monkey in enumerate(self.monkeys):
            self.counts[i] += monkey.take_turn()

    def print_monkeys(self):
        for monkey in self.monkeys:
            print(monkey.to_short_repr())


if __name__ == '__main__':
    Solution.run(source='input.txt')
