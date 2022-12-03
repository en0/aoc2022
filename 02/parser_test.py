from unittest import TestCase
from parser import RPCParser


class ParserTest(TestCase):
    def test_parser(self):
        source = [
            "A Y\n",
            "B X\n",
            "C Z\n",
        ]

        parser = RPCParser()
        result = list(parser.parse(source))

        self.assertListEqual([(1, 2), (2, 1), (3, 3)], result)
