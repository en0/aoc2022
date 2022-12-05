from typing import Generator
from aocfw import SolutionBase, IParser
from parser import StackParser, Stacks, MoveTuple


class Solution(SolutionBase):

    bindings = {IParser: StackParser}

    def solve(self, data: Generator[Stacks, MoveTuple, MoveTuple]) -> int:
        stacks = next(data)
        for count, source, dest in data:
            for i in range(count):
                stacks[dest].appendleft(stacks[source].popleft())

        return "".join([stacks[k][0][1] for k in sorted(stacks.keys())])


if __name__ == '__main__':
    Solution.run(source='input.txt')
