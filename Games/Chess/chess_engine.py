import pygame as p
from chess_board import ChessBoard
from chess_pieces import ChessPieces


class GameState():
    WIDTH = 800
    HEIGHT = 600
    DIMENSION = 8
    SQ_SIZE = HEIGHT/DIMENSION
    MAX_FPS = 8

    def __init__(self):
        p.init()

        self.win = p.display.set_mode((self.WIDTH, self.HEIGHT))
        p.display.set_caption("A Game of Chess")
        self.win.fill(p.Color('brown'))
        self.__initialise_board()
        self.__initialise_pieces()
        self.clock = p.time.Clock()

    def __initialise_board(self):
        # initialise tiles
        self.board = ChessBoard()
        self.board.setup_tiles(self.win)

    def __initialise_pieces(self):
        # initialise pieces
        self.pieces = ChessPieces()
        for wpiece in self.pieces.white_pieces:
            wpiece.draw(self.win, self.board.tiles)

        for bpiece in self.pieces.black_pieces:
            bpiece.draw(self.win, self.board.tiles)

    def update(self):
        run = True
        self.clock.tick(self.MAX_FPS)
        while run:
            for e in p.event.get():
                if e.type == p.QUIT:
                    run = False

            # render
            p.display.flip()    # what is this?
            p.display.update()


if __name__ == '__main__':
    game_of_chess = GameState()
    game_of_chess.update()
