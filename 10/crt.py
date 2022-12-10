class CRT:

    def __init__(self):
        self.buffer = [' ']*40*6
        self.p = 0

    def draw(self, x):
        v = self.p % 40
        if v in [x-1, x, x+1]:
            self.buffer[self.p] = '#'
        else:
            self.buffer[self.p] = '-'
        self.p = (self.p+1) % len(self.buffer)

    def show(self):
        line = []
        for i, v in enumerate(self.buffer):
            if i % 40 == 0:
                print("".join(line))
                line = []
            line.append(v)
        print("".join(line))
