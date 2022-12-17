from aocfw import StringParser


class Parser(StringParser):

    def parse(self, data):
        for line in super().parse(data):
            sensor, beacon = line.split(': ', 2)
            yield (
                self.to_xy(sensor[len("Sensor at "):]),
                self.to_xy(beacon[len("closest beacon is at "):]),
            )

    def to_xy(self, text):
        return tuple([int(s.strip()[2:]) for s in text.split(", ")])

