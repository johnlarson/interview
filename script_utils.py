import sys

from gamestate import InvalidFENFileError


USAGE = 'Usage: python {} <path/to/fen/file.fen>'
NOT_FOUND = 'FEN File not found: {}'
INVALID_FEN = 'FEN File invalid: {}'


def error_out(message):
    print(message, file=sys.stderr)
    sys.exit(1)


def run_fen_script(main_func):
    program_name = sys.argv[0]
    try:
        file_path = sys.argv[1]
    except IndexError:
        error_out(USAGE.format(program_name))
    try:
        main_func(file_path)
    except FileNotFoundError:
        error_out(NOT_FOUND.format(file_path))
    except InvalidFENFileError:
        error_out(INVALID_FEN.format(file_path))