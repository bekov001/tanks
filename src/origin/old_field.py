from itertools import product

import pygame
import random


EMPTY = 0
WALL = 1

# TODO not working


def get_neighbors(cell, matrix, n):

    iterator = list(product((2, -2, 0), repeat=2))
    print(iterator)
    cells = []
    for i, j in iterator:
        if abs(i) != abs(j) and 0 <= cell[0] + i < n and 0 <= cell[1] + j < n and not matrix[cell[0] + i][cell[1] + j]:
            cells.append((cell[0] + i, cell[1] + j))
    return cells


def remove_wall(cell1, cell2):
    x_diff = cell2[0] - cell1[0]
    y_diff = cell2[1] - cell1[1]

    addX = (x_diff // abs(x_diff)) if (x_diff != 0) else 0
    addY = (y_diff // abs(y_diff)) if (y_diff != 0) else 0

    return addX, addY


class Field:
    def __init__(self, width, height):
        self.move = True
        self.width = width
        self.height = height
        # self.board = [[0] * width for _ in range(height)]
        # print(self.board)
        # for i in range(random.randint(10, height)):
        #     x, y = random.randint(1, height - 1), random.randint(1, width - 1)
        #     print(x, y)
        #     self.board[x][y] = 10

        self.board = [[0] * width for _ in range(height)]
        for i in range(height):
            for j in range(width):
                if i % 2 != 0 and j % 2 != 0 and (i < height-1 and j < width-1):
                    self.board[i][j] = EMPTY
                else:
                    self.board[i][j] = WALL
        start = (1, 1)
        neighbors = get_neighbors(start, self.board, width)
        random_cell = random.choice(neighbors)
        print(remove_wall(start, random_cell, self.board))
        while len(neighbors) > 0:
            random_cell = random.choice(neighbors)
            wall = remove_wall(start, random_cell, self.board)
            self.board[wall[0]][wall[1]] = 0
            start = random_cell
            neighbors = get_neighbors(start, self.board, width)

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