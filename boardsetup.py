class BoardSetup:

    def __init__(self, fen):
        ...

    def __str__(self):
        ...

    @property
    def fen(self):
        return ''

    @property
    def board_text(self):
        return ''

    def _make_move(self, move):
        ...

    def _get_suggested_move(self):
        return ''

    def take_turn(self):
        ...