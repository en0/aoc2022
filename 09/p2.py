from typing import Iterable
from aocfw import SolutionBase, IParser
from parser import MovementParser
from vector import Vector


class Solution(SolutionBase):

    bindings = {IParser: MovementParser}

    def __init__(self) -> None:
        self.rope = [Vector(0, 0)]*10
        self.tail_visited = set()
        # Set this to 0, 1, or 2 to get more detail
        self.verbosity = 0
        self.debug = False

    def draw_field(self, verbosity: int):
        if verbosity < self.verbosity:
            print("")
            for y in range(-15, 6):
                line = []
                for x in range(-11, 15):
                    v = '.'
                    for i, p in enumerate(self.rope):
                        if p == Vector(x, y) and v == '.':
                            v = i if i != 0 else 'H'
                    line.append(f' {v} ')
                print("".join(line))

    def record_tail(self) -> None:
        v = self.rope[-1]
        self.tail_visited.add(v)

    def solve(self, data: Iterable[int]) -> int:
        self.draw_field(verbosity=0)
        for d, v in data:
            if self.debug:
                input(f"MOVE {d} {v} times >")
            self.move_rope(d, v)
            self.draw_field(verbosity=0)
        return len(self.tail_visited)

    def move_rope(self, d: str, v: int) -> None:
        for _ in range(v):
            self.move_one_step(d)
            self.record_tail()
            self.draw_field(verbosity=1)

    def move_one_step(self, d) -> None:
        p_last_pos = self.rope[0]
        self.rope[0] += Vector.from_direction(d)
        for i in range(1, len(self.rope)):
            c_last_pos = self.rope[i]
            self.rope[i] += self.find_vector(self.rope[i-1], p_last_pos, self.rope[i])
            p_last_pos = c_last_pos

    def find_vector(self, current_head, last_head, current_tail) -> Vector:
        if current_tail in current_head.get_nearby_positions() + [current_head]:
            return Vector(0, 0)
        head_vector = current_head - last_head
        tail_vector = current_head - current_tail
        if head_vector.x == 0 or head_vector.y == 0:
            return last_head - current_tail
        elif tail_vector.x == 0 or tail_vector.y == 0:
            return Vector(
                max(min(tail_vector.x, 1), -1),
                max(min(tail_vector.y, 1), -1)
            )
        else:
            return current_head - last_head


if __name__ == '__main__':
    Solution.run(source='sample2.txt')
