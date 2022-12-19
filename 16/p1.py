from typing import Iterable, List, Set, Deque, Tuple, Dict
from math import inf
from aocfw import SolutionBase, IParser
from parser import Parser
from graph import AdjacencyList
from collections import deque


class Solution(SolutionBase):

    bindings = {IParser: Parser}

    def __init__(self):
        self.graph: AdjacencyList = None
        self.valves: Set[str] = None

    def build_graph(self, data: Iterable):
        self.graph = AdjacencyList()
        self.valves = set()
        for v, w, e in data:
            self.graph.set_vertex_value(v, w)
            [self.graph.add_edge(v, a) for a in e]
            if w > 0:
                self.valves.add(v)

    def solve(self, data: Iterable) -> int:
        ans, path = -inf, None
        self.build_graph(data)
        for _ans, _path in self.search_for_valid_paths():
            if _ans > ans:
                ans = _ans
                path = _path
                self.log.info("%s -> %s", ans, path)
        return ans

    def search_for_valid_paths(self):
        # Incrementally build path values and trim branches that cannot succeed.
        #                 path, val, time, remaining
        stack = deque([ (['AA'], 0, 30, self.valves) ])
        while stack:
            path, value, time, remaining = stack.popleft()
            if time >= 0:
                yield value, path
            if value < 0 or time < 0:
                self.log.debug("Trimming branch: %s -> [%sT%s]", path, value, time)
                continue
            for item in remaining:
                _t, _v = self.compute_target_values(path[-1], item, time)
                _p = path + [item]
                _r = remaining - set([item])
                stack.append((_p, value + _v, _t, _r))

    def compute_target_values(self, current: str, target: str, time: int) -> Tuple[int, int]:
        path = self.graph.get_path(current, target)
        time_after = time - len(path) - 1
        rate = self.graph.get_vertex_value(target)
        value = time_after * rate
        return time_after, value

    def compute_target_path(self, path: List[str]) -> int:
        # Used in dubugging, not in solution
        ans = 0
        time = 30
        for i, target in enumerate(path[1:]):
            current = path[i]
            time, value = self.compute_target_values(current, target, time)
            ans += value
        return ans


if __name__ == '__main__':
    Solution.run(source='input.txt')
