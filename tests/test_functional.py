from unittest import TestCase


class Task1Tests(TestCase):
    """Functional tests for Task 1."""

    def test_valid_input(self):
        """If input is valid, it should correctly display the board."""
        ...

    def test_no_fen_file_provided(self):
        """If the user does not provide a fen file, show usage."""
        ...

    def test_invalid_file_path(self):
        """If file path is invalid, display 'File not found.'"""
        ...

    def test_invalid_fen_file(self):
        """If fen file is invalid, display 'Invalid FEN file.'"""
        ...


class Task2Tests(TestCase):
    """Functional tests for Task 2."""

    def test_valid_input(self):
        """
        If input is valid, it should make the move directed by the api
        and display the resulting fen-formatted text.
        """
        ...

    def test_no_fen_file_provided(self):
        """If the user does not provide a fen file, show usage."""
        ...

    def test_invalid_file_path(self):
        """If file path is invalid, display 'File not found.'"""
        ...

    def test_invalid_fen_file(self):
        """If fen file is invalid, display 'Invalid FEN file.'"""
        ...


class StretchTaskTests(TestCase):
    """Functional tests for stretch task."""

    def test_valid_input(self):
        """
        If input is valid, it should make the move directed by the api
        and display the resulting board and fen-formatted game state.
        """
        ...

    def test_no_fen_file_provided(self):
        """If the user does not provide a fen file, show usage."""
        ...

    def test_invalid_file_path(self):
        """If file path is invalid, display 'File not found.'"""
        ...

    def test_invalid_fen_file(self):
        """If fen file is invalid, display 'Invalid FEN file.'"""
        ...