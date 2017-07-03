"""
Python program for Task 2.

Given the path to a FEN-formatted file, loads the FEN-formatted data,
makes the move suggested by the API endpoint at
https://syzygy-tables.info/api/v2, displays the resulting board setup,
and prints the resulting FEN-formatted game state to the terminal.

Usage: python stretch.py <fen-file-path>
"""

from sys import argv

from gamestate import GameState


def main(fen_file):
    game_state = GameState(fen_file)
    game_state.take_turn()
    print()
    print(game_state.board_text)
    print()
    print(game_state.fen)
    print()


main(argv[1])