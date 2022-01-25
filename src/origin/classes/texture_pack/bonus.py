import pygame as pg


from ..texture import Texture
from origin.helpers.func import load_image
from origin.helpers.variables import CELL_SIZE, STRIKE_GROUP, SCREEN, \
    HEAL_BONUS_GROUP


class Heal(Texture):
    """Класс кирпичей"""
    heal_points = 50
    def __init__(self, *args):
        print(args)
        super().__init__(*args)
        self.add(HEAL_BONUS_GROUP)
        self.heal_points = 50
        self.image = load_image("texture_pack/bonus.png")

    def check_collision(self):
        pass

