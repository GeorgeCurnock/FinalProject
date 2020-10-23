from pentago import player as p
from pentago import board as b
import numpy as np


class RandomPlayer(p.Player):

    def play(self, board):
        valid_move = False

        # Place a stone on the board
        while not valid_move:
            x, y = [np.random.randint(0, 6) for _ in range(2)]
            if board.get_grid_value(x, y) == b.BoardTile.EMPTY.value:
                print("RP placing at " + str(x) + ", " + str(y))
                board.place_stone(x, y, self.colour)
                valid_move = True

        # Rotate a quadrant
        quad = np.random.randint(0, 4)
        direction = np.random.randint(0, 2)
        print("RP rotating quad " + str(quad) + " in direction " + str(direction))
        board.rotate_quadrant(quad, direction)
