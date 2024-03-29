import pygame
import random
import time

from ..texture_pack.bonus import Heal, CoolDown
from origin.helpers.variables import ALL_SPRITES, TEXTURE_GROUP, CELL_SIZE, \
    TANK_GROUP, STRIKE_GROUP, HEAL_BONUS_GROUP, COOLDOWN_BONUS_GROUP
from origin.helpers.func import load_image


class Tank(pygame.sprite.Sprite):
    """Базовый танк класс"""
    def __init__(self, x, y, music):
        super().__init__(ALL_SPRITES)
        self.health = 100
        self.image = pygame.transform.scale(load_image("base/player_base.png"),
                                            (CELL_SIZE, CELL_SIZE))
        self.rect = pygame.Rect(x, y, CELL_SIZE,
                                CELL_SIZE)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)
        self.music = music
        self.healed = False
        self.delay = 3
        self.cd_time = 0

    def check_collision(self):
        if pygame.sprite.spritecollideany(self, HEAL_BONUS_GROUP):
            if not self.healed:
                self.health = 100
                self.healed = True
                self.music['boost'].play()
        if pygame.sprite.spritecollideany(self, COOLDOWN_BONUS_GROUP):
            self.cd_time = time.time()
            self.delay = CoolDown.cooldown_time
            self.music['boost'].play()

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, TEXTURE_GROUP):
            self.vy = -self.vy
            self.vx = -self.vx

