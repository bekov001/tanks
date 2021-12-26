from classes.texture import Texture
from helpers import load_image, CELL_SIZE, STRIKE_GROUP
import pygame as pg


class Brick(Texture):
    """Класс железного блока, при попадании не ломается"""
    def __init__(self, *args):
        super().__init__(*args)
        self.image = pg.transform.scale(load_image("good_brick.png"),
                                            (CELL_SIZE, CELL_SIZE))