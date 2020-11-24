from enum import IntEnum

from asset_loader import AssetLoader


class BoardSide(IntEnum):
    WHITE = -1  # White moves up
    BLACK = 1   # Black moves down


class ChessPieces():
    def __init__(self):
        self.white_pieces = []
        self.black_pieces = []
        self.__initialize_positions()

    def __initialize_positions(self):
        loader = AssetLoader()
        white_sprites = loader.load_white_pieces()
        black_sprites = loader.load_black_pieces()

        self.white_pieces = [
            Rook('A8', white_sprites['R'], BoardSide.WHITE),
            Knight('B8', white_sprites['N'], BoardSide.WHITE),
            Bishop('C8', white_sprites['B'], BoardSide.WHITE),
            Queen('D8', white_sprites['Q'], BoardSide.WHITE),
            King('E8', white_sprites['K'], BoardSide.WHITE),
            Bishop('F8', white_sprites['B'], BoardSide.WHITE),
            Knight('G8', white_sprites['N'], BoardSide.WHITE),
            Rook('H8', white_sprites['R'], BoardSide.WHITE)
        ]
        white_pawns = [
            Pawn(col + '7', white_sprites['p'], BoardSide.WHITE)
            for col in 'ABCDEFGH'
        ]
        self.white_pieces.extend(white_pawns)

        self.black_pieces = [
            Rook('A1', black_sprites['R'], BoardSide.BLACK),
            Knight('B1', black_sprites['N'], BoardSide.BLACK),
            Bishop('C1', black_sprites['B'], BoardSide.BLACK),
            Queen('D1', black_sprites['Q'], BoardSide.BLACK),
            King('E1', black_sprites['K'], BoardSide.BLACK),
            Bishop('F1', black_sprites['B'], BoardSide.BLACK),
            Knight('G1', black_sprites['N'], BoardSide.BLACK),
            Rook('H1', black_sprites['R'], BoardSide.BLACK),
        ]

        black_pawns = [
            Pawn(col + '2', black_sprites['p'], BoardSide.BLACK)
            for col in 'ABCDEFGH'
        ]
        self.black_pieces.extend(black_pawns)


class ChessPiece():
    def __init__(self, initial_position, sprite, side):
        self.position = initial_position
        self.sprite = sprite
        self.side = side

    def list_possible_movement(self, win):
        column = ord(self.position[0])
        row = self.position[1]
        pass

    def draw(self, win, tiles):
        win.blit(self.sprite, tiles[self.position].pos)


class Pawn(ChessPiece):
    def __init__(self, initial_position, sprite, side):
        super().__init__(initial_position, sprite, side)
        self.possible_movement = [(0, 1)]


class Rook(ChessPiece):
    def __init__(self, initial_position, sprite, side):
        super().__init__(initial_position, sprite, side)
        self.possible_movement = [(0, 1)]

    def list_possible_movements(self):
        pass


class Knight(ChessPiece):
    def __init__(self, initial_position, sprite, side):
        super().__init__(initial_position, sprite, side)
        self.possible_movement = [(0, 1)]


class Bishop(ChessPiece):
    def __init__(self, initial_position, sprite, side):
        super().__init__(initial_position, sprite, side)
        self.possible_movement = [(0, 1)]


class Queen(ChessPiece):
    def __init__(self, initial_position, sprite, side):
        super().__init__(initial_position, sprite, side)
        self.possible_movement = [(0, 1)]


class King(ChessPiece):
    def __init__(self, initial_position, sprite, side):
        super().__init__(initial_position, sprite, side)
        self.possible_movement = [(0, 1)]
