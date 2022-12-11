from typing import List, Callable, Tuple
from collections import deque


class MonkeyOperation:

    def __init__(self, a: str, op: str, b: str):
        self.a = a
        self.b = b
        self.op = op

    def __repr__(self) -> str:
        return f"Operation: new = {self.a} {self.op} {self.b}"

    def __call__(self, old: int) -> int:
        return {
            '+': lambda a, b: a + b,
            '*': lambda a, b: a * b,
        }[self.op](
            old if self.a == 'old' else int(self.a),
            old if self.b == 'old' else int(self.b),
        )


class MonkeyThrowTest:

    def __init__(self, divisor: int):
        self.divisor = divisor

    def __repr__(self) -> str:
        return f"Test: divisible by {self.divisor}"

    def __call__(self, worry: int) -> bool:
        return worry % self.divisor == 0


class Monkey:

    def __init__(
        self,
        name: str,
        starting_items: List[int],
        operation: MonkeyOperation,
        throw_test: MonkeyThrowTest,
        targets: Tuple[int, int],
    ) -> None:
        self._name = name
        self._items = deque(starting_items)
        self._operation = operation
        self._test = throw_test
        self._targets = targets
        self._group = None

    def __repr__(self) -> str:
        return "\n".join([
            f"{self._name}",
            f" Starting Items: [{', '.join([str(x) for x in self._items])}]",
            f" {str(self._operation)}",
            f" {str(self._test)}",
            f"  True: Throw to Monkey {self._targets[0]}",
            f"  False: Throw to Monkey {self._targets[1]}",
            ""
        ])

    def to_short_repr(self) -> str:
        return f"{self._name}: {', '.join([str(x) for x in self._items])}"

    def add_to_group(self, group: List["Monkey"]) -> None:
        self._group = group
        group.append(self)

    def receive_item(self, worry: int) -> None:
        self._items.append(worry)

    def take_turn(self):
        counter = len(self._items)
        while self._items:
            item = self._items.popleft()
            item = self._operation(item)
            item //= 3
            if self._test(item):
                self.throw_at(item, self._targets[0])
            else:
                self.throw_at(item, self._targets[1])
        return counter

    def throw_at(self, item, target):
        self._group[target].receive_item(item)
