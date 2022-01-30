from itertools import product
import time
import pygame
import math
import random

from .inheritors.strike import Strike
from .inheritors.tank import Tank
from .player_muzzle import Muzzle
from ..helpers import CELL_SIZE, TANK_GROUP, ENEMY_TANK_GROUP, load_image, \
    SCREEN


class PlayerTank(Tank):
    def __init__(self, x, y, music):
        super().__init__(x, y, music)
        self.add(TANK_GROUP)
        self.image = pygame.transform.scale(load_image("base/player_base.png"),
                                            (CELL_SIZE, CELL_SIZE))
        self.muzzle = Muzzle("muzzle/player_muzzle.png", x, y)
        self.current_angle = 0
        self.created = time.time()
        self.music = music

    def strike(self, event):
        """Функция выстрела"""
        if event.type == pygame.MOUSEBUTTONDOWN \
                and time.time() - self.created > self.delay * 0.3:
            self.music['player_shot'].play()
            Strike(self.rect.center, event.pos, ENEMY_TANK_GROUP)
            self.created = time.time()
            self.muzzle.get_muzzle(self.rect.center, event.pos)

    def get_position(self):
        return self.rect.center

    def show_xp(self):
        """Показывает здоровье танка"""
        xp = self.health / 100
        font = pygame.font.Font(pygame.font.match_font('comicsansms'), 15)
        pygame.draw.rect(SCREEN, "green", (10, 10, 200 * xp, 10))
        pygame.draw.rect(SCREEN, "red", (
            200 * xp + 10, 10, 200 - 200 * xp, 10))
        SCREEN.blit(font.render(str(self.health) + 'hp', True, 'green'),
                    (210, 7))

    def update(self, *args):
        if self.cd_time:
            if time.time() - self.cd_time >= 3:
                self.delay = 3
                self.cd_time = 0
        if self.health:
            data = zip((-90, 90, 180, 0), ((CELL_SIZE, 0),
                                           (-CELL_SIZE, 0),
                                           (0, -CELL_SIZE), (0, CELL_SIZE)),
                       [(pygame.K_RIGHT, pygame.K_d),
                        (pygame.K_LEFT, pygame.K_a), (pygame.K_UP, pygame.K_w),
                        (pygame.K_DOWN, pygame.K_s)])
            self.muzzle.get_muzzle(self.rect.center, pygame.mouse.get_pos())
            if args and args[0].type == pygame.KEYDOWN:
                board = args[1]
                for angle, move, direction in data:
                    if args[0].key in direction and \
                            board.is_empty(
                                board.get_cell(
                                    (self.rect.x + move[0],
                                     self.rect.y + move[1])
                                )
                            ) and all((self.rect.x + move[0],
                                       self.rect.y + move[1]) !=
                                      (tank.rect.x, tank.rect.y)
                                      for tank in ENEMY_TANK_GROUP):
                        self.rect = self.rect.move(*move)
                        self.image = pygame.transform.rotate(
                            self.image,
                            self.current_angle - angle)
                        self.muzzle.get_muzzle(self.rect.center,
                                               pygame.mouse.get_pos())
                        self.current_angle = angle
                        self.healed = False
            if args:
                self.strike(args[0])
            self.show_xp()
        else:
            self.muzzle.kill()
            self.kill()
