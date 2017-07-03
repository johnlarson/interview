import requests
from urllib.parse import quote_plus


class BoardSetup:
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
        ...

    def _parse_castling(self, castling_str):
        ...

    def _parse_en_passant(self, en_passant_str):
        ...

    def _parse_halfmove_clock(self, halfmove_str):
        ...

    def _parse_fullmove_number(self, fullmove_str):
        ...

    def _piece_by_col_and_row(self, col, row):
        return self._board[col][row]

    def _piece_by_postion(self, pos):
        return self._piece_by_col_and_row(pos[0], pos[1])

    def _get_row(self, row):
        return [self._board[col][row] for col in self.COLS]

    def __str__(self):
        return self.fen

    @property
    def fen(self):
        return ''

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
        self._make_move(*suggested_move)

    def _get_suggested_move(self):
        body = requests.get('https://syzygy-tables.info/api/v2',
                            params={'fen': self.fen})
        return tuple('a2a3')

    def _make_move(self, col_0, row_0, col_1, row_1):
        ...