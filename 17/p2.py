from typing import Iterable
from aocfw import SolutionBase
from p1 import Solution as P1Solution


class Solution(P1Solution):
    def solve(self, data: Iterable[int]) -> int:

        self.initialize(data)

        seen = {}
        key_count = -1
        cycles_to_get = 2
        heights = []
        rocks_to_drop = 1000000000000
        padding = 999
        padding_height = 0

        for i in range(rocks_to_drop):
            key = self.move()
            if i < padding:
                padding_height = abs(self._cave.height)
                continue
            if key in seen:
                seen[key] += 1
            else:
                seen[key] = 1
            if len(seen) == key_count and all([seen[key] == v for v in seen.values()]):
                heights.append((i, abs(self._cave.height)))
                self.log.debug("Cycle detected @ %s", i)
                cycles_to_get -= 1
                if cycles_to_get == 0:
                    break
            key_count = len(seen)

        delta_height = heights[1][1] - heights[0][1]
        delta_index = heights[1][0] - heights[0][0]
        rocks_dropped_after_padding = rocks_to_drop - padding
        cycles_to_multiply = rocks_dropped_after_padding // delta_index
        rocks_dropped_in_cycles = cycles_to_multiply * delta_index
        rocks_not_accounted_for = rocks_to_drop - rocks_dropped_in_cycles - padding
        accumulated_height_during_cycles = cycles_to_multiply * delta_height

        # I didn't want to wait for a cycle count divisuble by rocks_to_drop
        diff = abs(self._cave.height)
        for _ in range(rocks_not_accounted_for):
            self.move()
        diff = abs(self._cave.height) - diff

        self.log.info("Rocks dropped after padding = %s", rocks_dropped_after_padding)
        self.log.info("Cycles to account for dropped rocks = %s", cycles_to_multiply)
        self.log.info("Total rocks dropped in %s cycles = %s", cycles_to_multiply, rocks_dropped_in_cycles)
        self.log.info("Rocks not accounted for = %s", rocks_not_accounted_for)
        self.log.info("Height accumulated after cycles =  %s", diff)
        self.log.info("Height accumulated in padding =  %s", padding_height)
        self.log.info("Height accumulated during cycles = %s", accumulated_height_during_cycles)

        return accumulated_height_during_cycles + padding_height + diff


if __name__ == '__main__':
    Solution.run(source='input.txt')
