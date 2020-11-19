from enum import IntEnum

import pygame as p
from asset_loader import AssetLoader


class CharacterFacing(IntEnum):
    FRONT = 0
    RIGHT = 1
    LEFT = -1


class PlayerState():
    def __init__(self):
        self.walkcount = 0
        self.win_width, self.win_height = p.display.get_surface().get_size()
        self.facing = CharacterFacing. FRONT

    def update(self, win, player, all_states):
        if self.walkcount + 1 >= 27:
            self.walkcount = 0

    def facing(self):
        return self.facing


class PlayerWalkingLeft(PlayerState):
    def __init__(self):
        super().__init__()
        loader = AssetLoader()
        self.animation = loader.load_walk_left_sprites()
        self.facing = CharacterFacing.LEFT

    def update(self, win, player, all_states):
        super().update(win, player, all_states)
        player.pos_x -= player.movement_speed
        player.pos_x = max(player.pos_x, 0)
        win.blit(
            self.animation[self.walkcount//3],
            (player.pos_x, player.pos_y)
            )
        self.walkcount += 1

        keys = p.key.get_pressed()
        if keys[p.K_LEFT]:
            return self
        if keys[p.K_RIGHT]:
            return all_states['right']
        if keys[p.K_UP]:
            return all_states['jump']
        else:
            stand_obj = all_states['stand']
            stand_obj.update_direction(self.animation, self.facing)
            return stand_obj


class PlayerWalkingRight(PlayerState):
    def __init__(self):
        super().__init__()
        loader = AssetLoader()
        self.animation = loader.load_walk_right_sprites()
        self.facing = CharacterFacing.RIGHT

    def update(self, win, player, all_states):
        super().update(win, player, all_states)
        max_pos_x = self.win_width - player.movement_speed - player.width
        player.pos_x += player.movement_speed
        player.pos_x = min(player.pos_x, max_pos_x)

        win.blit(
            self.animation[self.walkcount//3],
            (player.pos_x, player.pos_y)
            )
        self.walkcount += 1

        keys = p.key.get_pressed()
        if keys[p.K_LEFT]:
            return all_states['left']
        if keys[p.K_RIGHT]:
            return self
        if keys[p.K_UP]:
            return all_states['jump']
        else:
            stand_obj = all_states['stand']
            stand_obj.update_direction(self.animation, self.facing)
            return stand_obj


class PlayerStanding(PlayerState):
    def __init__(self):
        super().__init__()
        loader = AssetLoader()
        self.animation = loader.load_character()
        self.facing = CharacterFacing.FRONT

    def update(self, win, player, all_states):
        win.blit(self.animation[0], (player.pos_x, player.pos_y))

        keys = p.key.get_pressed()
        if keys[p.K_LEFT]:
            return all_states['left']
        if keys[p.K_RIGHT]:
            return all_states['right']
        if keys[p.K_UP]:
            return all_states['jump']
        else:
            return self

    def update_direction(self, animation, facing):
        self.animation = animation
        self.facing = facing


class PlayerJump(PlayerState):
    def __init__(self):
        super().__init__()
        self.jump_max_count = 10
        self.jump_count = self.jump_max_count
        loader = AssetLoader()
        self.standing = loader.load_character()
        self.lookleft = loader.load_walk_left_sprites()
        self.lookright = loader.load_walk_right_sprites()
        self.animation = self.standing

    def update(self, win, player, all_states):

        keys = p.key.get_pressed()
        if keys[p.K_LEFT]:
            player.pos_x -= player.movement_speed
            self.animation = self.lookleft
            self.facing = CharacterFacing.LEFT
        elif keys[p.K_RIGHT]:
            player.pos_x += player.movement_speed
            self.animation = self.lookright
            self.facing = CharacterFacing.RIGHT
        # else:
            # self.animation = self.standing
            # self.facing = CharacterFacing.FRONT

        max_pos_x = self.win_width - player.movement_speed - player.width
        player.pos_x = max(0, min(max_pos_x, player.pos_x))

        if self.jump_count >= -self.jump_max_count:
            player.pos_y -= (self.jump_count * abs(self.jump_count)) * 0.5
            self.jump_count -= 1
            win.blit(self.animation[0], (player.pos_x, player.pos_y))
            return self
        else:
            self.jump_count = self.jump_max_count
            win.blit(self.animation[0], (player.pos_x, player.pos_y))
            return all_states['stand']
