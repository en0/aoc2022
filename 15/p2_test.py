from unittest import TestCase, main
from aocfw import TestCaseMixin
from p2 import Solution
from sensor import Sensor


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 56000011

    def test_eight_seven(self):
        s = [Sensor(s, b) for s, b in self.get_parsed_data() if s == (8, 7)][0]
        expected = [
                ( 8, -3),
                ( 7, -2), ( 9, -2),
                ( 6, -1), (10, -1),
                ( 5,  0), (11,  0),
                ( 4,  1), (12,  1),
                ( 3,  2), (13,  2),
                ( 2,  3), (14,  3),
                ( 1,  4), (15,  4),
                ( 0,  5), (16,  5),
                (-1,  6), (17,  6),
                (-2,  7), (18,  7),
                (-1,  8), (17,  8),
                ( 0,  9), (16,  9),
                ( 1, 10), (15, 10),
                ( 2, 11), (14, 11),
                ( 3, 12), (13, 12),
                ( 4, 13), (12, 13),
                ( 5, 14), (11, 14),
                ( 6, 15), (10, 15),
                ( 7, 16), ( 9, 16),
                ( 8, 17),
        ]
        self.assertSetEqual(set(s.get_boarder()), set(expected))

    def test_eight_seven_unique(self):
        s = [Sensor(s, b) for s, b in self.get_parsed_data() if s == (8, 7)][0]
        seen = set()
        for b in s.get_boarder():
            if b in seen:
                self.fail(f"Found {b} more then once!")
            seen.add(b)


if __name__ == '__main__':
    main()
