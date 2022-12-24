from typing import Iterable
from aocfw import SolutionBase, IParser
from parser import Parser
from p1 import Solution as P1Solution


class Solution(P1Solution):

    def solve(self, data: Iterable[int]) -> int:

        exprs = {name: self.to_expr(expr) for name, expr in map(self.patch, data)}

        last_humn, humn = 0, 0
        exprs["humn"] = lambda d:humn
        val = exprs["root"](exprs)
        i, m = 0, int(val)

        while True:

            val = exprs["root"](exprs)
            self.log.debug(
                "%s == %s : i=%s, m=%s",
                str(val).ljust(20),
                str(humn).ljust(20),
                str(i).ljust(5),
                str(m).ljust(5)
            )

            if val == 0:
                break
            elif val < 0:
                i = 0
                m = max(m//2, 1)
                humn = last_humn
            else:
                last_humn = humn

            i += 1
            humn += i*m

        return humn

    def patch(self, entry):
        name, expr = entry
        if name == "root":
            a, _, b = expr.split(" ")
            return name, f"{a} - {b}"
        else:
            return name, expr


if __name__ == '__main__':
    Solution.run(source='input.txt')
