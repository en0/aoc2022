import json
from aocfw import StringParser


class PacketParser(StringParser):

    def parse(self, data):
        pair = []
        for line in super().parse(data):
            if line == "":
                yield pair
                pair = []
            else:
                pair.append(json.loads(line))
        yield pair
