"""Постоянные"""
import pygame

SIZE = WIDTH, HEIGHT = 1000, 890
N = 18
EMPTY = 0
BRICK = 1
IRON = 2
FPS = 60
CELL_SIZE = 55


ALL_SPRITES = pygame.sprite.Group()
TEXTURE_GROUP = pygame.sprite.Group()
STRIKE_GROUP = pygame.sprite.Group()
HEAL_BONUS_GROUP = pygame.sprite.Group()
SHIELD_BONUS_GROUP = pygame.sprite.Group()
TANK_GROUP = pygame.sprite.Group()
ENEMY_TANK_GROUP = pygame.sprite.Group()

field = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

DATA = zip(
            (-90, 90, 180, 0),
            ((CELL_SIZE, 0), (-CELL_SIZE, 0), (0, -CELL_SIZE), (0, CELL_SIZE)),
            [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN])

PARAMETERS = [(410, 310, 'Start', (255, 255, 255), (89, 118, 10), 0),
              (350, 430, 'Settings', (255, 255, 255), (89, 118, 10), 1),
              (420, 550, 'Quit', (255, 255, 255), (89, 118, 10), 2)]

SCREEN = pygame.display.set_mode(SIZE)
SURFACE = pygame.Surface(SIZE)

IRON_BLOCK = "#"
BRICK_BLOCK = "$"
EMPTY_BLOCK = " "
ENEMY = "%"
PLAYER = "@"
CLOCK = pygame.time.Clock()
# test = [["#" if i == 2 else "$" if i == 1 else " " for i in el] for el in field]
# print("\n".join(["".join(el) for el in test]))