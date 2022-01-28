import pygame as pg


from ..texture import Texture
from origin.helpers.func import load_image
from origin.helpers.variables import CELL_SIZE, STRIKE_GROUP, SCREEN, \
    HEAL_BONUS_GROUP, ALL_SPRITES, TANK_GROUP, ENEMY_TANK_GROUP, \
    COOLDOWN_BONUS_GROUP


class Heal(Texture):
    """Класс кирпичей"""
    heal_points = 40

    def __init__(self, *args):
        super().__init__(*args)
        self.add(HEAL_BONUS_GROUP)
        self.heal_points = 50
        self.image = load_image("texture_pack/bonus.png")
        self.collision = False

    def check_collision(self):
        for group in [TANK_GROUP, ENEMY_TANK_GROUP, STRIKE_GROUP]:
            if pg.sprite.spritecollideany(self, group):
                self.collision = True

    def update(self):
        if self.collision:
            self.kill()


class CoolDown(Texture):
    """Класс кирпичей"""
    cooldown_time = 40

    def __init__(self, *args):
        super().__init__(*args)
        self.add(COOLDOWN_BONUS_GROUP)
        self.image = load_image("texture_pack/bonus.png")
        self.collision = False

    def check_collision(self):
        for group in [TANK_GROUP, ENEMY_TANK_GROUP, STRIKE_GROUP]:
            if pg.sprite.spritecollideany(self, group):
                self.collision = True

    def update(self):
        if self.collision:
            self.kill()

