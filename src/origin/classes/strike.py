import math
import pygame
import random
from itertools import product

from .tank import Tank
import pygame
import random

from ..helpers.func import load_image
from ..helpers.variables import *


class Strike(pygame.sprite.Sprite):
    """Класс выстрела"""
    def __init__(self, tank_pos, mouse_pos):
        super().__init__(ALL_SPRITES)
        radius = 10
        self.add(STRIKE_GROUP)
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(*tank_pos, 2 * radius, 2 * radius)
        self.current_angle = 0
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.vx, self.vy = (mouse_pos[0] - tank_pos[0]) // 3, (mouse_pos[1] - tank_pos[1]) // 3
        self.pos = (3, 3)
        self.step = 10

    def update(self, *args):
        step_x, step = 0, 0
        if self.vx > 0:
            self.vx -= self.step
            step_x = self.step
        if self.vy > 0:
            self.vy -= self.step
            step = self.step
        if pygame.sprite.spritecollideany(self, TEXTURE_GROUP):
            self.kill()
        self.rect = self.rect.move(step_x, step)