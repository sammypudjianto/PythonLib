import pygame as p
from asset_loader import AssetLoader


class HitBox():

    def __init__(self, x, y, width, height, offset_x=0, offset_y=0):
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.x = x + self.offset_x
        self.y = y + self.offset_y
        self.width = width
        self.height = height
        self.collision_grace_period = 60
        self.collision_counter = self.collision_grace_period
        self.debug = True
        self.enabled = True

        loader = AssetLoader()
        self.hit_sound = loader.load_hit_sound()

    def collide(self, others):
        """
        check whether hitbox collides with another hitbox

        """
        can_collide = self.collision_counter >= self.collision_grace_period
        self.collision_counter += 1

        if not(self.enabled and others.enabled):
            return False
        elif (
                self.x < others.x + others.width and
                self.x + self.width > others.x and
                self.y < others.y + others.height and
                self.y + self.height > others.y and
                can_collide
        ):
            self.hit_sound.play()
            self.collision_counter = 0
            return True
        else:
            return False

    def update(self, win, x, y):
        self.x = x + self.offset_x
        self.y = y + self.offset_y

        if self.debug and self.enabled:
            p.draw.rect(
                win,
                (255, 0, 0),
                (self.x, self.y, self.width, self.height),
                2
            )
