from sys import argv

from boardsetup import BoardSetup


def main(fen_file):
    board = BoardSetup(fen_file)
    board.take_turn()
    print(board.fen)


main(argv[1])