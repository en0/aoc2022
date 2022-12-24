from typing import Iterable, Tuple, Callable
from aocfw import SolutionBase, IParser
from parser import Parser


class Solution(SolutionBase):

    bindings = {IParser: Parser}

    def solve(self, data: Iterable) -> int:
        exprs = {name: self.to_expr(expr) for name, expr in data}
        return exprs["root"](exprs)

    def to_expr(self, expr: str) -> Tuple[str, Callable[[], int]]:
        a, *expr = expr.split(" ")
        if not expr:
            return lambda d:int(a)
        op, b = expr
        if op == "+":
            return lambda d:d[a](d) + d[b](d)
        elif op == "-":
            return lambda d:d[a](d) - d[b](d)
        elif op == "*":
            return lambda d:d[a](d) * d[b](d)
        elif op == "/":
            return lambda d:d[a](d) / d[b](d)


if __name__ == '__main__':
    Solution.run(source='input.txt')
