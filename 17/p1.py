import rock
from typing import Iterable, Iterator
from aocfw import SolutionBase, IParser
from cave import Cave
from vector import Vector, DOWN
from parser import Parser


class Solution(SolutionBase):

    bindings = { IParser: Parser }

    def __init__(self):
        self._cave = Cave(7)
        self._moves: Iterator[Vector] = None
        self._peices: Iterator[Rock] = None
        self._last_peice_index: int = None
        self._last_move_index: int = None

    def solve(self, data: Iterable[int]) -> int:
        self.initialize(data)
        for i in range(2022):
            self.move()
        self.log.debug("Cave State:%s", self._cave.render())
        return abs(self._cave.height)

    def move(self):
        _peice = self.next_peice()
        spawn_point = Vector(2, self._cave.height - 4)
        _peice.translate(spawn_point)
        while True:
            _move = self.next_move()
            _peice.translate(_move, self._cave)
            if not _peice.translate(DOWN, self._cave):
                return self._cave.add_blocks(_peice)

    def initialize(self, data: Iterable) -> None:
        def move_generator():
            _moves = list(data)
            while True:
                for i, move in enumerate(_moves):
                    self._last_move_index = i
                    yield move
        def peice_generator():
            _peices = [rock.H_LINE, rock.PLUS, rock.ANGLE, rock.V_LINE, rock.BOX]
            while True:
                for i, peice in enumerate(_peices):
                    self._last_peice_index = i
                    yield peice.copy()
        self._moves = move_generator()
        self._peices = peice_generator()

    def next_move(self):
        return next(self._moves)

    def next_peice(self):
        return next(self._peices)


if __name__ == '__main__':
    Solution.run(source='input.txt')
