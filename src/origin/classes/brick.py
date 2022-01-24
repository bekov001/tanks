import pygame as pg

from origin.helpers.func import load_image
from origin.helpers.variables import *

from .texture import Texture


class Brick(Texture):
    """Класс кирпичей"""
    def __init__(self, *args):
        super().__init__(*args)
        self.image = pg.transform.scale(load_image("good_brick.png"),
                                            (CELL_SIZE, CELL_SIZE))
        self.hp = 3

    def check_collision(self):
        if pygame.sprite.spritecollideany(self, STRIKE_GROUP):
            self.hp -= 1

    def show_xp(self):
        xp = self.hp / 3
        pygame.draw.rect(SCREEN, "green", (self.rect.x, self.rect.y - 10, CELL_SIZE * xp, 5))
        pygame.draw.rect(SCREEN, "red",
                         (self.rect.x + CELL_SIZE * xp, self.rect.y - 10, CELL_SIZE - CELL_SIZE * xp, 5))

    def update(self, *args):
        if not self.hp:
            self.board.set_empty(self.pos)
            self.kill()
        elif self.hp <= 2:
            self.show_xp()
