import pygame as p
from asset_loader import AssetLoader
from hitbox import HitBox
from player_states import CharacterFacing


class Projectiles():
    def __init__(self, x, y, color, curr_state):
        self.x = x
        self.y = y
        self.radius = 4
        self.color = color
        self.movement_speed = 5
        self.hitbox = HitBox(self.x, self.y, self.radius * 2, self.radius * 2)

        if curr_state.facing == CharacterFacing.RIGHT:
            self.facing = 1
        elif curr_state.facing == CharacterFacing.LEFT:
            self.facing = -1
        else:
            self.facing = 0

        loader = AssetLoader()
        loader.load_bullet_sound().play()

    def update(self, win):
        p.draw.circle(win, self.color, (self.x, self.y), self.radius)
        self.x += self.movement_speed * self.facing
        self.hitbox.update(win, self.x, self.y)
