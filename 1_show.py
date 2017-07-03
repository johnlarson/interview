from sys import argv

from boardsetup import BoardSetup


def main(fen_file):
    print()
    print(BoardSetup(fen_file).board_text)
    print()


main(argv[1])