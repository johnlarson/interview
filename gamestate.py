import json
import enum
from enum import Enum
from urllib.parse import quote_plus
from collections import OrderedDict

import requests


class GameState:
    """Holds game state information read from a FEN file."""

    ROWS = ['8', '7', '6', '5', '4', '3', '2', '1']
    COLS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    # When the board is displayed, each square should display a letter for the
    # piece on the square. If there is no piece, that space should be filled
    # with a single space character.
    EMPTY = ' '

    def __init__(self, fen_file_path=None):
        """
        Constructor for GameState class

        Arguments:
        fen_file_path -- the path to the FEN file from which the
        GameState object will be initialized.
        """
        if fen_file_path:
            with open(fen_file_path) as fen_file:
                fen_str = fen_file.read()
            self._parse_fen_str(fen_str)
        else:
            start = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
            self._parse_fen_str(start)

    def _parse_fen_str(self, fen_str):
        """
        Parse the given FEN file and load provided information into the
        GameState object.
        """
        fen_list = fen_str.split()
        self._parse_board(fen_list[0])
        self._parse_turn(fen_list[1])
        self._parse_castling(fen_list[2])
        self._parse_en_passant(fen_list[3])
        self._parse_halfmove_clock(fen_list[4])
        self._parse_fullmove_number(fen_list[5])

    def _parse_board(self, board_str):
        self.board = {}
        row_index = 0
        col_index = 0
        for char in board_str:
            try:
                # if number can be parsed as int, add that many empty squares
                num = int(char)
                for i in range(num):
                    self._set_piece(self.COLS[col_index], self.ROWS[row_index],
                                    self.EMPTY)
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
                    self._set_piece(self.COLS[col_index], self.ROWS[row_index],
                                    char)
                    col_index += 1

    def _parse_turn(self, turn_str):
        self.player = turn_str

    def _parse_castling(self, castling_str):
        self.castle_white_king = 'K' in castling_str
        self.castle_white_queen = 'Q' in castling_str
        self.castle_black_king = 'k' in castling_str
        self.castle_black_queen = 'q' in castling_str

    def _parse_en_passant(self, en_passant_str):
        if en_passant_str == '-':
            self.en_passant = None
        else:
            self.en_passant = Tuple(en_passant_str)

    def _parse_halfmove_clock(self, halfmove_str):
        self.halfmove_clock = int(halfmove_str)

    def _parse_fullmove_number(self, fullmove_str):
        self.fullmove_number = int(fullmove_str)

    def _get_piece(self, col, row):
        """
        Returns the letter of the piece at the given column and row, or
        a single space, if there is no piece there.

        Example:
        If there is a white pawn at a7, then 
        `game_state._get_piece('a', '7')` returns `'K'`. If there is no
        piece at c3, then `game_state._get_piece('c', '3')` returns
        `' '`.
        """
        return self.board[col][row]

    def _set_piece(self, col, row, val):
        """
        Sets a given square to a given string value. This string value
        should be a letter corresponding to a piece, such as 'K' or 'p',
        or a single space to represent an empty square.

        Arguments:
        col -- the column of the square.
        row -- the row of the square.
        val -- the string value to store on the square.
        """
        if not col in self.board.keys():
            self.board[col] = {}
        self.board[col][row] = val

    def __str__(self):
        return self.fen

    @property
    def fen(self):
        """Property. The FEN representation of the GameState object."""
        parts = [self._board_to_fen(), self.player, self._castling_to_fen(),
                 self._en_passant_to_fen(), self._halfmove_to_fen(),
                 self._fullmove_to_fen()]
        return ' '.join(parts)

    def _board_to_fen(self):
        """
        Returns the first part of the FEN representation, a string
        telling the positions of pieces on the board.
        """
        rows = [self._row_to_fen(row) for row in self.ROWS]
        return '/'.join(rows)

    def _row_to_fen(self, row):
        # Note: The empty count continues to add up until either the
        # a non-empty square is reached, or the end of the row is
        # reached, at which point the count is added to the
        # FEN-formatted row information.
        ret = ''
        empty_count = 0
        for col in self.COLS:
            piece = self._get_piece(col, row)
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

        if self.castle_white_king:
            ret += 'K'
        if self.castle_white_queen:
            ret += 'Q'
        if self.castle_black_king:
            ret += 'k'
        if self.castle_black_queen:
            ret += 'q'

        if ret == '':
            ret = '-'
        return ret

    def _en_passant_to_fen(self):
        return ''.join(self.en_passant) if self.en_passant else '-'

    def _halfmove_to_fen(self):
        return str(self.halfmove_clock)

    def _fullmove_to_fen(self):
        return str(self.fullmove_number)

    @property
    def board_text(self):
        """
        Property. The to be printed to the output in order to form a
        picture of the chess board.
        """
        ret = ''
        ret += self._get_enclosing_line()
        row_lines = [self._get_row_line(row) for row in self.ROWS]
        row_lines = self._get_divider_line().join(row_lines)
        ret += row_lines
        ret += self._get_enclosing_line()
        ret += self._get_col_label_line()
        return ret

    def _get_enclosing_line(self):
        """
        Returns the text needed to form the top or bottom edge of the
        board.
        """
        return '  ---------------------------------\n'

    def _get_row_line(self, row):
        """Returns the text needed to form a row of the the board."""
        ret = ''
        to_join = [row] + self._get_row_list(row)
        ret += ' | '.join(to_join)
        ret += ' |\n'
        return ret

    def _get_row_list(self, row):
        """
        Returns a list of piece values for all squares in the given row,
        in order from column a to column h.
        """
        return [self.board[col][row] for col in self.COLS]

    def _get_divider_line(self):
        """
        Returns the text needed to form a line between rows on the
        board.
        """
        return '  |-------------------------------|\n'

    def _get_col_label_line(self):
        """Returns the text needed to form the column labels."""
        return '    a   b   c   d   e   f   g   h\n'

    def take_turn(self):
        """
        Get a suggested move from the API and carry it out, updating all
        state information to reflect the move.
        """
        suggested_move = self._get_suggested_move()
        self._make_move(suggested_move)

    def _get_suggested_move(self):
        body = requests.get('https://syzygy-tables.info/api/v2',
                            params={'fen': self.fen})
        json_dict = json.loads(body.text, object_pairs_hook=OrderedDict)
        return list(json_dict['moves'].keys())[0]

    def _make_move(self, move_str):
        """
        Make the move described by the given columns and rows.
        """
        col_0, row_0, col_1, row_1 = tuple(move_str)
        self._update_castling(col_0, row_0)
        self._update_halfmove_clock(col_0, row_0, col_1, row_1)
        piece = self._get_piece(col_0, row_0)
        self._set_piece(col_0, row_0, self.EMPTY)
        self._set_piece(col_1, row_1, piece)
        self._toggle_player()
        self._update_en_passant(col_0, row_0, col_1, row_1)

    def _toggle_player(self):
        self.player = 'b' if self.player == 'w' else 'w'

    def _update_castling(self, col, row):
        """
        Update castling status based on where the piece moves from. For
        checking rooks, the starting square is used instead of the piece
        type. This is because information on where a rook started is not
        stored in the GameState data model. If a rook is moved from one
        of those spaces, that disqualifies the rook from being used in
        castling. If any other piece is moved from one of those spaces,
        that means the rook that started there has already been
        disqualified, so the rook should still be marked as not
        available for castling.

        Arguments:
        col -- the starting column of the move to update based on.
        row -- the starting row of the move to update based on.
        """
        if self._get_piece(col, row) == 'K':
            self.castle_white_king = False
            self.castle_white_queen = False
        elif col == 'a' and row == '1':
            self.castle_white_queen = False
        elif col == 'h' and row == '1':
            self.castle_white_king = False
        elif self._get_piece(col, row) == 'k':
            self.castle_black_king = False
            self.castle_black_queen = False
        elif col == 'a' and row == '8':
            self.castle_black_queen = False
        elif col == 'h' and row == '8':
            self.castle_black_king = False

    def _update_en_passant(self, col_0, row_0, col_1, row_1):
        moved_piece = self._get_piece(col_1, row_1)
        row_0 = int(row_0)
        row_1 = int(row_1)
        if moved_piece == 'P' and row_1 == row_0 + 2 and col_0 == col_1:
            # white player has moved pawn two spaces forward
            self.en_passant = (col_0, str(row_1 - 1))
        elif moved_piece == 'p' and row_1 == row_0 - 2 and col_0 == col_1:
            # black player has moved pawn two spaces forward
            self.en_passant = (col_0, str(row_1 + 1))
        else:
            self.en_passant = None

    def _update_halfmove_clock(self, col_0, row_0, col_1, row_1):
        if self._get_piece(col_0, row_0) in ('P', 'p'):
            # piece moved is a pawn, reset the halfmove clock
            self.halfmove_clock = 0
        elif self._get_piece(col_1, row_1) != self.EMPTY:
            # opponent's piece is captured, reset the halfmove clock
            self.halfmove_clock = 0
        else:
            self.halfmove_clock += 1