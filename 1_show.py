from sys import argv

from boardsetup import BoardSetup


def main(fen):
    print()
    print(BoardSetup(fen).board_text)
    print()


main(argv[1])