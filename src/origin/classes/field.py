import os

from .texture_pack.brick import Brick
from .enemy_tank import EnemyTank
from .player_tank import PlayerTank
from .texture_pack.iron import Iron
from ..helpers.variables import *


class Field:
    """Класс поля"""
    def __init__(self, width, height, music):
        self.move = True
        self.width = width
        self.height = height
        self.board = field
        self.player = None

        # значения по умолчанию
        self.left = 5
        self.top = 5
        self.cell_size = CELL_SIZE

        self.music = music

    def set_player(self, player):
        self.player = player

    def load_level(self, filename):
        file = open(os.path.join("origin", "media", 'data', "maps", filename),
                    encoding="utf8")
        for index, el in enumerate(file.read().split("\n")):
            for i, letter in enumerate(el):
                if letter == IRON_BLOCK:
                    result = IRON
                elif letter == BRICK_BLOCK:
                    result = BRICK
                elif letter == PLAYER_BLOCK:
                    result = PLAYER
                elif letter == ENEMY_BLOCK:
                    result = ENEMY
                else:
                    result = EMPTY

                self.board[index][i] = result

    def set_empty(self, pos: tuple):
        """Делает данную клетку пустой"""
        pos = self.get_cell(pos)
        self.board[pos[0]][pos[1]] = EMPTY

    def is_empty(self, pos):
        """Проверяет клетка пуста или нет и возвращает значение"""
        return not self.board[pos[0]][pos[1]]

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        """Функция для изменения размеров и координаты поля"""
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        """Функция прорисовки поля"""

        for index, lst in enumerate(self.board):
            for j, el in enumerate(lst):
                start_pos = (self.left + index * self.cell_size,
                             self.top + j * self.cell_size)
                if el == BRICK:
                    Brick(start_pos, self, self.music)
                elif el == IRON:
                    Iron(start_pos, self, self.music)
                elif el == ENEMY:
                    EnemyTank(*start_pos, self.player, self.music)
                    self.board[index][j] = EMPTY
                elif el == PLAYER:
                    self.player.rect.x, self.player.rect.y = start_pos[0], \
                                                             start_pos[1]
                    self.player.muzzle.rect.x, self.player.muzzle.rect.y =\
                        start_pos[0], start_pos[1]
                    self.board[index][j] = EMPTY

    def pos_in_board(self, x, y):
        """Функция проверки координат на нахождении в поле"""
        return self.left < x < self.left + len(
            self.board) * self.cell_size and self.top < y < self.top + len(
            self.board[0]) * self.cell_size

    def get_cell(self, mouse_pos):
        """Возвращает координату клетки, по координатом окна"""
        x, y = mouse_pos
        if self.pos_in_board(x, y):
            return (x - self.left) // self.cell_size, (
                    y - self.top) // self.cell_size
        return (-1, -1)