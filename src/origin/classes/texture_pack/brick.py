import pygame as pg

from ..inheritors.texture import Texture
from origin.helpers.variables import CELL_SIZE, SCREEN, STRIKE_GROUP
from origin.helpers.func import load_image


class Brick(Texture):
    """Класс кирпичей"""
    def __init__(self, *args):
        super().__init__(*args)
        self.image = load_image(r"texture_pack\good_brick.png")
        self.hp = 3

    def check_collision(self):
        if pg.sprite.spritecollideany(self, STRIKE_GROUP):
            self.hp -= 1

    def update(self, *args):
        if not self.hp:
            self.board.set_empty(self.pos)
            self.music['break'].play()
            self.kill()
        elif self.hp == 2:
            self.image = load_image(r"texture_pack\hitted_brick.png")
        elif self.hp == 1:
            self.image = load_image(r"texture_pack\crashing_brick.png")
