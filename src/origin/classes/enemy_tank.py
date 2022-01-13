import random
import time

from ..helpers.variables import *
from ..helpers.func import load_image

from .strike import Strike
from .tank import Tank
from .field import Field


class EnemyTank(Tank):
    """Вражеский танк"""
    def __init__(self, x, y, enemy):
        super().__init__(x, y)
        self.add(ENEMY_TANK_GROUP)
        self.image = pygame.transform.scale(load_image("enemy_tank.png"),
                                            (CELL_SIZE, CELL_SIZE))
        self.current_angle = 0
        self.enemy = enemy
        self.do_strike = 0
        self.xp = 100

    def strike(self):
        Strike(self.rect.center, self.enemy.rect.center, TANK_GROUP)


    def get_muzzle(self):
        """Функция для получения дула танка"""
        pass

    def generate_direction(self, enemy_pos):
        if enemy_pos[0] > self.rect.center[0]:
            if enemy_pos[1] > self.rect.center[1]:
                dir = random.choice(
                    [pygame.K_DOWN, pygame.K_RIGHT] * 3 +
                    [pygame.K_RIGHT, pygame.K_LEFT,
                     pygame.K_UP, pygame.K_DOWN])
            elif enemy_pos[1] < self.rect.center[1]:
                dir = random.choice([pygame.K_RIGHT, pygame.K_UP] * 3 +
                                    [pygame.K_RIGHT, pygame.K_LEFT,
                                     pygame.K_UP, pygame.K_DOWN])
            else:
                dir = random.choice([pygame.K_RIGHT, pygame.K_DOWN,
                                     pygame.K_UP] * 3 +
                                    [pygame.K_RIGHT, pygame.K_LEFT,
                                     pygame.K_UP, pygame.K_DOWN])
        elif enemy_pos[0] < self.rect.center[0]:
            if enemy_pos[1] > self.rect.center[1]:
                dir = random.choice([pygame.K_LEFT, pygame.K_DOWN] * 3 +
                                    [pygame.K_RIGHT, pygame.K_LEFT,
                                     pygame.K_UP, pygame.K_DOWN])
            elif enemy_pos[1] < self.rect.center[1]:
                dir = random.choice([pygame.K_LEFT, pygame.K_UP] * 3 +
                                    [pygame.K_RIGHT, pygame.K_LEFT,
                                     pygame.K_UP, pygame.K_DOWN])
            else:
                dir = random.choice([pygame.K_DOWN,
                                     pygame.K_UP, pygame.K_LEFT] * 3 +
                                    [pygame.K_RIGHT, pygame.K_LEFT,
                                     pygame.K_UP, pygame.K_DOWN])
        else:
            if enemy_pos[1] > self.rect.center[1]:
                dir = random.choice([pygame.K_DOWN, pygame.K_LEFT,
                                     pygame.K_RIGHT] * 3 +
                                    [pygame.K_RIGHT, pygame.K_LEFT,
                                     pygame.K_UP, pygame.K_DOWN])
            elif enemy_pos[1] < self.rect.center[1]:
                dir = random.choice([pygame.K_UP, pygame.K_LEFT,
                                     pygame.K_RIGHT] * 3 +
                                    [pygame.K_RIGHT, pygame.K_LEFT,
                                     pygame.K_UP, pygame.K_DOWN])
            else:
                dir = random.choice([pygame.K_RIGHT,
                                     pygame.K_LEFT, pygame.K_UP,
                                     pygame.K_DOWN])
        return dir

    # def generate_direction(self, available_directions):
    #     return random.choice(available_directions)

    def update(self, *args):
        data = zip(
            (-90, 90, 180, 0),
            ((CELL_SIZE, 0), (-CELL_SIZE, 0), (0, -CELL_SIZE), (0, CELL_SIZE)),
            [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN])

        if args:
            board = args[0]
            enemy_pos = self.enemy.get_position()
            # available = []
            # for angle, move, direction in data:
            #     if board.is_empty(board.get_cell((self.rect.x + move[0], self.rect.y + move[1]))):
            #         available.append(direction)
            chosen = self.generate_direction(enemy_pos)
            for angle, move, direction in data:
                if chosen == direction and board.is_empty(
                        board.get_cell((self.rect.x + move[0],
                                        self.rect.y + move[1]))):
                    self.rect = self.rect.move(*move)
                    self.image = pygame.transform.rotate(
                        self.image, self.current_angle - angle)
                    self.current_angle = angle
                    self.do_strike += 1
            if self.do_strike == 7:
                self.strike()
                self.do_strike = 0



