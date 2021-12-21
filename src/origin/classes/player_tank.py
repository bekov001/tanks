from itertools import product

from .tank import Tank
import pygame
import random

from helpers import *


class PlayerTank(Tank):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(load_image("player_tank.png"),
                                            (CELL_SIZE, CELL_SIZE))

        self.current_angle = 0

    def update(self, *args):
        # data = product([pygame.KEYDOWN], [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN])
        data = zip((-90, 90, 180, 0), ((CELL_SIZE, 0), (-CELL_SIZE, 0), (0, -CELL_SIZE), (0, CELL_SIZE)), [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN])

        if args and args[0].type == pygame.KEYDOWN:
            board = args[1]
            for angle, move, direction in data:
                if args[0].key == direction and board.is_empty(board.get_cell((self.rect.x + move[0], self.rect.y + move[1]))):
                    self.rect = self.rect.move(*move)
                    print(self.current_angle - angle)
                    self.image = pygame.transform.rotate(self.image, self.current_angle - angle)
                    self.current_angle = angle
        # if args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_RIGHT:
        #     self.rect = self.rect.move(CELL_SIZE, 0)
        # elif args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_LEFT:
        #     self.rect = self.rect.move(-CELL_SIZE, 0)
        # elif args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_UP:
        #     self.rect = self.rect.move(0, -CELL_SIZE)
        # elif args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_DOWN:
        #     self.rect = self.rect.move(0, CELL_SIZE)