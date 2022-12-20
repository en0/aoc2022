from unittest import TestCase, main
from aocfw import TestCaseMixin
from p1 import Solution
from vector import Vector, LEFT, RIGHT, DOWN
from cave import Cave
from rock import Rock


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 3068

    def test_vector(self):
        self.assertEqual(Vector(0, 0) + RIGHT, Vector(1, 0))
        self.assertEqual(Vector(0, 0) + LEFT, Vector(-1, 0))
        self.assertEqual(Vector(0, 0) + DOWN, Vector(0, 1))
        self.assertEqual(Vector(1, 1) + RIGHT, Vector(2, 1))
        self.assertEqual(Vector(1, 1) + LEFT, Vector(0, 1))
        self.assertEqual(Vector(1, 1) + DOWN, Vector(1, 2))
        self.assertEqual(Vector(-1, -1) + RIGHT, Vector(0, -1))
        self.assertEqual(Vector(-1, -1) + LEFT, Vector(-2, -1))
        self.assertEqual(Vector(-1, -1) + DOWN, Vector(-1, 0))

    def test_cave(self):
        cave = Cave(7)
        in_set = [Vector(0, -1), Vector(1, -1), Vector(2, -1), Vector(3, -1)]
        out_set = [Vector(4, -1), Vector(5, -1), Vector(6, -1)]
        out_of_bounds = [Vector(-1, -1), Vector(7, -1), Vector(0, 0)]
        self.assertEqual(cave.height, 0)
        cave.add_blocks(in_set)
        for v in in_set: self.assertTrue(v in cave, f"{v} is not in set")
        for v in out_set: self.assertTrue(v not in cave, f"{v} is in set")
        for v in out_of_bounds: self.assertTrue(v in cave, f"{v} is not in set")
        self.assertEqual(cave.height, -1)
        cave.add_blocks([Vector(0, -100)])
        self.assertEqual(cave.height, -100)

    def test_rock(self):
        rock = Rock([Vector(0, 0)])
        self.assertTrue(rock.translate(Vector(5, -5)))



if __name__ == '__main__':
    main()
