import time

import pygame
import pygame_gui as gui

from classes.exit import start_screen
from helpers import load_image
from origin.classes.player_tank import PlayerTank
from origin.classes.tank import Tank
from origin.classes.enemy_tank import EnemyTank
from origin.classes.field import Field
from origin.helpers.variables import *


class Menu:
    def __init__(self, parameters=None):
        if parameters is None:
            parameters = [
                (120, 140, 'Start', (125, 0, 255), (255, 255, 255), 0)]
        self.parameters = parameters

    def render(self, surf, font, index):
        for i in self.parameters:
            if index == i[-1]:
                surf.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surf.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self):
        done = True
        font_menu = pygame.font.Font(pygame.font.match_font('pacifico'), 50)
        index = 0
        while done:
            surface.fill((231, 247, 151))
            pos = pygame.mouse.get_pos()
            for i in self.parameters:
                if i[0] < pos[0] < i[0] + 155 and i[1] < pos[1] < i[1] + 50:
                    index = i[-1]
            self.render(surface, font_menu, index)
            screen.blit(surface, (0, 0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()



def main():
    """Главная функция запуска"""
    active = True
    running = True
    timing = time.time()
    step_timing = time.time()
    seconds = 0.1
    player = PlayerTank(60, 60)
    enemy = EnemyTank(885, 775, player)
    board.render(screen)
    manager = gui.UIManager(SIZE)
    hello_button = gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH - 105, 5), (90, 50)),
        text='SETTINGS',
        manager=manager)
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == gui.UI_BUTTON_PRESSED:
                if event.ui_element == hello_button:
                    print('Hello World!')
                    start_screen()
                    active = False
            if active:
                player.update(event, board)
            manager.process_events(event)

        if active:
            if time.time() - step_timing > 0.3:
                enemy.update(board)
                step_timing = time.time()
            if time.time() - timing > seconds:
                timing = time.time()
                screen.fill("black")
                ALL_SPRITES.draw(screen)
                for sprite in ALL_SPRITES.sprites():
                    sprite.check_collision()
                ALL_SPRITES.update()

        manager.update(fps)
        manager.draw_ui(screen)
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
    pygame.display.set_caption('Tanks')
    menu = Menu(PARAMETERS)
    menu.menu()
    # main()
    pygame.quit()