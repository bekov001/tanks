import time

import pygame
import sys
import pygame_gui as gui

# from origin.classes.exit import start_screen
from origin.helpers.func import load_image
from origin.classes.player_tank import PlayerTank
from origin.classes.tank import Tank
from origin.classes.enemy_tank import EnemyTank
from origin.classes.field import Field
from origin.helpers.variables import *
from src.origin.classes.exit import start_screen
from src.origin.classes.menu import Menu


class Game:
    """Класс игры, здесь происходит сама игра, а также загружается карта"""
    def __init__(self):
        self.board = Field(N - 2, N)

    def main(self):
        """Главная функция игры"""
        running = True
        timing = time.time()
        step_timing = time.time()
        seconds = 0.1
        player = PlayerTank(60, 60)
        enemy = EnemyTank(885, 775, player)
        self.board.render(screen)
        manager = gui.UIManager(SIZE)
        hello_button = gui.elements.UIButton(
            relative_rect=pygame.Rect((WIDTH - 105, 5), (90, 50)),
            text='SETTINGS',
            manager=manager)
        clock = pygame.time.Clock()
        btn_click = False
        while running:
            time_delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                manager.process_events(event)
                if event.type == gui.UI_BUTTON_PRESSED:
                    if event.ui_element == hello_button:
                        res = start_screen()
                        if res == "EXIT":
                            self.stop_game()
                        timing = time.time()
                        btn_click = True
                elif not btn_click:
                    player.update(event, self.board)
                else:
                    btn_click = False

                player.update(event, self.board)
                manager.process_events(event)

            if time.time() - step_timing > 0.3:
                enemy.update(self.board)
                step_timing = time.time()
            if time.time() - timing > seconds:
                timing = time.time()
                screen.fill("black")
                ALL_SPRITES.draw(screen)
                for sprite in ALL_SPRITES.sprites():
                    sprite.check_collision()
                ALL_SPRITES.update()
                manager.update(time_delta)
                manager.draw_ui(screen)
                pygame.display.flip()

    def stop_game(self):
        pass


cell_size = 55
print(cell_size)
screen = pygame.display.set_mode(SIZE)
surface = pygame.Surface(SIZE)
fps = 120
clock = pygame.time.Clock()
screen.fill((0, 0, 0))

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Tanks')
    game = Game()
    menu = Menu(PARAMETERS)
    menu.menu()
    while True:
        res = game.main()
        if res == 0:
            menu.menu()
    pygame.quit()
