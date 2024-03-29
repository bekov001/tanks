import random
import time

from ..helpers.variables import *
from ..helpers.func import load_image

from .inheritors.strike import Strike
from .inheritors.tank import Tank
from .player_muzzle import Muzzle


class EnemyTank(Tank):
    """Вражеский танк"""
    def __init__(self, x, y, enemy, music):
        super().__init__(x, y, music)
        self.add(ENEMY_TANK_GROUP)
        self.image = pygame.transform.scale(load_image("base/enemy_base.png"),
                                            (CELL_SIZE, CELL_SIZE))
        self.current_angle = 0
        self.enemy = enemy
        self.muzzle = Muzzle('muzzle/enemy_muzzle.png', x, y)
        self.do_strike = 0
        self.music = music

    def strike(self):
        """Функция стрельбы"""
        Strike(self.rect.center, self.enemy.rect.center, TANK_GROUP)
        self.music['shot'].play()

    def show_xp(self):
        """Функция показать здоровье танка"""
        xp = self.health / 100
        pygame.draw.rect(SCREEN, "green",
                         (self.rect.x, self.rect.y - 10, CELL_SIZE * xp, 5))
        pygame.draw.rect(SCREEN, "red",
                         (self.rect.x + CELL_SIZE * xp,
                          self.rect.y - 10, CELL_SIZE - CELL_SIZE * xp, 5))

    def generate_direction(self, enemy_pos):
        """Функция генерирует ход танка ИИ"""
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

    def update(self, *args):
        if self.cd_time:
            if time.time() - self.cd_time >= 3:
                self.delay = 3
                self.cd_time = 0
        if self.health > 0:
            self.muzzle.get_muzzle(self.rect.center,
                                   self.enemy.rect.center)
            data = zip(
                (-90, 90, 180, 0),
                ((CELL_SIZE, 0), (-CELL_SIZE, 0), (0, -CELL_SIZE), (0,
                                                                    CELL_SIZE)
                 ),
                [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN])

            if args:
                board = args[0]
                enemy_pos = self.enemy.get_position()
                chosen = self.generate_direction(enemy_pos)
                for angle, move, direction in data:
                    if chosen == direction and board.is_empty(
                            board.get_cell((self.rect.x + move[0],
                                            self.rect.y + move[1]))) and \
                            all((self.rect.x + move[0],
                                 self.rect.y + move[1]) !=
                                (tank.rect.x, tank.rect.y)
                                for tank in ENEMY_TANK_GROUP) and \
                            (self.rect.x + move[0],
                             self.rect.y + move[1]) != (
                            self.enemy.rect.x, self.enemy.rect.y):
                        self.rect = self.rect.move(*move)
                        self.image = pygame.transform.rotate(
                            self.image, self.current_angle - angle)
                        self.muzzle.get_muzzle(self.rect.center,
                                               self.enemy.rect.center)
                        self.current_angle = angle
                        self.healed = False
                        self.do_strike += 1
                        # соблюдение кулдауна
                if self.do_strike == self.delay:
                    self.strike()
                    self.do_strike = 0
            self.show_xp()
        else:
            self.music['death'].play()
            self.muzzle.kill()
            self.kill()
