import math
import pygame
import random
from itertools import product

from .iron import Iron
import pygame
import random

from ..helpers.func import load_image
from ..helpers.variables import *


class Strike(pygame.sprite.Sprite):
    damage = 20
    """Класс выстрела"""
    def __init__(self, pos, mouse_pos, sender, muzzle):
        super().__init__(ALL_SPRITES)
        radius = 5
        self.address = sender
        self.destination = mouse_pos
        self.pos = pos
        self.add(STRIKE_GROUP)
        self.vector = (self.destination[0] - self.pos[0],
                       self.destination[1] - self.pos[1])
        self.hypotenuse = (self.vector[0] ** 2 + self.vector[1] ** 2) ** 0.5
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        try:
            self.rect = pygame.Rect(*pos, 2 * radius, 2 * radius).move(28 * self.vector[0] / self.hypotenuse, 28 * self.vector[1] / self.hypotenuse)
        except ZeroDivisionError:
            self.rect = pygame.Rect(*pos, 2 * radius, 2 * radius)
        self.current_angle = 0
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.vx, self.vy = 0, 0
        self.collision = False
        self.speed = 30

    def check_collision(self):
        for group in [TEXTURE_GROUP, self.address]:
            if pygame.sprite.spritecollideany(self, group):
                self.collision = True
                if self.address == ENEMY_TANK_GROUP and group == ENEMY_TANK_GROUP:
                    for tank in self.address:
                        if tank.rect.x - 20 < self.rect.x\
                                < tank.rect.x + tank.rect.width and \
                                tank.rect.y - 20 < self.rect.y \
                                < tank.rect.y + tank.rect.height:
                            tank.health -= self.damage
                elif self.address == TANK_GROUP and group == TANK_GROUP:
                    for tank in self.address:
                        tank.health -= self.damage
                self.kill()

    def update(self, *args):
        try:
            self.vx = round((self.vector[0] * self.speed) / self.hypotenuse)
            self.vy = round((self.vector[1] * self.speed) / self.hypotenuse)
        except ZeroDivisionError:
            self.vx = 0
            self.vy = 0
        # if self.destination[0] < self.pos[0]:
        #     self.vx = -1 * self.vx
        # if self.destination[1] < self.pos[1]:
        #     self.vy = -1 * self.vy
        self.rect = self.rect.move(self.vx, self.vy)


