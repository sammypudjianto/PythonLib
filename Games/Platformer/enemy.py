from asset_loader import AssetLoader
from healthbar import HealthBar
from hitbox import HitBox


class Enemy():
    def __init__(self):
        self.x = 10
        self.y = 400
        self.width = 20
        self.height = 50
        self.health = 10
        self.hitbox = HitBox(
            self.x, self.y, self.width, self.height, 20, 5
        )
        self.healthbar = HealthBar(self.x, self.y, self.health, 20, -5)
        self.path = [10, 450]
        self.walkcount = 0
        self.movement_speed = 1
        loader = AssetLoader()
        self.animations = {
            'walkright': loader.load_enemy_walk_right_sprites(),
            'walkleft': loader.load_enemy_walk_left_sprites(),
        }
        self.visible = True

    def update(self, win):
        if self.visible:
            self.move()

            if self.walkcount + 1 >= 33:
                self.walkcount = 0

            if self.movement_speed > 0:
                win.blit(
                    self.animations['walkright'][self.walkcount//3],
                    (self.x, self.y))
            else:
                win.blit(
                    self.animations['walkleft'][self.walkcount//3],
                    (self.x, self.y))

            self.walkcount += 1

            self.hitbox.update(win, self.x, self.y)
            self.healthbar.update(win, self.health, self.x, self.y)

            if self.health == 0:
                self.visible = False
                self.hitbox.enabled = False

    def move(self):
        if (
            self.x + self.width >= self.path[1] or
            self.x < self.path[0]
        ):
            self.movement_speed *= -1

        self.x += self.movement_speed
