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
    """Класс выстрела"""
    def __init__(self, pos, mouse_pos, sender):
        super().__init__(ALL_SPRITES)
        radius = 10
        self.address = sender
        self.destination = mouse_pos
        self.pos = pos
        self.add(STRIKE_GROUP)
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(*pos, 2 * radius, 2 * radius)
        self.current_angle = 0
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.vx, self.vy = 0, 0
        self.vector = (self.destination[0] - self.pos[0],
                       self.destination[1] - self.pos[1])
        self.hypotenuse = (self.vector[0] ** 2 + self.vector[1] ** 2) ** 0.5
        self.collision = False
        self.damage = 20

    def check_collision(self):
        for group in [TEXTURE_GROUP, self.address]:
            if pygame.sprite.spritecollideany(self, group):
                self.collision = True

    def update(self, *args):
        try:
            self.vx = round((self.vector[0] * 10) / self.hypotenuse)
            self.vy = round((self.vector[1] * 10) / self.hypotenuse)
        except ZeroDivisionError:
            self.vx = 0
            self.vy = 0
        # if self.destination[0] < self.pos[0]:
        #     self.vx = -1 * self.vx
        # if self.destination[1] < self.pos[1]:
        #     self.vy = -1 * self.vy
        # if pygame.sprite.spritecollideany(self, TEXTURE_GROUP):
        #     self.kill()
        self.rect = self.rect.move(self.vx, self.vy)
        if self.collision:
            self.kill()
            self.collision = False


