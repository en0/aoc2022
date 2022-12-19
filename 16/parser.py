import re
from aocfw import StringParser


REXP = re.compile(r"Valve (\w*) has flow rate=(\d*); tunnels? leads? to valves? ([\w, ]*)")


class Parser(StringParser):

    def parse(self, data):
        for line in super().parse(data):
            matches = REXP.match(line)
            a, b, c = matches.groups()
            yield a, int(b), c.split(", ")

