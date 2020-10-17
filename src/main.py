from pentago import board as b
from pentago import human_player as hp


def main():
    board = b.Board()
    player1 = hp.HumanPlayer(None, b.BoardTile.WHITE)
    player2 = hp.HumanPlayer(None, b.BoardTile.BLACK)

    while True:
        player1.play(board)
        gameOver = board.gameEnd()
        if gameOver == 1:
            break

        player2.play(board)
        gameOver = board.gameEnd()
        if gameOver == 2:
            break


if __name__ == '__main__':
    main()
