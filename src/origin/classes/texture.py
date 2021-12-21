import pygame

from helpers import TEXTURE_GROUP, ALL_SPRITES, CELL_SIZE


class Texture(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(ALL_SPRITES)
        self.add(TEXTURE_GROUP)
        self.image = pygame.Surface([CELL_SIZE, CELL_SIZE])
        self.image.fill("white")
        self.rect = pygame.Rect(*pos, CELL_SIZE, CELL_SIZE)
