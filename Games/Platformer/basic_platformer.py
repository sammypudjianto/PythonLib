import pygame as p
from asset_loader import AssetLoader
from enemy import Enemy
from player import Player


class GameState():

    WIN_WIDTH = 500
    WIN_HEIGHT = 480

    def __init__(self):
        p.init()
        p.display.set_caption("First Platformer Game")
        self.win = p.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT))

        self.player = Player()
        self.enemy = Enemy()
        asset_loader = AssetLoader()
        self.bg = asset_loader.load_background()
        self.music = asset_loader.load_music()
        self.music.play(-1)

        self.score = 0
        self.clock = p.time.Clock()

    def update(self):
        run = True
        while run:
            self.win.blit(self.bg, (0, 0))
            self.clock.tick(60)

            for event in p.event.get():
                if event.type == p.QUIT:
                    run = False

            self.player.update(self.win)
            self.enemy.update(self.win)
            self._check_collision()
            self._display_score()
            p.display.update()

    def _check_collision(self):
        """
        1. check collision between enemy vs player
        2. check collision between enemy vs player bullets
        """
        enemy_collided = self.player.hitbox.collide(self.enemy.hitbox)
        if enemy_collided:
            self.player.health -= 1
            print('player vs enemy hit')  # reduce health of the player

        bullets = self.player.bullets
        for bullet in bullets:
            bullet_hit = bullet.hitbox.collide(self.enemy.hitbox)
            if bullet_hit:
                bullets.remove(bullet)
                self.score += 1
                self.enemy.health -= 1
                print('bullet hit vs enemy')

    def _display_score(self):
        font = p.font.SysFont('comicsans', 30, True)
        text = font.render('Score: ' + str(self.score), 1, (0, 0, 0))
        self.win.blit(text, (390, 10))


if __name__ == '__main__':
    game = GameState()
    game.update()
