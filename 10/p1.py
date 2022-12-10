from typing import Iterable
from aocfw import SolutionBase, IParser
from parser import InstParser
from emu import Emulator


class Solution(SolutionBase):

    bindings = {IParser: InstParser}

    def solve(self, data: Iterable[int]) -> int:
        emu = Emulator()
        emu.load(data)
        samples = []
        i = 1
        while not emu.done:
            if (i-20) % 40 == 0:
                samples.append(emu.x * i)
            emu.tick()
            i += 1
        return sum(samples)


if __name__ == '__main__':
    Solution.run(source='input.txt')
