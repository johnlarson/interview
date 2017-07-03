from sys import argv

from gamestate import GameState


def main(fen_file):
    game_state = GameState(fen_file)
    game_state.take_turn()
    print(game_state.fen)


main(argv[1])