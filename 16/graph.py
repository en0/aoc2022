from typing import Dict, List, Any, Tuple, Set, Iterable, Deque
from collections import deque
from functools import lru_cache


class AdjacencyList:

    def __init__(self) -> None:
        self._adj: Dict[str, Set[str]] = {}
        self._val: Dict[str, Any] = {}

    def __iter__(self) -> Iterable[str]:
        return iter(set(self._adj.keys()) | set(self._val.keys()))

    def add_edge(self, a, b) -> None:
        self._adj.setdefault(a, set()).add(b)
        self._adj.setdefault(b, set()).add(a)

    def set_vertex_value(self, v: str, value: Any) -> None:
        self._val[v] = value

    def get_vertex_value(self, v: str) -> Any:
        return self._val.get(v, 0)

    def get_adjacent(self, v) -> List[Tuple[str, Any]]:
        return self._adj.get(v, [])

    def get_path(self, a, b) -> List[str]:
        # These graphs are small so i am going to
        # be lazy and just use a bredth-first-search
        visited: Set[str] = set()
        queue: Deque[Tuple[str, List[str]]] = deque([(a, [])])
        while queue:
            c, p = queue.popleft()
            visited.add(c)
            p.append(c)
            if c == b:
                return p[1:]
            for a in self.get_adjacent(c):
                if a not in visited:
                    queue.append((a, list(p)))

