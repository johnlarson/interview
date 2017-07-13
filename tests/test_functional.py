from unittest import TestCase
from subprocess import check_output, CalledProcessError


class Task1Tests(TestCase):
    """Functional tests for Task 1."""

    def test_valid_input(self):
        """If input is valid, it should correctly display the board."""
        actual = check_output(['python3', '1_show.py', 'tests/fen/valid.fen'])
        expected = b"""
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

"""
        self.assertEqual(actual, expected)

    def test_no_fen_file_provided(self):
        """If the user does not provide a fen file, show usage."""
        try:
            actual = check_output(['python3', '1_show.py'])
            self.fail()
        except CalledProcessError as err:
            usage = b'Usage: python 1_show.py <path/to/fen/file.fen>'
            self.assertEqual(err.output, usage)

    def test_invalid_file_path(self):
        """
        If file path is invalid, display 'FEN File not found: <path>'.
        """
        try:
            args = ['python3', '1_show.py', 'tests/fen/idontexist.fen']
            actual = check_output(args)
            self.fail()
        except CalledProcessError as err:
            message = 'FEN File not found: tests/fen/idontexist.fen'
            self.assertEqual(err.output, message)

    def test_invalid_fen_file(self):
        """
        If fen file is invalid, display 'FEN file invalid: <path>'.
        """
        try:
            args = ['python3', '1_show.py', 'tests/fen/invalid.fen']
            actual = check_output(args)
            self.fail()
        except CalledProcessError as err:
            message = 'FEN File invalid: tests/fen/invalid.fen'
            self.assertEqual(err.output, message)


class Task2Tests(TestCase):
    """Functional tests for Task 2."""

    def test_valid_input(self):
        """
        If input is valid, it should make the move directed by the api
        and display the resulting fen-formatted text.
        """
        actual = check_output(['python3', '2_move.py', 'tests/fen/valid.fen'])
        expected = (b'rnbqkbnr/1p1ppppp/8/p1p5/4P3/5N2/PPPP1PPP/RNBQKB1R '
                    b'w KQkq a6 0 3\n')
        self.assertEqual(actual, expected)

    def test_no_fen_file_provided(self):
        """If the user does not provide a fen file, show usage."""
        try:
            actual = check_output(['python3', '1_show.py'])
            self.fail()
        except CalledProcessError as err:
            usage = b'Usage: python 2_move.py <path/to/fen/file.fen>'
            self.assertEqual(err.output, usage)

    def test_invalid_file_path(self):
        """
        If file path is invalid, display 'FEN File not found: <path>'.
        """
        try:
            args = ['python3', '2_move.py', 'tests/fen/idontexist.fen']
            actual = check_output(args)
            self.fail()
        except CalledProcessError as err:
            message = 'FEN File not found: tests/fen/idontexist.fen'
            self.assertEqual(err.output, message)

    def test_invalid_fen_file(self):
        """
        If fen file is invalid, display 'FEN file invalid: <path>'.
        """
        try:
            args = ['python3', '2_move.py', 'tests/fen/invalid.fen']
            actual = check_output(args)
            self.fail()
        except CalledProcessError as err:
            message = 'FEN File invalid: tests/fen/invalid.fen'
            self.assertEqual(err.output, message)


class StretchTaskTests(TestCase):
    """Functional tests for stretch task."""

    def test_valid_input(self):
        """
        If input is valid, it should make the move directed by the api
        and display the resulting board and fen-formatted game state.
        """
        actual = check_output(['python3', 'stretch.py', 'tests/fen/valid.fen'])
        expected = b"""
  ---------------------------------
8 | r | n | b | q | k | b | n | r |
  |-------------------------------|
7 |   | p |   | p | p | p | p | p |
  |-------------------------------|
6 |   |   |   |   |   |   |   |   |
  |-------------------------------|
5 | p |   | p |   |   |   |   |   |
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

rnbqkbnr/1p1ppppp/8/p1p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq a6 0 3

"""
        self.assertEqual(actual, expected)

    def test_no_fen_file_provided(self):
        """If the user does not provide a fen file, show usage."""
        try:
            actual = check_output(['python3', 'stretch.py'])
            self.fail()
        except CalledProcessError as err:
            usage = b'Usage: python 1_show.py <path/to/fen/file.fen>'
            self.assertEqual(err.output, usage)

    def test_invalid_file_path(self):
        """
        If file path is invalid, display 'FEN File not found: <path>'.
        """
        try:
            args = ['python3', 'stretch.py', 'tests/fen/idontexist.fen']
            actual = check_output(args)
            self.fail()
        except CalledProcessError as err:
            message = 'FEN File not found: tests/fen/idontexist.fen'
            self.assertEqual(err.output, message)

    def test_invalid_fen_file(self):
        """
        If fen file is invalid, display 'FEN file invalid: <path>'.
        """
        try:
            args = ['python3', 'stretch.py', 'tests/fen/invalid.fen']
            actual = check_output(args)
            self.fail()
        except CalledProcessError as err:
            message = 'FEN File invalid: tests/fen/invalid.fen'
            self.assertEqual(err.output, message)