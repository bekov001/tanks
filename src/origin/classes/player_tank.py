from itertools import product
import time
import pygame
import math
import random

from .strike import Strike
from .tank import Tank
from ..helpers import CELL_SIZE, TANK_GROUP, ENEMY_TANK_GROUP, load_image
from .player_muzzle import Muzzle


class PlayerTank(Tank):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.add(TANK_GROUP)
        self.image = pygame.transform.scale(load_image("player_tank.png"),
                                            (CELL_SIZE, CELL_SIZE))
        self.muzzle = Muzzle("player_muzzle.png", x, y)
        self.current_angle = 0
        self.created = time.time()

    def strike(self, event):
        """Функция выстрела"""
        if time.time() - self.created > 0.5:
            Strike(self.rect.center, event.pos, ENEMY_TANK_GROUP)
            self.created = time.time()
            self.muzzle.get_muzzle(self.rect.center, event.pos)

    def get_position(self):
        return self.rect.center

    def update(self, *args):
        data = zip((-90, 90, 180, 0), ((CELL_SIZE, 0), (-CELL_SIZE, 0), (0, -CELL_SIZE), (0, CELL_SIZE)), [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN])
        self.muzzle.get_muzzle(self.rect.center, pygame.mouse.get_pos())
        if args and args[0].type == pygame.KEYDOWN:
            board = args[1]
            for angle, move, direction in data:
                if args[0].key == direction and board.is_empty(board.get_cell((self.rect.x + move[0], self.rect.y + move[1]))):
                    self.rect = self.rect.move(*move)
                    self.image = pygame.transform.rotate(self.image, self.current_angle - angle)
                    self.muzzle.get_muzzle(self.rect.center, pygame.mouse.get_pos())
                    self.current_angle = angle
        if args:
            if args[0].type == pygame.MOUSEBUTTONDOWN:
                self.strike(args[0])