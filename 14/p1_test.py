from unittest import TestCase, main
from aocfw import TestCaseMixin
from p1 import Solution
from common import point_range


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = None


class CommonTests(TestCase):

    def test_range_x_pos(self):
        expected = [(3, 0), (4, 0), (5, 0)]
        actual = list(point_range((3, 0), (5, 0)))
        self.assertListEqual(expected, actual)

    def test_range_x_neg(self):
        expected = [(1, 0), (2, 0), (3, 0)]
        actual = list(point_range((3, 0), (1, 0)))
        self.assertListEqual(expected, actual)

    def test_range_y_pos(self):
        expected = [(0, 3), (0, 4), (0, 5)]
        actual = list(point_range((0, 3), (0, 5)))
        self.assertListEqual(expected, actual)

    def test_range_y_neg(self):
        expected = [(0, 1), (0, 2), (0, 3)]
        actual = list(point_range((0, 3), (0, 1)))
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    main()
