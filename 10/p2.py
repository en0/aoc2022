from typing import Iterable
from aocfw import SolutionBase, IParser
from parser import InstParser
from emu import Emulator
from crt import CRT


class Solution(SolutionBase):

    bindings = {IParser: InstParser}

    def solve(self, data: Iterable[int]) -> int:
        crt = CRT()
        emu = Emulator()
        emu.load(data)
        while not emu.done:
            crt.draw(emu.x)
            emu.tick()
        crt.show()


if __name__ == '__main__':
    Solution.run(source='input.txt')
