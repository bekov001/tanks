import pygame as pg

from src.origin.helpers.func import load_image
from src.origin.helpers.variables import *

from src.origin.classes.texture import Texture


class Brick(Texture):
    """Класс кирпичей"""
    def __init__(self, *args):
        super().__init__(*args)
        self.image = pg.transform.scale(load_image("good_brick.png"),
                                            (CELL_SIZE, CELL_SIZE))

    def update(self, *args):
        print(121312312312)
        if pg.sprite.spritecollideany(self, STRIKE_GROUP):
            self.board.set_empty(self.pos)
            self.kill()
