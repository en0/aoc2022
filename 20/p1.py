from typing import Iterable, List
from aocfw import SolutionBase, IParser
from parser import Parser
from dataclasses import dataclass


@dataclass
class LLNode:
    value: int
    next: "LLNode"
    prev: "LLNode"


class Solution(SolutionBase):

    bindings = {IParser: Parser}
    all_nodes = None

    def solve(self, data: Iterable[int]) -> int:
        zero_node = self.load_data(data)
        self.mix()
        return sum(self.get_coords(zero_node))

    def load_data(self, data: Iterable[int]) -> LLNode:
        self.all_nodes = []
        zero_node = None
        for i, dat in enumerate(data):
            node = LLNode(dat, None, None)
            self.all_nodes.append(node)
            if dat == 0:
                zero_node = node
            if i > 0:
                self.all_nodes[i-1].next = self.all_nodes[i]
                self.all_nodes[i].prev = self.all_nodes[i-1]
        self.all_nodes[0].prev = self.all_nodes[-1]
        self.all_nodes[-1].next = self.all_nodes[0]
        return zero_node

    def mix(self, times=1):
        # I added times for part 2
        for j in range(times):
            self.log.info(f"Pass number %s", j + 1)
            for i, node in enumerate(self.all_nodes):
                if i % 100 == 0:
                    self.log.info(f"Processing %s/%s", i+1, len(self.all_nodes))
                self.move_node(node)

    def get_coords(self, zero_node) -> List[int]:
        coords = []
        target = zero_node
        for _ in range(3):
            for _ in range(1000):
                target = target.next
            coords.append(target.value)
        return coords

    def move_node(self, node: LLNode) -> None:

        if node.value == 0:
            return

        # original code for part 1
        val = node.value

        # Optimization for part 2.
        while abs(val) > len(self.all_nodes):
            val = sum(divmod(val, len(self.all_nodes)))

        self.log.debug("Before Moving %s -> %s", node.value, self.nodes_in_order(limit=10))
        for i in range(0, abs(val)):
            nn = node.next
            pn = node.prev
            nn.prev = pn
            pn.next = nn
            if val < 0:
                node.prev = pn.prev
                pn.prev = node
                node.next = pn
                node.prev.next = node
            else:
                node.next = nn.next
                nn.next = node
                node.prev = nn
                node.next.prev = node
        self.log.debug(" After Moving %s -> %s", node.value, self.nodes_in_order(limit=10))

    def nodes_in_order(self, start_at=0, limit=None):
        root = self.all_nodes[start_at]
        out = [root.value]
        node = root.next
        limit = min(limit or len(self.all_nodes), len(self.all_nodes))
        for _ in range(limit - 1):
            out.append(node.value)
            node = node.next
        return out

if __name__ == '__main__':
    Solution.run(source='input.txt')
