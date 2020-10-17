from pentago import player as p
from pentago import board as b
import numpy as np


class RandomPlayer(p.Player):

    def play(self, board):
        valid_move = False

        # Place a stone on the board
        while not valid_move:
            x, y = [np.random.randint(0, 6) for _ in range(2)]
            if board.getGridValue(x - 1, y - 1) == b.BoardTile.EMPTY.value:
                board.placeStone(x - 1, y - 1, self.colour)
                valid_move = True

        # Rotate a quadrant
        quad = 0
        while (quad != 0) and (quad != 1) and (quad != 2) and (quad != 3):
            quad = np.random.randint(0, 4)

        direction = 0
        while direction != 0 and direction != 1:
            direction = np.random.randint(0, 2)

        board.rotateQuadrant(quad, direction)
