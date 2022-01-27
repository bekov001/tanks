import os

import pygame

from .inheritors.brick import Brick
from .inheritors.iron import Iron
from .tank import Tank
from .texture import Texture
from origin.helpers.variables import *


class Field:
    """Класс поля"""
    def __init__(self, width, height):
        self.move = True
        self.width = width
        self.height = height
        self.board = field

        # значения по умолчанию
        self.left = 5
        self.top = 5
        self.cell_size = CELL_SIZE

    def load_level(self, filename):
        file = open(os.path.join("origin", "media", 'data', filename), encoding="utf8")
        for index, el in enumerate(file.read().split("\n")):
            for i, letter in enumerate(el):
                if letter == IRON_BLOCK:
                    self.board[index][i] = IRON
                elif letter == BRICK_BLOCK:
                    self.board[index][i] = BRICK
                else:
                    self.board[index][i] = EMPTY

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
                    # TODO рисование блоков
                    Brick(start_pos, self)
                elif el == IRON:
                    Iron(start_pos, self)

    def pos_in_board(self, x, y):
        """Функция проверки координат на нахождении в поле"""
        return self.left < x < self.left + len(self.board) * self.cell_size and \
               self.top < y < self.top + len(self.board[0]) * self.cell_size

    def get_cell(self, mouse_pos):
        """Возвращает координату клетки, по координатом окна"""
        x, y = mouse_pos
        if self.pos_in_board(x, y):
            return (x - self.left) // self.cell_size, (
                    y - self.top) // self.cell_size
        return (-1, -1)

    # def get_click(self, mouse_pos):
    #     """Принимает координаты нажатия"""
    #     cell = self.get_cell(mouse_pos)
    #     if cell is not None:
    #         self.on_click(cell)
    #         self.move = not self.move
    #
    # def on_click(self, cell):
    #     """Изменение поля, при помощи изменения 0 на 1 или наоборот"""
    #     self.board[cell[0]][cell[1]] = (self.board[cell[0]][cell[1]] + 1) % 2
