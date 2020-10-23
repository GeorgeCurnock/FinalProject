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

    def test_game_end_for_not_finished(self):
        board = b.Board()
        board.place_stone(0, 0, b.BoardTile.WHITE.value)
        self.assertEqual(board.game_end(), 0)

    def test_game_end_for_horizontal_win(self):
        board = b.Board()
        board.place_stone(0, 0, b.BoardTile.WHITE.value)
        board.place_stone(1, 0, b.BoardTile.WHITE.value)
        board.place_stone(2, 0, b.BoardTile.WHITE.value)
        board.place_stone(3, 0, b.BoardTile.WHITE.value)
        board.place_stone(4, 0, b.BoardTile.WHITE.value)
        self.assertEqual(board.game_end(), 1)

    def test_game_end_for_vertical_win(self):
        board = b.Board()
        board.place_stone(0, 0, b.BoardTile.WHITE.value)
        board.place_stone(0, 1, b.BoardTile.WHITE.value)
        board.place_stone(0, 2, b.BoardTile.WHITE.value)
        board.place_stone(0, 3, b.BoardTile.WHITE.value)
        board.place_stone(0, 4, b.BoardTile.WHITE.value)
        self.assertEqual(board.game_end(), 1)

    def test_game_end_for_diagonal_center_win(self):
        board = b.Board()
        board.place_stone(0, 0, b.BoardTile.WHITE.value)
        board.place_stone(1, 1, b.BoardTile.WHITE.value)
        board.place_stone(2, 2, b.BoardTile.WHITE.value)
        board.place_stone(3, 3, b.BoardTile.WHITE.value)
        board.place_stone(4, 4, b.BoardTile.WHITE.value)
        self.assertEqual(board.game_end(), 1)

    def test_game_end_for_diagonal_win(self):
        board = b.Board()
        board.place_stone(1, 0, b.BoardTile.WHITE.value)
        board.place_stone(2, 1, b.BoardTile.WHITE.value)
        board.place_stone(3, 2, b.BoardTile.WHITE.value)
        board.place_stone(4, 3, b.BoardTile.WHITE.value)
        board.place_stone(5, 4, b.BoardTile.WHITE.value)
        self.assertEqual(board.game_end(), 1)

    def test_game_end_for_draw(self):
        board = b.Board()
        for i in range(6):
            for j in range(6):
                board.place_stone(i, j, b.BoardTile.WHITE.value)
        self.assertEqual(board.game_end(), 1)




