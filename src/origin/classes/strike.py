import math
from itertools import product

from .tank import Tank
import pygame
import random

from helpers import *


class Strike(pygame.sprite.Sprite):
    def __init__(self, tank_pos, mouse_pos):
        super().__init__(ALL_SPRITES)
        radius = 10
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(*tank_pos, 2 * radius, 2 * radius)
        self.current_angle = 0
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.vx, self.vy = (mouse_pos[0] - tank_pos[0]), (mouse_pos[1] - tank_pos[1])
        print(self.vx, self.vy)

    def update(self, *args):
        self.rect = self.rect.move(self.vx, self.vy)