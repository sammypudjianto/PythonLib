import pygame as p
from asset_loader import AssetLoader

WIN_WIDTH = WIN_HEIGHT = 500


class GameState():
    def __init__(self):
        self.asset_loader = AssetLoader()

    def update(self):
        pass

    def render(self):
        pass


def render(win, x, y, width, height):
    win.fill((0, 0, 0))
    p.draw.rect(win, (255, 0, 0), (x, y, width, height))
    p.display.update()


if __name__ == '__main__':
    p.init()

    win = p.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    p.display.set_caption("First Platformer Game")

    x = 50
    y = 420
    width = 40
    height = 50
    velocity = 5

    run = True
    is_jump = False
    jump_max_count = 10
    jump_count = jump_max_count

    left = False
    right = False
    walkCount = 0

    walk_right = []
    while run:
        p.time.delay(50)
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
        keys = p.key.get_pressed()
        if keys[p.K_LEFT] and x > velocity:
            x -= velocity
        elif keys[p.K_RIGHT] and x < (WIN_WIDTH - velocity - width):
            x += velocity
        if not(is_jump):
            if keys[p.K_UP] and y > velocity:
                y -= velocity
            elif keys[p.K_DOWN] and y < (WIN_HEIGHT - velocity - height):
                y += velocity
            elif keys[p.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -10:
                y -= (jump_count * abs(jump_count)) * 0.5
                jump_count -= 1
            else:
                is_jump = False
                jump_count = jump_max_count
        render(win, x, y, width, height)
