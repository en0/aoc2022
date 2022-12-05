from typing import Generator
from aocfw import SolutionBase, IParser
from parser import StackParser, Stacks, MoveTuple


class Solution(SolutionBase):

    bindings = {IParser: StackParser}

    def solve(self, data: Generator[Stacks, MoveTuple, MoveTuple]) -> int:
        stacks = next(data)
        for count, source, dest in data:
            buffer = []
            for i in range(count):
                block = stacks[source].popleft()
                buffer.append(block)
            for block in reversed(buffer):
                stacks[dest].appendleft(block)
        return "".join([stacks[k][0][1] for k in sorted(stacks.keys())])


if __name__ == '__main__':
    Solution.run(source='input.txt')
