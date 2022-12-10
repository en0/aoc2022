from typing import Iterable, NamedTuple,Any, List, Optional, Dict, Union
from aocfw import SolutionBase, IParser
from collections import deque
from parser import TerminalSessionParser, Command, File, Directory
from dataclasses import dataclass


class Node:

    node_type: str
    value: Union[int, None]
    _children: Dict[str, "Node"]

    def __init__(self, node_type: str, value: Optional[int] = None):
        self.node_type = node_type
        self.value = value
        self._children = {}

    def size_of(self) -> int:
        if self.node_type == "file":
            return self.value
        return sum([c.size_of() for c in self._children.values()])

    def list(self) -> List["Node"]:
        return list(self._children.values())

    def get_child(self, name: str) -> None:
        return self._children[name]

    def add_child(self, node_type: str, name: str, value: Optional[int]) -> None:
        self._children[name] = Node(node_type, value)


class FileSystem:

    def __init__(self):
        self._pwd = deque()
        self._root = Node("dir", None)

    def _get_node(self, path: List[str]) -> Node:
        n = self._root
        for p in path:
            n = n.get_child(p)
        return n

    def get_node(self, path: str) -> Node:
        path = path.strip('/')
        if path == "":
            return self._get_node([])
        return self._get_node(path.split("/"))

    def walk(self, path: str) -> Iterable[Node]:
        queue = deque([self.get_node(path)])
        while queue:
            n = queue.pop()
            yield n
            for c in n.list():
                queue.appendleft(c)

    def add_file(self, name: str, size: int):
        n = self._get_node(self._pwd)
        n.add_child("file", name, size)

    def add_dir(self, name: str):
        n = self._get_node(self._pwd)
        n.add_child("dir", name, None)

    def cd(self, name: str = None):
        if name == "/":
            self._pwd = deque()
        elif name == "..":
            self._pwd.pop()
        elif name != ".":
            self.add_dir(name)
            self._pwd.append(name)


class Solution(SolutionBase):

    bindings = {IParser: TerminalSessionParser}

    def solve(self, data: Iterable[int]) -> int:
        fs = self.build_filesystem(data)
        ans = 0
        for node in fs.walk("/"):
            if node.node_type == "dir" and node.size_of() < 100000:
                ans += node.size_of()
        return ans

    def build_filesystem(self, data: Iterable) -> FileSystem:
        fs = FileSystem()
        for line in data:
            if isinstance(line, Command) and line.cmd == 'cd':
                fs.cd(line.args[0] if line.has_args() else None)
            elif isinstance(line, File):
                fs.add_file(line.name, line.size)
            elif isinstance(line, Directory):
                fs.add_dir(line.name)
        return fs


if __name__ == '__main__':
    Solution.run(source='input.txt')
