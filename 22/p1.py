from typing import Iterable, Dict, Tuple, Union, List
from aocfw import SolutionBase, IParser
from parser import Parser
from board import Board, Player, EMPTY, WALL, OPEN


class Solution(SolutionBase):

    bindings = {IParser: Parser}
    board: Board
    player: Player
    moves: List[Union[str, int]]


    def solve(self, data: Iterable[int]) -> int:
        self.load_data(data)
        self.set_player_spawn()
        for op, move in self.moves:
            if op == "turn":
                self.turn_player(move)
            elif op == "travel":
                self.move_player(move)
        return self.player.get_password()

    def load_data(self, data) -> None:
        self.board = Board({(x, y): t for x, y, t in next(data)})
        self.moves = next(data)
        self.player = Player()

    def set_player_spawn(self) -> None:
        pos = (1, 1)
        while self.board.get_tile(pos) != OPEN:
            pos = (pos[0] + 1, pos[1])
        self.log.info("Set player spawn: %s", pos)
        self.player.set_position(pos)

    def turn_player(self, direction) -> None:
        p = str(self.player)
        self.player.turn(direction)
        self.log.info("Turning player %s: %s : %s", direction, p, self.player)

    def move_player(self, distance) -> None:
        p = str(self.player)
        for i in range(distance):

            target = self.player.get_forward_position()
            tile = self.board.get_tile(target)

            if tile == EMPTY:
                d = 1
                while self.board.get_tile(self.player.get_backward_position(d)) != EMPTY:
                    target = self.player.get_backward_position(d)
                    d += 1
                tile = self.board.get_tile(target)

            if tile == OPEN:
                self.player.set_position(target)
            elif tile == WALL:
                break;
        self.log.info("Moving player %s: %s : %s", distance, p, self.player)


if __name__ == '__main__':
    Solution.run(source='input.txt')
