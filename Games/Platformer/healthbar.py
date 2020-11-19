import pygame as p


class HealthBar:
    def __init__(self, x, y, width, offset_x, offset_y):
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.x = x + offset_x
        self.y = y + offset_y
        self.width = width * 5
        self.height = 5

    def update(self, win, health, x, y):
        self.x = x + self.offset_x
        self.y = y + self.offset_y
        p.draw.rect(
            win,
            (0, 255, 0),
            (self.x, self.y, self.width, self.height)
        )  # green
        p.draw.rect(
            win,
            (255, 0, 0),
            (
                self.x + 5 * (10 - health),
                self.y,
                self.width - 5 * (10 - health),
                self.height)
        )  # red
