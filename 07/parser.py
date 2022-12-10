from typing import NamedTuple, List
from aocfw import IParser, StringParser


class Command(NamedTuple):
    cmd: str
    args: List[str]

    def has_args(self):
        return bool(self.args)

    @classmethod
    def parse(cls, line: str):
        cmd, *args = line[2:].split(' ')
        return cls(cmd, args)


class File(NamedTuple):
    name: str
    size: int

    @classmethod
    def parse(cls, line: str):
        size, name = line.split(' ')
        return cls(name, int(size))


class Directory(NamedTuple):
    name: str

    @classmethod
    def parse(cls, line: str):
        return cls(line[4:])


class TerminalSessionParser(StringParser):

    def parse(self, data):
        for line in super().parse(data):
            if line.startswith("$ "):
                yield Command.parse(line)
            elif line.startswith("dir "):
                yield Directory.parse(line)
            else:
                yield File.parse(line)
