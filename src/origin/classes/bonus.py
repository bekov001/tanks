import pygame


from ..helpers.variables import TEXTURE_GROUP, ALL_SPRITES, CELL_SIZE


class Bonus(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Bonus, self).__init__(ALL_SPRITES)
        self.image = pygame.Surface([CELL_SIZE, CELL_SIZE])
        self.pos = pos
        self.rect = pygame.Rect(*pos, CELL_SIZE, CELL_SIZE)