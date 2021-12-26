import pygame as pg

from ..helpers.variables import *
from ..helpers.func import load_image

from .texture import Texture


class Iron(Texture):
    """Класс железного блока, при попадании не ломается"""
    def __init__(self, *args):
        super().__init__(*args)
        self.image = pg.transform.scale(load_image("good_brick.png"),
                                            (CELL_SIZE, CELL_SIZE))