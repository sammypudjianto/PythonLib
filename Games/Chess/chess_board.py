import pygame as p
from game_object import GameObject


class ChessBoard(GameObject):
    WIDTH = HEIGHT = 512

    def __init__(self):
        super().__init__((0, 0), (self.WIDTH, self.HEIGHT))
        self.tile_names = [
            col + str(row) for col in 'ABCDEFGH'
            for row in range(1, 9)
        ]

        self.tiles = {}

    def setup_tiles(self, win):
        initial_x = 20
        initial_y = 40
        tile_size = self.WIDTH // 8

        for i, tile_name in enumerate(self.tile_names):
            col_offset = (i) // 8
            row_offset = (i) % 8
            color = (
                p.Color('white')
                if (i + col_offset) % 2 == 0 else p.Color('dark gray')
            )
            x = initial_x + col_offset * tile_size
            y = initial_y + row_offset * tile_size

            t = Tile(tile_name, x, y, tile_size, color)
            self.tiles[tile_name] = t
            t.draw(win)


class Tile(GameObject):
    def __init__(self, name, x, y, size, color):
        super().__init__((x, y), (size, size))
        self.name = name
        self.color = color

    def draw(self, win):
        p.draw.rect(win, self.color, self.pos + self.size)
