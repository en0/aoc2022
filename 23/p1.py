from typing import Iterable, Dict
from aocfw import SolutionBase, IParser
from parser import Parser
from elf import Point, Elf


class Solution(SolutionBase):

    bindings = {IParser: Parser}
    elves: Dict[Point, Elf]

    def solve(self, data: Iterable) -> int:
        self.load_data(data)
        self.print_field("INITIAL STATE")

        for i in range(10):
            print(self.move())
            self.print_field(f"End of round {i+1}")
        return self.count_empty()

    def move(self):
        props: Dict[Point, Elf] = {}
        for elf in self.elves.values():
            point = elf.propose(self.elves)
            if point:
                props.setdefault(point, []).append(elf)
        if props:
            [e[0].move() for e in props.values() if len(e) == 1]
            self.elves = {e.get_pos(): e for e in self.elves.values()}
        return len(props)

    def load_data(self, data: Iterable) -> None:
        self.elves: Dict[Point, Elf] = {}
        for x, y, d in filter(lambda x: x[2] == '#', data):
            pos = (x, y)
            self.elves[pos] = Elf(pos)

    def count_empty(self):
        min_x = min([k[0] for k in self.elves.keys()])
        max_x = max([k[0] for k in self.elves.keys()])
        min_y = min([k[1] for k in self.elves.keys()])
        max_y = max([k[1] for k in self.elves.keys()])
        ans = 0
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if (x, y) not in self.elves:
                    ans += 1
        return ans

    def print_field(self, label):
        min_x = min([k[0] for k in self.elves.keys()])
        max_x = max([k[0] for k in self.elves.keys()])
        min_y = min([k[1] for k in self.elves.keys()])
        max_y = max([k[1] for k in self.elves.keys()])
        self.log.info("== %s ============", label)
        for y in range(min_y, max_y + 1):
            line = []
            for x in range(min_x, max_x + 1):
                line.append("." if (x, y) not in self.elves else "#")
            self.log.info("".join(line))


if __name__ == '__main__':
    Solution.run(source='input.txt')
