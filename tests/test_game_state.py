from unittest import TestCase
from unittest.mock import patch

import gamestate
from gamestate import GameState, InvalidFENFileError


class InitTests(TestCase):
    """Unit tests for GameState.__init__()"""

    def test_no_fen_file_path(self):
        """
        If no fen file is provided, should initialize game state to
        match start-of-game state.
        """
        g = GameState()
        expected = {
            'a': {'1': 'R', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'r'},  # noqa
            'b': {'1': 'N', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'n'},  # noqa
            'c': {'1': 'B', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'b'},  # noqa
            'd': {'1': 'Q', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'q'},  # noqa
            'e': {'1': 'K', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'k'},  # noqa
            'f': {'1': 'B', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'b'},  # noqa
            'g': {'1': 'N', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'n'},  # noqa
            'h': {'1': 'R', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'r'},  # noqa
        }
        self.assertEqual(g.board, expected)

    def test_invalid_file_path(self):
        """If file path is invalid, should raise FileNotFoundError."""
        with self.assertRaises(FileNotFoundError):
            GameState('idontexist.fen')


class ParseFenStrTests(TestCase):
    """Tests GameState._parse_fen_str()."""

    def test_valid_input(self):
        """Should correctly parse a valid fen string."""
        fen = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2'
        g = GameState()
        g._parse_fen_str(fen)
        expected = {
            'a': {'1': 'R', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'r'},  # noqa
            'b': {'1': 'N', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'n'},  # noqa
            'c': {'1': 'B', '2': 'P', '3': ' ', '4': ' ', '5': 'p', '6': ' ', '7': ' ', '8': 'b'},  # noqa
            'd': {'1': 'Q', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'q'},  # noqa
            'e': {'1': 'K', '2': ' ', '3': ' ', '4': 'P', '5': ' ', '6': ' ', '7': 'p', '8': 'k'},  # noqa
            'f': {'1': 'B', '2': 'P', '3': 'N', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'b'},  # noqa
            'g': {'1': ' ', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'n'},  # noqa
            'h': {'1': 'R', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'r'},  # noqa
        }
        self.assertEqual(g.board, expected)
        self.assertEqual(g.player, 'b')
        self.assertTrue(g.castle_white_king)
        self.assertTrue(g.castle_white_queen)
        self.assertTrue(g.castle_black_king)
        self.assertTrue(g.castle_black_queen)
        self.assertIsNone(g.en_passant)
        self.assertEqual(g.halfmove_clock, 1)
        self.assertEqual(g.fullmove_number, 2)

    def test_invalid_fen_string(self):
        """
        If fen string is not valid fen, should raise
        InvalidFENFileError.
        """
        g = GameState()
        with self.assertRaises(InvalidFENFileError):
            g._parse_fen_str('asdf 32ds 0-=fe')

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

    def test_halfmove_clock_multi_digit(self):
        """Should correctly parse multi-digit halfmove clock."""
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
        g = GameState()
        g.board = {
            'a': {'1': 'R', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'r'},  # noqa
            'b': {'1': 'N', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'n'},  # noqa
            'c': {'1': 'B', '2': 'P', '3': ' ', '4': ' ', '5': 'p', '6': ' ', '7': ' ', '8': 'b'},  # noqa
            'd': {'1': 'Q', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'q'},  # noqa
            'e': {'1': 'K', '2': ' ', '3': ' ', '4': 'P', '5': ' ', '6': ' ', '7': 'p', '8': 'k'},  # noqa
            'f': {'1': 'B', '2': 'P', '3': 'N', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'b'},  # noqa
            'g': {'1': ' ', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'n'},  # noqa
            'h': {'1': 'R', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'r'},  # noqa
        }
        g.player = 'b'
        g.castle_white_king = True
        g.castle_white_queen = True
        g.castle_black_king = True
        g.castle_black_queen = True
        g.en_passant = None
        g.halfmove_clock = 1
        g.fullmove_number = 2
        exp = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2'
        self.assertEqual(g.fen, exp)

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

    def test_halfmove_clock_multi_digit(self):
        """Should correctly display a multi-digit halfmove clock."""
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
        g = GameState()
        g.board = {
            'a': {'1': 'R', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'r'},  # noqa
            'b': {'1': 'N', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'n'},  # noqa
            'c': {'1': 'B', '2': 'P', '3': ' ', '4': ' ', '5': 'p', '6': ' ', '7': ' ', '8': 'b'},  # noqa
            'd': {'1': 'Q', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'q'},  # noqa
            'e': {'1': 'K', '2': ' ', '3': ' ', '4': 'P', '5': ' ', '6': ' ', '7': 'p', '8': 'k'},  # noqa
            'f': {'1': 'B', '2': 'P', '3': 'N', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'b'},  # noqa
            'g': {'1': ' ', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'n'},  # noqa
            'h': {'1': 'R', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'r'},  # noqa
        }
        expected = """
  ---------------------------------
8 | r | n | b | q | k | b | n | r |
  |-------------------------------|
7 | p | p |   | p | p | p | p | p |
  |-------------------------------|
6 |   |   |   |   |   |   |   |   |
  |-------------------------------|
5 |   |   | p |   |   |   |   |   |
  |-------------------------------|
4 |   |   |   |   | P |   |   |   |
  |-------------------------------|
3 |   |   |   |   |   | N |   |   |
  |-------------------------------|
2 | P | P | P | P |   | P | P | P |
  |-------------------------------|
1 | R | N | B | Q | K | B |   | R |
  ---------------------------------
    a   b   c   d   e   f   g   h
""".strip('\n')  # the outer newlines are only there to make this code readable
        self.assertEqual(g.board_text, expected)


class TakeTurnTests(TestCase):
    """Tests GameState.take_turn()"""

    @patch.object(GameState, '_get_suggested_move', return_value='a2a4')
    def test_makes_suggested_move(self, mocked):
        """Should make move suggested by api."""
        g = GameState()
        g.board = {
            'a': {'1': 'R', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'r'},  # noqa
            'b': {'1': 'N', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'n'},  # noqa
            'c': {'1': 'B', '2': 'P', '3': ' ', '4': ' ', '5': 'p', '6': ' ', '7': ' ', '8': 'b'},  # noqa
            'd': {'1': 'Q', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'q'},  # noqa
            'e': {'1': 'K', '2': ' ', '3': ' ', '4': 'P', '5': ' ', '6': ' ', '7': 'p', '8': 'k'},  # noqa
            'f': {'1': 'B', '2': 'P', '3': 'N', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'b'},  # noqa
            'g': {'1': ' ', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'n'},  # noqa
            'h': {'1': 'R', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'r'},  # noqa
        }
        g.take_turn()
        expected = """
  ---------------------------------
8 | r | n | b | q | k | b | n | r |
  |-------------------------------|
7 | p | p |   | p | p | p | p | p |
  |-------------------------------|
6 |   |   |   |   |   |   |   |   |
  |-------------------------------|
5 |   |   | p |   |   |   |   |   |
  |-------------------------------|
4 | P |   |   |   | P |   |   |   |
  |-------------------------------|
3 |   |   |   |   |   | N |   |   |
  |-------------------------------|
2 |   | P | P | P |   | P | P | P |
  |-------------------------------|
1 | R | N | B | Q | K | B |   | R |
  ---------------------------------
    a   b   c   d   e   f   g   h
""".strip('\n')  # the outer newlines are only there to make this code readable
        self.assertEqual(g.board_text, expected)


class MakeMoveTests(TestCase):
    """Tests GameState._make_move()"""

    def test_make_basic_move(self):
        """
        Should be able to handle moving a piece from one square to another.
        """
        g = GameState()
        g.board = {
            'a': {'1': 'R', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'r'},  # noqa
            'b': {'1': 'N', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'n'},  # noqa
            'c': {'1': 'B', '2': 'P', '3': ' ', '4': ' ', '5': 'p', '6': ' ', '7': ' ', '8': 'b'},  # noqa
            'd': {'1': 'Q', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'q'},  # noqa
            'e': {'1': 'K', '2': ' ', '3': ' ', '4': 'P', '5': ' ', '6': ' ', '7': 'p', '8': 'k'},  # noqa
            'f': {'1': 'B', '2': 'P', '3': 'N', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'b'},  # noqa
            'g': {'1': ' ', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'n'},  # noqa
            'h': {'1': 'R', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'r'},  # noqa
        }
        g._make_move('a2a4')
        expected = """
  ---------------------------------
8 | r | n | b | q | k | b | n | r |
  |-------------------------------|
7 | p | p |   | p | p | p | p | p |
  |-------------------------------|
6 |   |   |   |   |   |   |   |   |
  |-------------------------------|
5 |   |   | p |   |   |   |   |   |
  |-------------------------------|
4 | P |   |   |   | P |   |   |   |
  |-------------------------------|
3 |   |   |   |   |   | N |   |   |
  |-------------------------------|
2 |   | P | P | P |   | P | P | P |
  |-------------------------------|
1 | R | N | B | Q | K | B |   | R |
  ---------------------------------
    a   b   c   d   e   f   g   h
""".strip('\n')  # the outer newlines are only there to make this code readable
        self.assertEqual(g.board_text, expected)

    def test_correctly_handles_capturing(self):
        """
        When one piece lands on another, the other should be removed
        from the board, and moving piece should replace it.
        """
        g = GameState()
        g.board = {
            'a': {'1': 'R', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'r'},  # noqa
            'b': {'1': 'N', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'n'},  # noqa
            'c': {'1': 'B', '2': 'P', '3': ' ', '4': ' ', '5': 'p', '6': ' ', '7': ' ', '8': 'b'},  # noqa
            'd': {'1': 'Q', '2': 'P', '3': ' ', '4': ' ', '5': 'p', '6': ' ', '7': ' ', '8': 'q'},  # noqa
            'e': {'1': 'K', '2': ' ', '3': ' ', '4': 'P', '5': ' ', '6': ' ', '7': 'p', '8': 'k'},  # noqa
            'f': {'1': 'B', '2': 'P', '3': 'N', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'b'},  # noqa
            'g': {'1': ' ', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'n'},  # noqa
            'h': {'1': 'R', '2': 'P', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': 'p', '8': 'r'},  # noqa
        }
        g._make_move('e4d5')
        expected = """
  ---------------------------------
8 | r | n | b | q | k | b | n | r |
  |-------------------------------|
7 | p | p |   |   | p | p | p | p |
  |-------------------------------|
6 |   |   |   |   |   |   |   |   |
  |-------------------------------|
5 |   |   | p | P |   |   |   |   |
  |-------------------------------|
4 |   |   |   |   |   |   |   |   |
  |-------------------------------|
3 |   |   |   |   |   | N |   |   |
  |-------------------------------|
2 | P | P | P | P |   | P | P | P |
  |-------------------------------|
1 | R | N | B | Q | K | B |   | R |
  ---------------------------------
    a   b   c   d   e   f   g   h
""".strip('\n')  # the outer newlines are only there to make this code readable
        self.assertEqual(g.board_text, expected)

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
        game = GameState()
        game.board['a']['2'] = 'P'
        game._make_move('a2a4')
        self.assertEqual(game.en_passant, ('a', '3'))

    def test_en_passant_only_lasts_one_turn(self):
        """
        Even if there was previously an en passant square, if no pawn
        moved two spaces this turn, en passant should be set to None.
        """
        game = GameState()
        game.board['a']['1'] = 'R'
        game.en_passant = ('a', '3')
        game._make_move('a1a2')
        self.assertEqual(game.en_passant, None)

    def test_en_passant_non_pawn_moves(self):
        """When a non-pawn piece moves, en passant should be None."""
        game = GameState()
        game.board['a']['1'] = 'R'
        game._make_move('a1a2')
        self.assertEqual(game.en_passant, None)

    def test_en_passant_non_pawn_moves_two_squares(self):
        """
        Even if a non-pawn moves two spaces, en passant should be None.
        """
        game = GameState()
        game.board['a']['1'] = 'R'
        game._make_move('a1a3')
        self.assertEqual(game.en_passant, None)

    def test_en_passant_pawn_moves_one_square(self):
        """
        If pawn moves but it does not move two squares, en passant
        should be None.
        """
        game = GameState()
        game.board['a']['2'] = 'P'
        game._make_move('a2a3')
        self.assertEqual(game.en_passant, None)

    def test_halfmove_clock_increments_after_white_player_makes_move(self):
        """
        When either player makes a reversible move, the halfmove clock
        should be incremented. This tests for moves made by the white
        player.
        """
        game = GameState()
        game.board['a']['2'] = 'R'
        game.halfmove_clock = 3
        game._make_move('a2a3')
        self.assertEqual(game.halfmove_clock, 4)

    def test_halfmove_clock_increments_after_black_player_makes_move(self):
        """
        When either player makes a reversible move, the halfmove clock
        should be incremented. This tests for moves made by the black
        player.
        """
        game = GameState()
        game.board['a']['2'] = 'r'
        game.halfmove_clock = 3
        game._make_move('a2a3')
        self.assertEqual(game.halfmove_clock, 4)

    def test_halfmove_clock_resets_on_capture(self):
        """
        When a player captures a piece, the halfmove clock should be
        reset to 0.
        """
        game = GameState()
        game.board['a']['2'] = 'r'
        game.board['a']['3'] = 'R'
        game.halfmove_clock = 3
        game._make_move('a2a3')
        self.assertEqual(game.halfmove_clock, 0)


    def test_halfmove_clock_resets_on_pawn_move(self):
        """
        When a player moves a pawn, the halfmove clock should be reset
        to 0.
        """
        game = GameState()
        game.board['a']['2'] = 'P'
        game.board['a']['3'] = GameState.EMPTY
        game.halfmove_clock = 3
        game._make_move('a2a3')
        self.assertEqual(game.halfmove_clock, 0)

    def test_fullmove_number_increments_when_black_takes_a_turn(self):
        game = GameState()
        game.player = 'b'
        game.fullmove_number = 3
        game._make_move('a2a3')
        self.assertEqual(game.fullmove_number, 4)

    def test_fullmove_number_does_not_increment_when_white_moves(self):
        game = GameState()
        game.player = 'w'
        game.fullmove_number = 3
        game._make_move('a2a3')
        self.assertEqual(game.fullmove_number, 3)