"""
Python program for Task 1.

Given the path to a FEN-formatted file, displays what the chess board
would look like.

Usage: python 1_show.py <fen-file-path>
"""

from sys import argv

from gamestate import GameState


def main(fen_file):
    print()
    print(GameState(fen_file).board_text)
    print()


main(argv[1])