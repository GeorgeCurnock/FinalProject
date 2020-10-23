import enum

import numpy as np


class BoardTile(enum.Enum):
    EMPTY = 0
    WHITE = 1
    BLACK = 2


class BoardQuad(enum.Enum):
    TOPLEFT = 0
    TOPRIGHT = 1
    BOTTOMLEFT = 2
    BOTTOMRIGHT = 3


class BoardDirection(enum.Enum):
    CLOCKWISE = 0
    ANTICLOCKWISE = 1


class Board:
    def __init__(self):
        self.matrix = np.full((6, 6), BoardTile.EMPTY.value, dtype=BoardTile)

    def set_grid_value(self, x, y, value):
        self.matrix[y][x] = value

    def get_grid_value(self, x, y):
        return self.matrix[x][y]

    def place_stone(self, x, y, value):
        if self.matrix[y][x] is BoardTile.EMPTY.value:
            self.set_grid_value(x, y, value)

    def rotate_quadrant(self, quad, direction):
        startx, starty = 0, 0
        endx, endy = 6, 6
        direct = 0
        if quad == BoardQuad.TOPLEFT.value:
            print("Rotating Top Left")
            startx = 0
            starty = 0
            endx = 3
            endy = 3
        elif quad == BoardQuad.TOPRIGHT.value:
            startx = 3
            starty = 0
            endx = 6
            endy = 3
        elif quad == BoardQuad.BOTTOMLEFT.value:
            startx = 0
            starty = 3
            endx = 3
            endy = 6
        elif quad == BoardQuad.BOTTOMRIGHT.value:
            startx = 3
            starty = 3
            endx = 6
            endy = 6
        else:
            print("Rotation stage not reached")

        quadrant = self.matrix[starty:endy, startx:endx]
        if direction == BoardDirection.CLOCKWISE.value:
            direct = -1
        elif direction == BoardDirection.ANTICLOCKWISE.value:
            direct = 1
        quadrant = np.rot90(quadrant, direct)
        self.matrix[starty:endy, startx:endx] = quadrant

    def game_end(self):
        diag1 = np.diag(self.matrix, k=-1).copy().tolist() + [0]
        diag2 = np.diag(self.matrix, k=1).copy().tolist() + [0]
        diag3 = np.diag(self.matrix).copy().tolist()
        diag4 = np.diag(np.rot90(self.matrix)).copy().tolist()  # off-diagonal, middle
        diag5 = np.diag(np.rot90(self.matrix), k=1).copy().tolist() + [0]
        diag6 = np.diag(np.rot90(self.matrix), k=-1).copy().tolist() + [0]
        diagonals = np.array([diag1, diag2, diag3, diag4, diag5, diag6])
        columns = np.rot90(self.matrix)
        IsGameOver = False

        def board_check(matrix):
            for row in matrix:
                if row[1] != 0:
                    if (row[1] == row[2]) and (row[1] == row[3]) and (row[1] == row[4]) and (
                            row[1] == row[5] or row[0] == row[1]):
                        print("Game over."),
                        if row[1] == 1:
                            print("Player 1 wins.")
                        elif row[1] == 2:
                            print("Player 2 wins.")
                        return True
            return False

        IsGameOver = board_check(self.matrix)
        IsGameOver = IsGameOver or board_check(columns)
        IsGameOver = IsGameOver or board_check(diagonals)
        if IsGameOver is True:
            return 1
        else:
            return 0

    def print_board(self):
        print("{:^12} | {:^12} | {:^12} | {:^12} | {:^12} | {:^12} | {:^12} |".format(" ", 0, 1, 2, 3, 4, 5))
        print("-" * 106)
        i = -1
        for row in self.matrix:
            i += 1
            print(
                "{:^12} | {:^12} | {:^12} | {:^12} | {:^12} | {:^12} | {:^12} |"
                    .format(i, BoardTile(row[0]).name, BoardTile(row[1]).name, BoardTile(row[2]).name, BoardTile(row[3]).name
                            , BoardTile(row[4]).name, BoardTile(row[5]).name))
            print("-" * 106)

    def print_quadrant(self, quad):
        switcher = {
            0: self.matrix[0:3, 0:3],
            1: self.matrix[3:6, 0:3],
            2: self.matrix[0:3, 3:6],
            4: self.matrix[3:6, 3:6]
        }
        print(switcher.get(quad))
        print("Clockwise: \n " + str(np.rot90(switcher.get(quad), -1)))
        print("Anti-Clockwise: \n " + str(np.rot90(switcher.get(quad), 1)))

