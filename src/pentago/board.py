import enum

import numpy as np


class BoardTile(enum.Enum):
    EMPTY = 0,
    WHITE = 1,
    BLACK = 2

class BoardQuad(enum.Enum):
    TOPLEFT = 0,
    TOPRIGHT = 0,
    BOTTOMLEFT = 0,
    BOTTOMRIGHT = 0


class Board:
    def __init__(self):
        self.matrix = np.full((6, 6), BoardTile.EMPTY.value, dtype=BoardTile)

    def setGridValue(self, x, y, value):
        self.matrix[x][y] = value

    def getGridValue(self, x, y):
        return self.matrix[x][y]

    def placeStone(self, x, y, value):
        if self.matrix[x][y] is BoardTile.EMPTY.value:
            self.setGridValue(x, y, value)

    def rotateQuadrant(self, quad, direction):
        if quad == BoardQuad.TOPLEFT.value:
            startx = 0
            starty = 0
            endx = 3
            endy = 3
        elif quad == BoardQuad.TOPRIGHT.value:
            startx = 3
            starty = 0
            endx = 4
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
            return

        quadrant = self.matrix[startx:endx, starty:endy]
        quadrant = np.rot90(quadrant, direction)
        self.matrix[startx:endx, starty:endy] = quadrant

    def gameEnd(self):
        diag1 = np.diag(self.matrix, k=-1).copy().tolist() + [0]
        diag2 = np.diag(self.matrix, k=1).copy().tolist() + [0]
        diag3 = np.diag(self.matrix).copy().tolist()
        diag4 = np.diag(np.rot90(self.matrix)).copy().tolist()  # off-diagonal, middle
        diag5 = np.diag(np.rot90(self.matrix), k=1).copy().tolist() + [0]
        diag6 = np.diag(np.rot90(self.matrix), k=-1).copy().tolist() + [0]
        diagonals = np.array([diag1, diag2, diag3, diag4, diag5, diag6])
        columns = np.rot90(self.matrix)
        IsGameOver = False

        def boardcheck(matrix):
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

        IsGameOver = boardcheck(self.matrix)
        IsGameOver = IsGameOver or boardcheck(columns)
        IsGameOver = IsGameOver or boardcheck(diagonals)
        if IsGameOver is True:
            return 1
        else:
            return 0


