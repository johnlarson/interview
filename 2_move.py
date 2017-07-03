from sys import argv

from boardsetup import BoardSetup


def main(fen):
    board = BoardSetup(fen)
    board.take_turn()
    print(board.fen)


main(argv[1])