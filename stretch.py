from sys import argv

from boardsetup import BoardSetup


def main(fen_file):
    board = BoardSetup(fen_file)
    board.take_turn()
    print()
    print(board.board_text)
    print()
    print(board.fen)
    print()


main(argv[1])