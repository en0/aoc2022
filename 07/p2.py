from typing import Iterable
from aocfw import SolutionBase
from p1 import Solution as P1Solution

class Solution(P1Solution):
    def solve(self, data: Iterable[int]) -> int:
        fs = self.build_filesystem(data)

        total = 70000000
        needed = 30000000
        used = fs.get_node("/").size_of()
        unused = total - used
        delta = needed - unused

        print("TOTAL", total)
        print("NEEDED", needed)
        print("USED", used)
        print("UNUSED", unused)
        print("DELTA", delta)


        ans = total
        for node in fs.walk("/"):
            if node.node_type == "dir" and node.size_of() >= delta:
                ans = min(ans, node.size_of())
        return ans


if __name__ == '__main__':
    Solution.run(source='input.txt')
