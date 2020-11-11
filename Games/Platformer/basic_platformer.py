from enum import Enum

import pygame as p
from asset_loader import AssetLoader

WIN_WIDTH = 500
WIN_HEIGHT = 480


class Action(Enum):
    STANDING = 0
    WALK_LEFT = 1
    WALK_RIGHT = 2


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


def redraw_game_window(win, walkcount, action, animation, bg):
    # setup the background
    win.blit(bg, (0, 0))

    if walkcount + 1 >= 27:
        walkcount = 0

    if action == Action.WALK_LEFT:
        win.blit(animation[walkcount//3], (x, y))
        walkcount += 1

    elif action == Action.WALK_RIGHT:
        win.blit(animation[walkcount//3], (x, y))
        walkcount += 1

    else:
        win.blit(animation[0], (x, y))

    p.display.update()


if __name__ == '__main__':
    p.init()

    win = p.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    p.display.set_caption("First Platformer Game")

    loader = AssetLoader()
    walk_right = loader.load_walk_right_sprites()
    walk_left = loader.load_walk_left_sprites()
    bg = loader.load_background()
    char = loader.load_character()
    animation = {
        'walk_right': walk_right,
        'walk_left': walk_left,
        'character': char
        }

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
    walkcount = 0

    walk_right = []
    while run:
        p.time.delay(50)

        for event in p.event.get():
            if event.type == p.QUIT:
                run = False

        keys = p.key.get_pressed()
        anim = animation['character']

        if keys[p.K_LEFT] and x > velocity:
            x -= velocity
            anim = animation['walk_left']
            action = Action.WALK_LEFT
        elif keys[p.K_RIGHT] and x < (WIN_WIDTH - velocity - width):
            x += velocity
            anim = animation['walk_right']
            action = Action.WALK_RIGHT
        else:
            anim = animation['character']
            action = Action.STANDING

        if not(is_jump):
            is_jump = keys[p.K_SPACE]
        else:
            if jump_count >= -10:
                y -= (jump_count * abs(jump_count)) * 0.5
                jump_count -= 1
            else:
                is_jump = False
                jump_count = jump_max_count

        redraw_game_window(win, walkcount, action, anim, bg)
