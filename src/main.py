import os
import time
import pygame
import random
import pygame_gui as gui

from origin.classes.player_tank import PlayerTank
from origin.classes.enemy_tank import EnemyTank
from origin.classes.field import Field
from origin.helpers.variables import *
from origin.classes.exit import Settings
from origin.classes.menu import Menu
from origin.classes.texture_pack.bonus import Heal


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
        Heal((170, 60), self.board)
        self.player = PlayerTank(60, 60)
        self.enemy = EnemyTank(885, 775, self.player)
        self.enemy = EnemyTank(885, 775, self.player)
        # heal = Heal((160, 60), self.board)
        running = True
        started_time = time.time()
        timing = time.time()
        step_timing = time.time()
        seconds = 0.1

        while running:
            start = time.monotonic()
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
            for sprite in ALL_SPRITES.sprites():
                sprite.check_collision()
            if time.time() - timing > seconds:
                timing = time.time()
                SCREEN.fill("black")
                ALL_SPRITES.draw(SCREEN)
                ALL_SPRITES.update()
                self.manager.update(time_delta)
                self.manager.draw_ui(SCREEN)
                pygame.display.flip()
            if not TANK_GROUP:
                res = self.lost(SCREEN, round(time.time() - started_time, 1))
                return res
            if not ENEMY_TANK_GROUP:
                res = self.won(SCREEN, round(time.time() - started_time, 1))
                return res

    def stop_game(self):
        """Останавливает игру, уничтожая все элементы"""
        for al in ALL_SPRITES.sprites():
            al.kill()

    def lost(self, surface, time):
        running = True
        res_font = pygame.font.Font(pygame.font.match_font('comicsansms'), 70)
        main_font = pygame.font.Font(pygame.font.match_font('pacifico'), 50)
        window = pygame.Surface((500, 600))
        window.fill((16, 164, 149))
        while running:
            window.blit(res_font.render('GAME OVER', True, 'purple'), (50, 10))
            window.blit(res_font.render('YOU LOST', True, 'red'), (70, 240))
            window.blit(main_font.render('BACK', True, 'white'), (200, 530))
            pygame.draw.rect(window, 'white', (195, 525, 110, 40), 1)
            window.blit(
                main_font.render('Your time: ' + str(time), True, 'black'),
                (100, 170))
            surface.blit(window, (250, 145))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 445 <= pos[0] <= 555 and 670 <= pos[1] <= 710:
                        self.stop_game()
                        return 'Lose', time
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 'Lose', time
            pygame.display.flip()

    def won(self, surface, time):
        running = True
        res_font = pygame.font.Font(pygame.font.match_font('comicsansms'), 70)
        congrat_font = pygame.font.Font(pygame.font.match_font('comforter'),
                                        60)
        main_font = pygame.font.Font(pygame.font.match_font('pacifico'), 50)
        window = pygame.Surface((500, 600))
        window.fill((16, 164, 149))
        while running:
            window.blit(res_font.render('GAME OVER', True, 'purple'), (50, 10))
            window.blit(res_font.render('YOU WON', True, 'green'), (70, 240))
            window.blit(congrat_font.render(
                'CONGRATULATIONS!', True, random.choice(
                    ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
                )), (30, 360))
            window.blit(main_font.render('BACK', True, 'white'), (200, 530))
            pygame.draw.rect(window, 'white', (195, 525, 110, 40), 1)
            window.blit(
                main_font.render('Your time: ' + str(time), True, 'black'),
                (100, 170))
            surface.blit(window, (250, 145))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 445 <= pos[0] <= 555 and 670 <= pos[1] <= 710:
                        self.stop_game()
                        return 'Win', time
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 'Win', time
            pygame.display.flip()


SCREEN.fill((0, 0, 0))

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Tanks')
    game = Game("map.txt")
    menu = Menu(PARAMETERS)
    settings = Settings()
    while True:
        ans = menu.menu()
        if not ans:
            game.main()
