from sys import argv

from boardsetup import BoardSetup


def main(fen):
    print(BoardSetup(fen).board_text)


main(argv[1])