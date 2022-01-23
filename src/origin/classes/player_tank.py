from itertools import product
import time
import pygame
import random

from .strike import Strike
from .tank import Tank
from ..helpers import CELL_SIZE, TANK_GROUP, ENEMY_TANK_GROUP, load_image


class PlayerTank(Tank):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.add(TANK_GROUP)
        self.image = pygame.transform.scale(load_image("player_tank.png"),
                                            (CELL_SIZE, CELL_SIZE))

        self.current_angle = 0
        self.created = time.time()

    def strike(self, event):
        """Функция выстрела"""
        if event.type == pygame.MOUSEBUTTONDOWN \
                and time.time() - self.created > 1:
            Strike(self.rect.center, event.pos, ENEMY_TANK_GROUP)
            self.created = time.time()

    def get_muzzle(self):
        """Функция для получения дула танка"""
        pass

    def get_position(self):
        return self.rect.center

    def update(self, *args):
        data = zip((-90, 90, 180, 0), ((CELL_SIZE, 0), (-CELL_SIZE, 0), (0, -CELL_SIZE), (0, CELL_SIZE)), [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN])

        if args and args[0].type == pygame.KEYDOWN:
            board = args[1]
            for angle, move, direction in data:
                if args[0].key == direction and board.is_empty(board.get_cell((self.rect.x + move[0], self.rect.y + move[1]))):
                    self.rect = self.rect.move(*move)
                    self.image = pygame.transform.rotate(self.image, self.current_angle - angle)
                    self.current_angle = angle
        if args:
            self.strike(args[0])