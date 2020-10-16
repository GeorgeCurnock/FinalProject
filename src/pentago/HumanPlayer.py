from pentago import player as p
from pentago import board as b


class HumanPlayer(p.Player):

    def play(self, board):
        validMove = False

        # Place a stone on the board
        while not validMove:
            x, y = [int(x) for x in input("Enter the coordinates to play (x, y): ").split(',')]
            if board.getGridValue(x - 1, y - 1) == b.BoardTile.EMPTY.value:
                board.placeStone(x - 1, y - 1, self.colour)

        # Rotate a quadrant
        quad = 0
        while (quad != 1) and (quad != 2) and (quad != 3) and (quad != 4):
            quad = int(input("Which quadrant (0, 1, 2 or 3) to rotate? "))

        direction = 0
        while direction != 0 and direction != 1:
            direction = input("Which direction to rotate: clockwise(0) or anti-clockwise(1)? ")

        board.rotateQuadrant(quad, direction)
