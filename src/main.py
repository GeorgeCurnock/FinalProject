from pentago import board as b
from pentago import human_player as hp
from pentago import random_player as rp


def main():
    board = b.Board()
    player1 = hp.HumanPlayer(None, b.BoardTile.WHITE.value)
    player2 = rp.RandomPlayer(None, b.BoardTile.BLACK.value)
    board.print_board()

    while True:
        print("Players 1's Turn")
        player1.play(board)
        game_over = board.game_end()
        if game_over == 1:
            break

        board.print_board()

        print("Players 2's Turn")
        player2.play(board)
        game_over = board.game_end()
        if game_over == 2:
            break

        board.print_board()


if __name__ == '__main__':
    main()
