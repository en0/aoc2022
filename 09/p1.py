from typing import Iterable
from aocfw import SolutionBase, IParser
from parser import MovementParser
from vector import Vector


class Solution(SolutionBase):

    bindings = {IParser: MovementParser}

    def __init__(self) -> None:
        self.head = Vector(0, 0)
        self.tail = Vector(0, 0)
        self.last_head = Vector(0, 0)
        self.tail_visited = set()

    def solve(self, data: Iterable[int]) -> int:
        for d, v in data:
            self.move_rope(d, v)
        return len(self.tail_visited)

    def move_rope(self, d, v) -> None:
        for _ in range(v):
            self.move_head(Vector.from_direction(d))
            self.adjust_tail()
            self.record_tail()

    def move_head(self, vector: Vector) -> None:
        self.last_head = self.head
        self.head += vector

    def adjust_tail(self) -> None:
        if self.tail not in self.head.get_nearby_positions() + [self.head]:
            self.tail = self.last_head

    def record_tail(self) -> None:
        self.tail_visited.add(self.tail)

if __name__ == '__main__':
    Solution.run(source='input.txt')
