import os
import time
import pygame
import random
import schedule
import pygame_gui as gui

from origin.classes.player_tank import PlayerTank
from origin.classes.field import Field
from origin.helpers import *
from origin.classes.exit import Settings
from origin.classes.menu import Menu
from origin.classes.texture_pack.bonus import Heal, CoolDown
from origin.classes.levels import Levels


class Game:
    """Класс игры, здесь происходит сама игра, а также загружается карта"""
    def __init__(self, map_name, music):
        self.board = Field(N - 2, N, music)
        self.map_name = map_name
        self.manager = gui.UIManager(SIZE, load_file("data/theme.json"))
        self.settings_btn = gui.elements.UIButton(
            relative_rect=pygame.Rect((WIDTH - 65, 5), (60, 60)),
            text='',
            manager=self.manager)
        self.volume = 1
        self.music = {}
        self.player = PlayerTank(60, 60, music)
        self.running = True
        # self.enemy = EnemyTank(885, 775, self.player)

    def set_level(self, map_name):
        """"""
        self.map_name = map_name

    def generate_bonus(self):
        if self.running:
            empty_coords = []
            for i in range(len(self.board.board)):
                for j in range(len(self.board.board[0])):
                    if self.board.board[i][j] == 0:
                        empty_coords.append((i, j))
            pos = random.choice(empty_coords)
            bonus = random.choice([Heal, CoolDown])
            bonus((
                self.board.left + 55 * pos[0], self.board.top + 55 * pos[1]
            ), self.board, self.music)

    def main(self, music, volume):
        """Главная функция игры"""
        self.music = music
        self.volume = volume
        self.board.set_player(self.player)
        self.board.load_level(self.map_name)
        self.board.render(SCREEN)
        self.running = True
        bonus_time = time.time()
        font = pygame.font.Font(pygame.font.match_font('comicsansms'), 20)
        started_time = time.time()
        timing = time.time()
        step_timing = time.time()
        seconds = 0.1

        while self.running:
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
            if time.time() - bonus_time >= 10:
                self.generate_bonus()
                bonus_time = time.time()
            for sprite in ALL_SPRITES.sprites():
                sprite.check_collision()
            if time.time() - timing > seconds:
                SCREEN.fill("black")
                ALL_SPRITES.draw(SCREEN)
                SCREEN.blit(font.render(
                    'Time: ' + str(round(time.time() - started_time, 1)
                                   ), True, 'black'), (10, 20))
                SCREEN.blit(font.render(
                    'Cooldown: ' + str(round(self.player.delay * 0.3, 1)
                                       ) + ' sec', True, 'black'), (120, 20))
                ALL_SPRITES.update()
                self.manager.update(time_delta)
                self.manager.draw_ui(SCREEN)
                timing = time.time()
                pygame.display.flip()
            if not TANK_GROUP:
                TEXTURE_GROUP.draw(SCREEN)
                res = self.lost(SCREEN, round(time.time() - started_time, 1))
                return res
            if not ENEMY_TANK_GROUP:
                TEXTURE_GROUP.draw(SCREEN)
                res = self.won(SCREEN, round(time.time() - started_time, 1))
                return res
        self.running = False

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
        pygame.mixer.music.pause()
        self.music['lose'].play()
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
                        pygame.mixer.music.unpause()
                        return 'Lose', time
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.unpause()
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
        pygame.mixer.music.pause()
        self.music['victory'].play()
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
                        pygame.mixer.music.unpause()
                        return 'Win', time
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.unpause()
                        return 'Win', time
            pygame.display.flip()


SCREEN.fill((0, 0, 0))

if __name__ == '__main__':
    pygame.mixer.pre_init(44100, -16, 7, 512)
    pygame.init()
    load_sound('background.wav')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    sounds = {}
    for file in ['boost.wav',
                 'death.wav', 'lose.wav', 'player_shot.wav',
                 'shot.wav', 'victory.wav', 'break.wav']:
        sounds[file[:-4]] = make_sound(file)
    pygame.display.set_caption('Tanks')
    menu = Menu(PARAMETERS)
    levels = Levels()
    settings = Settings(sounds)
    while True:
        ans = menu.menu(sounds)
        map = levels.start_screen()
        game = Game(map, sounds)
        game.main(sounds, ans)
