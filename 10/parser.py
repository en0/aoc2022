from aocfw import StringParser


class InstParser(StringParser):
    def parse(self, data):
        for x in super().parse(data):
            i, *a = x.split(' ')
            yield i, int(a[0]) if a else None
