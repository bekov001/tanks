import time

import pygame

from origin.classes.player_tank import PlayerTank
from origin.classes.tank import Tank
from origin.classes.field import Field
from origin.helpers.variables import N, SIZE, ALL_SPRITES


def main():
    active = True
    running = True
    timing = time.time()
    seconds = 0.1
    player = PlayerTank(60, 60)
    board.render(screen)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            player.update(event, board)
        if active:
            if time.time() - timing > seconds:
                timing = time.time()
                screen.fill("black")
                ALL_SPRITES.draw(screen)
                ALL_SPRITES.update()
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
    print(board.board)
    pygame.quit()