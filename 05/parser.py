from typing import Generator, Dict, Tuple, Deque, Iterable
from aocfw import StringParser
from itertools import zip_longest
from collections import deque
from re import compile as re_compile


MoveTuple = Tuple[int, int, int]
Stacks = Dict[int, Deque[str]]


class StackParser(StringParser):

    def __init__(self):
        self._re_move = re_compile(r'move\ (\d*)\ from (\d*)\ to (\d*)')

    def parse(self, data) -> Generator[Stacks, MoveTuple, MoveTuple]:
        data = super().parse(data)
        yield self.parse_stacks(data)
        yield from self.parse_moves(data)

    def parse_stacks(self, data) -> Stacks:
        stacks = {}
        for line in data:
            if line == '':
                break
            for i, block in enumerate(self.chunks(4, line, ' ')):
                block = block.strip(" ")
                if block:
                    stacks.setdefault(i+1, deque()).append(block)
        return stacks

    def chunks(self, count, data, fillvalue) -> Iterable[str]:
        # Using simplifed version of grouper from itertools docs
        args = [iter(data)] * count
        return map("".join, zip_longest(fillvalue=fillvalue, *args))

    def parse_moves(self, data) -> Iterable[MoveTuple]:
        for move in data:
            m = self._re_move.match(move)
            yield map(int, m.groups())
