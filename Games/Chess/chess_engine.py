import pygame as p

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT/DIMENSION
MAX_FPS = 8


def load_images():
    """
    load images from the images folder
    """
    images = []
    pieces = ["bB", "bK"]
    for piece in pieces:
        images[piece] = p.image.load("Images/" + piece + ".png")


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    # gs = chess_engine.GameState()
    load_images()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        clock.tick(MAX_FPS)
        p.display.flip()


def draw_game_state(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)


def draw_board(screen):
    pass


def draw_pieces(screen, board):
    pass


if __name__== '__main__':
    main()
