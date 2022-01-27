import pygame as pg

from src.origin.helpers.variables import *
from src.origin.helpers.func import load_image

from src.origin.classes.texture import Texture


class Iron(Texture):
    """Класс железного блока, при попадании не ломается"""
    def __init__(self, *args):
        super().__init__(*args)
        self.image = pg.transform.scale(load_image("new_iron.png"),
                                        (CELL_SIZE, CELL_SIZE))

    def update(self):
        pass
