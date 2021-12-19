import time

import pygame

from src.origin.classes.field import Field
from helpers import N, SIZE


def main():
    active = False
    running = True
    timing = time.time()
    seconds = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and \
                    not active:
                board.get_click(event.pos)
                board.render(screen)
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) \
                    or (
                    event.type == pygame.MOUSEBUTTONDOWN and event.button == 3):
                active = not active
            if event.type == pygame.MOUSEWHEEL and active:
                if seconds - 0.01 * event.y > 0:
                    seconds -= 0.01 * event.y
        if active:
            if time.time() - timing > seconds:
                timing = time.time()
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()


cell_size = 55
print(cell_size)
screen = pygame.display.set_mode(SIZE)
fps = 120
clock = pygame.time.Clock()
board = Field(N - 2, N)
board.set_view(5, 5, cell_size)
screen.fill((0, 0, 0))
board.render(screen)

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    main()
    pygame.quit()