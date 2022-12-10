from typing import Iterable, NamedTuple
from aocfw import SolutionBase, IParser, StringParser

from pprint import pprint as pp

VALUE = 0
SOUTH = 1
NORTH = 2
EAST = 3
WEST = 4


class Solution(SolutionBase):

    bindings = {IParser: StringParser}

    def __init__(self):
        self.trees = None
        self.visible = None

    def solve(self, data: Iterable[str]) -> int:
        self.load_trees(data)
        self.mark_visible(SOUTH)
        self.rotate()
        self.mark_visible(EAST)
        self.rotate()
        self.mark_visible(NORTH)
        self.rotate()
        self.mark_visible(WEST)
        self.rotate()
        return self.count_visible()

    def count_visible(self):
        ans = 0
        for row in self.visible:
            for tree in row:
                if tree:
                    ans += 1
        return ans

    def mark_visible(self, tag):
        for i, t in enumerate(self.trees[0]):
            t[tag] = t[0]
            self.visible[0][i] = True
        for y, row in enumerate(self.trees[1:], start=1):
            for x, tree in enumerate(row):
                val = self.trees[y-1][x][tag]
                tree[tag] = max(val, tree[0])
                if val < tree[0]:
                    self.visible[y][x] = True

    def rotate(self):
        self.trees = list(zip(*self.trees[::-1]))
        self.visible = [list(l) for l in list(zip(*self.visible[::-1]))]

    def load_trees(self, data: Iterable[str]):
        self.trees = []
        self.visible = []
        for line in data:
            row = []
            v_row = []
            for tree in line:
                row.append([int(tree), 0, 0, 0, 0])
                v_row.append(False)
            self.trees.append(row)
            self.visible.append(v_row)


if __name__ == '__main__':
    Solution.run(source='input.txt')
