import unittest
import numpy as np
from pentago import board as b


class TestBoard(unittest.TestCase):

    def test_create_board(self):
        board = b.Board()
        empty_matrix = np.array([[b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                  b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                                 [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                  b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                                 [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                  b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                                 [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                  b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                                 [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                  b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                                 [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                  b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ]])
        self.assertTrue(np.array_equal(board.matrix, empty_matrix))

    def test_place_stone(self):
        board = b.Board()
        board.place_stone(0, 0, b.BoardTile.WHITE.value)
        one_stone_matrix = [[b.BoardTile.WHITE.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                             b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                            [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                             b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                            [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                             b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                            [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                             b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                            [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                             b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                            [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                             b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ]]
        self.assertTrue(np.array_equal(board.matrix, one_stone_matrix))

        #TODO Test placing stone out of bounds in x
        #TODO Test placing stone out of bounds in y
        #TODO Test placing stone in spot that currently has a stone


    def test_rotate_quadrant_clockwise(self):
        board = b.Board()
        board.place_stone(0, 0, b.BoardTile.WHITE.value)
        board.rotate_quadrant(0, 1)
        rotated_one_stone_matrix = [[b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                     b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                                    [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                     b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                                    [b.BoardTile.WHITE.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                     b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                                    [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                     b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                                    [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                     b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                                    [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                     b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ]]

        self.assertTrue(np.array_equal(board.matrix, rotated_one_stone_matrix))

    def test_rotate_quadrant_anti_clockwise(self):
        board = b.Board()
        board.place_stone(0, 0, b.BoardTile.WHITE.value)
        board.rotate_quadrant(0, 0)
        rotated_one_stone_matrix = [[b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.WHITE.value,
                                     b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                                    [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                     b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                                    [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                     b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                                    [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                     b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                                    [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                     b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ],
                                    [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                     b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, ]]

        self.assertTrue(np.array_equal(board.matrix, rotated_one_stone_matrix))

        #TODO Test rotating in out of bounds direction

        #TODO Test endgame condition for all possible wins/draws
