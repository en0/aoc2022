from aocfw import StringParser


class MapParser(StringParser):

    def parse(self, data):
        ret = {}
        start = None
        end = None
        for y, line in enumerate(super().parse(data)):
            for x, char in enumerate(line):
                if char == "S":
                    start = (x, y)
                    ret[(x, y)] = ord('a')
                elif char == "E":
                    end = (x, y)
                    ret[(x, y)] = ord('z')
                else:
                    ret[(x, y)] = ord(char)
        yield ret
        yield start
        yield end

