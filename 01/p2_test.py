from unittest import TestCase, main
from aocfw import TestCaseMixin
from p2 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 45000


if __name__ == '__main__':
    main()
