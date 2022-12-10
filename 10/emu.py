from collections import deque


class Emulator:

    def __init__(self):
        self.instuction_map = {
            "noop": self.noop,
            "addx": self.addx,
        }
        self.done = False
        self.prog = []
        self.pipeline = deque()
        self.x = 1
        self.ip = 0

    def noop(self, args):
        self.add_to_pipline(lambda:None)

    def addx(self, args):
        def _addx():
            self.x += args
        self.add_to_pipline(lambda:None)
        self.add_to_pipline(_addx)

    def load_inst(self):
        try:
            inst, args = self.prog[self.ip]
        except IndexError:
            self.done = True
        else:
            self.ip += 1
            hdlr = self.instuction_map[inst]
            hdlr(args)

    def load(self, prog):
        self.ip = 0
        self.prog = list(prog)
        self.done = False

    def tick(self):
        if not self.pipeline:
            self.load_inst()
        if not self.done:
            self.from_pipeline()()

    def add_to_pipline(self, fn):
        self.pipeline.append(fn)

    def from_pipeline(self):
        return self.pipeline.popleft()

