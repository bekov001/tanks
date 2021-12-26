import pygame as pg

from ..helpers.func import load_image
from ..helpers.variables import *

from .texture import Texture


class Brick(Texture):
    """Класс кирпичей"""
    def __init__(self, *args):
        super().__init__(*args)
        self.image = pg.transform.scale(load_image("good_brick.png"),
                                            (CELL_SIZE, CELL_SIZE))

    def update(self, *args):
        if pg.sprite.spritecollideany(self, STRIKE_GROUP):
            self.board.set_empty(self.pos)
            self.kill()
