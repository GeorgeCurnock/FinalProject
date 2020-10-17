from pentago import player as p
from pentago import board as b


class HumanPlayer(p.Player):

    def play(self, board):
        valid_move = False

        # Place a stone on the board
        while not valid_move:
            x, y = [int(x) for x in input("Enter the coordinates to play (x, y): ").split(',')]
            if board.getGridValue(x - 1, y - 1) == b.BoardTile.EMPTY.value:
                board.placeStone(x - 1, y - 1, self.colour)
                valid_move = True
            else:
                print("Invalid play. Please choose again!")

        # Rotate a quadrant
        quad = 0
        while (quad != 0) and (quad != 1) and (quad != 2) and (quad != 3):
            quad = int(input("Which quadrant (0, 1, 2 or 3) to rotate? "))

        direction = 0
        while direction != 0 and direction != 1:
            direction = input("Which direction to rotate: clockwise(0) or anti-clockwise(1)? ")

        board.rotateQuadrant(quad, direction)
