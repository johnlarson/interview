import json
import enum
from enum import Enum
from urllib.parse import quote_plus
from collections import OrderedDict

import requests


class GameState:
    ROWS = ['8', '7', '6', '5', '4', '3', '2', '1']
    COLS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    EMPTY = ' '

    def __init__(self, fen_file_path):
        self._parse_fen_file(fen_file_path)

    def _parse_fen_file(self, fen_file_path):
        with open(fen_file_path) as fen_file:
            fen_str = fen_file.read()
        fen_list = fen_str.split()
        self._parse_board(fen_list[0])
        self._parse_turn(fen_list[1])
        self._parse_castling(fen_list[2])
        self._parse_en_passant(fen_list[3])
        self._parse_halfmove_clock(fen_list[4])
        self._parse_fullmove_number(fen_list[5])

    def _parse_board(self, board_str):
        self._board = {}
        row_index = 0
        col_index = 0
        for char in board_str:
            try:
                # if number can be parsed as int, add that many empty squares
                num = int(char)
                for i in range(num):
                    self._set_by_indices(row_index, col_index, self.EMPTY)
                    col_index += 1
            except ValueError:
                if char == '/':
                    # slash means go to beginning of next row
                    col_index = 0
                    row_index += 1
                else:
                    # in absence of slash or number, set the square as
                    # containing the current piece type (given by the
                    # character) and move on to the next square
                    self._set_by_indices(row_index, col_index, char)
                    col_index += 1

    def _set_by_indices(self, row_index, col_index, value):
        row = self.ROWS[row_index]
        col = self.COLS[col_index]
        if not col in self._board.keys():
            self._board[col] = {}
        self._board[col][row] = value

    def _parse_turn(self, turn_str):
        self._player = turn_str

    def _parse_castling(self, castling_str):
        self._can_castle_white_king = 'K' in castling_str
        self._can_castle_white_queen = 'Q' in castling_str
        self._can_castle_black_king = 'k' in castling_str
        self._can_castle_black_queen = 'q' in castling_str

    def _parse_en_passant(self, en_passant_str):
        self._en_passant = None if en_passant_str == '-' else en_passant_str

    def _parse_halfmove_clock(self, halfmove_str):
        self._halfmove_clock = int(halfmove_str)

    def _parse_fullmove_number(self, fullmove_str):
        self._fullmove_number = int(fullmove_str)

    def _get_by_col_and_row(self, col, row):
        return self._board[col][row]

    def _get_by_postion(self, pos):
        return self._get_by_col_and_row(pos[0], pos[1])

    def _set_at_col_and_row(self, col, row, val):
        self._board[col][row] = val

    def _set_at_position(self, pos, val):
        self._set_by_col_and_row(pos[0], pos[1])

    def _get_row(self, row):
        return [self._board[col][row] for col in self.COLS]

    def __str__(self):
        return self.fen

    @property
    def fen(self):
        parts = [self._board_to_fen(), self._player, self._castling_to_fen(),
                 self._en_passant_to_fen(), self._halfmove_to_fen(),
                 self._fullmove_to_fen()]
        return ' '.join(parts)

    def _board_to_fen(self):
        rows = [self._row_to_fen(row) for row in self.ROWS]
        return '/'.join(rows)

    def _row_to_fen(self, row):
        ret = ''
        empty_count = 0
        for col in self.COLS:
            piece = self._get_by_col_and_row(col, row)
            if piece == self.EMPTY:
                empty_count += 1
            else:
                if empty_count > 0:
                    ret += str(empty_count)
                    empty_count = 0
                ret += piece
        if empty_count > 0:
            ret += str(empty_count)
        return ret

    def _castling_to_fen(self):
        ret = ''

        if self._can_castle_white_king:
            ret += 'K'
        if self._can_castle_white_queen:
            ret += 'Q'
        if self._can_castle_black_king:
            ret += 'k'
        if self._can_castle_black_queen:
            ret += 'q'

        if ret == '':
            ret = '-'
        return ret

    def _en_passant_to_fen(self):
        return self._en_passant if self._en_passant else '-'

    def _halfmove_to_fen(self):
        return str(self._halfmove_clock)

    def _fullmove_to_fen(self):
        return str(self._fullmove_number)

    @property
    def board_text(self):
        ret = ''
        ret += self._get_enclosing_line()
        row_lines = [self._get_row_line(row) for row in self.ROWS]
        row_lines = self._get_divider_line().join(row_lines)
        ret += row_lines
        ret += self._get_enclosing_line()
        ret += self._get_col_label_line()
        return ret

    def _get_enclosing_line(self):
        return '  ---------------------------------\n'

    def _get_row_line(self, row):
        ret = ''
        to_join = [row] + self._get_row(row)
        ret += ' | '.join(to_join)
        ret += ' |\n'
        return ret

    def _get_divider_line(self):
        return '  |-------------------------------|\n'

    def _get_col_label_line(self):
        return '    a   b   c   d   e   f   g   h\n'

    def take_turn(self):
        suggested_move = self._get_suggested_move()
        print(suggested_move)
        self._make_move(*suggested_move)

    def _get_suggested_move(self):
        body = requests.get('https://syzygy-tables.info/api/v2',
                            params={'fen': self.fen})
        json_dict = json.loads(body.text, object_pairs_hook=OrderedDict)
        move_str = list(json_dict['moves'].keys())[0]
        return tuple(move_str)

    def _make_move(self, col_0, row_0, col_1, row_1):
        piece = self._get_by_col_and_row(col_0, row_0)
        self._set_at_col_and_row(col_0, row_0, self.EMPTY)
        self._set_at_col_and_row(col_1, row_1, piece)