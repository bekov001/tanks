import os
import time
import pygame_gui as gui

from origin.classes.player_tank import PlayerTank
from origin.classes.enemy_tank import EnemyTank
from origin.classes.field import Field
from origin.helpers.variables import *
from src.origin.classes.exit import Settings
from src.origin.classes.menu import Menu


class Game:
    """Класс игры, здесь происходит сама игра, а также загружается карта"""
    def __init__(self, map_name):
        self.board = Field(N - 2, N)
        self.map_name = map_name
        self.manager = gui.UIManager(SIZE)
        self.settings_btn = gui.elements.UIButton(
            relative_rect=pygame.Rect((WIDTH - 105, 5), (90, 50)),
            text='SETTINGS',
            manager=self.manager)
        # self.player = PlayerTank(60, 60)
        # self.enemy = EnemyTank(885, 775, self.player)

    def set_level(self, map_name):
        """"""
        self.map_name = map_name

    def main(self):
        """Главная функция игры"""
        self.board.load_level(self.map_name)
        self.board.render(SCREEN)
        self.player = PlayerTank(60, 60)
        self.enemy = EnemyTank(885, 775, self.player)
        self.enemy = EnemyTank(885, 775, self.player)
        running = True
        timing = time.time()
        step_timing = time.time()
        seconds = 0.1

        while running:
            time_delta = CLOCK.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
                self.manager.process_events(event)
                if event.type == gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.settings_btn:
                        res = settings.start_screen()
                        if res == "EXIT":
                            self.stop_game()
                            return 0
                        elif res == "CLOSE":
                            self.stop_game()
                            exit(0)
                        timing = time.time()

                self.player.update(event, self.board)
                self.manager.process_events(event)

            if time.time() - step_timing > 0.3:
                ENEMY_TANK_GROUP.update(self.board)
                step_timing = time.time()
            if time.time() - timing > seconds:
                timing = time.time()
                SCREEN.fill("black")
                ALL_SPRITES.draw(SCREEN)
                for sprite in ALL_SPRITES.sprites():
                    sprite.check_collision()
                ALL_SPRITES.update()
                self.manager.update(time_delta)
                self.manager.draw_ui(SCREEN)
                pygame.display.flip()

    def stop_game(self):
        """Останавливает игру, уничтожая все элементы"""
        for al in ALL_SPRITES.sprites():
            al.kill()


SCREEN.fill((0, 0, 0))

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Tanks')
    game = Game("map.txt")
    menu = Menu(PARAMETERS)
    settings = Settings()
    while True:
        menu.menu()
        game.main()
    pygame.quit()
