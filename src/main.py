from pentago import board as b
from pentago import human_player as hp


def main():
    board = b.Board()
    player1 = hp.HumanPlayer(None, b.BoardTile.WHITE.value)
    player2 = hp.HumanPlayer(None, b.BoardTile.BLACK.value)
    board.printBoard()

    while True:
        print("Players 1's Turn")
        player1.play(board)
        game_over = board.gameEnd()
        if game_over == 1:
            break

        board.printBoard()

        print("Players 2's Turn")
        player2.play(board)
        game_over = board.gameEnd()
        if game_over == 2:
            break


if __name__ == '__main__':
    main()
