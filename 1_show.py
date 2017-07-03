from sys import argv

from gamestate import GameState


def main(fen_file):
    print()
    print(GameState(fen_file).board_text)
    print()


main(argv[1])