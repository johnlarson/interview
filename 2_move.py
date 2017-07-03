"""
Python program for Task 2.

Given the path to a FEN-formatted file, loads the FEN-formatted data,
makes the move suggested by the API endpoint at
https://syzygy-tables.info/api/v2, and displays the resulting
FEN-formatted game state.

Usage: python 2_move.py <fen-file-path>
"""

from sys import argv

from gamestate import GameState


def main(fen_file):
    game_state = GameState(fen_file)
    game_state.take_turn()
    print(game_state.fen)


main(argv[1])