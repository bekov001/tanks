import pygame


from ..helpers.func import load_image
from ..helpers.variables import ALL_SPRITES
from .bonus import Bonus


class Heal(Bonus):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = pg.transform.scale(load_image("heal.png"),
                                        (CELL_SIZE, CELL_SIZE))
        self.heal_points = 20

    def update(self):
        if pygame.sprite.spritecollideany(self, ALL_SPRITES):
            self.kill()

