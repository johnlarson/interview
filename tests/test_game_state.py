from unittest import TestCase

import gamestate
from gamestate import GameState



class InitTests(TestCase):
    """Unit tests for GameState.__init__()"""

    def test_no_fen_file_path(self):
        """
        If no fen file is provided, should raise NoFENFileProvidedError.
        """
        ...


class ParseFenStrTests(TestCase):
    """Tests GameState._parse_fen_str()."""

    def test_valid_input(self):
        """Should correctly parse a valid fen string."""
        ...

    def test_invalid_fen_string(self):
        """
        If fen string is not valid fen, should raise
        InvalidFENFileError.
        """
        ...

    def test_parse_positions(self):
        """Should correctly parse positions of pieces on board."""
        ...

    def test_whites_turn(self):
        """
        Tests the parsing of the turn field in the FEN string when it is
        white player's turn.
        """
        ...

    def test_blacks_turn(self):
        """
        Tests the parsing of the turn field in the FEN string when it is
        black player's turn.
        """
        ...

    def test_castling_all(self):
        """
        Tests the parsing of castling when both kings can be castled
        with either rook.
        """
        ...

    def test_castling_some(self):
        """
        Tests the parsing of castling when some castling options are
        still open.
        """
        ...

    def test_castling_none(self):
        """
        Tests the parsing of castling when neither king can be castled.
        """
        ...

    def test_en_passant(self):
        """
        Should correctly parse when FEN string contains an en passant
        position.
        """
        ...

    def test_no_en_passant(self):
        """Should correctly parse when en passant field is '-'."""
        ...

    def test_halfmove_clock(self):
        """Should correctly parse the halfmove clock."""
        ...

    def test_halfmove_clock_multi_digit(self):
        """Should correctly parse multi-digit halfmove clock."""
        ...

    def test_fullmove_number(self):
        """Should correctly parse the fullmove number."""
        ...

    def test_fullmove_number_multi_digit(self):
        """Should correctly parse multi-digit fullmove number."""
        ...


class FenTests(TestCase):
    """Tests the `fen` property method."""

    def test_correctly_display(self):
        """
        Should return a correct fen-formatted description of the current
        game state.
        """
        ...

    def test_correctly_display_board(self):
        """Board state should be correct in returned fen string."""
        ...

    def test_whites_turn(self):
        """
        Should return correct description of turn when it is white's
        turn.
        """
        ...

    def test_blacks_turn(self):
        """
        Should return correct description of turn when it is black's
        turn.
        """
        ...

    def test_castling_all(self):
        """
        Should return correct description of castling when both kings
        can castle with either rook.
        """
        ...

    def test_castling_some(self):
        """
        Should return correct description of castling when some but not
        all castling moves are open.
        """
        ...

    def test_castling_none(self):
        """
        Should return correct description of castling when neither king
        can be castled.
        """
        ...

    def test_en_passant(self):
        """Should return correct description of en passant square."""
        ...

    def test_no_en_passant(self):
        """
        Should give correct description of en passant when there is no
        current en passant square.
        """
        ...

    def test_halfmove_clock(self):
        """Should correctly display the halfmove clock."""
        ...

    def test_halfmove_clock_multi_digit(self):
        """Should correctly display a multi-digit halfmove clock."""
        ...

    def test_fullmove_number(self):
        """Should correctly display the fullmove number."""
        ...

    def test_fullmove_number_multi_digit(self):
        """Should correctly display a multi-digit fullmove number."""
        ...


class BoardTextTests(TestCase):
    """Tests `board_text` property method of GameState."""

    def test_correctly_display(self):
        """
        Should correctly display the board based on the state of the
        GameState object.
        """
        ...


class TakeTurnTests(TestCase):
    """Tests GameState.take_turn()"""

    def test_makes_suggested_move(self):
        """Should make move suggested by api."""
        ...


class MakeMoveTests(TestCase):
    """Tests GameState._make_move()"""

    def test_correctly_handles_capturing(self):
        """
        When one piece lands on another, the other should be removed
        from the board, and moving piece should replace it.
        """
        ...

    def test_white_turn_to_black(self):
        """
        When white makes a move, the turn tracker should be set to
        black's turn.
        """
        game = GameState()
        game.player = 'w'
        game._make_move('a1a2')
        self.assertEqual(game.player, 'b')

    def test_black_turn_to_white(self):
        """
        When black makes a move, the turn tracker should be set to
        white's turn.
        """
        game = GameState()
        game.player = 'b'
        game._make_move('a1a2')
        self.assertEqual(game.player, 'w')

    def test_castling_move_white_king(self):
        """Moving white king should disable all white castling."""
        game = GameState()
        game.board['e']['1'] = 'K'
        game.board['e']['2'] = GameState.EMPTY
        game.castle_white_king = True
        game.castle_white_queen = True
        game._make_move('e1e2')
        self.assertFalse(game.castle_white_king)
        self.assertFalse(game.castle_white_queen)

    def test_castling_move_white_king_side_rook(self):
        """
        Moving white king-side rook should disable it for castling.
        """
        game = GameState()
        game.board['h']['1'] = 'R'
        game.board['h']['2'] = GameState.EMPTY
        game.castle_white_king = True
        game._make_move('h1h2')
        self.assertFalse(game.castle_white_king)

    def test_castling_move_white_queen_side_rook(self):
        """
        Moving white queen-side rook should disable it for castling.
        """
        game = GameState()
        game.board['a']['1'] = 'R'
        game.board['a']['2'] = GameState.EMPTY
        game.castle_white_queen = True
        game._make_move('a1a2')
        self.assertFalse(game.castle_white_queen)

    def test_castling_move_black_king(self):
        """Moving black king should disable all black castling."""
        game = GameState()
        game.board['e']['8'] = 'k'
        game.board['e']['7'] = GameState.EMPTY
        game.castle_black_king = True
        game.castle_black_queen = True
        game._make_move('e8e7')
        self.assertFalse(game.castle_black_king)
        self.assertFalse(game.castle_black_queen)

    def test_castling_move_black_king_side_rook(self):
        """
        Moving black king-side rook should disable it for castling.
        """
        game = GameState()
        game.board['h']['8'] = 'r'
        game.board['h']['7'] = GameState.EMPTY
        game.castle_black_king = True
        game._make_move('h8h7')
        self.assertFalse(game.castle_black_king)

    def test_castling_move_black_queen_side_rook(self):
        """
        Moving black queen-side rook should disable it for castling.
        """
        game = GameState()
        game.board['a']['8'] = 'r'
        game.board['a']['7'] = GameState.EMPTY
        game.castle_black_queen = True
        game._make_move('a8a7')
        self.assertFalse(game.castle_black_queen)

    def test_castling_move_other_piece(self):
        """
        Moving any piece other than a king or rook should not disable
        castling.
        """
        game = GameState()
        game.board['a']['8'] = 'b'
        game.board['b']['2'] = GameState.EMPTY
        game.castle_black_king = True
        game.castle_black_queen = True
        game._make_move('a1b2')
        self.assertTrue(game.castle_black_king)
        self.assertTrue(game.castle_black_queen)

    def test_en_passant_pawn_moves_two_squares(self):
        """
        When a pawn moves two spaces, the square behind it should be
        set as the en passant square.
        """
        ...

    def test_en_passant_only_lasts_one_turn(self):
        """
        Even if there was previously an en passant square, if no pawn
        moved two spaces this turn, en passant should be set to None.
        """
        ...

    def test_en_passant_non_pawn_moves(self):
        """When a non-pawn piece moves, en passant should be None."""
        ...

    def test_en_passant_non_pawn_moves_two_squares(self):
        """
        Even if a non-pawn moves two spaces, en passant should be None.
        """
        ...

    def test_en_passant_pawn_moves_one_square(self):
        """
        If pawn moves but it does not move two squares, en passant
        should be None.
        """
        ...

    def test_halfmove_clock_increments_after_player_makes_move(self):
        """
        When a player makes a reversible move, the halfmove clock should
        be incremented.
        """
        ...

    def test_halfmove_clock_resets_on_capture(self):
        """
        When a player captures a piece, the halfmove clock should be
        reset to 0.
        """
        ...

    def test_halfmove_clock_resets_on_pawn_move(self):
        """
        When a player moves a pawn, the halfmove clock should be reset
        to 0.
        """
        ...

    def test_halfmove_clock_resets_on_castling(self):
        """
        When a player makes a castling move, the halfclock should be
        reset, as this is an irreversible move (see
        http://www.open-chess.org/viewtopic.php?f=3&t=2209).
        """
        ...

    def test_fullmove_number_increments_when_black_takes_a_turn(self):
        ...

    def test_fullmove_number_does_not_increment_when_white_moves(self):
        ...