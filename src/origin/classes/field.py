import pygame

from .brick import Brick
from .tank import Tank
from .texture import Texture
from ..helpers.variables import *


class Field:
    """Класс поля"""
    def __init__(self, width, height):
        self.move = True
        self.width = width
        self.height = height
        self.board = field

        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

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
        # image = load_image("player_tank.png")
        # image1 = pygame.transform.scale(image, (55, 55))
        # screen.blit(image1, (5, 5))
        #
        # image = load_image("enemy_tank.png")
        # image1 = pygame.transform.scale(image, (55, 55))
        # screen.blit(image1, (55, 55))

        for index, lst in enumerate(self.board):
            for j, el in enumerate(lst):
                start_pos = (self.left + index * self.cell_size,
                             self.top + j * self.cell_size)
                if el != 0:
                    # TODO рисование блоков
                    Brick(start_pos, self)

    def pos_in_board(self, x, y):

        return self.left < x < self.left + len(self.board) * self.cell_size and \
               self.top < y < self.top + len(self.board[0]) * self.cell_size

    def get_cell(self, mouse_pos):
        """Возвращает координату клетки, по координатом окна"""
        x, y = mouse_pos
        if self.pos_in_board(x, y):
            return (x - self.left) // self.cell_size, (
                    y - self.top) // self.cell_size
        return (-1, -1)

    def get_click(self, mouse_pos):
        """Принимает координаты нажатия"""
        cell = self.get_cell(mouse_pos)
        if cell is not None:
            self.on_click(cell)
            self.move = not self.move

    def on_click(self, cell):
        """Изменение поля, при помощи изменения 0 на 1 или наоборот"""
        self.board[cell[0]][cell[1]] = (self.board[cell[0]][cell[1]] + 1) % 2
