import pygame

from origin.helpers.variables import *


class Texture(pygame.sprite.Sprite):
    """Базовый класс текстур - железа и кирпичей"""
    def __init__(self, pos: tuple, board, music):
        super().__init__(ALL_SPRITES)
        self.add(TEXTURE_GROUP)
        self.image = pygame.Surface([CELL_SIZE, CELL_SIZE])
        self.image.fill("white")
        self.rect = pygame.Rect(*pos, CELL_SIZE, CELL_SIZE)
        self.pos = pos
        self.board = board
        self.hit = False
        self.music = music

    def check_collision(self):
        if pygame.sprite.spritecollideany(self, STRIKE_GROUP):
            self.hit = True
