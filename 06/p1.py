from typing import Iterable
from aocfw import SolutionBase, IParser, StringParser
from collections import deque


class Solution(SolutionBase):

    bindings = {IParser: StringParser}
    offset = 3

    def solve(self, data: Iterable[str]) -> int:
        data = next(data)
        buffer = deque(data[:self.offset])
        for i, c in enumerate(data[self.offset:]):
            buffer.append(c)
            if len(buffer) > self.offset + 1:
                buffer.popleft()
            if len(set(buffer)) == self.offset + 1:
                return i + self.offset + 1
        raise Exception("No sequence detected.")


if __name__ == '__main__':
    Solution.run(source='input.txt')
