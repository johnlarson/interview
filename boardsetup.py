class BoardSetup:

    def __init__(self, fen_file_path):
        with open(fen_file_path) as fen_file:
            fen_str = fen_file.read()
        self._parse_fen(fen_str)

    def _parse_fen(self, fen_list):
        self._parse_board(fen_list[0])
        self._parse_turn(fen_list[1])
        self._parse_castling(fen_list[2])
        self._parse_en_passant(fen_list[3])
        self._parse_halfmove_clock(fen_list[4])
        self._parse_fullmove_number(fen_list[5])

    def _parse_board(self, board_str):
        ...

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

    def __str__(self):
        return self.fen

    @property
    def fen(self):
        return ''

    @property
    def board_text(self):
        return ''

    def take_turn(self):
        ...

    def _get_suggested_move(self):
        return ''

    def _make_move(self, move):
        ...