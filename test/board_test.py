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

    def test_place_stone_out_of_bounds_in_x(self):
        board = b.Board()
        board.place_stone(0, 7, b.BoardTile.WHITE.value)
        one_stone_matrix_x = [[b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
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
        self.assertTrue(np.array_equal(board.matrix, one_stone_matrix_x))

    def test_place_stone_out_of_bounds_in_y(self):
        board = b.Board()
        board.place_stone(7, 0, b.BoardTile.WHITE.value)
        one_stone_matrix_y = [[b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
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
        self.assertTrue(np.array_equal(board.matrix, one_stone_matrix_y))

    def test_place_stone_in_taken_tile(self):
        board = b.Board()
        board.place_stone(0, 0, b.BoardTile.WHITE.value)
        board.place_stone(0, 0, b.BoardTile.BLACK.value)
        one_stone_matrix_taken = [[b.BoardTile.WHITE.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
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
        self.assertTrue(np.array_equal(board.matrix, one_stone_matrix_taken))

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

    def test_rotate_quadrant_out_of_bounds_quadrant(self):
        board = b.Board()
        board.place_stone(0, 0, b.BoardTile.WHITE.value)
        board.rotate_quadrant(4, 0)
        rotated_out_of_bounds_quad = [[b.BoardTile.WHITE.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
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
        self.assertTrue(np.array_equal(board.matrix, rotated_out_of_bounds_quad))

    def test_rotate_quadrant_out_of_bounds_direction(self):
        board = b.Board()
        board.place_stone(0, 0, b.BoardTile.WHITE.value)
        board.rotate_quadrant(0, 3)
        rotated_out_of_bounds_dir = [[b.BoardTile.WHITE.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                      b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                      b.BoardTile.EMPTY.value, ],
                                     [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                      b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                      b.BoardTile.EMPTY.value, ],
                                     [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                      b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                      b.BoardTile.EMPTY.value, ],
                                     [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                      b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                      b.BoardTile.EMPTY.value, ],
                                     [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                      b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                      b.BoardTile.EMPTY.value, ],
                                     [b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                      b.BoardTile.EMPTY.value, b.BoardTile.EMPTY.value,
                                      b.BoardTile.EMPTY.value, ]]

        self.assertTrue(np.array_equal(board.matrix, rotated_out_of_bounds_dir))

        # TODO Test endgame condition for all possible wins/draws
