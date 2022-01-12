import pygame
import random

from ..helpers.variables import ALL_SPRITES, TEXTURE_GROUP, CELL_SIZE, TANK_GROUP, BONUS_GROUP, STRIKE_GROUP
from ..helpers.func import load_image
from .heal_bonus import Heal


class Tank(pygame.sprite.Sprite):
    """Базовый танк класс"""
    def __init__(self, x, y):
        super().__init__(ALL_SPRITES)
        self.add(TANK_GROUP)
        self.health = 100
        self.heal = False
        self.hit = False
        self.image = pygame.transform.scale(load_image("old_tank.png"),
                                            (CELL_SIZE, CELL_SIZE))
        self.rect = pygame.Rect(x, y, CELL_SIZE,
                                CELL_SIZE)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)

    def check_collision(self):
        if pygame.sprite.spritecollideany(self, STRIKE_GROUP):
            self.hit = True
        if pygame.sprite.spritecollideany(self, Heal):
            self.heal = True
            print('heal')

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, TEXTURE_GROUP):
            self.vy = -self.vy
            self.vx = -self.vx
