import pygame
import math

from ..helpers.func import load_image
from ..helpers.variables import ALL_SPRITES, CELL_SIZE


class Muzzle(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        super(Muzzle, self).__init__(ALL_SPRITES)
        self.image = pygame.transform.scale(load_image(filename),
                                            (CELL_SIZE, CELL_SIZE))
        self.copy = pygame.transform.scale(load_image(filename),
                                            (CELL_SIZE, CELL_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.angle = 0
    
    def get_muzzle(self, pos, mouse_pos):
        """Функция для получения дула танка"""
        mouse = mouse_pos
        catets = abs(mouse[0] - pos[0]), abs(mouse[1] - pos[1])
        hypotenuse = ((mouse[0] - pos[0]) ** 2 + (
                    mouse[1] - pos[1]) ** 2) ** 0.5
        if mouse[0] < pos[0]:
            if mouse[1] < pos[1]:
                self.angle = -90 + -math.acos(catets[0] / hypotenuse) * \
                             (180 / math.pi)
            elif mouse[1] > pos[1]:
                self.angle = - math.asin(catets[0] / hypotenuse) * (
                            180 / math.pi)
            else:
                self.angle = -90
        elif mouse[0] > pos[0]:
            if mouse[1] < pos[1]:
                self.angle = 90 + math.acos(catets[0] / hypotenuse) * \
                             (180 / math.pi)
            elif mouse[1] > pos[1]:
                self.angle = math.asin(catets[0] / hypotenuse) * (
                            180 / math.pi)
            else:
                self.angle = 90
        else:
            if mouse[1] > pos[1]:
                self.angle = 0
            elif mouse[1] < pos[1]:
                self.angle = 180
        self.image = pygame.transform.rotozoom(self.copy, self.angle, 1)
        self.rect = self.image.get_rect(center=pos)
    
    def check_collision(self):
        pass
