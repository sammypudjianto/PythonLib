import pygame as p
from healthbar import HealthBar
from hitbox import HitBox
from player_states import (CharacterFacing, PlayerJump, PlayerStanding,
                           PlayerWalkingLeft, PlayerWalkingRight)
from projectiles import Projectiles


class Player():
    def __init__(self):
        self.pos_x = 50
        self.pos_y = 400
        self.width = 20
        self.height = 50
        self.health = 10
        self.hitbox = HitBox(
            self.pos_x, self.pos_y, self.width,
            self.height, 20, 15
        )
        self.healthbar = HealthBar(
            self.pos_x,
            self.pos_y,
            self.health,
            20,
            5
        )
        self.movement_speed = 5
        self.bullet_timer = 0
        self.bullet_canshoot_timer = 30
        self.bullets = []
        self.all_states = {
            'stand': PlayerStanding(),
            'jump': PlayerJump(),
            'left': PlayerWalkingLeft(),
            'right': PlayerWalkingRight()
        }
        self.curr_state = self.all_states['stand']
        self.visible = True

    def update(self, win):
        if self.visible:
            self.curr_state = self.curr_state.update(
                                                win,
                                                self,
                                                self.all_states
                                                )
            self.hitbox.update(win, self.pos_x, self.pos_y)
            self._update_bullet_fire(win)

            self.healthbar.update(win, self.health, self.pos_x, self.pos_y)

            if self.health == 0:
                self.visible = False
                self.hitbox.enabled = False

    def _update_bullet_fire(self, win):
        keys = p.key.get_pressed()

        if (
            keys[p.K_SPACE] and
            self.curr_state.facing != CharacterFacing.FRONT and
            self.bullet_timer >= self.bullet_canshoot_timer
        ):
            self.bullet_timer = 0
            bullet = Projectiles(
                    self.pos_x + int(self.curr_state.facing) * self.width//2,
                    self.pos_y + self.height//2,
                    (0, 0, 0),
                    self.curr_state
                )
            self.bullets.append(bullet)

        for bullet in self.bullets:
            bullet.update(win)
            if bullet.x < 0 or bullet.x > win.get_width():
                self.bullets.remove(bullet)

        self.bullet_timer += 1

    def hit(self, others):
        pass
