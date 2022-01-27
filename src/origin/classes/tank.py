import pygame
import random

from .texture_pack.bonus import Heal
from ..helpers.variables import ALL_SPRITES, TEXTURE_GROUP, CELL_SIZE, \
    TANK_GROUP, STRIKE_GROUP, HEAL_BONUS_GROUP
from ..helpers.func import load_image


class Tank(pygame.sprite.Sprite):
    """Базовый танк класс"""
    def __init__(self, x, y):
        super().__init__(ALL_SPRITES)
        self.health = 100
        self.image = pygame.transform.scale(load_image("old_tank.png"),
                                            (CELL_SIZE, CELL_SIZE))
        self.rect = pygame.Rect(x, y, CELL_SIZE,
                                CELL_SIZE)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)
        self.healed = False

    def check_collision(self):
        if pygame.sprite.spritecollideany(self, HEAL_BONUS_GROUP):
            if not self.healed and self.health < 100:
                if self.health + Heal.heal_points > 100:
                    self.health = 100
                else:
                    self.health += Heal.heal_points
                self.healed = True

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, TEXTURE_GROUP):
            self.vy = -self.vy
            self.vx = -self.vx

