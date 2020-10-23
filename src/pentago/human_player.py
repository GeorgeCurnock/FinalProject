from pentago import player as p
from pentago import board as b


class HumanPlayer(p.Player):

    def play(self, board):
        valid_move = False

        # Place a stone on the board
        while not valid_move:
            x, y = 0, 0
            try:
                x, y = [int(x) for x in input("Enter the coordinates to play (x, y): ").split(',')]
            except ValueError:
                print("Invalid play. Please enter 2 coordinates!")
                continue
            if board.get_grid_value(x, y) == b.BoardTile.EMPTY.value:
                board.place_stone(x, y, self.colour)
                valid_move = True
            else:
                print("Invalid play. That coordinate is already filled!")

        board.print_board()
        # Rotate a quadrant
        valid_rotation = False
        quad = 0
        direction = 0
        while not valid_rotation:
            try:
                quad = int(input("Which quadrant (0, 1, 2 or 3) to rotate? "))
            except ValueError:
                print("Please enter a valid quadrant")
                continue
            if (quad != 0) and (quad != 1) and (quad != 2) and (quad != 3):
                print("Invalid quad. Please enter a valid quad: (0, 1, 2 or 3)!")
            else:
                try:
                    direction = int(input("Which direction to rotate: clockwise(0) or anti-clockwise(1)? "))
                except ValueError:
                    print("Please enter a valid direction: clockwise(0) or anti-clockwise(1)")
                    continue
                if (direction != 0) and (direction != 1):
                    print("Invalid direction. Valid directions: clockwise(0) or anti-clockwise(1)")
                else:
                    valid_rotation = True
        board.rotate_quadrant(quad, direction)
        board.print_board()
