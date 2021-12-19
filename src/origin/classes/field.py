import pygame
from helpers import *


class Field:
    def __init__(self, width, height):
        self.move = True
        self.width = width
        self.height = height
        self.board = field

        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for index, lst in enumerate(self.board):
            for j, el in enumerate(lst):
                start_pos = (self.left + index * self.cell_size,
                             self.top + j * self.cell_size)
                pygame.draw.rect(screen, "white", (start_pos[0], start_pos[1],
                                                   self.cell_size,
                                                   self.cell_size), 1
                                 if el == 0 else 0)

    def pos_in_board(self, x, y):
        return self.left < x < self.left + len(self.board) * self.cell_size and \
               self.top < y < self.top + len(self.board[0]) * self.cell_size

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if self.pos_in_board(x, y):
            return (x - self.left) // self.cell_size, (
                    y - self.top) // self.cell_size

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is not None:
            self.on_click(cell)
            self.move = not self.move

    def on_click(self, cell):
        self.board[cell[0]][cell[1]] = (self.board[cell[0]][cell[1]] + 1) % 2